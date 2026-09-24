# 演示工艺清单 · Presentation Craft（L2 · Mode A）

> **何时读**：Mode A / 正式演示 / 路演 / 演讲 / Fast 演示路径。与 `default-surface.md` 同级常读。  
> **何时不读**：Mode B 密排、Mode C 架构深读（能力保留，不反向污染 A）。  
> **定位**：大气、演讲友好；一屏一主张；图标/图表克制配文——非 gadget deck、非咨询 dump。

## 铁律速查（Hard rules）

| 中文原则 | English | 可执行 |
|----------|---------|--------|
| 一屏一主张 | one idea per slide | 标题即结论；第二主张拆页 |
| 三秒可读 | 3-second / glance rule | 主信息 3 秒可抓；广告牌不是文档 |
| 留白即设计 | whitespace as design | 合法空：封面/章节幕/金句/收尾；内容页半空 = underfill |
| 最后一排 | back of the room | 投影正文宜大；少字号档（display/h1 · body · caption） |
| CRAP | Contrast / Repetition / Alignment / Proximity | 强焦点；跨页 chrome 锁死；左缘顶边齐；相关成组 |
| 行动标题 | action / claim title | 主张句，非「现状分析」式话题标签 |
| 少色单强调 | single accent | 2–3 主色 + 灰阶；1 accent；红仅警示 |
| 图表克制 | restrain / reduce / emphasize | 8 核图优先；简单图禁全幅；极偏禁 donut→V3 |
| 图标语义 | icons as meaning | 约 3–8/屏；固定 px 档；禁表内/图内乱插 |
| **默认无动画** | **motion = none** | 禁炫技转场/飞入作默认；HTML 翻页即可 |
| 无障碍对比 | WCAG AA | 正文 ≥4.5:1；大字/图形 ≥3:1；不靠颜色单独编码 |
| 舞台纪律 | 16:9 stage | 安全边距；一屏一重心；同页双大件 FAIL |

## 默认面（与 default-surface 对齐）

- **页型**：12 默认页型；主力 **V1–V4 / P1–P4** 解决约 80% 页。
- **P5–P12 / advanced 图**：按需，不进 A 默认轮换。
- **核图 8**：`bar` · `hbar` · `line` · `donut` · `progress` · `area` · `stack` · `dualline`。
- **多样性**：按内容选型拉开图种（核图优先；advanced 意图命中再用）；禁为过门禁硬上冷门图。

## 交付门禁（Mode A）

```
validate_report.py --strict   # presentation 自动隐含 --layout-qa
quality_gate.py … --deliver   # 同口径
```

检查：V 契约 · 简单全幅 · 骨架连用 · 主张标题 WARN · 核图多样性 · WCAG（audit_styles）。

## 自检（上台前 30 秒）

- [ ] 标题是主张句，不是话题词  
- [ ] 眯眼可见：一条左线、一条顶线、一块重心  
- [ ] 休止页有意留白；内容页不无故半空  
- [ ] 无多强调色、无动画墙、无冷门图硬凑  
- [ ] `motion = none`；翻页靠内容节奏  

> *Hard rules protect the stage; adaptive choices serve the content.*
