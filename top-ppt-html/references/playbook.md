# 作战手册 · Playbook（唯一常读入口 · L1）

> **每次生成都读这一份，通常就够了。**
> 本文件是**决策层**：定模式、选页型、选版式组合、选图表、定配色、跑校验。
> **代码、几何、穷举表不在本文件**——需要时按 `SKILL.md` 的 L2 路由读深度文件，**读完即停，不预读**。

---

## 〇、排版总序（先骨架后内容 · 整齐优雅）

```
角色 → 预设骨架 P1–P12（layout-grammar.md）→ 元素落位 → 间距 token → 对齐/填充率 → LAYOUT_* 门禁
```

**禁止**临场发明栅格、写死间距、同页两个视觉重心。详规 `references/layout-grammar.md`。

---

## 一、三模式契约（生成时锁定，页面无切换）

| | A 演示汇报 | B 研究报告 | C 信息架构图 |
|--|--|--|--|
| `data-mode` | `presentation` | `research` | `architecture` |
| 阅读契约 | 3 秒一屏，听讲 | 30 秒一页，深读 | 一眼看全结构 |
| 版心 / 正文 | 1400px / 17–18px | 1240px / 14–15px | 1600px / 图注级 |
| 单页文字 | ≤1500 | ≤3200 | ≤600 |
| 并列单元 | ≤8 | ≤12 | 节点 ≤24 |
| 表格行 | ≤8 | ≤16 | 表转图 |
| 每页图表 | **按复杂度定面积**（V1–V4；简单图禁全幅） | 1–2 个（取尺寸下限） | 1 张全幅（宽 ≥85% 版心） |
| 论证结构 | 主张 → 证据 → 休止 | 发现 → 证据 → 含义 + so-what | 标题 → 图 → 图注 |
| Exhibit 编号 | 不用 | **全篇连续 + 来源行** | 不用 |
| 篇幅 | 8–15 页 | 12–25 页 | 1–3 张图（6–8 页） |
| PPTX 正文 | 13pt | 10.5pt | 13pt |

**密度选错的症状**：A 出现双栏小字（投影看不清）→ 拆页；B 出现大面积留白（坐读信息量不足）→ 合页或补证据；C 出现成段正文 → 转图注。
**节奏**：禁止连续 3 页同密度档；同一版式不连用超过 2 页；research 每 3–4 页插一个低密度页（指标带/金句/大数）。

---

## 二、两条生成路径（先判定，再动手）

**轻量路径**（默认）——同时满足：≤12 页 · 材料单一完整 · 无未敲定关键判断 · 用户没要求看框架。
```
Gate 0 参考图 → 六项问询（1 轮）→ 1 张规划卡 → scaffold_report.py → 填内容+模型 → 校验 → 交付
```

**完整路径**（任一命中）——研究 ≥20 页 / 演示 ≥12 页 / 材料量大且杂 / 含未敲定关键判断 / 用户要看框架。
```
Gate 0 参考图 → 六项问询（1 轮）→ 证据表 → 故事线脑暴 → SCR+主张树 → 逐页规划卡 → 大纲确认（1 轮）→ 生成 → 校验 → 交付
```

**预算（硬）**：交互轮次 ≤3；必读文件 = `SKILL.md` + 本文件（≤2 份）；L2 深度文件按需且单份读完即停。

---

## 三、页型选型（意图 → 页型 → 关键约束）

> 穷举表（内容形态 → 版式 → PPTX 页型）见 `components.md` §46；密度档适配见 `components.md` §46b；组合见下节 §四。

| 我要表达 | 首选页型 | 次选 | 关键约束 |
|---------|---------|------|---------|
| 要点式并列主张（默认页） | `points` | `cards` | 每卡 ≤4 条（research ≤5） |
| 现状基线 / 指标快照 | `metrics` | `kpi` | 4–6 个；单数压场用 `kpi` |
| 单个核心数字压场 | `kpi` | `metrics` | hero 一数一结论 |
| 多维对标清单 | `table` | `halftable` | ≤8 行（research ≤16） |
| 时间趋势 / 爬坡 | `bar`（chart.type=line/area/dualline） | `exhibit` | 时间点 >8 改折线 |
| 构成占比 | `donut`（pie/multidonut/waffle） | `halftable` / **V3 KPI** | 扇区 ≤5，最小扇区 ≥8%；**极偏（min&lt;5% 或 max/min&gt;20）禁 donut→V3** |
| 排名 / 大小对比 | `bar`（chart.type=hbar/lollipop/pareto） | `table` | 类别 >8 取 Top 7 + 附录 |
| 现状 vs 目标 | `bullet` / `comparison` | `bar`（vsbar/bulletchart） | 目标线与实际条同量纲 |
| 两期升降（谁升谁降） | `bar`（slope/dumbbell） | `table` | 两端都要标数值 |
| 双维分布 / 优先级 | `bar`（scatter/bubble） | `matrix` | 气泡半径 ∝ √值 |
| 分布 / 离散度 | `boxplot` | `bar`（dotplot） | 组数 ≤8；箱线四件齐备 |
| 增减归因（A→B） | `bar`（waterfall） | `table` | 每段标变化量 + 合计收口 |
| 转化 / 筛选漏斗 | `bar`（funnel） | `sankey` | 层数 ≤5 |
| 计划排期（并行） | `bar`（gantt） | `timeline` | 里程碑叙事用 `timeline`，勿混 |
| 里程碑 / 路线叙事 | `timeline` | `steps` | 3–5 个，每个 ≤2 行 |
| 步骤 / 实施节奏 | `steps` | `timeline` | 3–6 步；高亮步 ≤2 处 |
| 二维强度对标 | `heatmap` | `matrix` | 行列 ≤5×5；只用强调色明度阶梯 |
| 定位 / 优先级 / 象限 | `matrix` | `bar`（scatter） | ≤3×3 |
| 层级递进 / 价值阶梯 | `pyramid` | `diagram` | 3–5 层；强调层 ≤1 |
| 关键判断 / 金句休止 | `quote` | `points` | 全文 1–2 处，多了廉价 |
| 完整论述（发现→证据→含义） | `twocol`（research R1） | `threecol` | 段 ≤200 字；标题必须结论句 |
| 数据证据页（主力） | `exhibit`（R2） | `split` | 全篇 Exhibit 连续编号 |
| 三栏并列论点 | `threecol`（R6） | `cards` | 每栏 ≤150 字 |
| 系统分层架构 | `diagram` | `bar`（chart.type=network） | 节点 ≤24；层 ≤4 |
| 流程 / 职责协作 | `lane` | `diagram` | 每行 ≤6 步；正交折线优先 |
| 素材图片（实拍/截图） | `image` | `split` | 六版式；无图用 `image.placeholder` |
| 待核实项收口 | `flags` 字段 | `table` | 标色必须配说明 |

---

## 三-b、图文演讲版式 V1–V4（演示材料默认构图）

> **何时用**：A presentation 默认；任何「要上台讲」的图文页。目标：**3 秒看清主张，30 秒讲完证据**。
> 简单数据禁止全幅大图；极偏占比禁 donut/pie。

| 版式 | 结构 | 适用 | 视觉:注解 |
|------|------|------|-----------|
| **V1 主视觉+右注解** | 图/照片 55–60% + 3–4 条要点 + so-what | 场景、产品、对比 | 6:4 |
| **V2 上图下带** | 通栏图 50–55% + 指标带/三卡 | 总览→分解 | 55:45 |
| **V3 大数+佐证** | KPI 40% + 小图/迷你表 + 口径 | 极偏占比、单点结论 | 不用 donut |
| **V4 双图对照** | A/B 各 40% + 中缝结论条 | 前后、方案、竞品 | 8:2 |

**硬规则**：
1. ≤2 类占比或 max/min ≥20 或最小扇区 <5% → **V3（KPI/进度/对比条）**，禁 donut/pie。
2. 图旁必须有口头注解 3–4 条（每条 ≤2 行）；禁止「一张图+标题」独页（金句/章节幕除外）。
3. 环图/饼图数值放**图例行**，禁止叠在弧上（治标签叠字）。
4. 全幅图仅限：架构总览 / ≥8 节点结构 / ≥8 系列趋势 / 用户素材大图。
5. 简单图表永不截图；照片只承担情绪/场景。
6. 每 4–6 页插 V3/金句/指标带作节奏休止。

> 废除旧契约「presentation 每页 1 张大图」。图表面积随信息复杂度走（`layout-constants.json` `charts.sizeByComplexity`）。

---

## 四、组合版式矩阵（"内容丰富"的落地方式）

> **先选骨架**：P1–P12（`layout-grammar.md`）；下表是「主件+从件+注释」内容组合，必须落在某 P__ 上。

> **默认一页 = 主件 + 从件 + 注释层**。单件页（只有一张图/一张表）是**例外**（金句/大数/章节幕），不是默认。
> **复杂内容页可扩展组合**：主件 + 双从件、或 `split`/`halftable` 双区并置、或信息图 + 指标带 + so-what + flags——不必强行「一主一从」。先定主件（视觉重心），再从本表挑从件与注释层；表外自由组合须落在已登记页型字段上（否则 PPTX 无法交付）。

| 主件（视觉重心） | 从件（辅助承载） | 注释层 | 页型 | 适用 |
|-----------------|----------------|--------|------|------|
| 图表 | 要点 3–4 条 | so-what / 来源行 | `exhibit` | 证据页主力 |
| 图表 | 要点（左文右图） | so-what | `split` | 结论先行 |
| 图表 | 表格（互证） | 口径行 | `halftable` | 表图对照 |
| 表格（密表） | 图表 | so-what | `halftable` / `split` | 多维对标 |
| 指标带 4–6 个 | 图表 / 小表 | 口径行 | `metrics` | 现状基线 |
| 要点列表 | 指标带 | — | `points`（`metrics` 字段） | 主张 + 基线 |
| 分层架构图 | 图例 chips | 图注 1–2 行 | `diagram`（`legend`） | 架构页 |
| 图片 | 要点 3–4 条 | 图注 + 来源 | `image`（layout=half） | 图文互证 |
| 卡片网格 | 结论条 | — | `cards` / `points` | 并列观察 |
| 双区自由组合 | 左/右各可为 图表·表格·图片·要点·指标 | so-what / flags | `split`（双区升级版） | **组合页通用解** |
| 信息图（桑基/树图/流带…） | 小指标 2–3 / 要点 | 数据表 notes + so-what | 同名信息图页型 | 复杂结构页 |
| 密表 + 图表互证 | 要点摘要 + 指标 | flags | `halftable` + 通用可选件 | 复杂对标页 |

**组合纪律**：
1. **一屏一个视觉重心**——主件明显大于从件；两个并列大件走 `split` 明确左右分工，或拆页。
2. **从件不是装饰**：从件必须承载主件表达不了的信息（趋势、对比、含义），不得复述主件数字。
3. **注释层必写口径**：so-what ≤60 字、来源行写清期间与口径、待核实项走 `flags`。
4. **复杂页允许三承载及以上**：信息图 + 指标 + 要点 + so-what 是合法组合；校验器的「组合版式」按「内容页含 ≥2 种承载」计。
5. 放不下时的顺序是 **优化内容形态 → 升级承载 → 换/扩组合 → 分区 → 拆页 → 有限缩字号**（见 §六与 `containers.fontShrink`）。

---

## 五、图表选型决策树（先问"要回答什么"，再选图）

> 穷举代码见 `charts.md` §16–§31、§35、§52–§70；误用反例与多样性纪律见 `charts.md` §66。
> **默认生成面（P1 收敛）**：优先 `bar / hbar / line / donut / progress / area / stack / dualline`。
> **高级图型**（waterfall/gantt/funnel/slope/… 与 6 类信息图）按需选用，不进默认轮换。
> **纪律**：全篇不同 `data-chart` 类型 ≥ `min(模式上限, ⌈图表页数 × 0.6⌉)`（上限：research 6 / presentation 4 / architecture 3）；**相邻图表页不得同型**。

| 分析意图（读者要得出的结论） | 首选 | 次选 | 禁用 / 改判条件 |
|---------------------------|------|------|----------------|
| 谁大谁小 | `hbar` | `lollipop` / `bar` | 类别 >8 → Top7 + 附录 |
| 随时间怎么变 | `line` | `area` / `dualline` | 时间点 >8 不标点值 |
| 占比是多少 | `donut` | `pie` / `multidonut` | 扇区 >5 → 合并"其他"或 `treemap` |
| 每 1% 的直觉 | `waffle` | `donut` | 类别 >3 改 `marimekko` |
| 结构在变形 | `streamgraph` | `stackline` | 系列 >6 合并 |
| 总量 × 构成双编码 | `marimekko` | `treemap` | 列 >6 / 段 >4 → 拆 |
| 份额悬殊（头部集中） | `treemap` | `donut` | 叶 >16 → 合并小项 |
| 从 A 到 B 是谁贡献的 | `waterfall` | `pareto` | 段 >6 → 合并 |
| 主要矛盾是哪几个 | `pareto` | `waterfall` | 类别 >7 → 合并 |
| 转化/流失在哪一环 | `funnel` | `sankey` | 层 >5 → 改 `hbar` |
| 多对多的流向 | `sankey` | `network` | 节点 >12 / 流带 >24 → 拆页 |
| 谁和谁相连 | `network` | `diagram` | 节点 >18 / 边 >30 → 拆页 |
| 两期谁升谁降 | `slope` | `dumbbell` | 系列 >6 → 取 Top 6 |
| 单指标前后对比（多对象） | `dumbbell` | `vsbar` | 行 >6 → 拆页 |
| 实际 vs 目标（含区间） | `bulletchart` | `bullet` | 行 >6 → 拆页 |
| 达成率（多指标同心） | `radialbar` | `gauge` | 环 >5 → 改 `bullet` |
| 一个值够不够 | `gauge` | `radialbar` | 单值叙事，勿与图并存 |
| 分布不是均值 | `boxplot` | `dotplot` | 组 >8 → 拆页 |
| 双维定位 + 第三维权重 | `bubble` | `scatter` | 气泡 >8 → 标注关键项 |
| 六维能力画像 | `radar` | `rose` | 维度 >6 → 拆两组 |
| 区间波动（开高低收） | `candlestick` | `line` | 蜡烛 >12 → 聚合 |
| 多项目完成度 | `progress` | `bullet` | 行 >6 → 拆页 |
| 迷你趋势（卡内） | `sparkline` | — | 只用于指标卡，不与大图并存 |

**七种最常见的误用（出现即改判）**：
1. 用 `bar` 表达占比 → 改 `donut`/`stackline`/`waffle`。
2. 用 `donut` 表达 8 个类别 → 合并或改 `treemap`。
3. 用 `line` 表达类别对比（无时间轴）→ 改 `hbar`。
4. 用 `table` 表达趋势 → 改 `line`/`area`。
5. 用均值型图表表达分布 → 改 `boxplot`/`dotplot`。
6. 同一页放两张同型图 → 改 `split`/`halftable` 并让两图**编码不同维度**。
7. 多系列图用单色明度阶梯（分不清） → 用 `f-c1~c5` 编码色板（见 §八）。

---

## 六、内容规则（先保全，后呈现 · 细则在 content-rules.md）

**核心判据**：先问 **"这条信息是决策必需的吗？"** —— 是 → **必须进主页面**，再想用什么形态承载；不是但需可查 → 沉图注/来源行/附录；都不是 → 才允许删。**禁止**为排版方便砍口径列/时间列。

**减量顺序（唯一）**：优化内容形态（列表化/精炼）→ 升级承载（文字→表→图）→ 换/扩组合 → 分区 → 拆页 → **最后才**有限缩字号（`containers.fontShrink`）。拆页必须保持信息完整。

**生成时必守五条**：① research 标题即结论（≥12 字，含数字/判断）② 表格正文用 `body` 字号，禁无限缩字号装下 ③ 容器级溢出即失败 ④ 连续语义句不得拆多文本框 ⑤ `.tbd` 必须配图例/flagbar。

> 字数上限、段落→列表转换、表格语义字号、密度三档、去 AI 味写法 → **只读** `content-rules.md`（本节不展开）。

---

## 七、信息图页型族（一张图说清"一整套结构"）

**判据**：普通图表回答"一个数是多少"；信息图页型回答"一整套结构长什么样"。边界表与通用铁律见 `infographics.md`。

| 族 | 页型 | 代码/规格 |
|----|------|----------|
| 统计图形 | `sankey` `treemap` `boxplot` `network` `marimekko` `streamgraph` | `infographics-stats.md` |
| 结构图形 | `flow` `tree` `sequence` `loop`（HTML 主图 SVG）；PPTX 映射 `diagram`/`steps` | `infographics-structure.md` |
| 架构主图 | `diagram`（层≤4/节点≤24）`lane`（每行≤6步） | `layouts-architecture.md` |

**共用纪律（摘要）**：一页一图；采样 ≥16（流带 ≥24）且双边界；禁预设形状；`dataTable` 至少 `notes`；超上限**拆页**。完整上限与写法用 `extract_snippet --chart <类型>` 或上表物理文件。

---

## 八、配色与主题

- **9 套风格**（`styles.md`）：覆盖 8 个色族（蓝 / 藏青 / 蓝青深色 / 黑白 / 红 / 金棕 / 墨绿 / 紫）+ 1 个彩色数据板；`data-style` 即换皮肤，header 可实时切换（交付前切回选定值）。**刻意不再扩张**——新增门槛见 `styles.md` §10。
- **两套颜色职能，纪律不同**：
  - **结构色**（标题/正文/边框/按钮/大面积底色）= **永远中性 + 单一强调色**；层次靠表面明度差 + 1px 边框。禁止渐变、彩色阴影、用红/绿/紫区分模块。
  - **编码色**（图表数据系列 / 图例色点 / 小段标签）= 用 `f-c1~c5` / `s-c1~c5` 语义类，**9 套风格各自有可区分的 `c1..c5`**（不写死 hex，随主题切换）；同屏彩色系列 ≤5。
- **亮暗双主题**：`data-theme="light|dark"`，与 `REPORT_MODEL.theme` 一致；石墨深灰为深色优先（架构模板出厂 dark）；HTML 与 PPTX 同主题导出。
- **强调带**：收尾/CTA 用 `band--accent`（accent-soft）；金句可 `band--accent--solid`；**禁止**用 `band--deep` 作末页（浅色主题下会变深色页）。

---

## 九、校验与交付（命令）

```bash
python scripts/scaffold_report.py --mode research --style mckinsey --theme light \
       --title "报告标题" --sections 8 --out 2026-09-15-主题.html   # 起点（不要手抄模板）
# 或用黄金节奏包：--preset consulting|diagnostic|pitch|ops-review|layered-arch|flow-arch
python scripts/validate_report.py 2026-09-15-主题.html --strict     # HTML 硬门禁（0 FAIL / 0 WARN）
python scripts/extract_model.py   2026-09-15-主题.html              # → .model.json
node  scripts/build_pptx.js 2026-09-15-主题.pptx --model=….model.json
python scripts/validate_pptx.py 2026-09-15-主题.pptx --strict --model=….model.json   # 0/0
```

**交付前必过**：`validate_report.py --strict` 0/0；含 PPTX 时 `validate_pptx.py --strict --model=` 0/0（`pictures` 数 = 声明数）。
**推荐一键门禁**：`python scripts/quality_gate.py 报告.html [--pptx x.pptx --model x.model.json]`（strict + evals + rubric 启发式五维；交付时加 `--deliver` 开关自动产出七要素说明，不要手拼）。
**失败自修复**：按输出逐条修 → 重跑，直到 0/0；修复顺序见 `failure-modes.md`。

---

## 十、L2 节级路由（按任务只读这些，读完即停）

> **不要整读** `components.md` / `charts.md` 背后的物理拆分大文件。需要代码时优先：
> `python scripts/extract_snippet.py --list` · `--task <名>` · `--chart <类型>` · `--page-type <页型>` · `--file components.md --section 46`（逻辑名自动路由）

| 任务 | 只读 |
|------|------|
| research 证据页 / Exhibit / 密表 | `components.md` §36d/§46/§46c · 本文件 §三/§四 · `extract_snippet.py --task research-evidence` |
| 演示组合版式 | `components.md` §39–§42/§46/§46b/§46c · `--task presentation-combo` |
| 架构 / 泳道 / 分层 | `components.md` §37–§38b · `infographics.md` §78–§80 · `--task architecture-diagram` |
| 选图 / 取图表代码 | 本文件 §五 · `--chart <类型>` · 误用见 `charts.md` §66 |
| 密度 / 字数 / 去 AI 味 | `content-rules.md` §一/§四 · 本文件 §六 · `--task content-rules` |
| 素材图片 / 占位 | `components.md` §11c · `--task image-layout` |
| PPTX 精导字段 | `pptx-export.md` · 本文件 §九 · `--task pptx-export` |
| 高保真 / 锚点 | `high-fidelity.md` · `--task high-fidelity` |
| 配色 / 风格 | `styles.md` · `design-system.md` §1a–§1b/§9 · `--task style-theme` |
| 图标 / 语义速查 | `icons.md` · `--task icons` |
| 起骨架用节奏包 | `scaffold_report.py --list-types` → `--preset consulting` 等 |

**纪律**：L0+L1 是默认全部所需；上表命中才开 L2；**读完即执行，不预读下一份**。页型语义槽位见 `scripts/layout_slots.json`（双通道同源 IR）。
**维护者**：改常量/schema/引擎后必跑 `sync_runtime.py` → `audit_styles.py` → `audit_docs.py` → `audit_skill.py` → `build_examples.py` → `regression.py`。
