---
name: top-ppt-html
description: "TopPPT HTML：报告 / 演示 / 信息架构图生成器。单文件零外链 HTML（可翻页、亮暗双主题）+ 版式保真的原生可编辑 16:9 PPTX。三模式（A 演示·每屏一主张 / B 研究·咨询密排 / C 架构·图为王）× 9 风格；布局骨架 P1–P12；内容只填 REPORT_MODEL，render_from_model 回填正文；strict 0/0 才交付。Use when 用户要做报告、演示、汇报、PPT、slides、deck、路演，或写研究报告、分析报告、咨询报告、白皮书、调研、评测、对标、经营分析、复盘、项目汇报、商务/HTML/网页报告，或做架构图、拓扑图、流程图、泳道图、方案图，或把材料/数据做成可视化报告，或导出 HTML/PPT/PPTX（保真、可编辑、高保真、1:1），或优化排版、版式、配色、密度、图文布局。Do NOT use for 纯代码工程、非报告类网页或应用开发、视频/图片生成、直接改写已有 Word/PPT 源文件本身。"
---

# TopPPT HTML

**让 idea 飞，好想法被看见。** 一套技能、三种模式、两种交付：**单文件 HTML 报告**（可翻页、可演示、header 自带工具栏）+ **版式保真的原生可编辑 PPTX**（智能体精导唯一交付通道）。两者同源于一个内容模型 `REPORT_MODEL`。设计对齐 Material Design 3，执行克制（Google/Apple 风）；研究模式对齐咨询机构（McKinsey/BCG）的密度与论证结构，但**克制优先**——不加多余的页头标签、页脚信息与装饰。

## Gate 0 · 先给参考图（任何生成动作之前 · 硬门禁）

用户表达做报告意向后，**第一件事**是展示参考图，再进入问询：

| 给什么 | 路径 | 何时 |
|--------|------|------|
| 整体图（默认先给这张） | `assets/theme-overview.png` | 每次开场 |
| 按模式拆分的参考图 | 演示 → `assets/theme-overview.png`；研究 → `-research.png`；架构 → `-architecture.png` | 模式已明确时给对应那张（演示态与整体图相同，不再单独存 presentation 副本） |
| 交互画廊（实时切风格×模式×亮暗） | `assets/style-gallery.html` | 用户想边看边挑 |

**理由**：风格与主题是用户最需要"看见"才能决策的形式参数。**跳过参考图直接问询 = 不合格**（`audit_skill.py` 校验 Gate 0 位于六项问询之前）。

## 唯一入口流程

```
听意图 → Gate 0 参考图 → 六项问询（1 轮）→ 内容架构 → 起骨架
      → 只填内容模型 → 回填正文 → validate --strict 0/0 → 交付
      （命令与 PPTX 链见 tech-design §六 / pptx-export）
```

**预算（硬）**：交互轮次 **≤3**；默认必读仅 2 份——本文件 + L1 决策层 `references/playbook.md`；L2 深度文件命中才读、读一份用一份、不预读。

## 六项问询（一次问完 · 唯一一次形式参数确认）

用户表达意图后**一次问完六项**，每项都带意图推荐；用户不选即按推荐执行，不再追问。

1. **意图与模式**（合并确认）——演示/汇报类 → A；研究/调研类 → B；架构/拓扑类 → C；混合选主模式（完整判据 `modes.md`「意图 → 模式默认推荐」）。给推荐 + 理由。
2. **篇幅**——A 8–15 页（图文 V1–V4，简单图禁全幅）/ B 12–25 页 / C 1–3 张图共 6–8 页；有材料按材料量推荐。
3. **风格（始终选择）**——默认商务蓝；B 推荐麦肯锡/墨绿/暖沙金；C 推荐石墨深灰/商务蓝/彩色；拿不准给 Gate 0 参考图。
4. **亮暗主题（始终确认）**——浅色默认（打印/外发）/ 深色（沉浸/发布会/大屏）；石墨深灰出厂深色；双主题经 `REPORT_MODEL.theme` 贯穿 HTML 与导出。
5. **交付格式**——仅 HTML（默认）/ HTML+PPTX（正式汇报、需协作修改时推荐）。
6. **参考图确认**——复述 Gate 0 路径，确认用户已看到。

**载体**：优先结构化选项卡一次收集，否则对话文本一次列全。此后形式层面不再反复确认（内容层面按需一次大纲确认，见下）。

## 两条路径（先判定，再动手）

| 路径 | 何时 | 多做什么 |
|------|------|---------|
| **轻量**（默认） | 页数不多、材料单一完整、关键判断已敲定 | 仅 1 张规划卡，直接生成 |
| **完整** | 长篇、材料量大且杂、含未敲定关键判断、用户要看框架 | 证据盘点 → 故事线 → 主张树 → 逐页规划卡 → 大纲确认（1 轮） |

两条路径的**精确判定条件与完整步骤以 `references/playbook.md` §二为准**。完整路径确认只做一次，用户说"调整"只改指定处；确认后不再有内容层面的反复确认。

## 变更与中断（过程可控 · 不重启六项问询）

| 情形 | 处理 |
|------|------|
| 只改风格 / 亮暗 | header 即切 → 同步 `REPORT_MODEL.style/theme` → 重跑校验；**不重写内容** |
| 加页 / 减页 | 只动受影响页 + Agenda + Exhibit 编号 + 页码；重跑校验 |
| 换模式 A↔B↔C | 不可就地改：保留证据/数字/结论，按目标模式重排；仅重确认篇幅 |
| 对话中断后续写 | 用提取脚本取回模型后重渲染正文，**不要从零重写** |
| 校验不通过 | 按输出的**修复指引**逐条改；连续 2 轮不收敛才升级读 `references/failure-modes.md` |

## 阶段路由（渐进式披露）

> 披露分层（机器可读）：`L0=SKILL.md` · `L1=references/playbook.md` · `L2=按需`
>
> **纪律**：L0+L1 是默认全部所需；**只在命中"何时读"时才打开 L2，读完即执行、不预读下一份**。需要代码时**一律先走节级取码** `extract_snippet.py`（`--list` 查全量路由；`--task 任务名 / --chart 图表类型 / --page-type 页型 / --file 文件 --section 节号`），逻辑名 `components.md` / `charts.md` 自动路由到物理拆分文件。

**L2 一览**（命中条件与逐任务只读清单的**详表以 playbook §十为准**，此处仅索引）：

- 模式契约与锁定版式 → `references/modes.md` · 完整路径七步 → `references/outline-design.md`
- **布局骨架/元素/组合/留白 → `references/layout-grammar.md`（P1–P12 · 每页动手前）**
- 组件/版式**代码**与 §46 选型表 → `references/components.md` · 图表**代码** → `references/charts.md` · 信息图页型 → `references/infographics.md`（→ stats / structure 两分册）
- 配色/主题/字阶 → `references/styles.md` + `references/design-system.md`（`design-system-engine.md` 为实现镜像，生成场景不读）· 写作纪律 → `references/content-rules.md` · 图标语义表 → `references/icons.md`
- PPTX 精导 → `references/pptx-export.md` · 深度高保真 → `references/high-fidelity.md` · 修复顺序 → `references/failure-modes.md` · 技能维护 → `references/tech-design.md` + `references/industry-benchmark.md`

**操作方式**：定模式/页型/组合/图 → 只读 `playbook.md`；取代码 → `extract_snippet.py`；**禁止整读** `layouts-combo.md` / `charts-basic.md` 等大文件；**同一阶段不重复读同一文件**。

## 铁律（12 条 · 交付硬门禁）

> 本节是**门禁语义**；阈值与细则见 playbook（常量在 scripts 下的 layout 常量 JSON）。排版只读 `layout-grammar.md`。

1. **单文件零外链**——无 CDN/外部字体/外部图片，图形一律内联 SVG；`<img src>` 仅 `data:` 或相对路径且必带 `alt`（单图 ≤1.5MB、全篇 ≤8MB）；无素材图不留空不省略，用配图占位（`components.md` §11c-3）。
2. **模式先定后写**——从对应模式模板起步；`data-mode` = `REPORT_MODEL.mode`，页面无模式切换；MD3 映射；PPTX 字号走三模式独立比例尺。
3. **亮暗双主题一致**——CSS 变量整块换肤 + header 切换 + 文件级记忆；`REPORT_MODEL.theme` 与页面一致，PPTX 同主题导出；强调带只用 accent 家族，**末页禁 `band--deep`**。
4. **每页一屏 + 高度稳定**——`section.band` ≥ 一屏高且垂直居中；六七成屏用 `.band--top`，长结构页 `.band--flow`。放不下按「优化内容 → 升级承载 → 扩组合 → 分区 → 拆页 → 最后才有限缩字号」（下限 `containers.fontShrink`）；禁止砍决策必需信息，拆页保持信息完整。
5. **PPT 式翻页 + 骨架固定**——`section.band` 即一页；方向键翻页、页码可点；Agenda 第二页（arch 内容页 ≤4 可省）；页头只留 eyebrow + 标题 + 可选导语，页脚全文一个；页头页脚之外不加装饰。
6. **标题与字号**——主标题粗体（`--fw-title/--fw-display`）；research 主标题必须是**结论句**（≥12 字含数字/判断词）；字号随模式（playbook §一），全部 `clamp()`，图表不缩水。
7. **组合版式 + 细节保全**——默认一页 = 主件 + 从件 + 注释层（矩阵 playbook §四）；先判定决策必需信息再定形态，**禁砍口径列/时间列/维度**；密度 L/M/H 禁连续 3 页同档；同一版式不连用超 2 页（扩展签名可 3 页）。
8. **列表优先 + 去 AI 味 + 图标克制**——大段文字转列表（research 双/三栏正文除外）；`aiFlavor` 词表零命中；图标每屏 3–8 个（架构图为王可无）。
9. **图表够大 + 够多样 + 双通道**——尺寸 ≥ `charts.minSize`；`data-chart` 须在 `charts.registry`（36 种）登记；多样性下限与相邻不同型按 `charts.variety`（playbook §五）；原生通道 `addChart` 双击可编辑数据，形状通道须按登记策略附数据表（口径注解见 tech-design §二）。
10. **引用与待核实**——外部数据 `[n]` + 文末参考资料（来源+时间+口径）双向对齐；research 关键图表 Exhibit N 连续编号 + 来源行；`.tbd` 强调色标注必须配图例（content-rules §五-b），单页 ≤12 处；只标色不解释即不合格。
11. **容器级门禁 + 语义字号**——溢出按**归属容器**判定，越过容器即失败（哪怕未越页）；容器保留内边距，不得缩字号解决溢出；表格正文用 `body` 层级，`micro` 只给轴标签/单位/短标签；连续句不拆文本框。
12. **双单源 + 校验闭环**——schema 只改 `scripts/model-schema.json`，其余常量只改 `scripts/layout-constants.json`，改后必跑 `sync_runtime.py`（禁手改注入副本）；**HTML strict 0/0 才交付**，带 PPTX 加验 `validate_pptx.py --strict --model=` 0/0；页面只提供「预览 PPTX」与提示词，不做文件导出。

## 交付物与验收

- **HTML**：单文件零外链、可翻页可演示、每页一屏高；header 工具栏（T 亮暗 / 9 风格即切 / P 预览 / H 指引 / F 全屏 / B 折叠）。
- **PPTX**：16:9 全原生形状/文本框/表格（`pictures=0` 可编辑）；带数据图表为原生数据图表，非原生附数据表；lead/soWhat/口径/来源写入演讲者备注；按 `REPORT_MODEL.theme` 导出亮/暗版。
- **验收**：HTML strict 0 FAIL / 0 WARN；带 PPTX 加验 PPTX 严格模式 0/0；未通过时末尾给**定向修复指引**。
- **交付说明**：`quality_gate.py` 加 `--deliver`（含 PPTX 时带 `--pptx/--model`）自动生成七要素（路径/字节数/模式/风格/篇幅/格式/校验+引用），缺一即 gate FAIL——不要手拼。

## 环境依赖

- **零依赖可用**：HTML 生成与全部 Python 脚本只用 **Python 标准库**。
- **PPTX 精导**：另需 Node + pptxgenjs（安装与 `TOP_PPT_NODE_EXE`/`TOP_PPT_NODE_PATH` 探测细节见 `pptx-export.md` 环境备注，探测失败会打印指引）。
- **硬门禁**：标签泄漏/空页/极偏图/简单大图等见 `layout-constants.qualityGates` 与 `reform-plan.md`。
- **可选**：浏览器页高/裁切真值、参考图重生成需 playwright（`regression.py` 自动探测，缺失即跳过）。
- **一键回归**：`scripts/regression.py`——模板/常量/schema/运行时/示例改动后必跑。
- **技能自检**：`audit_skill.py`（体积/披露/Gate 0/内容重复）· `audit_docs.py`（§ 引用 + 任务路由可解析）· `audit_styles.py`（9 风格 × 亮暗 token 与对比度）· `audit_css.py`（CSS 类覆盖率 · 报告制）。
