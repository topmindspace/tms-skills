# 业界对标与设计决策

四大主流 PPT/报告技能的调研结论 → TopPPT HTML 的采纳/改造/不采用决策。生成报告前不必读本文档；**改动导出机制、版式体系或校验体系前必读**（防止无依据地破坏既有决策）。

## 对标结论速览

| 技能 | 路线 | 核心机制 | TopPPT HTML 取舍 |
|------|------|---------|----------|
| CyberPPT（sdarpeng） | 原生 PPTX · 咨询级 | 三阶段流程（分析→蓝图→混合还原）、组件签名锁定、渲染回归、15 级排版比例尺、双硬门槛 | **大量采纳**（改造） |
| guizang（op7418） | 单文件 HTML | 双视觉系统、22 锁定版式、颜色预设制、Node+Playwright 量化校验、演讲者模式 | 版式纪律采纳；颜色锁死不采纳 |
| 花叔 huashu（alchaincyf） | HTML 设计系统 → PPTX | 内容结构化→设计选型（9 风格）→AI 插画→组装；20 设计哲学 + 5 维评审 | 内容结构化先行已内建 |
| PPT Master（hugohe3） | 原生 PPTX | 方案先行确认、SVG 中间态、本地预览服务、断点恢复 | 断点恢复采纳；SVG 中间态不采纳 |
| McKinsey/BCG 咨询材料实践 | 咨询机构 deck | 行动标题、金字塔论证（发现→证据→含义）、Exhibit 编号体系、密排高信息密度 | **研究模式全面对齐**（R1–R8 版式 + 密排比例尺） |

## 采纳明细（落到了哪里）

| 借鉴点 | 来源 | TopPPT HTML 落地位置 |
|--------|------|--------------|
| 排版比例尺（C0 封面→T14 注释，15 级） | CyberPPT | `scripts/layout-constants.json` `typeScale`（基准 8 级）+ **`modeTypeScale` 三模式独立取值**（research 咨询密排：正文 10.5pt） |
| 页型 = 锁定版式（不允许临场发明结构） | CyberPPT / guizang | `components.md` §36d–36f（research R1–R8）/ `components.md` §37–38b（arch A1–A3）+ pptx-export.md 页型表 |
| 双硬门槛（可编辑 + 保真，pictures=0 是结果不是目标） | CyberPPT | `validate_pptx.py`（原生形状/字号下限/覆盖率）+ 铁律 16 |
| 模型完整性校验前移 | CyberPPT | `validateModel`（预览端三态校验）+ `extract_model.py` 一致性抽查 + `validate_report.py` 模型一致性检查 |
| 版式常量同源（防两通道漂移） | CyberPPT（组件签名）的轻量化 | `layout-constants.json` + `sync_runtime.py` 单源注入（三模板引擎/UI/运行时三类片段注入） |
| 量化溢出检测（字号×行高×字数 vs 版心预算，无需浏览器） | guizang（Playwright 真实渲染） | `validate_report.py` 溢出估算（静态近似，零依赖，三模式独立预算） |
| 页面方案先行确认（比 PPT Master 更轻） | PPT Master | 单次交互三项默认推荐（模式/风格/篇幅） |
| 断点可恢复（REPORT_MODEL = 恢复锚点） | PPT Master | 重跑 extract → build 即恢复，无需重新生成 |
| 内容结构化先行、设计选型 | 花叔 | 意图→模式/风格/篇幅默认推荐表（SKILL.md） |
| WYSIWYG 预览（导出所见） | —（自研，回应"保真复刻"诉求） | header 预览模态：`slidesXml`（与导出同一序列化输出）→ DOMParser → 16:9 缩略 |
| **行动标题 + 金字塔论证 + Exhibit 编号 + so-what** | McKinsey/BCG 咨询 deck 实践 | research 模式铁律 8/13 + R1/R2 版式 + `validate_report.py` 行动标题/Exhibit 连续性检查 |
| **密排高信息密度（每页一个完整论证，不是每屏一个口号）** | 咨询材料"坐读"传统 | research 密度层（1240 版心/14–15px 正文/16 行密表）+ 密排比例尺（PPTX 正文 10.5pt）+ 单页预算 3200 字 |
| **帮助即文档（in-product guidance）** | MD3 对话式设计 / 现代 SaaS onboarding | header「?」PPT 生成指引弹窗：双通道说明 + 可复制提示词 |

## 明确不采用（及原因）

| 机制 | 来源 | 不采用原因 |
|------|------|-----------|
| AI 位图蓝图 / ImageGen 逐页蓝图 | CyberPPT | 环境依赖重；TopPPT HTML 以"锁定版式 + CSS token + 常量单源"达成同等的版式可复现性，且保住 `pictures=0` 可编辑性 |
| 渲染回归（PowerPoint COM 导 PNG 对照）作为硬门禁 | CyberPPT | 需本机 PowerPoint；降级为**可选路径 C**（`pptx-export.md`），日常由通道 A 预览模态覆盖 WYSIWYG 对照 |
| 颜色完全锁死（用户不可自定义） | guizang | 保留预设风格制（9 套）+ 工具栏实时切换（切换仅影响预览与导出风格，交付一致性由校验器把关） |
| SVG 中间态逐页生成 | PPT Master | 双通道模型驱动更直接；SVG 中间态增加一次格式转换损耗 |
| AI 插画配图 | 花叔 | 违反单文件零外链铁律；图形一律内联 SVG |

## 开源复用清单（不重复造轮子）

| 能力 | 复用的业界开源成果 | 形态 |
|------|------------------|------|
| PPTX 生成引擎（通道 B） | **pptxgenjs**（业界标准，CyberPPT 唯一许可引擎同款） | npm 依赖（技能目录 `npm install pptxgenjs` 或指向已有 node_modules） |
| PPTX 质检器 | **cyber-ppt 的 validate_pptx**（strict 硬门禁、越界/字号/密度/占位检查） | 已内置 `scripts/validate_pptx.py`（纯标准库改写） |
| 排版比例尺 | **CyberPPT 15 级 Typography Scale** | 收敛为 8 级进 `layout-constants.json` |
| 版式纪律 | **guizang 锁定版式**（不允许临时发明结构） | `components.md` R1–R8 / A1–A3 锁定版式表 |
| 咨询论证结构（行动标题/Exhibit/so-what/密排） | **McKinsey/BCG 公开方法论**（金字塔原理、slide-by-slide 论证） | research 模式全套规则（`modes.md`「模式 B · 研究报告」） |
| **第三方裁判交叉验证（防止自研栈自说自话）** | **python-pptx**（开源标准解析器） | `scripts/cross_verify.py`：A/B 双通道产物均经 python-pptx 严格解析 + 逐页文本一致性比对（实测抓出 rels 路径与 `a:graphic` 前缀两处 OOXML 规范缺陷——PowerPoint 宽容掩盖、严格解析器暴露） |
| **check-overflow 溢出启发式** | **grapeot/pptx.skill**（AI-first pptx 检查库） | cross_verify 内置：文本估宽（CJK 1em/ASCII .55em）vs shape 宽×可容行数，18% 容差 |
| **WCAG 对比度审计** | WCAG 2.1 AA + MD3 颜色角色 | `scripts/audit_styles.py`：9 风格 × light/dark × 8 组配对自动核查（实测修复 spectrum/warm-sand 按钮对比度） |
| **原生图表（addChart 数据可编辑）** | PptxGenJS Charts | **已采纳**：交付通道 B 的带数据图表一律走 `addChart` → 真 chart part + 内嵌 Excel 工作簿（双击可"编辑数据"），并列为 `MODEL_CHART_COUNT` 硬门禁；A 通道（浏览器预览/回归双裁判）保留形状近似渲染，两者逐页文本由 `cross_verify.py` 保证一致 |
| 设计系统 | **Material Design 3**（m3.material.io） | `design-system.md` §1b 对齐映射 |
| 渲染回归（可选） | cyber-ppt `export_ppt_render.ps1`（PowerPoint COM）→ **开源替代：LibreOffice headless**（soffice --convert-to pdf，grapeot/pptx.skill 同路线，保真度约 85%） | 可选路径 C，不做硬门禁；本机未装 LibreOffice 时跳过 |

**为何手写预览运行时而非内嵌 pptxgenjs**：pptxgenjs 浏览器版约 700KB（含 JSZip），内嵌进每份单文件报告体积不可接受；手写运行时约 120KB（OOXML 序列化，只做 WYSIWYG 预览与回归双裁判），且与交付通道 B 消费同一份 `layout-constants.json` 常量单源——**复用的是"引擎与规范"，自研的只是"轻量序列化轮毂"**，两者产出经同一 `validate_pptx.py --strict` 验证一致（0/0）。

## TopPPT HTML 的差异化立场

1. **一套模型、两通道、一常量源**：`REPORT_MODEL` 是唯一事实源；预览端是真正的 OOXML 序列化器（不是截图、不是粗糙转换），与交付通道共用同一序列化语义与常量单源。
2. **页面仅预览、交付走精导**：页面提供 WYSIWYG 预览 + 可复制提示词（引导回 AI 对话生成）；正式 PPTX 由智能体精导通道产出并过 strict 硬门禁（浏览器端跑不了门禁，不承担交付）。
3. **预览即交付所见**：预览模态渲染的就是交付同一序列化语义产出的 slide XML，不是另一套模拟。
4. **锁定版式纪律贯穿 HTML 与 PPTX**：research R1–R8 / arch A1–A3 与页型一一成对，新增版式必须"先扩表（含 PPTX 页型与 layout-constants.json 页型几何）、再使用"。
5. **三模式独立成体系**：模式不是切换关系而是三种输出形态——独立模板/密度/组件/预算/比例尺；咨询密排（R1–R8）与全幅图（A1–A3）各自对标业界最优实践（McKinsey deck / 架构图评审材料），而非同一骨架的参数缩放。
6. **双裁判验证（不止一个裁判）**：自研 `validate_pptx.py --strict` 之外，产物再经开源 python-pptx 严格解析与逐页文本比对（`scripts/cross_verify.py`）——自研校验器与手写序列化器同源，存在"自己验自己"盲区；正是靠第三方裁判抓出两处 OOXML 规范缺陷（`ppt/_rels/presentation.xml.rels` 路径、`a:graphic` 命名空间前缀）后才真正达成双通道保真。**改导出/预览运行时后必跑 cross_verify。**

---

## 深度对标（业界调研）

**调研对象**：CyberPPT（sdarpeng，Codex Skill，SKILL.md 约 78KB）、ppt-master（Categorytyy）、ppt-agent-skill（Akxan，148★）、ppt-skill（Cyberceratops）。

### 采纳明细（落到了哪里）

| 借鉴点 | 来源 | 落地位置 |
|--------|------|--------------|
| **图表通道分层 + 数据可追溯** | CyberPPT 的「可编辑信息层」门 | `charts.registry` 四元组（html / pptx 通道 / nativeType 或 path 约束 / dataTable）；原生 16 类走 `addChart`，形状通道**强制附数据表**（`MODEL_CHART_DATATABLE`） |
| **曲线/异形精确还原规则** | CyberPPT「曲线精确追踪门」 | 改造为**可复现常量约束**：采样点 ≥16（流带 ≥24）、双边界分别追踪、禁用 preset shape 替代 → `charts.registry[type].path` + `build_pptx.js ribbonRects` + `infographics.md` |
| **容器边界溢出（按归属容器判定）** | CyberPPT「容器溢出门」 | `validate_pptx.py` `CONTAINER_OVERFLOW`（扣容器内边距，比页面级更严格）+ `containers.pad` 常量 |
| **表格语义字号 / 表格密度** | CyberPPT「表格语义字号门」 | `TABLE_SEMANTIC_TYPE`（句子型内容禁 micro 档）+ `TABLE_DENSITY`（大面积空洞即失败）+ `design-system.md` §1f 语义字阶 C0–T14 |
| **连续文本流（禁拆文本框）** | CyberPPT「连续文本流门」 | `CONTINUOUS_TEXT_FLOW`（深度模式）+ `content-rules.md` §四-f 写作纪律 |
| **空间锚点注册** | CyberPPT「空间锚点门」（中心偏差 ≤2%、关键锚点 ≤6px） | `anchorTolerance` 常量 + `ANCHOR_TITLE_MISALIGNED`（页头标题对齐版心）+ manifest `anchors` 登记 + 人眼对照清单 P0/P1/P2 分级 |
| **固定语义字阶** | CyberPPT `C0`/`T1–T14` 15 级 | `typography.levels`（15 级，role 指向 `modeTypeScale`，不重复存 pt） |
| **设计原理注入** | ppt-master 的 14 本文献映射（CRAP / 7:2:1 / 字体决策矩阵） | `design-system.md` §1a（四条可自检准则） |
| **12 列网格 + 安全边距** | ppt-master 的 `MARGIN` / `GRID` 常量 | `layout-constants.json` `grid`（13 条列轨 + 6 条行基线 + `safe`）+ `design-system.md` §1e |
| **风格集 + 每风格 JSON 定义 + 画廊** | 业界常见 20+ 风格 | 风格 **9 套**（8 色族 + 1 彩色数据板），`styles`+`stylesDark`+`styleAccents`+`styleDataColors` 同源 + 画廊 + 参考图。**不追数量**：同色族换名的冗余已删；新增门槛见 `styles.md` §10 |
| **SCR 论证 + 证据可追溯 + 多故事线脑暴** | CyberPPT 三阶段（证据表 → 脑暴 → SCR） | `outline-design.md` 七步法：② 证据表（MBB 字段 + 冲突不静默归一）③ 故事线脑暴（2–3 条 + issue tree / hypothesis tree）④ SCR 收敛 + 主张树 |
| **跨页叙事节奏** | ppt-agent-skill（密度交替 / 章节递进 / 首尾呼应 / 渐进揭示） | `outline-design.md` §一-续（含 5 条节奏回查清单） |
| **失败模式库 + 修复顺序** | ppt-agent-skill 的 8 failure modes | `failure-modes.md`（十四类模式 + 修复顺序铁律 + 错误解释纠正表） |
| **数据表随行（可追溯）** | CyberPPT「数据表 / 证据 ID」 | `chart.dataTable` 三态（notes / inline / off）+ `inline` 在图表下方附原生表格（双通道同渲染） |
| **PowerPoint 兼容门（打开 + 导 PNG）** | CyberPPT | 降级为**可选深度模式** `render_compare.py`（soffice 渲染 + 并排对照 + 偏差登记），缺失依赖自动跳过 |

### 明确不采纳（及原因）

| 机制 | 来源 | 不采纳原因 |
|------|------|-----------|
| ImageGen 逐页蓝图（生成 16:9 位图再逐页还原） | CyberPPT 第二阶段 | 环境依赖重；与「单文件零外链 + `pictures=0` 默认」冲突。本技能以「锁定版式 + 常量单源 + 形状还原规则」达成同等可复现性 |
| SHA-256 冻结签名 + 逐页人工验收确认 | CyberPPT | 交互轮次与耗时显著增加，与「一次问询 + 自动生成 + 校验闭环」定位冲突；改为 manifest 登记（可复现、无需冻结） |
| 禁止 `python-pptx`（必须只用 pptxgenjs） | CyberPPT 生成工具门 | 本技能用 pptxgenjs **生成**、用 python-pptx 做**第三方裁判**——职责分离比"单一引擎"更能暴露问题（实测抓出两处 OOXML 缺陷） |
| 联网检索素材脚本 | ppt-skill / ppt-agent-skill | 越出「报告生成」边界；外部数据由用户提供或对话中检索，来源须可追溯（`[n]` + 参考资料） |
| HTML→SVG→PPTX 三段式管线 | ppt-skill / ppt-agent-skill | 增加一次格式转换损耗；本技能的双通道模型（同一 `REPORT_MODEL` → 原生形状 + 原生图表）保真度更高且保住数据可编辑 |
| 允许 `pictures>0` 承载复杂视觉 | CyberPPT 混合还原 | 本技能默认 `pictures=0` 全原生可编辑；复杂信息图改用**形状/SVG 精确还原 + 数据表**达成同等视觉语义（且数据仍可核对） |
