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
## [LRN-20261022-001] method

**Logged**: 2026-10-22
**Priority**: high
**Status**: pending
**Area**: deai

### Summary
产品文档去 AI 味时，「分档/决策信息散落多处」是比句法更重的读者负担；盲读实测 10 处。

### Details
hekouwang-terminal-kit README 改写任务：开源/付费分档说明散落在开头两段、3 个 badge、blockquote、对比节、第二章条目标签、第三章整节、付费清单、doctor 免责、安装括号、第七节共约 10 处；「细节去文档站」指针约 7 处。盲读读者（全新上下文子 Agent）明确报告读到第二遍觉得啰嗦。合并动作：删与开头定义段重复的 blockquote；决策句（只用 iTerm2 → 免费，不确定 → 先装免费版）移到开头只留一次；第七节付费清单压缩为指向第三节表格；第九节指针表整删（链接已在别处）。
### Suggested Action
分档、口径、免责类信息默认只完整写两处（开头决策 + 专章节）；其余位置一行指针。晋升候选：同一 Pattern-Key 跨 2 个任务复发即写进文章模式改写清单。
### Metadata
- Source: self_check
- Pattern-Key: doc.tier-info-scattered
- Recurrence-Count: 1

## [LRN-20261022-002] method

**Logged**: 2026-10-22
**Priority**: high
**Status**: pending
**Area**: deai

### Summary
术语首现补人话时，自家产品词（色板/色槽/节）比通用术语更容易漏，读者卡住的正是这些。

### Details
同一任务：盲读读者卡住的位置依次是「16 个色槽」（色板全文无定义）、「第 1～4、6～8 节」（doctor 输出的节，零说明）、「反解」「258ms 是什么的耗时」。通用术语（WCAG、Dynamic Profile）反而不是最卡的。补法：16 个 ANSI 色槽、第 5 节是付费档的全生态同色（不要求）、compinit（zsh 的补全初始化）、正文与底色 5.5:1。每条只补半句，不展开。
### Suggested Action
术语检查清单里加一类「产品自造词」：色板/色槽/档/节/层这类作者以为读者懂的词，首现必须挂半句人话。
### Metadata
- Source: self_check
- Pattern-Key: doc.product-jargon-unexplained
- Recurrence-Count: 1

## [LRN-20261022-003] method

**Logged**: 2026-10-22
**Priority**: medium
**Status**: pending
**Area**: deai

### Summary
第一人称「 credibility 三连」（我每天都在用/我交过学费/不是演示品）连读像自我评价；保留可验证动作，删不可验证声明。

### Details
同一任务：原文「泡在终端时间翻倍」「我交过学费（16 槽错了 8 个）」「这套终端是我自己每天在用的那一套，不是演示品」三段连出。删「不是演示品」（不可验证的自我声明），保留「功能我先在每天用的这台机器上跑通，再写进文档」（可验证动作）和学费故事（带测量数字）。盲读读者原话：像简历自我评价。
### Suggested Action
第一人称锚点按「可验证动作 > 带数字的经历 > 品质声明」排序；同篇品质声明最多一处，没有就删。
### Metadata
- Source: self_check
- Pattern-Key: deai.credibility-claim-cluster
- Recurrence-Count: 1

## [LRN-20261022-004] method

**Logged**: 2026-10-22
**Priority**: medium
**Status**: pending
**Area**: borrow

### Summary
借用 dbs-plain-writing 四块规则的实测结果：四块全部命中，无冲突。

### Details
先借后蒸馏方案（用户 2026-10-22 确认）首次执行。借用项：①产品结构（第一段直接定义对象）——把「同色→同观感」口号位换成定义句，盲读复述测试通过；②理解障碍七查——落为 8 处术语补半句；③体裁服从——README 保留轻销售力（决策句、付费清单在位），未全强度平铺直叙；④禁用清单——删「不是演示品」自我声明与「你要做的是描述结果，不用记命令」口号句。未借用：dbs 的行末去句号（与 voice-samples 冲突，正确）、英文阈值（skill 边界正确）。skill 自带机制全部跑通：事实账 15 项、中档改写、三脚本、盲读子 Agent（5 个可落地发现）、change_list 对账（57 处，2 处数字变动均有解释）。
### Suggested Action
30 天窗口内若第二个真实任务再次借用同几块且无冲突，将①②④蒸馏为文章模式的默认步骤；③保持任务级指令。
### Metadata
- Source: self_check
- Pattern-Key: borrow.dbs-plain-writing
- Recurrence-Count: 1
## [LRN-20261022-005] method

**Logged**: 2026-10-22
**Priority**: medium
**Status**: pending
**Area**: skill-self

### Summary
按与 dbs-plain-writing 的对比结论升级 skill 本身（v1.5.0）：直接吸收 4 处、改造吸收 4 处、明确不借鉴 3 处。

### Details
直接吸收：frontmatter handoff 契约、检查档/格式档豁免（1.1）、用户文字五级优先级表+三硬操作（1.2）、修订档交付前四项（4.3）。改造吸收：句式级黑名单（deai-flavor 一b，补全「词级-句式级-结构级」三级防御的断环）、反例库（新增 references/counter-examples.md，13 组）、clarify 先读再问+提问门槛、README/_meta/CHANGELOG 同步。不借鉴：行末去句号（作者个人文风）、ASD-STE100 官方引用（style-rules 已中文本地化）、最多一问（自己的 3 问+默认值更适合文档场景）。验证：change_list 对账 17 处全部申报（数字变动仅版本号 1.4.0→1.5.0 与日期）；sawdust/doc_lint 对新增内容 0 命中（counter-examples 的命中在反例引文内，文件头已声明预期）；skill doctor 100/100 门禁 PASS。
### Suggested Action
30 天窗口内若第二个真实修订任务再次用到五级优先级表或检查档豁免，将二者从「新增规则」确认常驻；若反例库在体检中从未被引用，考虑合并进 deai-flavor 减文件数。
### Metadata
- Source: self_check
- Pattern-Key: skill-upgrade.dbs-borrow-v150
- Recurrence-Count: 1
