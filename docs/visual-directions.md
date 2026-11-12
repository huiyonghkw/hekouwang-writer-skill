# 视觉方向选型卡（给 Agent / Skill 产品页）

本文件给智能体设计网页时选型用。一次只锁 **一个主方向**，最多加 **一个辅方向**。先定内容骨架，再选视觉；不要先堆效果。

## 给 Agent 的固定指令格式

下设计任务时按这四字段写：

1. **方向名**：从下文清单选一个主方向（可选一个辅方向）
2. **气质一句话**：给谁看、什么感觉
3. **硬约束**：颜色 / 字体 / 首屏预算 / 禁止项
4. **对标站**：1–2 个；要求「像气质，不抄结构」

### 通用禁止项（默认写入）

- 紫–靛渐变、大面积 glow、满屏卡片仪表盘
- 奶油底 + 强衬线 + 赤陶默认脸（除非明确选 Warm Organic）
- 假 UI mock、无出处数字、装饰性 emoji 堆砌
- 首屏塞统计条、日程、多段营销文案（首屏只留品牌 + 一句标题 + 一句说明 + CTA + 一个主视觉）

---

## 本仓库现状

| 项 | 说明 |
|---|---|
| 当前主方向 | Atelier 纸面（偏 Editorial + 轻 Evidence） |
| 落地页 | `docs/index.html`、`docs/cases/*` |
| 共享 token | `docs/tokens.css` |
| 若继续强化差异 | 优先试 **Evidence Desk** 或 **Typeset Terminal** |

**Atelier 纸面（已用，不在下方 12 类重复展开）**  
暖灰纸底、柔光层次、墨青强调、纸上时间轴证据链、字标 + SVG icon。气质：安静工作室里摊开的校对稿。

---

## 12 个可选方向

### 1. Editorial Print（杂志 / 印刷编辑风）

- **信号**：大衬线或强对比标题、短行宽、页边空白、脚注/边注、少卡片
- **适合**：写作、研究、质控、方法论 Skill
- **案例**：[Linear](https://linear.app)、[ReadMe](https://readme.com)、[Footnote 模板](https://framplates.com/footnote)
- **风险**：做成报纸密栏；别堆细线与多栏正文

### 2. Typeset Terminal（排版终端 / 开发工具纸白）

- **信号**：白底、极克制字重、等宽代码块、几乎无装饰
- **适合**：CLI、检查脚本、安装页、技术可信度优先
- **案例**：[Vercel](https://vercel.com)、[Resend](https://resend.com)、[Cursor](https://cursor.com)
- **风险**：过平会像「又一个 AI 工具」；靠排版精度取胜

### 3. Midnight Instrument（深夜精密仪器）

- **信号**：深色底、细高对比、仪表感、冷色点缀（非霓虹）
- **适合**：监控、安全、自动化 Agent、运维类
- **案例**：[Warp](https://www.warp.dev)、[Neon](https://neon.tech)、Linear 深色产品感
- **风险**：默认深色易滑向「AI 紫光」；禁止 glow 堆叠

### 4. Swiss Modern（瑞士国际主义）

- **信号**：网格、左对齐、无衬线、功能优先、少情绪色
- **适合**：规范、标准、企业文档、设计系统说明
- **案例**：[Embru](https://www.embru.ch/en/products/moser-armchair)、[horgenglarus](https://horgenglarus.com/en/collection/chairs/lyra)
- **风险**：冷、硬、品牌记忆弱；要靠秩序与留白建立品质

### 5. Soft Brutalism（软粗野）

- **信号**：粗边框、大字、不规则块、低装饰、结构外露
- **适合**：独立站、工作室、有态度的小产品
- **案例**：[Lyon Béton](https://lyonbeton.com)
- **风险**：易丑；中文必须控行长、字号与对比度

### 6. Gallery / Lookbook（画廊图录）

- **信号**：大幅留白、作品图主导、极简导航、像展览
- **适合**：视觉类 Skill、作品集、模板库
- **案例**：家具/物件品牌产品页（Embru、horgenglarus）；画廊式作品站
- **风险**：文案型 Skill 没真图会空；需要真实截图或证据图

### 7. Product UI First（产品界面即主视觉）

- **信号**：首屏就是真实 UI / 终端 / 报告截图，文案让位
- **适合**：有明确界面或报告输出的 Agent
- **案例**：[Notion](https://www.notion.com)、[Figma](https://www.figma.com)、[Supabase](https://supabase.com)
- **风险**：假 mock 一多就假；报告型应用真实输出片段

### 8. Docs-as-Product（文档即产品）

- **信号**：侧栏、搜索、窄正文栏、代码面、版本与锚点导航
- **适合**：Skill 说明书、API、安装与规则页
- **案例**：[Stripe Docs](https://stripe.com/docs)、[Cloudflare Docs](https://developers.cloudflare.com)、[Mintlify](https://mintlify.com)、[Protocol 模板说明](https://tailwindcss.com/blog/2022-12-15-protocol-api-documentation-template)
- **风险**：营销首页硬套 docs 布局会沉闷

### 9. Evidence Desk / Audit Bench（证据台 / 审计台）

- **信号**：前后对照、表格、时间轴、印章式状态、可核对数字
- **适合**：质控、合规、对账、体检类 Skill（贴近本仓库定位）
- **案例**：审计/报告型产品页；[PostHog](https://posthog.com)（产品 + 证据叙事）；本仓库案例页可继续强化
- **风险**：表格墙像后台；要「证据镜头」，不是全量数据倾倒

### 10. Warm Organic Editorial（暖色有机编辑）

- **信号**：象牙底、赤陶点缀、插画/植物几何、叙事感
- **适合**：生活方式、教育、温和陪伴型 Agent
- **案例**：Organic Editorial SaaS 类设计说明（如 [Devault 条目](https://devault.design/design-md/exclusive-web/organic-editorial-saas--20aeb07e)）
- **风险**：极易撞「奶油底 + 衬线 + 赤陶」AI 默认脸；非明确选择勿用

### 11. Motion-Led Spatial（动效主导空间）

- **信号**：滚动叙事、图层位移、光影过渡；靠 motion 建层级
- **适合**：品牌故事、高端工具发布页
- **案例**：[GSAP](https://gsap.com)、部分 Awwwards 叙事站
- **风险**：可读性下降；Skill 页只保留 2–3 个意图动效

### 12. Bento System（便当格系统面板）

- **信号**：不规则格网、功能块拼贴、信息密度中高
- **适合**：功能很多的平台型 Agent / 工具箱
- **案例**：[Apple](https://www.apple.com) 产品区块、现代 SaaS feature bento
- **风险**：AI landing 高发区；格太多会像仪表盘

---

## 对照速查

| 方向 | 信任感 | 品牌感 | 信息密度 | 最适合的 Skill 类型 |
|---|---|---|---|---|
| Editorial Print | 高 | 高 | 中 | 写作 / 研究 |
| Typeset Terminal | 很高 | 中 | 中高 | CLI / 检查 |
| Midnight Instrument | 高 | 中高 | 高 | 监控 / 安全 |
| Swiss Modern | 高 | 中 | 中 | 规范 / 标准 |
| Soft Brutalism | 中 | 很高 | 中 | 个性品牌 |
| Gallery | 中 | 很高 | 低 | 视觉作品 |
| Product UI First | 很高 | 中 | 高 | 有界面产品 |
| Docs-as-Product | 很高 | 低 | 很高 | 说明书 |
| Evidence Desk | 极高 | 中 | 高 | 质控 / 对账 |
| Warm Organic | 中 | 高 | 低中 | 温和教育 |
| Motion-Led | 中 | 很高 | 低 | 品牌发布 |
| Bento | 中 | 中 | 很高 | 多功能平台 |

---

## 组合建议（主 + 辅）

| 场景 | 推荐主方向 | 可选辅方向 |
|---|---|---|
| 写作质控落地页 | Evidence Desk | Editorial Print |
| 安装 / CLI 说明 | Typeset Terminal | Docs-as-Product |
| 案例证据页 | Evidence Desk | Product UI First（真实报告片段） |
| 视觉 / 主题 Skill | Gallery | Motion-Led（克制） |
| 平台型工具箱 | Bento | Typeset Terminal |
| 规范 / 标准说明 | Swiss Modern | Docs-as-Product |

中文场景优先：**Editorial Print / Evidence Desk / Typeset Terminal**；Brutalism 与强 Motion 需额外过中文可读性检查。

---

## 选型检查（交稿前）

1. 去掉导航后，首屏是否仍能认出品牌？
2. 是否只有一个主方向，没有混成「又紫又纸又 bento」？
3. 主视觉是真实产品证据，还是装饰渐变？
4. 数字、出处、脚本边界是否仍可读、可核对？
5. 移动端首屏是否仍只做一件事？

---

## 维护

- 新增方向：补「信号 / 适合 / 案例 / 风险」四行，并更新对照表。
- 本仓库改视觉时：在「本仓库现状」更新主方向名，并在 `CHANGELOG.md` 记一笔。
