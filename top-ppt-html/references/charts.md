# 图表全库（逻辑索引 · 纪律优先 · 按需取码）

> 本文件已拆分，**禁止整读**物理大文件。§编号跨文件稳定。取码：
> `python scripts/extract_snippet.py --file charts.md --section <编号>`
> 或 `--chart <类型>`（自动路由）。

## 读序（P1-3 facade · 不缩减 registry）

1. **先纪律**：`charts-discipline.md`（§64 合理性 · §66 误用与多样性）——选型与反模式。
2. **核图 8**（Mode A / Fast 默认池）：`bar` · `hbar` · `line` · `donut` · `progress` · `area` · `stack` · `dualline` → 代码在 `charts-basic.md`。
3. **基础扩展**：其余 basic 类型按意图取节（仍属 `charts-basic.md`）。
4. **高级 / extended**：waterfall、sankey 相关形状、boxplot… → **意图命中才读** `charts-extended.md`；勿预读。
5. **信息图页型**（非 `chart.type`）：`infographics.md` §71–§77。

**多样性地板不变**：`charts.variety.minTypes.presentation ≥ 4`（及 B/C 对应下限）；registry 36 种不删。  
**preferCoreFirst**：先拉开核图 8；advanced 使用时**计入** minTypes（不罚），但**禁止预读/默认选用** `charts-extended.md`——仅意图命中时 `extract_snippet.py --chart`；**禁**为凑下限垫冷门图。

| § 范围 | 物理文件 | 何时读 |
|--------|----------|--------|
| §64、§66 | `charts-discipline.md` | **默认先读**（误用/多样性） |
| §16–§31、§29b、§35 等 | `charts-basic.md` | 核图与常规图代码 |
| §52–§70（除纪律节） | `charts-extended.md` | advanced / 意图命中 |

# 图表全库（纯 SVG · `data-chart` 标记）

复制即用。类名依赖 `design-system.md` token；版式见 `components.md`；复杂信息图见 `infographics.md`。

**约定**：图表 svg 一律 `class="chart" data-chart="类型"`（**36 种登记**：donut / multidonut / pie / radar / gauge / rose / bar / stack / stackline / waterfall / line / dualline / area / scatter / bubble / funnel / gantt / hbar / vsbar / treemap / progress / sparkline / sankey / slope / dumbbell / lollipop / marimekko / dotplot / bulletchart / waffle / boxplot / pareto / radialbar / streamgraph / candlestick / network）。事实源 = `scripts/layout-constants.json` → `charts`（`types` + `minSize`）。

> **编号说明**：跨文件唯一稳定编号（§1–§77）。图表 §16–§31、§29b、§35、§52–§70。  
> **六类信息图**（sankey / treemap / boxplot / network / marimekko / streamgraph）**不是** `chart.type`——专属页型见 `infographics.md`。

---

# 第一部分 · 基础图表（核图优先）

> 单维对比 / 趋势 / 占比 / 分布；多系列配色见 §29b。Mode A 默认从核图 8 起选。
