# 图表全库（逻辑索引 · 节级物理文件）

> 本文件已拆分，**禁止整读**。§编号保持不变。取码入口：
> `python scripts/extract_snippet.py --file charts.md --section <编号>`

| § 范围 | 物理文件 |
|--------|----------|
| §16、17、18、19、20、21 … | `charts-basic.md` |
| §52、53、54、55、57、58 … | `charts-extended.md` |
| §64、66 … | `charts-discipline.md` |

原始前言与说明保留如下（规范正文已迁出）。

# 图表全库（纯 SVG · `data-chart` 标记）

复制即用。所有类名依赖 `design-system.md` 的 token；版式与页型见 `components.md`，复杂信息图页型见 `infographics.md`。

**约定**：图表 svg 一律加 `class="chart" data-chart="类型"`（**36 种登记类型**：donut / multidonut / pie / radar / gauge / rose / bar / stack / stackline / waterfall / line / dualline / area / scatter / bubble / funnel / gantt / hbar / vsbar / treemap / progress / sparkline / sankey / slope / dumbbell / lollipop / marimekko / dotplot / bulletchart / waffle / boxplot / pareto / radialbar / streamgraph / candlestick / network），供动效脚本与 `validate_report.py` 识别。**类型登记表与最小尺寸的唯一事实源 = `scripts/layout-constants.json` 的 `charts`**（新增类型必须同时登记 `types` 与 `minSize`）。

> **编号说明**：跨文件唯一稳定编号（§1–§77）。本文件收录图表 §16–§31、§29b、§35、§52–§70。
> **六类信息图**（sankey / treemap / boxplot / network / marimekko / streamgraph）**不作为 `chart.type`**——它们是**专属页型**，HTML 写法见 `infographics.md` §71–§77。

---

# 第一部分 · 基础图表

> 单维对比 / 趋势 / 占比 / 分布等常规图表；多系列配色见 §29b。

