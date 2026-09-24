## Unreleased

### top-ppt-html · Agent Skills 兼容 + 全链路质量（agent-compat）

- **P0-1 Trigger eval**：`evals/trigger-queries.json`（22 正 / 11 负）+ `scripts/check_triggers.py`（keyword/heuristic，无 LLM）；`package_skill.py --check` 门禁。
- **P0-2 Mode A 读预算诚实**：统一 L0+L1=2；Mode A/Fast 可加 L1.5（`default-surface` + `presentation-craft`）——SKILL + playbook 同口径。
- **P0-3 反过读**：SKILL 阶段路由 + playbook §十 明确禁止整读清单；强制 `extract_snippet.py`。
- **P1-1/2 Frontmatter**：`license: MIT` · `compatibility` · `metadata.version/author`；description 祈使 Use when…（去实现jargon）；`audit_skill` 校验可选键。
- **P1-3 安装路径**：`bin/tms-skills.js` 增加 `.cursor` / `.codex`（项目+用户级）；根 README 安装表。
- **P1-4 Fast 最小大纲**：`outline-design.md`「轻量最小集」；SKILL Fast/轻量路径链接。
- **P1-5 插画 brief**：新建 `references/illustration-layout.md`；接入 L2 / default-surface / presentation-craft / playbook。
- **配图质量**：presentation-craft / playbook 插画页规则；`validate_report` WARN `IMAGE_CAPTION` + 负例 N18。
- **P2**：`agents/openai.yaml`（Codex UI 元数据）。
- **红线保持**：`minTypes.presentation≥4`；反截断溢出序；Mode A 大气正式演示。**本轮不发版 / 不打 tag / 不 npm publish。**

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
