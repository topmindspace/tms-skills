# Changelog

## Unreleased

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
