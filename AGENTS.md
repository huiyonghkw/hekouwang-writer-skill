# hekouwang-writer-skill · 维护规则

本仓库是一个 Agent Skill（中文文档写作）。运行时入口是 `SKILL.md`；本文件只管"改这个仓库时"的规矩。

## 30 秒速览

- 产品：中文文档写作/体检 skill。技术栈：Markdown + Python 3 stdlib 脚本，零依赖。
- 新内容放哪：规则细节 → `references/`；可执行检查 → `scripts/`；`SKILL.md` 只放铁律、路由和指针。

## 铁律

1. 改 `scripts/*.py` 后必须跑 `python3 scripts/<脚本>.py --selftest`，全部通过才能提交。
2. 改版本号时同步三处：`SKILL.md` 的 `metadata.version`、`_meta.json`、`CHANGELOG.md`。
3. 新增或改名 `references/*.md` 时，同步 `SKILL.md` 指针、`_meta.json` 的 `references` 和 README 目录树。
4. `SKILL.md` 不重复 `references/` 的细节，只留要点 + 一行指针；改完跑 skill doctor 确认无死链、门禁 PASS。

## 禁止清单（Do NOT）

- 不要引入第三方依赖（因为卖点是零依赖、装上即跑）。
- 不要让脚本改写用户文档（因为修订铁律要求改动可列出、可回退，脚本只报告）。
- 不要在 `.learnings/`、`examples/` 写入真实姓名、证件号、令牌（因为仓库会公开分发）。
