# hekouwang-writer-skill

**会勇禾口王 · 写作技能** —— 把任何素材写成**结构清晰、内容易懂、数字可对账**的中文文档；公众号文章、长文章母版和文案的去 AI 味也在这里（文章模式）。

一句话方法论：**先想清楚写给谁、用来做什么，再用纪律把内容装进结构。**

## 它解决什么问题

AI 写的文档常见五宗罪：结论埋在第六节、一段塞三个事实、数字对不上、术语前后不一、"AI 味"扑面而来。本技能用一套可执行的流程 + 四把机械检查器治这五件事。

## 两种模式

| 模式 | 对象 | 做什么 |
|---|---|---|
| 文档模式（默认） | 方案、报告、说明、办事指南、家庭文档、邮件、汇报 | 结构化写作、修订、文档体检；不补第一人称 |
| 文章模式 | 公众号文章、长文章母版、文案 | 先诊断再改写去 AI 味：补 2–4 处作者真实在场的第一人称，处理破折号、对仗、拔高词；保留事实、原意和信息密度 |

文章模式由原 [hekouwang-deai-skill](https://github.com/huiyonghkw/hekouwang-deai-skill) 并入（v1.2.0），`/deai` 入口改由本 skill 承接。

## 五层架构

| 层 | 管什么 | 核心产出 |
|---|---|---|
| 路由层 | 请求三档（轻量/常规/复杂）+ 场景路由表 + 修订模式 | 什么文档用什么结构 |
| 骨架层 | 澄清清单 + WRITE 五步法（Who→Why→How→Draft→Polish） | 每节一句核心句的骨架 |
| 文风层 | 句法纪律：一句一事、≤45/60字、一词一义、模态保留 | 无歧义短句 |
| 质量层 | 五轴心 + 出口闸门两问 + 交付格式 + 降级三件套 | 可核对的交付物 |
| 自进化层 | learnings 台账 + 晋升规则 | 越用越准 |

## 三大铁律

1. **出处铁律**：政策、数字、专有名词必须有出处；查不到标注"暂无出处"，不编造。
2. **模态铁律**："可能/约/待核实"是内容不是噪音，简化时原样保留。
3. **修订铁律**：改文档保留事实与意图，每处改动列出、可回退。

## 5分钟上手

1. 说"写一份XX文档"或"帮我改这份文档"即触发；信息不够时最多问 3 个问题（读者/用途/篇幅），其余用默认值，不连环追问。
2. 拿到稿后跑一遍体检：
   ```bash
   python3 scripts/sawdust_scan.py   文档.md  # AI味（锯末词密度）
   python3 scripts/sentence_load.py  文档.md  # 长句/分句堆叠/修饰嵌套/分号
   python3 scripts/doc_lint.py       文档.md  # 表格列数/标题跳跃/同义词轮换/待核实项
   python3 scripts/check_fidelity.py 文档.md  # 数字对账：合计行/列、乘法、加法链
   ```
3. 有告警逐条处理；放行项（公式/等式链/操作路径/联系人行）注明理由，不硬拆。

## 四把检查器（只报告，不修改；纯 stdlib；全带 --selftest）

| 脚本 | 查什么 | 硬错误退出码 1 |
|---|---|---|
| sawdust_scan.py | 锯末词密度（阈值 3 处/千字） | 否（advisory） |
| sentence_load.py | 句长/分句堆叠/修饰嵌套 | 否（advisory） |
| doc_lint.py | 表格列数一致性、标题层级跳跃（硬错误）；同义词轮换、敏感信息（告警） | **是** |
| check_fidelity.py | 算术不一致（合计/乘法/加法链） | **是** |

修订时另有一个对账工具：`change_list.py 改前.md 改后.md` 列出两稿全部改动处并标出数字变动，用来核对手写改动清单有没有漏项（`--strict-numbers` 时数字变动退出码 1）。

改动脚本前先跑 `python3 scripts/<脚本>.py --selftest`。

## 被其他 skill 调用

四把检查器都支持从 stdin 读文本、`--json` 输出，字段只增不改，可以当接口用：

```bash
echo "$TEXT" | python3 "$SKILL_DIR/scripts/sawdust_scan.py" --json    # over / density / findings
echo "$TEXT" | python3 "$SKILL_DIR/scripts/sentence_load.py" --json   # over / warn_items / stacked / hard
echo "$TEXT" | python3 "$SKILL_DIR/scripts/doc_lint.py" --json        # hard_errors / warnings
echo "$TEXT" | python3 "$SKILL_DIR/scripts/check_fidelity.py" --json  # errors
```

已接入：[dianping-review-skill](https://github.com/huiyonghkw/dianping-review-skill) >= 1.2.0，它的内容检查按这里的规范拦截点评文案。

## 接入 git hook / CI

```bash
#!/bin/sh
# .git/hooks/pre-commit：只查暂存区里改动的 .md
SKILL_DIR="$HOME/.codebuddy/skills/hekouwang-writer-skill"  # 改成你的实际安装位置
files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$')
[ -z "$files" ] && exit 0
python3 "$SKILL_DIR/scripts/doc_lint.py" $files && python3 "$SKILL_DIR/scripts/check_fidelity.py" $files || exit 1
```

## 目录结构

```
hekouwang-writer-skill/
├── SKILL.md                      # Agent Skill 主文件（铁律+路由+流程要点+指针，细则在 references/）
├── AGENTS.md                     # 维护本仓库时的 Agent 规则
├── README.md
├── CHANGELOG.md
├── LICENSE                       # MIT-0
├── _meta.json
├── .gitignore
├── .learnings/                   # 自进化台账模板（LEARNINGS/ERRORS/FEATURE_REQUESTS）
├── references/
│   ├── write-flow.md             # WRITE 操作卡 + 七种文档原型 + 进度卡模板
│   ├── style-rules.md            # 句法纪律完整表 + 放行项判定流程
│   ├── deai-flavor.md            # 锯末词表 + G1-G5 + P1-P3 + 自检清单
│   ├── article-mode.md           # 文章模式：六类诊断 + 改写 + 输出格式（原 deai-skill）
│   ├── evidence-and-delivery.md  # 证据三分 + 出口闸门 + 降级三件套 + learnings 格式
│   ├── clarify-questions.md      # 动笔前澄清清单（分文体五问 + 三方向选择法）
│   └── glossary.md               # 术语表机制（一词一义的数据源）
├── scripts/                      # 四把检查器（原创实现）
│   ├── sawdust_scan.py           # 锯末词密度
│   ├── sentence_load.py          # 句长/分句堆叠/修饰嵌套/分号
│   ├── doc_lint.py               # 表格列数/标题跳跃/同义词轮换/待核实项
│   ├── check_fidelity.py         # 算术对账：合计行/列、乘法、加法链
│   └── change_list.py            # 修订对账：改前/改后全部改动处 + 数字变动
└── examples/
    └── family-pension-case.md    # 实战案例（已脱敏）：方法如何落地
```

## 作为 Agent Skill 安装

拷贝到 skill 目录即可（CodeBuddy：`~/.codebuddy/skills/`）：

```bash
cp -r hekouwang-writer-skill ~/.codebuddy/skills/
```

SKILL.md 的 frontmatter `description` 已含触发词，加载后由"写文档/改文档/去AI味/文档体检"等意图自动触发。

## 方法论来源（致谢）

本技能的方法论提炼自以下 9 个公开 skill 与 1 个标准，代码为原创实现：

- **kunlun-doc-write / doc-write**（昆仑增长）：WRITE 流程、每节核心句、边界声明
- **universal-writer**：出处铁律、修订模式、进度卡、风险告知格式
- **asd-ste100**（GitHub: danyuchn/asd-ste100-skill）：句法纪律、模态保留、一词一义
- **chenlin-credible-translate**（真笔翻译）：五轴心、禁止层 P1-P3、G1-G5、机械检查思路
- **dev-god**（SkillHub 下载量第1）：证据三分、诚实状态标签、降级三件套
- **dev-expert**（第2）：三档机制、出口闸门思想
- **parenting-expert**（第3）：边界显式声明、输出前自检、最少输入原则
- **tencent-docs**（第4）：场景路由表
- **self-improving-agent**（第5）：learnings 台账与晋升规则
- **ASD-STE100 Issue 9**（2025-01）：受控语言标准本身

## 版本历史

见 [CHANGELOG.md](CHANGELOG.md)。
