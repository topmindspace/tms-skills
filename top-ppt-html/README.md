# TopPPT HTML

**让 idea 飞，好想法被看见。** 一套面向 AI 智能体的商务报告生成技能：把想法、调研、分析、架构方案，变成**专业级的 HTML 报告 + 版式保真的可编辑 PPTX**。

- 技能标识：`top-ppt-html`（安装/打包目录名与此一致）；品牌名：**TopPPT HTML**
- 版本：**v0.1.0** · 完整规范见 `SKILL.md`（智能体入口）+ `references/playbook.md`（唯一常读入口）+ `references/layout-grammar.md`（排版）+ 其余按需 L2

## 一、技能简介

| 维度 | 能力 |
|------|------|
| 产出物 ① | **单文件 HTML 报告**：零外链、可翻页（方向键整屏翻页）、**每页一屏的稳定页高**、亮暗双主题（记忆按文件隔离）、header 自带工具栏（主题/9 风格实时切换/PPTX WYSIWYG 预览/可复制 AI 提示词/全屏 F/收起工具栏 B） |
| 产出物 ② | **16:9 可编辑 PPTX**：全原生形状/文本框/表格（默认 `pictures=0`；模型显式声明 `section.image` 时按声明数导出素材图片，六版式 full/half/bleed/grid/compare/wall 与 HTML 同比例；无素材时出**原生配图占位框**——可编辑、`pictures` 不增），三模式独立排版比例尺 + **29 种页型**，带数据的图表为**原生数据图表**（双击"编辑数据"），非原生图表**附数据表**（备注/页内表格），口径自动写入演讲者备注，按所选主题导出亮色版或深色版 |
| 三种模式 | A 演示汇报（大字每屏一主张，8–15 页）/ B 研究报告（咨询密排：行动标题 + Exhibit 编号 + 双三栏 + 密表 + 矩阵，12–25 页）/ C 信息架构图（图为王：全幅分层带/泳道/管线，1–3 张图成篇） |
| 9 套风格 | 商务蓝（默认）/ 优雅黑白 / 麦肯锡 / 品牌红 / 暖沙金 / 墨绿 / 石墨深灰（深色优先）/ 靛紫 / 光谱彩色——与模式、主题正交组合；**每套风格各有自己的编码色板 c1–c5**（`styleDataColors` 单源，双引擎消费），多系列图表在任何风格下都可辨。**刻意不再扩张**：新增门槛（新色族 + 新语汇 + 场景缺口）见 `references/styles.md` §10 |
| 复杂信息图 | 桑基 / 树图 / 箱线 / 关系网络 / 马赛克 / 流带 六类专属页型：曲线采样点 ≥16（流带 ≥24）、双边界分别追踪、禁预设形状替代；每页一图，数据表可追溯 |
| 强调带 | 收尾/CTA 用 `band--accent`（软强调）、金句用 `band--accent--solid`（实底）——**浅色模式不再出现深色收尾页**；`band--deep` 仅显式反相页（≤1 处、不作末页） |
| 待核实标注 | `.tbd` 内联标色 + `.tbd-legend`/`.flagbar` 说明——无法核实的数字/判断用**强调色**标出，提示用户二次修改（PPTX 同源 + 演讲者备注） |
| 素材图片 | **六版式**：full 版心全宽 3:1 / half 左图右注 4:3 / bleed 通栏出血 21:9 / grid 多图网格 4:3（2·3·4·6 张）/ compare 双图 A/B / wall Logo 墙；比例由 `imageSpec` 单源锁定（HTML 用 `.media--r*` 类、PPTX 用同一比例算高度并居中）——**两通道比例一致**；`src` 仅 data: 内联或相对路径；PPTX 声明式放行 |
| 配图占位 | 无素材时不省略图也不塞无关图：`.media--ph`（虚线框 + 斜纹 + 图标 + 尺寸提示）+ 模型 `image.placeholder` → PPTX 出**原生圆角矩形占位框**（可编辑、`pictures` 不增），交付前替换 `src` 即可；预览模态会把图位替换成真实图片 |
| 用户图片准备 | `scripts/prepare_images.py <图片\|目录> --layout full\|half\|grid…`：读尺寸/格式/体积 → 按版式建议尺寸缩放压缩（有 Pillow 时）→ 自动选 data: 内联或相对路径 → 产出可粘贴的 `.media` HTML 片段与 `image` 模型对象 |
| 36 种图表 | 环形 / 多段环形 / 饼图 / 柱状 / 堆叠 / 100% 堆叠条 / 折线 / 双折线 / 面积 / 横向条形 / 双向条形 / 雷达 / 仪表盘 / 玫瑰 / 瀑布 / 漏斗 / 甘特 / 散点 / 气泡 / 矩形树图 / 马赛克 / 进度条组 / 迷你趋势线 / 桑基 / 斜率 / 哑铃 / 棒棒糖 / 点图 / 子弹图 / 华夫 / 箱线 / 帕累托 / 径向条 / 流图 / K 线 / 关系网络（全内联 SVG，随主题与风格变色；**16 类走 PPTX 原生图表，其余形状还原 + 数据表**） |
| 按需深度模式 | 命中「高保真/1:1/精确还原/正式交付」或含复杂信息图时自动升级：`--deep` 把连续文本流与空间锚点纳入 strict，`--emit-manifest` 产出锚点/容器/数据表/图表通道/图片资产登记，`render_compare.py` 准备渲染对照材料（缺依赖自动跳过） |
| 质量闭环 | `validate_report.py`（HTML strict 全 PASS，含强调带约束/待核实标注/素材图片与配图占位/图表数据表策略）+ `validate_pptx.py --strict`（0 错误 0 警告，含容器级溢出/表格语义字号与密度/未声明图片硬拦/图片版式·裁切·多图数量·相对路径文件存在性）+ WCAG 对比度与单源完整性审计 + 双通道回归双裁判 + 素材图片导出探针 |
| 设计标准 | Material Design 3 对齐（克制执行）；研究模式对齐咨询机构实践 |

**核心架构**：HTML 与 PPTX 出自同一内容模型 `window.REPORT_MODEL`（唯一事实源）；页面只预览不导出，PPTX 由智能体走「精导通道」生成（extract → build → strict 校验）。阈值与几何全部单源化：`scripts/layout-constants.json`（常量）+ `scripts/model-schema.json`（页型 DSL）。

## 二、安装与使用

### 安装

本技能是 [`tms-skills`](https://github.com/topmindspace/tms-skills) monorepo 中的一个技能包（路径 `top-ppt-html/`）。npm 安装器已发布：[`@topmindspace/tms-skills`](https://www.npmjs.com/package/@topmindspace/tms-skills)。

```bash
# 推荐 · npm
npx @topmindspace/tms-skills install top-ppt-html
# 或指定目录
npx @topmindspace/tms-skills install top-ppt-html --to ./.agents/skills

# 跟仓库 HEAD · GitHub 直装
npx github:topmindspace/tms-skills install top-ppt-html

# clone 后本地安装
git clone https://github.com/topmindspace/tms-skills.git
node tms-skills/bin/tms-skills.js install top-ppt-html
```

> **GitHub 更新不会自动进 npm。** 日常可钉 npm 版本；要最新技能用 GitHub 直装，或等 maintainer 打 tag 发版。
>
> 「找不到这个包」→ 换 GitHub 直装，或 `--registry https://registry.npmjs.org/`（镜像索引可能滞后）。不要 `npm install top-ppt-html`（技能 id 不是独立 npm 包）。

也可将本目录（或 GitHub Release 附件 `top-ppt-html.zip` 解压结果）复制到智能体技能目录，目录名保持 `top-ppt-html`。技能识别面为 `SKILL.md`（frontmatter 的 `name` / `description` 即触发描述）。

**依赖**：HTML 生成与全部校验脚本零第三方依赖（Python 标准库）。只有「生成 PPTX」需要 Node + pptxgenjs：

```bash
cd top-ppt-html
npm install                  # 依 package.json 安装 pptxgenjs（^4）
# 或：npm install pptxgenjs ／ 把 NODE_PATH 指向任意已含 pptxgenjs 的 node_modules
```

脚本会自动探测 Node 与 node_modules（`TOP_PPT_NODE_EXE` / `TOP_PPT_NODE_PATH` 环境变量 > `PATH` > 常见托管目录），不绑定任何机器的固定路径。参考图刷新（可选，非交付依赖）另需 playwright：`npm install playwright && npx playwright install chromium`。

### 用户视角（三步走）

1. 对智能体说出意图（例：「帮我把这份调研做成一份咨询风格的研究报告」）
2. 回答一次**六项问询**（全部带推荐，不选即按推荐走）：①模式 ②篇幅 ③风格 ④亮暗主题 ⑤交付格式（仅 HTML / HTML+PPTX）⑥参考图
3. 收到交付：HTML 落到指定输出目录（默认当前工作目录）；需要 PPTX 时智能体走精导通道一并生成——或事后打开报告页面点「预览 PPTX」复制提示词回对话补生成

### 智能体视角（工作流）

```
听意图 → Gate 0 参考图 → 六项问询 → 路径判定（轻量默认 / 完整走 outline-design.md 七步法）
→ scaffold_report.py 起骨架（勿整读/复制模板）→ **只填 window.REPORT_MODEL** → `render_from_model.py --inplace`
→ validate_report.py --strict 全 PASS → 交付
→（含 PPTX 时）extract_model.py → build_pptx.js --model → validate_pptx.py --strict 0/0
```

**渐进式披露三档**（详见 `SKILL.md` 阶段路由表）：`L0` = `SKILL.md`（路由 + 门禁 + 铁律，加载即用）；`L1` = `references/playbook.md`（**唯一常读入口**：模式契约 / 页型选型 / 组合版式矩阵 / 图表选型决策树 / 内容规则 / 配色 / 校验命令）；`L2` = 深度规范，**只在命中条件时读、读完即停**；**取码优先 `extract_snippet.py`**（`components.md`/`charts.md` 为逻辑索引，自动路由到 `components-atoms` / `layouts-*` / `charts-basic` / `charts-extended` / `charts-discipline` 等物理文件）。

## 三、目录结构

```
top-ppt-html/
├─ SKILL.md                     # 智能体入口：触发描述 + 工作流 + 铁律        ┐
├─ README.md                    # 本文件：人类视角的简介/开发/打包           │
├─ package.json                 # Node 依赖（pptxgenjs）与常用命令            │ 进包
├─ assets/                      #                                           │ 且
│  ├─ templates/                #   三份模式模板（presentation/research/architecture）  │ 入库
│  │                            #   + engine.css / ui.js（公共引擎/UI，sync_runtime 注入源）
│  ├─ examples/                 #   9 份示例 + 9 份 REPORT_MODEL（复制起点 · 覆盖全部 9 风格）   │
│  ├─ pptx-export.js            #   PPTX 预览运行时（含常量/schema 注入块）   │
│  ├─ style-gallery.html        #   风格 × 模式 × 亮暗主题交互画廊            │
│  └─ theme-overview*.png       #   3 张主题参考图（整体=演示 / 研究 / 架构）  │
├─ references/                  # 规范（L1 常读 1 篇 + L2 按需；components/charts 已按族拆分）│  ├─ playbook.md               #   ★ L1 唯一常读入口：模式/页型/组合/图表/配色/校验 │
│  ├─ components.md             #   逻辑索引（§ 路由到下列物理文件）              │
│  ├─ components-atoms.md       #   §1–§15c 结构组件                              │
│  ├─ layouts-research.md       #   §36–§36f research 锁定版式                    │
│  ├─ layouts-architecture.md   #   §37–§38b architecture 版式                    │
│  ├─ layouts-combo.md          #   §32–§34/§39–§50 组合与选型表 §46              │
│  ├─ charts.md                 #   逻辑索引（图表 § 路由）                       │
│  ├─ charts-basic.md           #   §16–§35 基础图表代码                          │
│  ├─ charts-extended.md        #   §52–§70 扩展图表代码                          │
│  ├─ charts-discipline.md      #   §64/§66 误用与多样性纪律                      │
│  ├─ infographics.md           #   铁律与边界（逻辑入口）；代码已拆分见下两行          │
│  ├─ infographics-stats.md     #   统计图形族 §1–§6 / §71–§77                        │
│  ├─ infographics-structure.md #   结构图形族 §78–§82                                │
│  └─ …（modes / styles / design-system + design-system-engine / content-rules / icons /  │
│        outline-design / pptx-export / high-fidelity /                               │
│        failure-modes / tech-design / industry-benchmark）                            │
├─ evals/                       # Eval 框架（结果/过程/风格/效率四类目标）    │
│  ├─ prompts.csv               #   14 条 prompt（显式/隐式/上下文/负对照）   │
│  ├─ rubric.schema.json        #   风格目标结构化评分契约                    │
│  ├─ run_evals.py              #   确定性检查 + 效率度量 + rubric 落地       │
│  └─ trace.example.json        #   过程/效率 trace 示例（轮次/工具调用/读取量）│
├─ scripts/                     # 生成/校验/回归/维护工具（见下表）          ┘
├─ .gitignore                   # 出库规则（dist/依赖/缓存/本地状态/临时脚本）
├─ dist/                        # 构建与回归产物 + 分发包 zip + 发布清单  ← 不进包、不入库
└─ （本地状态目录）                      # IDE / 智能体本地状态                  ← 不进包、不入库
```

**口径**：`assets/`（输出用素材）+ `references/`（按需加载规范）+ `scripts/`（确定性工具）构成官方规范的三类打包资源；`dist/`、依赖、缓存、IDE/智能体本地状态目录、`scripts/_*` 一律不进包也不入库（与 `.gitignore` 同口径，由 `package_skill.py` 校验）。

## 四、开发指南

### 4.1 脚本清单

| 脚本 | 用途 | 何时跑 |
|------|------|--------|
| `env_probe.py` | **公共环境探测模块**（Node 可执行文件 / 含 pptxgenjs 的 node_modules / python-pptx 可用性；统一解析优先级与安装指引，被 regression / probe_image_export 复用，杜绝各写一份） | 无需单独跑；`python scripts/env_probe.py` 可自检 |
| `sync_runtime.py` | 常量/schema 双注入（pptx-export.js 常量块 + 三模板引擎/UI/运行时内联副本）+ 双端引用与**页型四件套**校验 | **改 layout-constants.json / model-schema.json / engine.css / ui.js / pptx-export.js 后必跑** |
| `audit_styles.py` | 9 风格 × 亮/暗 WCAG 对比度 + engine.css ↔ JSON 双源一致 + **单源完整性**（强调色表 / 图表登记表 / 校验预算键） | 改任何风格色值或常量后必跑 |
| `audit_docs.py` | **文档一致性审计**：§ 引用可解析性（跨文件稳定编号）+ 文件前缀规范性 + §46 选型表对 36 图表/29 页型全覆盖 + 图表代码节齐备 + 元数据与必需文件 + **任务路由可解析**（TASK_ROUTES 每条路由实际抽取验证） | 改 `references/*` 或拆分规范文件后 |
| `audit_skill.py` | **技能工程审计（效率预算与门禁）**：SKILL.md（≤13KB）/ L1 playbook / 单份 reference / 模板的体积上限 · description 软硬上限 · 三档披露（L0/L1/L2）· **Gate 0 位于六项问询之前** · 交互轮次与必读文件预算声明 · 引用完整性 · **内容重复（归一化滑窗，含表格/公式/短语）** | 改 `SKILL.md` / `references/*` 后（与 `audit_docs.py` 互补） |
| `audit_css.py` | **CSS 类覆盖率审计（报告制）**：engine.css 选择器类 ↔ 消费方语料（模板剔除注入镜像 + 示例 + 运行时 + references 代码配方），列出疑似死类供维护者决策 | 删除/新增 engine.css 规则后 |
| `scaffold_report.py` | **报告骨架生成器**（替代"整份复制模板"）：锁模式/风格/主题 + `data-skel`/`layoutPreset` + REPORT_MODEL；`--plan`/`--preset`/`--list-types` | **每次生成第一步** |
| `render_from_model.py` | **模型驱动生成**：只填 REPORT_MODEL → `--inplace` 回填 HTML（`[n]`→cite；29 页型渲染器） | 填完模型后 |
| `extract_snippet.py` | **L2 节级片段抽取**：`--task` 任务路由 / `--chart` 图表代码节 / `--page-type` schema 字段 / `--file --section` 精确节——避免整读 70KB+ 规范 | 取 L2 代码/规范时优先于整文件读 |
| `lib_layout_regions.js` | **页型布局区域 IR**：槽位 → 英寸矩形（layout_slots + layout-constants 派生）；B 通道 exhibit 已消费 | 改布局 IR 后必跑 sync + regression |
| `quality_gate.py` | **交付一键质量门禁**：HTML strict + 可选 PPTX strict + evals 确定性 + rubric 启发式五维 + `--deliver` 自动生成七要素交付说明（缺一即 FAIL）+ 分项耗时 | 正式交付前推荐 |
| `checks_html.py` | **HTML 检查公共库**（承载正则 / 图表通道 / 多样性下限 / 组合版式）——validate_report / quality_gate / run_evals 共用，禁止再手抄 | 被上述脚本 import |
| `measure_height.py` | **页高与容器裁切真值测量**（可选 · Playwright）：无头浏览器量 band 真实高度 vs 视口，并检测「内容越过归属容器」（静态估算的盲区）；缺依赖自动跳过 | regression 内部 / 排版争议时 |
| `build_examples.py` | 从模板 + 内容包重建 9 份示例（三模式 × 9 风格全覆盖，含 REPORT_MODEL 与 theme） | 改模板/内容包后 |
| `validate_report.py` | HTML 质检（三模式预算 + 页高模型与溢出估算 + 模型一致性 + 页型↔版式对应 + 图表登记） | 每份报告交付前（`--strict` 连 WARN 不放过） |
| `extract_model.py` | 从 HTML 抽取 REPORT_MODEL（自动兜底 style/mode/theme） | 精导第一步 |
| `build_pptx.js` | PptxGenJS 生成 PPTX（`--model=` 必选，`--style=` / `--theme=light\|dark` 可覆盖） | 精导第二步 |
| `validate_pptx.py` | PPTX 质检（`--strict` 0/0 硬门禁；`--model` 启用往返保真） | 精导第三步 |
| `gen_channel_a.js` | A 通道：加载页面预览运行时组装 PPTX（回归双裁判专用） | regression 内部 |
| `cross_verify.py` | python-pptx 第三方裁判：A/B 产物逐页文本一致 + **B 通道原生图表数值 ↔ 模型一致**（可选依赖，未装则跳过） | regression 内部 |
| `prepare_images.py` | **用户图片素材准备**（读尺寸/格式/体积 → 按版式建议尺寸缩放压缩 → data: 内联或相对路径 → 产出 `.media` HTML 片段 + `image` 模型对象） | 报告要配用户图片时 |
| `probe_image_export.py` | **素材图片导出探针**（真实位图 build→strict 0/0 且 `pictures == 声明数`；示例矩阵刻意零图片，真实素材路径/版式/门禁靠它覆盖） | regression 内部 / 改图片相关代码后 |
| `negative_tests.py` | **门禁反向验证**（故障注入 · 14 例）：往合格产物里埋已知缺陷（Exhibit 漏编号 / 引用错配与跳号 / 备注被剔离 / 图表数值篡改 / 标题鉴别力 / 字号越尺 / 未登记图表类型 / 多样性塌陷 / 图片外链 / tbd 无图例 / 模型主题与模式矛盾 / 锚点断裂），断言门禁必须报错——正向全绿只能证明“没误报”，这里证明“真能报” | regression 内部 / 改校验器后必跑 |
| `regression.py` | **一键全链路回归**（9 示例 HTML strict + 双通道 PPTX 0/0 + 双裁判交叉一致 + 素材图片探针 + 深色主题探针 + 门禁反向验证 + **任务路由全量遍历** + 浏览器页高/裁切真值） | 任何模板/常量/schema/运行时/示例改动后必跑 |
| `render_compare.py` | **深度模式渲染对照**（PPTX→PDF→位图 + HTML/PPTX 并排对照 + 偏差登记；缺 LibreOffice 自动跳过） | 深度模式交付时（可选） |
| `capture_theme_overview.js` | playwright 截图画廊 → 3 张主题参考图（演示态=整体图；带 Tab 断言防雷同） | 改画廊后（可选，非交付依赖） |
| `package_skill.py` | **发布前校验 + 打包**：必需文件齐全 / frontmatter 合规（name 与包名一致、description ≤1024）/ 无临时·缓存路径 → `dist/top-ppt-html.zip` + 发布清单 `dist/top-ppt-html.manifest.json`（版本/条目/SHA-256）；`--check` 只校验 | 发布时 / 提交前自检 |

### 4.2 单源纪律（最重要的一条规矩）

**几何/字号/页型/图表登记/校验预算/强调色/去AI味词一律只改 `scripts/layout-constants.json`，页型字段只改 `scripts/model-schema.json`，公共片段只改注入源，然后跑 `sync_runtime.py`**——禁止手改任何注入副本（模板内联块、pptx-export.js 常量块）。

改一套风格色值只需**两处手改 + 一处受审计**（校验器阈值、图表登记、强调色表、去AI味词表全部从 JSON 读；画廊配色也从 JSON 派生，无手抄副本）：

1. `assets/templates/engine.css`（CSS 侧单源，light + dark 两个块）
2. `scripts/layout-constants.json` 的 `styles`（light）/ `stylesDark`（dark）/ `styleAccents`（强调色族，供单一强调色检查）
3. `assets/templates/ui.js` 的 `STYLES` 色板（header 下拉 12px 小色块）——在运行时块之前执行、无法直接读 `PRESETS`，故由 `audit_styles.py` 校验其与 JSON accent 一致（不一致即报 DIFF）

然后按顺序跑：`sync_runtime.py` → `audit_styles.py` → `audit_docs.py` → `audit_skill.py`（三项审计必须全绿）→ `build_examples.py` → `regression.py`。

### 4.3 新增一个 PPTX 页型（四件套，缺一不可）

1. `scripts/model-schema.json` 加页型条目（字段/必填/适用模式）
2. `scripts/layout-constants.json` 加页型几何（`pageTypes`）**并在 `pageTypeGeometry` 登记映射**（`sync_runtime.py` 会校验四件套完整性）
3. 双引擎渲染：`scripts/build_pptx.js` 与 `assets/pptx-export.js` 各实现（坐标/字号/文本内容严格一致，否则 cross_verify 会报文本差异）
4. `scripts/build_examples.py` 内容包覆盖新页型 + 校验断言（probes）

### 4.4 新增一种图表类型

1. `scripts/layout-constants.json` 的 `charts.types` 加类型名 + `charts.minSize` 配最小尺寸 + `charts.registry` 登记四元组（html / pptx 通道 / nativeType 或 path / dataTable 策略）
2. 补实现代码：普通图表写进 `references/charts.md`（内联 SVG + `data-chart` 标记 + `f-*`/`s-*` 语义类配色）；复杂信息图页型写进 `references/infographics.md` §六/§八
3. `references/components.md` §46 选型表补一行（内容形态 → 版式 → PPTX 页型映射）
4. 跑 `sync_runtime.py`（图表登记四元组与可达性不变量）+ `audit_styles.py`（图表登记表自洽）+ `regression.py`

### 4.5 新增一种图片版式

1. `scripts/layout-constants.json` 的 `imageSpec.layouts` 加版式名 + `ratioDefault`（比例，如 `"3:1"`）+ `ratioCssClass`（HTML 锁定类，如 `media--r3-1`）+ `recommendedSizePx`（建议像素）
2. `assets/templates/engine.css` 补该锁定类（`.media--r3-1{aspect-ratio:3/1}`）
3. 双引擎渲染：`scripts/build_pptx.js` 与 `assets/pptx-export.js` 的 `imageLayoutShapes` 各加一个分支（几何与比例必须完全一致，否则 HTML/PPTX 会走样）
4. `references/components.md` §11c-1 版式表补一行（layout ↔ HTML 版式 ↔ 比例 ↔ 建议像素 ↔ 适用）
5. 跑 `sync_runtime.py`（会校验「版式 ↔ 比例 ↔ 锁定类 ↔ 双引擎实现」四向完整）+ `build_examples.py` + `regression.py`

> **配图占位**无需新代码：任何版式的 `image.placeholder` 都复用同一几何（原生圆角矩形 + 虚线 + 居中标签），标签串由 `imageSpec.placeholderLabel` 派生，双引擎自动一致。

### 4.6 新增一套风格

`references/styles.md` 写 light+dark 两个覆盖块 → 按上节三处联动改单源（含 `layout-constants.json` 的 `styleAccents` 强调色族与 `styleDataColors` / `styleDataColorsDark` 编码色板 c1–c5）→ `assets/style-gallery.html` 的 `STYLE_META` 数组加一项（可选 `darkMain:true` 表示深色优先卡；卡片列表与配色由单源 `PRESETS` 自动派生）→ `audit_styles.py` 全绿 → 重截参考图。

## 五、构建与打包

```bash
# 环境：Python 标准库（零三方依赖）；cross_verify 可选 python-pptx
#       Node + pptxgenjs（仅精导与回归）：在技能目录 npm install（依 package.json）

python scripts/sync_runtime.py        # ① 单源注入 + 页型四件套 / 图表四元组 / 可达性不变量校验
python scripts/audit_styles.py        # ② WCAG + 双源 + 单源完整性（含编码色板 9×2×5）审计
python scripts/audit_docs.py          # ③ 文档一致性审计（§ 引用/前缀规范/§46 覆盖度/代码节）
python scripts/audit_skill.py         # ④ 技能工程审计（体积预算 / 三档披露 / Gate 0 / 交互预算）
python scripts/build_examples.py      # ⑤ 重建示例矩阵
python evals/run_evals.py --budget    # ⑥ 效率预算自检（可选：--list / --score <报告.html> --trace <trace.json>）
python scripts/regression.py          # ⑦ 全链路回归（发布前必绿）

# 参考图（可选，需 playwright）
npm install playwright && npx playwright install chromium
node scripts/capture_theme_overview.js            # 或 --channel=msedge 用本机浏览器；--scale=1.25 控单张体积

# 打包发布（校验不通过不产出 zip）
python scripts/package_skill.py --check   # 只跑发布门禁：必需文件 / frontmatter / 无临时路径
python scripts/package_skill.py           # → dist/top-ppt-html.zip + dist/top-ppt-html.manifest.json
```

**提交与打包口径**（详见 `.gitignore` 与 `package_skill.py` 头部说明）：

| 类别 | 路径 | 进包 | 入库 |
|------|------|:----:|:----:|
| 技能源（入口/规范/素材/工具） | `SKILL.md` `README.md` `package.json` `assets/` `references/` `scripts/` | ✅ | ✅ |
| 构建与回归产物 | `dist/`（zip、回归 PPTX、探针产物、manifest） | ❌ | ❌ |
| 工具中间产物 | `report-assets/`（prepare_images）、`render-compare/`（render_compare） | ❌ | ❌ |
| 依赖与缓存 | `node_modules/`、`__pycache__/`、`.venv/` | ❌ | ❌ |
| 本地状态 | IDE / 智能体会话与本地缓存目录（如 `.vscode/`、会话记忆等） | ❌ | ❌ |
| 临时脚本 | `scripts/_*`（下划线开头，用后即删） | ❌ | ❌ |

## 六、FAQ / 故障排查

- **技能没被智能体触发？** 检查 `SKILL.md` frontmatter 的 `description` 是否超 1024 字符（超限会被平台截断或拒载）——触发词（Use when）必须留在前 80% 以内。
- **PPTX 出来是浅色但页面是深色？** `REPORT_MODEL.theme` 未与 `data-theme` 同步（validate_report 会 WARN）；`build_pptx.js --theme=dark` 可强制覆盖。
- **regression 报找不到 Node 或 pptxgenjs？** 在技能目录 `npm install pptxgenjs`，或设 `TOP_PPT_NODE_EXE` / `TOP_PPT_NODE_PATH` 环境变量指向已有安装。
- **regression 里 cross_verify 被跳过？** 说明本机没装 python-pptx（可选第三方裁判）；`pip install python-pptx` 后即可启用，不影响交付判定。
- **改了 engine.css 但模板没变？** 模板里是注入副本——跑 `python scripts/sync_runtime.py`，禁止手改模板内联块。
- **预览与导出的 PPTX 不一致？** 两者共用同一序列化引擎，先跑 `sync_runtime.py` 确认常量/schema 未漂移，再跑 `regression.py` 的 cross_verify。
- **浅色模式下最后一页/金句页变成深色？** 该页用了 `band--deep`（反相强调页，浅色主题下必然渲染为深色）——收尾/CTA 改用 `band--accent`，金句改用 `band--accent--solid`；校验器会 WARN（`band--deep` ≤1 处且不得作末页）。
- **数字没法核实，怎么提示用户改？** 用 `.tbd` 标色 + `.tbd-legend`/`.flagbar` 说明（模型同步写 `section.flags`）；规则见 `content-rules.md` 五-b，**只标色不解释会被校验器 WARN**。
- **PPTX 里能放图片吗？** 默认 `pictures=0`（全原生可编辑）；需要时在模型里显式声明 `section.image`（或 `split.right.image`），图片数不得超过声明数（`PICTURES_NOT_DECLARED` 硬拦），`src` 仅允许 data: 内联或相对路径。
- **某页在浏览器里偏高/偏低？** 页高模型默认"每页一屏 + 垂直居中"（`--band-min`）；内容约六七成屏改用 `.band--top`，长结构页（参考资料/附录）用 `.band--flow`。详见 `design-system.md` §1c。

## 七、版本、规范与兼容

- **当前发布版**：v0.1.0（风格语汇 styleIdentity · 布局语法 · 模型单写 · 硬门禁）。**版本单源 = `scripts/layout-constants.json` `version`**；`model-schema.json` / `layoutSlots` 同步该值；`package_skill.py` 与 `sync_runtime.py` 校验一致。
- **frontmatter**：仅 `name` + `description`（触发词写清「做什么 + 何时用」，控制在 700 字符软上限内）。
- **目录与 token 预算**：`SKILL.md`（≤13KB 路由）→ L1 `references/playbook.md`（≤22KB 决策）→ L2 按需（`extract_snippet.py` 节级取码）→ `scripts/` 工具 → `assets/` 素材。`audit_skill.py` 把关体积 / 三档披露 / Gate 0 / 与 references 去重。
- **工作流（模型单写）**：`scaffold_report.py` → 只填 `REPORT_MODEL` → `render_from_model.py --inplace` → `validate_report --strict`（含 PPTX 再走 extract/build/validate_pptx）。
- **变更流水**：见仓库根目录 `CHANGELOG.md`。
- **命名**：`top-ppt-html`；注入标记 `__TOPPPT_*__`；环境变量 `TOP_PPT_NODE_*`；JS API `TopPptHtml`。
- **发布门禁**：`package_skill.py --check` 通过后产出 `dist/top-ppt-html.zip` + manifest（SHA-256）。
