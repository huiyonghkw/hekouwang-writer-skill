# Learnings

 corrections, insights, and knowledge gaps captured during writing work.

**Categories**: correction | insight | knowledge_gap | best_practice
**Status**: pending | in_progress | resolved | promoted | wont_fix

> 记录纪律：立即记、具体、含复现、给修复建议。**记录前脱敏**：不写证件号、电话全号、住址。
> 不想入库的条目不提交即可（见 .gitignore 说明）。

## 晋升规则（写进 SKILL.md 的自进化层）

同一 Pattern-Key 的 Recurrence-Count ≥ 3，且跨 2 个任务、30 天内 → 蒸馏成一条短规则，
晋升进 SKILL.md 的铁律/清单，并在 CHANGELOG.md 记一笔。

---

## [LRN-20261015-001] correction

**Logged**: 2026-10-15T15:31:00
**Priority**: medium
**Status**: resolved
**Area**: structure

### Summary
30秒导航表不是办事文档必备；摘要已写清要做什么、正文 ≤7 节时它和摘要/标题重复。

### Details
修订养老保险办事指南（examples/family-pension-case.md 同一文档）时，用户指出"30秒导航不需要"。skill 原规则把它列为办事文档必备。

### Suggested Action
已改为可选：正文 >7 节或摘要答不了常见问题时才加（write-flow.md、SKILL.md 五轴心、deai-flavor.md 自检第 7 条）。

### Metadata
- Source: user_feedback
- Pattern-Key: structure.navigation
- Recurrence-Count: 1

---

## [LRN-20261015-002] insight

**Logged**: 2026-10-15T15:29:00
**Priority**: medium
**Status**: pending
**Area**: calculation

### Summary
方案对比的指标要剔除"不管选哪个都有"的公共部分，否则会夸大选项差异。

### Details
养老保险档次方案表的"回本时间"= 自筹 ÷ 月养老金，月养老金含 223 元基础养老金（缴满 15 年就有，与选档无关）。按含基础养老金算回本 7.5–9.5 年，只算个人账户约 11 年且四档几乎相同——结论从"高档回本慢一点"变成"档次不影响回本，只影响每月多领多少"。

### Suggested Action
测算类对比表：写明口径；有公共基数时，另给一行"只算增量"的指标。再出现 2 次（跨任务）后晋升进 evidence-and-delivery.md 证据三分的"推断"纪律。

### Metadata
- Source: self_check
- Pattern-Key: calc.common-baseline
- Recurrence-Count: 1

---

## [LRN-20261015-003] best_practice

**Logged**: 2026-10-15T15:36:00
**Priority**: high
**Status**: promoted
**Area**: structure

### Summary
计划、截止日、金额只完整写一处（单一真源）；摘要最多 3 条；失效条件写在行动清单旁和摘要里。

### Details
同一办事指南里三步计划重复 5 处（摘要×2、规则表、时间线、行动清单），改一个截止日要同步 4 处；摘要 6 条；最大风险（政策空档）只藏在依据表。结构调整后三步计划只在"时间线与行动清单"完整出现一次。

### Suggested Action
用户确认后直接晋升（未走 Recurrence ≥3 门槛）：write-flow.md 新增「单一真源」「摘要」两节，办事指南结构合并时间线与行动清单；evidence-and-delivery.md 失效条件写明位置；SKILL.md 第二、四节同步。

### Metadata
- Source: user_feedback
- Pattern-Key: structure.single-source
- Recurrence-Count: 1
