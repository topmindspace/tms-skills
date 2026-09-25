---
name: top-ppt-html
description: "Use when 用户要做报告、演示、汇报、PPT、slides、deck、路演，或写研究报告、分析报告、咨询报告、白皮书、调研、评测、对标、经营分析、复盘、项目汇报、商务/HTML/网页报告，或做架构图、拓扑图、流程图、泳道图、方案图，或把材料做成可视化报告并导出 HTML/PPT/PPTX，或优化排版/版式/配色/图文布局，或要快速模式/fast/直接生成/一键出稿/少问一句。TopPPT HTML：优雅大气的正式场合演讲/汇报演示文稿——零外链可翻页 HTML（亮暗双主题）+ 版式保真可编辑 16:9 PPTX；核心=版式·排版·色彩·内容组织；三模式（A 演示·每屏一主张 / B 研究·咨询密排 / C 架构·图为王）× 9 风格。Do NOT use for 纯代码工程、非报告类网页或应用开发、视频/图片生成、直接改写已有 Word/PPT 源文件本身。"
license: MIT
compatibility: "Python 3 stdlib for HTML generation; Node >=18 + pptxgenjs for PPTX; optional playwright for browser regression / theme captures."
metadata:
  version: "0.1.6"
  author: TopMindspace
---
# TopPPT HTML

**让 idea 飞，好想法被看见。** 面向**演讲与正式场合**的优雅、大气的演示文稿——非 gadget 堆砌、非咨询 dump 默认。三种模式、两种交付：**单文件 HTML**（可翻页演示）+ **版式保真可编辑 PPTX**（**B 通道** `build_pptx.js` 为唯一交付；**A 通道**仅预览/`cross_verify`）。同源 `REPORT_MODEL`。设计对齐 MD3，执行克制；研究模式可对齐咨询密度，但**克制优先**——少装饰、一屏一重心。

## Gate 0 · 先给参考图（**标准模式**硬门禁）

标准路径下，用户表达做报告意向后，**第一件事**是展示参考图，再进入六项问询：

| 给什么 | 路径 | 何时 |
|--------|------|------|
| 整体图（默认） | `assets/theme-overview.png` | 每次开场 |
| 按模式拆分 | 演示→整体图；研究→`-research.png`；架构→`-architecture.png` | 模式已明确 |
| 交互画廊 | `assets/style-gallery.html` | 用户想边看边挑 |

**标准模式**：跳过参考图直接问询 = 不合格。**Fast Mode**（下节）豁免 Gate 0 与六项。

## Fast Mode · 快速模式（用户显式 opt-in）

触发词任一即进入（**跳过 Gate 0 与六项问询**）：`快速模式` / `fast` / `直接生成` / `一键出稿` / `fast mode` / `少问一句`。

| 参数 | 默认 | 推断 |
|------|------|------|
| mode | **B** | **路演/汇报/发布/演讲/demo/融资→A**；架构/拓扑→C；未点明→B |
| style | B→mckinsey · A→business-blue · C→graphite-dark | |
| theme | light（graphite→dark） | |
| 篇幅 | A=10 / B=12 / C=6 | |
| format | **html only**（默认；**仅当用户要 PPT / 交付含 PPTX 才开** B 通道） | |

流程：一行宣布「Fast 选用：…」→ **最小大纲**（`outline-design.md`「轻量最小集」）→ playbook §二轻量链（骨架→模型单写→回填→strict→`quality_gate --deliver`；**PPTX 显式 opt-in**）。路径轻量；末可附 `assets/style-gallery.html`。开场声明「已跳过参考图」。**标准模式**仍强制 Gate 0 + 六项。

## 唯一入口流程

```
听意图 → [Fast? → 快路径] : [Gate 0 → 六项（1 轮）→ 内容架构]
      → 起骨架 → 模型单写（禁改 HTML 正文）→ 脚本回填 → strict 0/0 → 交付
      （命令链见 playbook §二/§九；PPTX 见 pptx-export）
```

**预算（硬）**：交互轮次 **≤3**；**L0+L1 共 2 份**（本文件 + `playbook.md`）。**Mode A/Fast**可加 L1.5：`default-surface.md`+`presentation-craft.md`（非违约）。其余 L2 命中才读、不预读。

## 六项问询（标准模式 · 一次问完 · 唯一一次形式参数确认）

用户表达意图后**一次问完六项**，每项都带意图推荐；用户不选即按推荐执行，不再追问。

1. **意图与模式**（合并确认）——演示/汇报类 → A；研究/调研类 → B；架构/拓扑类 → C；混合选主模式（完整判据 `modes.md`「意图 → 模式默认推荐」）。给推荐 + 理由。
2. **篇幅**——A 8–15 页（图文 V1–V4，简单图禁全幅）/ B 12–25 页 / C 1–3 张图共 6–8 页；有材料按材料量推荐。
3. **风格（始终选择）**——默认商务蓝；B 推荐麦肯锡/墨绿/暖沙金；C 推荐石墨深灰/商务蓝/彩色；拿不准给 Gate 0 参考图。
4. **亮暗主题（始终确认）**——浅色默认（打印/外发）/ 深色（沉浸/发布会/大屏）；石墨深灰出厂深色；双主题经 `REPORT_MODEL.theme` 贯穿 HTML 与导出。
5. **交付格式**——仅 HTML（默认）/ HTML+PPTX（用户要可编辑演示文稿时；PPTX 走 **B 通道**）。
6. **参考图确认**——复述 Gate 0 路径，确认用户已看到。

**载体**：优先结构化选项卡一次收集，否则对话文本一次列全。此后形式层面不再反复确认（内容层面按需一次大纲确认，见下）。

## 两条路径（先判定，再动手）

| 路径 | 何时 | 多做什么 |
|------|------|---------|
| **轻量**（默认） | 页数不多、材料单一完整、关键判断已敲定 | 最小大纲→1 张规划卡（`outline-design.md`「轻量最小集」） |
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
> **纪律**：L0+L1 是默认全部所需；**只在命中"何时读"时才打开 L2，读完即执行、不预读下一份**。需要代码时**一律** `extract_snippet.py`（`--list` / `--task` / `--chart` / `--page-type` / `--file --section`）。**整读大 L2 文件 = FAIL / 不合格**（禁令清单见下与 playbook §十）。

**L2 一览**（命中条件与逐任务只读清单的**详表以 playbook §十为准**，此处仅索引）：

- 模式契约与锁定版式 → `references/modes.md` · 完整路径七步 → `references/outline-design.md`
- **A/Fast L1.5 → `default-surface.md` + `presentation-craft.md`** · 骨架 `layout-grammar.md` §七 · 插画 `illustration-layout.md`
- 组件/版式**代码** → `components.md` · 页型表 `page-type-matrix.md` · 图表门面 `charts.md` + 决策树 `chart-decision-tree.md`（extended 按需）· 信息图 → `infographics.md`
- 配色/主题/字阶 → `styles.md` + `design-system.md` · 写作 → `content-rules.md` · 图标语义 → `icons.md`
- PPTX 精导 → `references/pptx-export.md` · 深度高保真 → `references/high-fidelity.md` · 修复顺序 → `references/failure-modes.md` · 技能维护 → `references/tech-design.md`

**操作方式**：定模式/页型/组合/图 → 只读 `playbook.md`；取代码 → **必须** `extract_snippet.py`。**整读下列文件 = FAIL**：`layouts-combo` / `components-atoms` / `charts-basic` / `charts-extended` / `content-rules` 全文 / `pptx-export` / 模式模板 HTML（走 scaffold）。详表 playbook §十。同阶段不重读。

## 铁律（12 条 · 交付硬门禁）

> 门禁语义；阈值见 playbook / layout 常量 JSON。排版读 `layout-grammar.md`。**motion=none**（无炫技转场；`presentation-craft.md`）。

1. **单文件零外链**——无 CDN/外部字体/外部图片，图形一律内联 SVG；`<img src>` 仅 `data:` 或相对路径且必带 `alt`（单图 ≤1.5MB、全篇 ≤8MB）；无素材图不留空不省略，用配图占位（`components.md` §11c-3）。
2. **模式先定后写**——从对应模式模板起步；`data-mode` = `REPORT_MODEL.mode`，页面无模式切换；MD3 映射；PPTX 字号走三模式独立比例尺。
3. **亮暗双主题一致**——CSS 变量整块换肤 + header 切换 + 文件级记忆；`REPORT_MODEL.theme` 与页面一致，PPTX 同主题导出；强调带只用 accent 家族，**末页禁 `band--deep`**。
4. **每页一屏 + 高度稳定**——`section.band` ≥ 一屏高且垂直居中；六七成屏用 `.band--top`，长结构页 `.band--flow`。放不下按「重构承载 → 拆页/分章 → 换布局形态 → 有限缩字号」（`containers.overflowRule`）；**禁止**静默截断或为疏朗删 so-what/证据；拆页保持信息完整。
5. **PPT 式翻页 + 骨架固定**——`section.band` 即一页；方向键翻页、页码可点；Agenda 第二页（arch 内容页 ≤4 可省）；页头只留 eyebrow + 标题 + 可选导语，页脚全文一个；页头页脚之外不加装饰。
6. **标题与字号**——主标题粗体；research=结论句（≥12 字）；**presentation=主张/行动句**（禁话题标签）；字号随模式，`clamp()`，图表不缩水。
7. **组合版式 + 细节保全**——默认一页 = 主件 + 从件 + 注释层（矩阵 playbook §四）；先判定决策必需信息再定形态，**禁砍口径列/时间列/维度**；密度 L/M/H 禁连续 3 页同档；同一版式不连用超 2 页（扩展签名可 3 页）。
8. **列表优先 + 去 AI 味 + 图标克制**——大段文字转列表（research 双/三栏正文除外）；`aiFlavor` 词表零命中；图标每屏 3–8 个（架构图为王可无）。
9. **图表够大 + 够多样 + 双通道**——尺寸 ≥ `charts.minSize`；`data-chart` 须在 `charts.registry`（36 种）登记；多样性下限与相邻不同型按 `charts.variety`（playbook §五）；原生通道 `addChart` 双击可编辑数据，形状通道须按登记策略附数据表（口径注解见 tech-design §二）。
10. **引用与待核实**——外部数据 `[n]` + 文末参考资料（来源+时间+口径）双向对齐；research 关键图表 Exhibit N 连续编号 + 来源行；`.tbd` 强调色标注必须配图例（content-rules §五-b），单页 ≤12 处；只标色不解释即不合格。
11. **容器级门禁 + 语义字号**——溢出按**归属容器**判定，越过容器即失败（哪怕未越页）；容器保留内边距，不得缩字号解决溢出；表格正文用 `body` 层级，`micro` 只给轴标签/单位/短标签；连续句不拆文本框。
12. **双单源 + 校验闭环**——schema 只改 `scripts/model-schema.json`，其余常量只改 `scripts/layout-constants.json`，改后必跑 `sync_runtime.py`（禁手改注入副本）；**HTML strict 0/0 才交付**，带 PPTX 加验 `validate_pptx.py --strict --model=` 0/0；页面只提供「预览 PPTX」与提示词，不做文件导出。

## 交付物与验收

- **HTML**：单文件零外链、可翻页可演示、每页一屏高；header 工具栏（T 亮暗 / 9 风格即切 / P 预览 / H 指引 / F 全屏 / B 折叠）。
- **PPTX（B 通道交付）**：`extract_model` → `build_pptx.js` → `validate_pptx --strict`；16:9 全原生可编辑。**A 通道不交付**（仅预览 / `cross_verify`；细则 playbook §九）。
- **验收**：HTML strict 0/0；含 PPTX 再加 PPTX 0/0；失败给**定向修复指引**。
- **交付说明**：`quality_gate.py --deliver`（含 PPTX 带 `--pptx/--model`；子门禁并行）出七要素，缺一 FAIL——勿手拼。

## 版本口径

包 semver（现 0.1.6）≠ 布局 schema 线（layout-constants / model-schema 的 version，现 `0.1`）；patch 不抬 schema。

## 环境依赖

- **零依赖可用**：HTML 生成与全部 Python 脚本只用 **Python 标准库**。
- **PPTX 精导**：另需 Node + pptxgenjs（安装与 `TOP_PPT_NODE_EXE`/`TOP_PPT_NODE_PATH` 探测细节见 `pptx-export.md` 环境备注，探测失败会打印指引）。
- **硬门禁**：标签泄漏/空页/极偏图/简单大图 → `scripts/layout-constants.json`（qualityGates）+ `failure-modes.md`。
- **可选**：浏览器页高/裁切真值、参考图重生成需 playwright（`regression.py` 自动探测，缺失即跳过）。
- **一键回归**：`scripts/regression.py`——模板/常量/schema/运行时/示例改动后必跑。
- **技能自检**：`audit_skill.py`（体积/披露/Gate 0/内容重复）· `audit_docs.py`（§ 引用 + 任务路由可解析）· `audit_styles.py`（9 风格 × 亮暗 token 与对比度）· `audit_css.py`（CSS 类覆盖率 · 报告制）。
