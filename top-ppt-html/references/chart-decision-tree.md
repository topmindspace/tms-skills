# 图表选型决策树（L2）

> **何时读**：选图 / 分析意图→图型；常读入口仍是 `playbook.md` §五（核图 8 + 多样性摘要）。读完即停。
> 完整登记与代码 → `extract_snippet.py --chart <类型>`；误用纪律 → `charts.md`（先 `charts-discipline`，核图 8，extended 按需）。

## 决策表

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

## 七种最常见的误用（出现即改判）

1. 用 `bar` 表达占比 → 改 `donut`/`stackline`/`waffle`。
2. 用 `donut` 表达 8 个类别 → 合并或改 `treemap`。
3. 用 `line` 表达类别对比（无时间轴）→ 改 `hbar`。
4. 用 `table` 表达趋势 → 改 `line`/`area`。
5. 用均值型图表表达分布 → 改 `boxplot`/`dotplot`。
6. 同一页放两张同型图 → 改 `split`/`halftable` 并让两图**编码不同维度**。
7. 多系列图用单色明度阶梯（分不清） → 用 `f-c1~c5` 编码色板（见 playbook §八）。
