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
│  ├─ examples/                 #   3 份黄金样张 + model（每模式 1；风格见 style-gallery）      │
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
│  └─ …（modes / styles / design-system / content-rules / icons / default-surface /     │
│        outline-design / pptx-export / high-fidelity /                               │
│        failure-modes / tech-design；归档见 docs/archive/refs/）                         │
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

---

## 常用命令（细节见 `references/playbook.md`）

```bash
# 标准 / Fast 共用链（模型单写）
python scripts/scaffold_report.py --mode research --style mckinsey --theme light \
  --title "标题" --sections 8 --out report.html
# 只填 window.REPORT_MODEL 后：
python scripts/render_from_model.py report.html --inplace
python scripts/validate_report.py report.html --strict --layout-qa
python scripts/quality_gate.py report.html --deliver

# 布局建议 / PPTX
python scripts/recommend_layout.py --mode B --intent "经营分析" --pages 10 --json
python scripts/extract_model.py report.html report.model.json
node scripts/build_pptx.js report.pptx --model=report.model.json
python scripts/validate_pptx.py report.pptx --strict --model=report.model.json
bash scripts/smoke_pptx.sh

# 门禁
python scripts/package_skill.py --check
python scripts/audit_skill.py && python scripts/audit_docs.py
python scripts/audit_styles.py && python scripts/audit_css.py
python scripts/negative_tests.py
```

## 目录要点

| 路径 | 用途 |
|------|------|
| `SKILL.md` | L0 路由（≤13KB） |
| `references/playbook.md` | L1 决策层 |
| `references/default-surface.md` | 默认 12 页型 + 8 图 + V1–V4 |
| `assets/examples/` | 3 份黄金样张（每模式 1） |
| `assets/style-gallery.html` | 9 风格 × 模式 × 亮暗 |
| `docs/archive/` | 历史规范 / 旧示例 / 全量 build_examples |

风格画廊与主题参考图：`assets/theme-overview*.png`（Gate 0）。完整规范索引见 playbook §十。

