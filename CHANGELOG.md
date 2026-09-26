## 0.1.8 — 2026-09-26

### Showcase · docs · release polish

- **产品 Showcase**：新增 Mode A 样张 `top-ppt-html/assets/examples/2026-09-26-topmind-tms-skills-showcase.html`（+ model）——介绍 TopMind / tms-skills / top-ppt-html（三模式·风格主题·质量门禁·Fast Mode）；`validate_report --strict` 与 `smoke_pptx` **0/0**。
- **截图**：刷新 `theme-overview*.png`；新增 `docs/showcase/`（showcase 全页 + 三黄金样张关键页）与精简 `top-ppt-html/assets/showcase/`（进技能包，供 README）。
- **README 吸引力**：根 README + 技能 README 增加 banner、风格/模式画廊、showcase 链接与安装钉版本 **0.1.8**。
- **Banner**：`docs/assets/tms-skills-banner.png`。
- **打包**：`package_skill` 纳入 `assets/showcase/*`；examples 最小数量仍 ≥3（黄金样张 + 可选 showcase）。
- **文档清理**：用户向 README 对齐当前产品面；PUBLISHING 版本线 → 0.1.8；`build_examples` 说明允许 showcase 并存。
- 版本对齐 **0.1.8**（根 + 技能 package/lock / SKILL metadata / README）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版。

## 0.1.7 — 2026-09-26

### top-ppt-html · defect opt (D8/D9/D11/D13)

- **P0 D8**：`chartBottom(hasSoWhat, hasFootnote)` 不再 footnote 短路；`Math.min(soWhatY, footnoteY, contentBottomWithNote)` 与 flagY 让位同口径。双通道（`build_pptx.js` / `pptx-export.js`）对齐；flagBar 在 withNote 时底边不越过 `contentBottomWithNote`；Agenda 预留 0.25in 避免 severe 误伤。
- **P0 D9**：`annotation_band_overlap_check` 报告页内**全部**侵入者（去掉首条即 `break`）。
- **P1 D11**：有 so-what 时 `band_top = soWhatY`（6.05），捕获 (6.05, 6.40] 侵入；crush = 自带顶之上压下；注释自形状/窄 accent 条豁免保留。
- **P1 D13**：`ci_skill_gates.sh --with-pptx` 必跑 `smoke_pptx` × business-blue **与** research-mckinsey（覆盖 soWhat+footnote）；graphite-dark 可选。
- **CHROME_DRIFT**：页码只认 `N / M`，不再把年份/Exhibit 编号当页脚（research-mckinsey 假阳性清除）。
- **Fast Mode / 效率**：演讲/汇报线索→Mode A；明确跳过 vs 仍须（质检红线不降）；L0+L1 / `extract_snippet` 纪律不变。
- **门禁**：`test_feedback_gates` 锁定 D8/D9/D11/CHROME；research-mckinsey `--strict` **0/0**。
- 版本对齐 **0.1.7**（根 + 技能 package / SKILL metadata / README / PUBLISHING）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语保持。

## 0.1.6 — 2026-09-25

### CI / Release 硬化
- **根因 A**：`validate_pptx` 的 `ANNOTATION_BAND_OVERLAP` 把全幅背景（底边 7.50in）误判为侵入注释带；改为排除 full-bleed 背景 / 全高装饰条 / chrome 区，同时保留对图例/主图压进 so-what 带的真阳性。
- **根因 A′**：`FONT_SIZE_NOT_SNAPPED` 未收录 `modeTypeScale` 的 **h2=17pt**；改为从 typeScale ∪ 全模式 modeTypeScale ∪ ladder 动态取允许集。
- **冒烟可读性**：`smoke_pptx.sh` 可靠传播 validate 退出码；失败时 stderr 先打错误码/页码短摘要。
- **根因 B**：Release `npm publish` 遇已发布/已 staged 的 **E409** 时改为 exit 0（幂等）；GitHub Release + 资产仍成功。
- **DRY**：`scripts/ci_skill_gates.sh` 为 CI/Release 共用门禁；Release 对齐 CI 的 fixture + `smoke_pptx`；CI concurrency cancel-in-progress；npm cache；python-pptx 仅 PPTX 步骤安装。
- 文档：新增 `docs/ci.md`；版本对齐 **0.1.6**。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁保持。

## 0.1.5 — 2026-09-25

### top-ppt-html · defect close-out

- **P0 D1**：环图右栏可见标题去掉作者约束「禁止叠在弧上」→ 读者向「构成明细」。
- **P0 D2**：`sync_runtime.py` 注入 `/* __TOPPPT_RUNTIME_SHA__:<16hex> */`（源 = `assets/pptx-export.js`）；`validate_report` 缺戳/漂移 FAIL；负例 N19。
- **P1 D3**：`cross_verify.NUMERIC_TOKEN` 增补 YB|ZB|EB|PB 与 kWh|Gbps。
- **P1 D4**：CI 轻量生成 `dist/regression` 样张 + `python-pptx`，使 N4/N5/N7 真正跑通（非全量 regression）。
- **P2**：package-lock 对齐 0.1.5；README/PUBLISHING 2.x 弃用改为事实陈述；`deprecate-npm-2x.sh` 精简为 `@2.x` one-shot + verify；双版本口径（包 semver vs schema `0.1`）写入 SKILL/tech-design。
- **术语**：全库「甲板」→ 演示文稿/样页等（保留英文 trigger `deck`）。

### Installer

- `@topmindspace/tms-skills` → **0.1.5**（整仓同 tag）。

## 0.1.4 — 2026-09-25

### top-ppt-html · craft + quality + docs + perf close-out

- **P0 效率 / agent 工作流**（usage-feedback）：
  - 默认交付 **仅 B 通道 PPTX**（`build_pptx.js`）；A 通道（`pptx-export.js` / `gen_channel_a.js`）限预览与 `cross_verify` / 回归。
  - `extract_snippet` 强制 + **整读大 L2 = FAIL / 不合格**（SKILL + playbook）；`audit_skill` 新增对应门禁。
  - `quality_gate` 对互不依赖子进程（HTML strict / PPTX strict / evals）**并行**执行。
  - Fast / 轻量路径强化 **HTML-first**；PPTX 显式 opt-in（用户要 PPT 或交付含 PPTX）。
  - **未削弱**红线：反截断、图表多样性（`minTypes.presentation=4` / registry）、Mode A 大气正式工艺、Gate 0 语义。
- **质量 / 规范**：对齐 SKILL frontmatter、双 `package.json`、README 钉版本、PUBLISHING、安装说明；跑通 check / audit / feedback gates。
- **docs 工艺改写**：定位强调优雅·美观·大气·演讲/正式场合；版式/排版/色彩/内容组织 + 质检与高保真导出；L0 仍瘦、L2 按需。
- **此前 #7（validator / engine）**：`shape_bounds` 读 `p:xfrm`、`TEXT_OVERFLOW_VERTICAL`、`ANNOTATION_BAND_OVERLAP`、`FONT_SIZE_NOT_SNAPPED`、多系列 vbar、streamgraph 图例内收、image caption `capYImg`——随本版一并发布。

### Installer

- `@topmindspace/tms-skills` → **0.1.4**（整仓同 tag）。

### Intentional leftovers

- 不引入 Claude-only `when_to_use` / 跨端风险 `allowed-tools`（同 0.1.3）。
- `skills-ref validate` 仍为可选，非发布硬依赖。
- layout-constants / model-schema 事实源版本线仍为 `0.1`（patch 记在 package / metadata）。

## 0.1.3 — 2026-09-24

### top-ppt-html · QA close-out + docs

- **P2-4 playbook 拆表**：意图→页型穷举 → `references/page-type-matrix.md`；图表决策表+七种误用 → `references/chart-decision-tree.md`。playbook 保留 Mode 契约 / V1–V4 / 组合 / **图表多样性摘要** / **反截断** / 路径·命令·L2 路由（体积 22KB→~17KB）。
- **版本对齐**：根 README / 技能 README / PUBLISHING / `metadata.version` / 双 `package.json` → **0.1.3**（消除残留 0.1.0 横幅）。
- **IMAGE_CAPTION**：配图页亦认 so-what/lead/figcaption；新增 WARN `IMAGE_NEAR_EMPTY`（近图过空）。
- **P2-2/P2-3**：不引入 Claude-only `when_to_use`、不写跨端风险 `allowed-tools`（`skills-ref validate` 已通过开放标准字段；扩展字段留给宿主实验）。
- **P2-5**：可选 `npx skills-ref@0.1.5 validate ./top-ppt-html`（不作为发布硬依赖；主门禁仍 `audit_skill`）。
- **docs**：根 README 安装表/钉版本/`@0.1.3`；技能 README 改为人类维护指南并指向 SKILL；package REQUIRED + MIN refs ≥25。

### Installer

- `@topmindspace/tms-skills` → **0.1.3**（整仓同 tag）。

### 此前 Unreleased（agent-compat，随 0.1.3 一并发布）

- **P0-1 Trigger eval**：`evals/trigger-queries.json` + `scripts/check_triggers.py`；`package_skill.py --check` 门禁。
- **P0-2 Mode A 读预算诚实**：L0+L1=2；Mode A/Fast 可加 L1.5（`default-surface` + `presentation-craft`）。
- **P0-3 反过读**：禁止整读清单 + 强制 `extract_snippet.py`。
- **P1 Frontmatter / 安装路径 / Fast 最小大纲 / 插画 brief**：license·compatibility·metadata；Cursor/Codex 路径；`illustration-layout.md`；`agents/openai.yaml`。


## 0.1.2 — 2026-09-24

### top-ppt-html · P2 cleanup（advanced 按需 · Mode A 次级骨架 · icons 压缩）

- **Advanced charts 按需**：默认读面 = `charts-discipline` + 核图 8；`charts-extended.md` **禁止预读**，仅意图命中 `extract_snippet.py --chart`。`charts.variety.preferCoreFirst` + validate WARN（A/B）；advanced **计入** `minTypes`（不降 `presentation=4`，不缩 registry）。
- **Mode A 骨架分层**：主力 P1–P4+P6/P10；次级 P7–P9/P11–P12（`layoutSystem.modeSkels` + layout-grammar / default-surface / recommend_layout 同口径）；画廊侧重主力。
- **icons.md 压缩**：语义表 + 禁区 + 尺寸档 + 高频 20 SVG（~8.7KB）；完整枚举 → `docs/archive/refs/icons-catalog.md`；package 仍 REQUIRED。
- **docs 对齐**：SKILL / playbook / presentation-craft / modes / charts 门面同步；Fast Mode + 长文溢出序保持不变。

### Installer

- 安装器 `@topmindspace/tms-skills` → **0.1.2**（随技能包内容更新）。



### top-ppt-html · Long-text / Quality round（反截断 + 门禁加深）

- **反截断政策**：Mode A / content-rules / presentation-craft「长文与信息承载」——溢出顺序固定为 重构→拆页/分章→换形态→有限 fontShrink；**禁止**静默截断 / 砍 so-what / 为疏朗删实质。单页字数改预警（presentation char 1800），不为「字多」单独 FAIL。
- **结构引导取代硬砍刀**：列表/卡片 `maxItemChars` 等改为引导 + prefer；checklist 同步。
- **layout-qa 加深**：`LAYOUT_QA_TRUNCATION` / `OVERFLOW_NO_SPLIT` / `HALF_EMPTY` / `ALIGN_RHYTHM`；presentation `--strict` 仍自动 layout-qa。负例 L4–L6。
- **recommend_layout**：高容量意图 → 多页序列（议程→主张→证据卡→明细），禁一页塞爆。
- **P1-3 charts facade**：纪律优先 → 核图 8 → extended 按需；**不降** `minTypes.presentation=4`。
- **P1-4 会场字号**：pptx-export venue 表（小会议室 / 默认 / 礼堂）。
- **P1-6 chrome**：跨页页脚 y 漂移 `CHROME_DRIFT` WARN + 文档说明。

### top-ppt-html · Presentation Craft（Mode A 工艺）

- **P0-1 图表多样性（用户明确保留）**：**不降** `minTypes.presentation`（仍为 **4**）；registry/advanced 图种保留。纪律改为「按内容选型拉开多样」+ 禁反模式（简单全幅 / 极偏 donut / 为过门禁硬上冷门图）；playbook §五 / layout-qa 同步。
- **P0-2 default-surface**：升为 Mode A / Fast 演示主读面（12 页型 + 8 核图 + V1–V4；P5–P12/advanced 按需）；SKILL L2 索引指向。
- **P0-3 layout-qa 默认**：`validate_report --strict` 在 presentation 下自动 `--layout-qa`；`quality_gate` 同口径；B/C 不强制。
- **P0-4 主张标题**：Mode A action/claim title（禁话题标签）写入 content-rules / modes；校验 WARN。
- **P0-5 `presentation-craft.md`**：中英术语一页纸清单（one idea / 3s / whitespace / CRAP / motion=none / WCAG…）；package REQUIRED。
- **P1**：fillTarget A 58–75% + intentional whitespace 豁免；`recommend_layout` 偏 V1–V4、降 donut 默认权重；Fast 路演/汇报/发布/演讲/demo→A；motion=none 铁律短句。

### top-ppt-html · Batch 3（瘦身）

- **归档 L2**：`industry-benchmark.md` / `design-system-engine.md` → `docs/archive/refs/`（生成路径不读）。
- **layoutSlots 单源**：删除 `scripts/layout_slots.json`；`lib_layout_regions.js` / `sync_runtime.py` 只读 `layout-constants.layoutSlots`。
- **示例**：`assets/examples/` 仅留 3 份黄金样张（每模式 1）；其余 → `docs/archive/examples/`；`build_examples.py` 瘦身为自检（全量脚本归档）。
- **主题 PNG**：`theme-overview*.png` 量化压缩约 −70%。
- **default-surface.md**：12 页型 + 8 图 + V1–V4 速查；playbook §五标注默认 8 核心图。
- **package**：MIN refs ≥20、examples ≥3；`recommend_layout.py` 入 REQUIRED；README 缩为安装+命令索引。

### top-ppt-html · Batch 2（布局选型 + layout-qa + PPTX 对齐）

- **recommend_layout.py**：`--mode A|B|C` + `--intent` / `--from-model` / `--stdin` → `{pageType,skel,chart,rationale,v?}`（V1–V4 / 极偏禁 donut / sizeByComplexity）。
- **validate_report.py --layout-qa**：缺 data-skel、连续同骨架、极偏 donut、演示简单全幅、V 契约；negative_tests 增 L1–L3。
- **cross_verify.py** 默认 SKIP，`--full-ab` 才跑；regression 同口径。
- **build_pptx.js** 尊重 `layoutPreset`（缺省由 pageToPreset 回填，写入备注）。
- **smoke_pptx.sh** + CI skill-gates 冒烟：extract_model → build_pptx → validate_pptx --strict。

# Changelog

## Unreleased

### top-ppt-html 0.1.1 — Batch 1（工作流单写 · Fast Mode）

- **模型单写统一**：playbook / SKILL / pptx-export 命令链均为 scaffold → 只填 `REPORT_MODEL` → `render_from_model --inplace` → `validate_report --strict`（禁 HTML/模型双写）。
- **`render_from_model.py` 纳入 package REQUIRED**；references 最小篇数注释对齐实有数量（≥24）。
- **Fast Mode**：触发词跳过 Gate 0 + 六项；默认 B/mckinsey/light 等；标准路径仍为硬门禁；`audit_skill` 适配豁免声明。
- **归档** `references/reform-plan.md` → `docs/archive/reform-plan.md`；硬门禁改指 `qualityGates` + `failure-modes`。
- 技能 `package.json` 版本对齐仓库叙事 `0.1.1`（LC 仍为 `0.1`）。

## 0.1.1 — 2026-09-24

### Fixes (P0 / P1)

- **Release 顺序与稳健性**：Privacy → 技能门禁 → Package → Collect → GitHub Release → **npm publish（已发布则跳过，避免 E409）** → 再 Prune。
- **Prune 策略**：只删旧 GitHub Release（保留 2 个）；**不再删除 git tags**。
- **多技能发现**：`scripts/discover_skills.js` + CI/Release 动态打包/门禁；`npm run sync:files` 同步 `package.json` `files`。
- **CLI**：校验 skill id；目标目录已存在时须 `--force`；文档口径与 README 对齐（npm 推荐 / GitHub 跟 HEAD）。
- **python3**：根与技能 `package.json`、workflows 统一 `python3`。
- **打包门禁**：`references/layout-grammar.md` 纳入 REQUIRED；去掉与 `theme-overview.png` 完全重复的 `theme-overview-presentation.png`。
- **Lockfile**：提交 `top-ppt-html/package-lock.json`；CI 优先 `npm ci --omit=dev`。
- **npm 2.x**：文档警告勿装 `^2`；提供 `scripts/deprecate-npm-2x.sh`（须维护者本地 npm 登录后执行）。

## 0.1.0 — 2026-09-24

首个公开版本。

### 安装

```bash
npx @topmindspace/tms-skills install top-ppt-html
# 或
npx github:topmindspace/tms-skills install top-ppt-html
```

### 包含

- 技能 **top-ppt-html**（品牌 TopPPT HTML）：单文件 HTML 报告 + 可编辑 16:9 PPTX
- 安装器 CLI **tms-skills**（`list` / `install`）
- 双通道分发：npm 钉版本 / GitHub 跟 HEAD
- tag 发版自动：GitHub Release + npm publish；**Release 只保留最近 2 个**

### 版本策略

- 安装器 `@topmindspace/tms-skills` 与技能 `top-ppt-html` **各自独立**按 semver 演进
- 默认 **patch / minor**；**major 仅用于**技能 id、CLI、注入标记等破坏性变更
- 改代码 ≠ 发 npm：必须 bump 版本并打 tag（或手工 publish）
