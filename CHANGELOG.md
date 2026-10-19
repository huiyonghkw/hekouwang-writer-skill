# Changelog

## v1.2.2（2026-10-19）

- 文章模式新增第 7 类诊断与**白话硬门**：禁止「除雾权」「权限冲突」「抢回／还回」等文学隐喻，机制与改法写成可照做的句子。
- 将制作日历、发现路径、白话三条正文禁写收成 `article-mode.md` §2.1 速查表（与 1.2.1 日期/来源禁令并列）。

## v1.2.1（2026-10-19）

- 文章模式改写增两项硬清理：去掉正文/图注/页眉的制作日历（拍摄日、截图时分、研究截点、检索日）；去掉「在 B 站/小红书/抖音搜了…」及平台检索样本来源脚注。细则见 `references/article-mode.md`。

## v1.2.0（2026-10-15）

- **并入 hekouwang-deai-skill，新增文章模式**（SKILL.md 1.3 节、`references/article-mode.md`）：公众号文章、长文章母版、文案的去 AI 味。六类诊断（没有"我"、破折号过多、工整对仗、无据拔高词、章节符号、空泛总结或产品页腔调）+ `sawdust_scan.py`；改写补 2–4 处作者真实在场的第一人称锚点，素材里没有就问，不编经历；输出诊断清单 → 改写文本 → 事实保留说明 → 锚点数。
- 文档模式不补第一人称。description 加入去AI味、人性化、润色文章/文案、`/deai` 触发词，去掉"交给 hekouwang-deai-skill"的边界。
- 会勇禾口王内容工作流的 `/deai` 入口、运行时合同和外部依赖清单改指向本 skill。

## v1.1.0（2026-10-15）

- 修复：`sentence_load.py`、`doc_lint.py` 省略文件参数、从 stdin 读文本时崩溃（`texts` 未初始化）。
- `sentence_load.py` 新增 `--json` 输出（over / warn_items / stacked / nested / hard），selftest 增至 6 项。
- 四把检查器的 stdin + `--json` 定为对外接口，字段只增不改。dianping-review-skill 1.2.0 起在运行时依赖本 skill，用它的规则拦截点评文案。

## v1.0.0（2026-10-15）

初版。发布前将 P0/P1/P2 改进全部并入，**未升版本号**（从未推送远程，无历史包袱）。

- 三大铁律、三档路由、修订模式、WRITE 五步法、句法纪律、五轴心、出口闸门、去AI味（G1-G5 / P1-P3）、learnings 台账。
- 四把检查器全部带 `--selftest`；新增 `check_fidelity.py`（数字对账，含数值型表头求和、围栏跳过、非数字跳过）。脚本均为原创实现（思路借鉴，代码自研）。
- 新增 `references/clarify-questions.md`（澄清清单）与 `references/glossary.md`（术语表机制）；`.learnings/` 台账模板入库。
- 边界补充英文适用范围声明（英文按词数另设阈值，未实现，记为 FEAT 待办）。
- README 补 5 分钟上手与 CI 接入。
- 在王女士城乡居民养老保险文档（真实家庭办事稿）上完成回归：锯末词 0 命中、必拆长句 0、doc_lint 与 check_fidelity 退出码均 0（补差表 6 行、共入账行 17 列、对账等式链全部验算通过）。
- 发布前按 skill doctor / md doctor 体检重构：SKILL.md 改为路由入口，细则下沉并指向 `references/`；description 补与 hekouwang-deai-skill 的分界；脚本与 `.learnings/` 路径改为相对 skill 目录；`version` 收进 `metadata`；版本历史移入本文件；新增维护者 `AGENTS.md`。
- 按养老保险办事指南的二次修订复盘补规则：30秒导航改为可选；新增「单一真源」（计划/日期/金额只完整写一处，办事指南合并时间线与行动清单）与「摘要最多 3 条」；失效条件须写在行动清单旁和摘要里；修订回退方式（git → 改动清单 → 用户决定的备份）；自检清单加日期冲突、单一真源、敏感信息三条。
- `doc_lint.py`：新增完整身份证号/手机号告警；同义词检查识别文档里 `简称"X"` / `称"X"` 声明过的叫法，不再误报；selftest 增至 13 项。
- `.learnings/` 记入 3 条（导航纠正、回本口径、单一真源晋升）。
- 参考 ClawHub/SkillHub 同类 skill（chinese-official-writing、Claim Verifier、写作全流程助手）补 5 项：新增 `change_list.py`（改前/改后改动清单 + 数字变动告警，selftest 6 项）并接入修订模式第 6 步；审稿意见按性质分三级（已证实错误 / 依据不足待核 / 可选表达建议）；时效事实核查的触发条件、一次补搜即停的停止规则、依据表访问日期；真实稿 / 试写稿分流；边界新增协作分工表。进度卡等过程信息不写进用户文档。
- `change_list.py`：数字识别不再把中文逗号当千分位（实战误报），selftest 增至 7 项。
- 首次公开发布：许可证改为 MIT-0；案例去真名（`examples/family-pension-case.md`）；`doc_lint.py` 自检改用编造的测试身份证号；frontmatter `metadata` 补 SkillHub 所需的 slug / displayName / summary / homepage。

### 方法论来源与验证状态

| 来源 | 借鉴内容 | 验证状态 |
|---|---|---|
| kunlun-doc-write / doc-write | WRITE 流程、每节核心句、边界声明 | 实战验证（多轮改文档） |
| universal-writer | 出处铁律、修订模式、进度卡、风险告知格式 | 实战验证 |
| asd-ste100 | 句法纪律、模态保留、一词一义 | 实战验证（含 17 处误报调优） |
| chenlin-credible-translate | 五轴心、禁止层 P1-P3、G1-G5、机械检查思路 | 实战验证 |
| dev-god | 证据三分、诚实状态标签、降级三件套 | 实战验证 |
| dev-expert | 三档机制、出口闸门思想 | 实战验证 |
| parenting-expert | 边界显式声明、自检清单、最少输入原则 | 实战验证 |
| tencent-docs | 场景路由表 | 实战验证 |
| self-improving-agent | learnings 台账与晋升规则 | 机制就位，**未经时间检验** |
