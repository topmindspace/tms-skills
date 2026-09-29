# tms-skills

[English](./README.en.md) | 中文

[![Release](https://img.shields.io/github/v/release/topmindspace/tms-skills?style=flat-square&color=blue)](https://github.com/topmindspace/tms-skills/releases)
[![npm](https://img.shields.io/npm/v/@topmindspace/tms-skills?style=flat-square)](https://www.npmjs.com/package/@topmindspace/tms-skills)
[![CI](https://img.shields.io/github/actions/workflow/status/topmindspace/tms-skills/ci.yml?style=flat-square&label=CI)](https://github.com/topmindspace/tms-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

**TopMindspace 智能体技能 monorepo** —— 演示报告、公众号文章、X 长文、封面配图：四个技能，一个仓库。

### top-ppt-html · 正式商务演示

为**演示报告 / 正式商务演示**而生：**HTML + PPT 双交付**。日常用单文件 HTML 等同幻灯片演示；需要时再导出**高保真可编辑 PPTX**（图表带数据、可标注）。参考 MD3：合适的信息密度、克制的文字 / 图形 / 形状 / 颜色。主场是正式商务演示，不是 gadget。

```bash
npx @topmindspace/tms-skills install top-ppt-html
```

在线体验：[落地页](https://topmindspace.github.io/tms-skills/) · [完整演示文稿](https://topmindspace.github.io/tms-skills/showcase.html) · [风格画廊](https://topmindspace.github.io/tms-skills/style-gallery.html)；黄金样张见 [`top-ppt-html/assets/examples/`](./top-ppt-html/assets/examples/)。

### topmind-wechat-post · 公众号创作

公众号文章全生命周期：交付包、审校改写、质量三关（事实 / 逻辑 / 去 AI 味）、微信内联排版（图片必内嵌）、发布清单与状态同步。脚本纯 Python 标准库，零依赖。

```bash
npx @topmindspace/tms-skills install topmind-wechat-post
```

### topmind-x-article · X 长文一键发布

Markdown 原稿 → 可直接粘贴的纯文本（`md2x.py` 按 X Article 编辑器支持转制：图片→`[图N]`、表格→"项：值"列表）+ 封面图 + 发布清单。发布走人工粘贴，发布后抓回核对。

```bash
npx @topmindspace/tms-skills install topmind-x-article
```

### topmind-cover · 封面配图生成

X 长文与公众号共用的封面图：震撼、醒目、主题突出。**选风格 → 看示例 → 按配方组 prompt** 三步出图，`crop-cover.py` 一键裁出双平台尺寸（X 1200×675、公众号 900×383）。8 种风格索引与配方见 [`references/cover-styles.md`](./topmind-cover/references/cover-styles.md)。

```bash
npx @topmindspace/tms-skills install topmind-cover
```

<p align="center">
  <img src="https://github.com/topmindspace/tms-skills/raw/main/topmind-cover/assets/examples/overview.png" alt="topmind-cover · 8 封面风格总览" width="960" />
</p>

> 让 idea 飞，好想法被看见。

<p align="center">
  <img src="docs/assets/tms-skills-banner.png" alt="tms-skills · top-ppt-html — formal business presentations" width="960" />
</p>

> **警告**：不要安装 `@topmindspace/tms-skills@^2`（2.0.0–2.1.1 已弃用）。当前线 **0.2.x**（`latest`）。

## 技能一览

| 技能 | 版本 | 做什么 |
|------|------|--------|
| [`top-ppt-html`](./top-ppt-html/) | **0.1.19** | 正式商务演示：HTML 可翻页 + 16:9 可编辑 PPTX；双交付 · MD3 密度克制；三模式 × 九风格；strict 0/0 |
| [`topmind-wechat-post`](./topmind-wechat-post/) | **0.1.0** | 公众号文章全生命周期：交付包、审校改写、质量三关、微信内联排版与发布清单 |
| [`topmind-x-article`](./topmind-x-article/) | **0.1.0** | X 长文一键发布：Markdown 原稿转可直接粘贴的纯文本 + 封面图 + 发布清单 |
| [`topmind-cover`](./topmind-cover/) | **0.1.0** | 文章封面配图（X / 公众号共用）：震撼醒目主题突出；8 风格封面风格库 + 17 张双尺寸示例图 |

安装器 [`@topmindspace/tms-skills`](https://www.npmjs.com/package/@topmindspace/tms-skills) 为 **0.3.7**（整仓同 tag 发版）。

> SKILL.md frontmatter 除标准 `name`/`description` 外，本仓库扩展了 `action_category` / `triggers` / `triggers_cn` / `updated` 字段供安装器与路由使用。

## 安装

**npm = 钉版本快照**；**GitHub = 跟仓库 HEAD**。

```bash
npx @topmindspace/tms-skills list
npx @topmindspace/tms-skills install top-ppt-html
npx @topmindspace/tms-skills install top-ppt-html --to ./.claude/skills
npx @topmindspace/tms-skills@0.3.7 install top-ppt-html   # 钉版本
```

```bash
# 跟 HEAD
npx github:topmindspace/tms-skills install top-ppt-html
```

默认探测：`./.agents` → `./.claude` → `./.cursor` → `./.codex` → `./.mimocode`，再用户级 `~/.claude` 等；也可用 `--to`。不要 `npm install top-ppt-html`（技能 id 不是独立包）。

PPTX 精导需在技能目录 `npm install`（pptxgenjs）。HTML 生成仅 Python 标准库。

## 仓库结构

```
tms-skills/
├─ top-ppt-html/             # 技能（SKILL.md + assets + references + scripts）
├─ bin/tms-skills.js         # CLI：list / install
├─ docs/                     # 发布规范 · showcase 截图 · banner · Pages 源
├─ scripts/                  # 仓库级门禁 / 隐私扫描
├─ package.json              # @topmindspace/tms-skills
└─ LICENSE · CHANGELOG.md · README.md · README.en.md
```

## 发布与 CI

| 动作 | GitHub | npm |
|------|:------:|:---:|
| push main | 立即可见 | **不变** |
| tag `vX.Y.Z` | Release + zip | **自动 publish** |

```bash
npm run check && npm run audit && npm run privacy
```

详见 [docs/PUBLISHING.md](./docs/PUBLISHING.md) · [docs/ci.md](./docs/ci.md)。

## 许可证

MIT © TopMindspace — [LICENSE](./LICENSE)
