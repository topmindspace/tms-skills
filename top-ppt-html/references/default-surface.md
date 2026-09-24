# 默认生成面（L1.5 · ≤6KB）

> Fast / 标准共用。完整决策见 `playbook.md`；代码用 `extract_snippet.py`。

## 12 默认页型

| 意图 | pageType | skel |
|------|----------|------|
| 封面 | cover | P1 |
| 议程 | agenda | P2 |
| 大数/KPI | kpi | P3 |
| 要点 | points | P4 |
| 卡片 | cards | P5 |
| 指标带 | metrics | P2 |
| 对比 | comparison | P4 |
| 表 | table / halftable | P8 |
| 图证 | exhibit / bar | P8 |
| 双栏论述 | twocol | P6 |
| 结构/泳道 | diagram / lane | P10/P11 |
| 收尾 | closing | P1 |

选型：`recommend_layout.py --mode A|B|C`；矩阵见 playbook §三/§四。

## 8 核心图

`bar` · `hbar` · `line` · `donut` · `progress` · `area` · `stack` · `dualline`

极偏占比 → **禁 donut/pie**，改 KPI/进度/对比条（V3）。简单图禁全幅。

## V1–V4（演示默认）

| V | 结构 | 何时 |
|---|------|------|
| V1 | 主视觉 + 右注解 | 默认图文 |
| V2 | 上图下带 | 总览→分解 |
| V3 | 大数 + 佐证 | 极偏/单点结论 |
| V4 | 双图对照 | 前后/方案 |

## 命令链（模型单写）

```
scaffold_report → 只填 REPORT_MODEL → render_from_model --inplace
→ validate_report --strict --layout-qa → quality_gate --deliver →（可选）pptx
```
