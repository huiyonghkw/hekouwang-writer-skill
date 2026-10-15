#!/usr/bin/env python3
"""check_fidelity.py — 文档数字对账器（hekouwang-writer-skill）

机械复查文档里的算术，专治"表格合计对不上、乘法算错、等式链漏项"。
这类错误人工复核时最容易看漏（实测：一篇 3000 字文档的合计错误
是靠逐格重算才发现的，不该靠运气）。

硬检查（不一致 → 退出码 1）：
  1. 末列为"合计/共计/总共/小计"的表格：合计 = 该行其余单元格之和
  2. 首列为"合计/共计/总共/小计"的表格：合计 = 该列上方单元格之和
  3. 乘法表达式  A×B=C（兼容 A*B=C、AxB=C）
  4. 加法等式链  a + b + c = d

说明：
  - 代码围栏（```）内的示例不检查；
  - 单元格含"约/元/（注释）"等会先清洗；含"900×7=6,300"的取最后一个 = 后的值；
  - 某行/列含非数字单元格（如"待缴"）时跳过该行/列，不猜；
  - 只报告，不修改。

用法：
    check_fidelity.py FILE [FILE ...]
    echo "文本" | check_fidelity.py
    check_fidelity.py --json FILE
    check_fidelity.py --selftest

退出码：有算术不一致 = 1；否则 = 0。
"""

import argparse
import json
import re
import sys

TOTAL_WORDS = ("合计", "共计", "总共", "小计", "共入账")
MUL_RE = re.compile(r"(\d[\d,]*)\s*[×xX*]\s*(\d[\d,]*)\s*=\s*(\d[\d,]*)")
CHAIN_RE = re.compile(r"((?:\d[\d,]*\s*\+\s*)+\d[\d,]*)\s*=\s*(\d[\d,]*)")


def to_num(s):
    """从单元格文本提取数值；提取不到返回 None。"""
    if s is None:
        return None
    t = s.strip()
    if not t:
        return None
    # "900×7=6,300" → 取最后一个 = 之后
    if "=" in t:
        t = t.rsplit("=", 1)[1]
    t = t.replace(",", "").replace("，", "")
    t = re.sub(r"[元￥\s]", "", t)
    t = t.lstrip("约近").rstrip("元左右")
    m = re.search(r"-?\d+(?:\.\d+)?", t)
    return float(m.group()) if m else None


def is_pure_num(s):
    """表头单元格专用：仅当单元格是纯数字（可含千分位/元）才参与求和。

    "200" → 200.0；"1月" → None（不把月份当年份）；
    "2013-2019年（各已缴100）" → None。
    """
    if s is None:
        return None
    t = s.strip().replace(",", "").replace("，", "").replace("元", "").strip()
    m = re.fullmatch(r"-?\d+(?:\.\d+)?", t)
    return float(m.group()) if m else None


def strip_fences(lines):
    out, in_fence = [], False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return out


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_sep(line):
    return "-" in line and all(
        re.fullmatch(r":?-{2,}:?", c) for c in split_row(line) if c)


def check_tables(lines, path, errors):
    i, n = 0, len(lines)
    while i < n:
        if lines[i].strip().startswith("|"):
            block = []
            while i < n and lines[i].strip().startswith("|"):
                block.append((i + 1, lines[i]))
                i += 1
            rows = [(ln, split_row(raw)) for ln, raw in block
                    if not is_sep(raw)]
            if len(rows) < 2:
                continue
            header_ln, header = rows[0]
            data = rows[1:]
            ncol = len(header)

            # 模式1：末列是合计列 → 逐行验算
            if ncol >= 3 and any(w in header[-1] for w in TOTAL_WORDS):
                for ln, cells in data:
                    if len(cells) != ncol:
                        continue
                    vals = [to_num(c) for c in cells[1:-1]]
                    total = to_num(cells[-1])
                    if total is None or any(v is None for v in vals):
                        continue
                    s = sum(vals)
                    if abs(s - total) > 0.01:
                        errors.append(
                            f"L{ln} 行「{cells[0]}」合计不符："
                            f"{'+'.join(f'{v:g}' for v in vals)} = {s:g}，"
                            f"表中为 {total:g}")

            # 模式2：某数据行标签含合计类词 → 逐列验算
            # 数值型表头（如档次表的 200/300/...）参与求和；
            # 非纯数字表头（如"1月""2013-2019年"）不参与；
            # 少于 2 个加项不验（单项"合计"多是误报）。
            for ln, cells in data:
                if not cells or not any(w in cells[0] for w in TOTAL_WORDS):
                    continue
                if len(cells) != ncol:
                    continue
                others = [header] + [r for _ln2, r in data if r is not cells]
                for ci in range(1, ncol):
                    vals = []
                    for r in others:
                        if len(r) != ncol:
                            continue
                        v = is_pure_num(r[ci]) if r is header else to_num(r[ci])
                        if v is not None:
                            vals.append(v)
                    total = to_num(cells[ci])
                    if total is None or len(vals) < 2:
                        continue
                    s = sum(vals)
                    if abs(s - total) > 0.01:
                        errors.append(
                            f"L{ln} 「{cells[0]}」第{ci}列（{header[ci]}）"
                            f"合计不符：{len(vals)}项之和 = {s:g}，"
                            f"表中为 {total:g}")
        else:
            i += 1


def check_expressions(text, path, errors):
    for ln, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            continue
        for m in MUL_RE.finditer(line):
            a, b, c = (to_num(x) for x in m.groups())
            if None not in (a, b, c) and abs(a * b - c) > 0.01:
                errors.append(f"L{ln} 乘法不符：{a:g}×{b:g} = {a*b:g}，"
                              f"文中写 {c:g}")
        for m in CHAIN_RE.finditer(line):
            left, right = m.group(1), to_num(m.group(2))
            vals = [to_num(x) for x in left.split("+")]
            if right is not None and all(v is not None for v in vals):
                s = sum(vals)
                if abs(s - right) > 0.01:
                    errors.append(f"L{ln} 加法链不符：{' + '.join(f'{v:g}' for v in vals)}"
                                  f" = {s:g}，文中写 {right:g}")


def selftest():
    cases = [
        ("末列合计-对", "| 项 | 甲 | 乙 | 合计 |\n|---|---|---|---|\n| x | 1 | 2 | 3 |\n", 0),
        ("末列合计-错", "| 项 | 甲 | 乙 | 合计 |\n|---|---|---|---|\n| x | 1 | 2 | 4 |\n", 1),
        ("首列合计-对", "| 项 | 甲 |\n|---|---|\n| x | 1 |\n| y | 2 |\n| 合计 | 3 |\n", 0),
        ("首列合计-错", "| 项 | 甲 |\n|---|---|\n| x | 1 |\n| y | 2 |\n| 合计 | 4 |\n", 1),
        ("乘法-对", "共 900×7=6,300 元", 0),
        ("乘法-错", "共 900×7=6,400 元", 1),
        ("加法链-对", "46,400 + 4,000 + 4,000 = 54,400", 0),
        ("加法链-错", "46,400 + 4,000 + 4,000 = 54,500", 1),
        ("围栏不查", "```\n| 项 | 甲 | 合计 |\n|---|---|---|\n| x | 1 | 9 |\n```", 0),
        ("非数字跳过", "| 项 | 甲 | 合计 |\n|---|---|---|\n| x | 待缴 | 9 |\n", 0),
    ]
    ok = True
    for name, text, expect in cases:
        errs = []
        check_tables(strip_fences(text.splitlines()), "<t>", errs)
        check_expressions(text, "<t>", errs)
        got = 1 if errs else 0
        mark = "PASS" if got == expect else "FAIL"
        if got != expect:
            ok = False
        print(f"  [{mark}] {name}（期望退出码 {expect}，实际 {got}）")
    print("selftest:", "全部通过" if ok else "有失败项")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="文档数字对账（只报告，不修改）")
    ap.add_argument("files", nargs="*", help="待检查文件；省略时读 stdin")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    ap.add_argument("--selftest", action="store_true", help="运行内置自测")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    texts = []
    if args.files:
        for f in args.files:
            try:
                with open(f, encoding="utf-8") as fh:
                    texts.append((f, fh.read()))
            except OSError as e:
                print(f"读取失败：{f}（{e}）", file=sys.stderr)
                return 2
    else:
        texts.append(("<stdin>", sys.stdin.read()))

    any_err = False
    results = []
    for path, text in texts:
        errors = []
        check_tables(strip_fences(text.splitlines()), path, errors)
        check_expressions(text, path, errors)
        any_err = any_err or bool(errors)
        results.append({"path": path, "errors": errors})
        if not args.json:
            print(f"文件：{path}")
            if errors:
                print("【算术不一致】")
                for e in errors:
                    print("  ✗ " + e)
            else:
                print("✅ 未发现算术不一致（末列/首列合计、乘法、加法链）。")
            print()

    if args.json:
        print(json.dumps(results if len(results) > 1 else results[0],
                         ensure_ascii=False, indent=2))
    return 1 if any_err else 0


if __name__ == "__main__":
    sys.exit(main())
