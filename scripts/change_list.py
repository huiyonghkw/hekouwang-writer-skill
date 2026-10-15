#!/usr/bin/env python3
"""change_list.py — 修订改动清单生成器（hekouwang-writer-skill）

对比改前稿与改后稿，列出全部改动处（位置 + 改前 → 改后），
用来和手写的改动清单对账：脚本列出、手写清单没有的，就是"悄悄改了"。

另查一类高风险改动：
  - 数字变动：改前片段里的数字在改后片段里消失或变了（修订铁律：数字原样不动）

只报告，不修改任何文件。

用法：
    change_list.py 改前.md 改后.md
    change_list.py --json 改前.md 改后.md
    change_list.py --strict-numbers 改前.md 改后.md   # 有数字变动时退出码 1

退出码：读取失败 = 2；--strict-numbers 且有数字变动 = 1；否则 = 0。
"""

import argparse
import difflib
import json
import re
import sys

NUM_RE = re.compile(r"\d+(?:,\d{3})*(?:\.\d+)?")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")
SNIPPET = 60


def numbers(text):
    return [n.replace(",", "") for n in NUM_RE.findall(text)]


def clip(s):
    s = " ⏎ ".join(x.strip() for x in s.strip().splitlines() if x.strip())
    return s if len(s) <= SNIPPET else s[:SNIPPET] + "…"


def nearest_heading(lines, idx):
    for i in range(min(idx, len(lines) - 1), -1, -1):
        m = HEADING_RE.match(lines[i])
        if m:
            return m.group(2).strip()
    return "（文首）"


def char_diff(a, b):
    """只取变化的片段，前后带少量上下文；相距很近的改动合并成一处。"""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    for group in sm.get_grouped_opcodes(8):
        i1, j1 = group[0][1], group[0][3]
        i2, j2 = group[-1][2], group[-1][4]
        out.append((a[i1:i2], b[j1:j2]))
    return out


def diff(before, after):
    a_lines, b_lines = before.splitlines(), after.splitlines()
    sm = difflib.SequenceMatcher(None, a_lines, b_lines, autojunk=False)
    changes = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        old_block = a_lines[i1:i2]
        new_block = b_lines[j1:j2]
        where = f"改后 L{j1 + 1}" if new_block else f"改前 L{i1 + 1}"
        section = nearest_heading(b_lines, j1) if new_block else nearest_heading(a_lines, i1)
        if op == "replace":
            pairs = char_diff("\n".join(old_block), "\n".join(new_block))
        else:
            pairs = [("\n".join(old_block), "\n".join(new_block))]
        for old, new in pairs:
            if not old.strip() and not new.strip():
                continue
            lost = [x for x in numbers(old) if x not in numbers(new)]
            kind = {"insert": "新增", "delete": "删除"}.get(op, "修改")
            changes.append({
                "kind": kind,
                "where": where,
                "section": section,
                "before": old,
                "after": new,
                "numbers_changed": lost,
            })
    return changes


def selftest():
    cases = [
        ("无改动", "甲。\n乙。\n", "甲。\n乙。\n", 0, False),
        ("改一处措辞", "## 一\n窗口进行核定。\n", "## 一\n窗口核定。\n", 1, False),
        ("新增一行", "甲。\n", "甲。\n乙。\n", 1, False),
        ("删除一行", "甲。\n乙。\n", "甲。\n", 1, False),
        ("数字被改", "补缴4,000元。\n", "补缴5,000元。\n", 1, True),
        ("数字原样", "补缴4,000元，约。\n", "补缴4,000元。\n", 1, False),
        ("中文逗号不是千分位", "（2026-10-14，0827-3369682）\n", "（0827-3369682）2026-10-14\n", 1, False),
    ]
    ok = True
    for name, a, b, n, num_flag in cases:
        ch = diff(a, b)
        got_flag = any(c["numbers_changed"] for c in ch)
        good = len(ch) == n and got_flag == num_flag
        ok = ok and good
        print(f"  [{'PASS' if good else 'FAIL'}] {name}（期望 {n} 处/数字告警 {num_flag}，"
              f"实际 {len(ch)} 处/{got_flag}）")
    print("selftest:", "全部通过" if ok else "有失败项")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="对比改前/改后稿，列出全部改动处")
    ap.add_argument("before", nargs="?", help="改前稿")
    ap.add_argument("after", nargs="?", help="改后稿")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    ap.add_argument("--strict-numbers", action="store_true", help="有数字变动时退出码 1")
    ap.add_argument("--selftest", action="store_true", help="运行内置自测")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()
    if not (args.before and args.after):
        ap.error("需要两个文件：改前稿 改后稿")

    texts = []
    for f in (args.before, args.after):
        try:
            with open(f, encoding="utf-8-sig") as fh:
                texts.append(fh.read())
        except OSError as e:
            print(f"读取失败：{f}（{e}）", file=sys.stderr)
            return 2

    changes = diff(*texts)
    num_hits = [c for c in changes if c["numbers_changed"]]

    if args.json:
        print(json.dumps(changes, ensure_ascii=False, indent=2))
    else:
        print(f"改前：{args.before}\n改后：{args.after}")
        print(f"改动 {len(changes)} 处    其中数字变动 {len(num_hits)} 处")
        print("-" * 62)
        for i, c in enumerate(changes, 1):
            flag = "  ⚠ 数字变动：" + "、".join(c["numbers_changed"]) if c["numbers_changed"] else ""
            print(f"{i}. [{c['kind']}] {c['where']} · {c['section']}{flag}")
            if c["before"].strip():
                print(f"   改前：{clip(c['before'])}")
            if c["after"].strip():
                print(f"   改后：{clip(c['after'])}")
        if not changes:
            print("✅ 两稿一致。")
        print("\n【对账】逐条核对手写改动清单：脚本有、清单没有的改动 = 未申报改动，补进清单或还原。")

    return 1 if (args.strict_numbers and num_hits) else 0


if __name__ == "__main__":
    sys.exit(main())
