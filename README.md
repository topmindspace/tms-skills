# tms-skills

[English](./README.en.md) | 中文

[![Release](https://img.shields.io/github/v/release/topmindspace/tms-skills?style=flat-square&color=blue)](https://github.com/topmindspace/tms-skills/releases)
[![npm](https://img.shields.io/npm/v/@topmindspace/tms-skills?style=flat-square)](https://www.npmjs.com/package/@topmindspace/tms-skills)
[![CI](https://img.shields.io/github/actions/workflow/status/topmindspace/tms-skills/ci.yml?style=flat-square&label=CI)](https://github.com/topmindspace/tms-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

**TopMindspace 智能体技能 monorepo** — 把好想法做成可上台的正式商务演示。

当前主技能 **[top-ppt-html](./top-ppt-html/)**：**HTML + PPT 双交付**，为**演示报告 / 正式商务演示**而生。

### 为什么是 top-ppt-html

市面 PPT 技能很多：有的偏花哨装饰，有的偏咨询 dump。**top-ppt-html** 走另一条路——

- **双交付**：日常用**单文件 HTML**等同幻灯片演示；需要时再导出**高保真可编辑 PPTX**（图表带数据、可标注）
- **参考 MD3**：整体空间布局、**合适的信息密度**、克制的文字 / 图形 / 形状 / 颜色
- **产出即上台**：直观、美观大气、风格多样；主场是正式商务演示，不是 gadget

> 让 idea 飞，好想法被看见。

<p align="center">
  <img src="docs/assets/tms-skills-banner.png" alt="tms-skills · top-ppt-html — formal business presentations" width="960" />
</p>

> **警告**：不要安装 `@topmindspace/tms-skills@^2`（2.0.0–2.1.1 已弃用）。当前线 **0.1.x**（`latest`）。

## 一眼看到工艺

### 主题总览（Gate 0）

<p align="center">
  <img src="top-ppt-html/assets/theme-overview.png" alt="演示模式 · business-blue 主题总览" width="900" /><br/>
  <sub>演示 · business-blue（默认）· 另见 <a href="./top-ppt-html/assets/style-gallery.html">style-gallery</a> · <a href="./top-ppt-html/assets/theme-overview-research.png">研究总览</a> · <a href="./top-ppt-html/assets/theme-overview-architecture.png">架构总览</a></sub>
</p>

### 风格封面

| 演示 · business-blue | 研究 · mckinsey | 架构 · graphite-dark |
|:---:|:---:|:---:|
| ![bizblue](docs/showcase/presentation-business-blue/bizblue-cover.png) | ![mckinsey](docs/showcase/research-mckinsey/mckinsey-cover.png) | ![graphite](docs/showcase/architecture-graphite-dark/graphite-cover.png) |

### 产品 Showcase（Mode A · 双交付叙事 · 多图 · Header 工具栏）

| 定位 | 双交付 | 图表 | Header 工具栏 |
|:---:|:---:|:---:|:---:|
| ![pos](docs/showcase/topmind-showcase/showcase-s1.png) | ![split](docs/showcase/topmind-showcase/showcase-s3.png) | ![charts](docs/showcase/topmind-showcase/showcase-s5.png) | ![toolbar](docs/showcase/topmind-showcase/showcase-s11.png) |

**在线体验**

- 落地页：[topmindspace.github.io/tms-skills/](https://topmindspace.github.io/tms-skills/)
- 完整演示文稿：[showcase.html](https://topmindspace.github.io/tms-skills/showcase.html)
- 风格画廊：[style-gallery.html](https://topmindspace.github.io/tms-skills/style-gallery.html)
- 仓库内交互画廊：[top-ppt-html/assets/style-gallery.html](./top-ppt-html/assets/style-gallery.html)
- 仓库内 Showcase：[top-ppt-html/assets/examples/2026-09-26-topmind-tms-skills-showcase.html](./top-ppt-html/assets/examples/2026-09-26-topmind-tms-skills-showcase.html)
- 更多截图：[docs/showcase/](./docs/showcase/)

### HTML Header 工具栏（打开即用）

| 控件 | 快捷键 | 做什么 |
|------|--------|--------|
| 亮暗主题 | **T** | 浅/深切换，按文件记忆，同步 `REPORT_MODEL.theme` |
| 风格选择 | 9 套 | 九风格实时换肤；交付前写回 `REPORT_MODEL.style` |
| 预览 PPTX | **P** | 页序列预览 + 可复制精导提示词 |
| PPT 生成指引 | **H** | 双通道与环境说明 |
| 全屏 | **F** | 沉浸演示 |
| 收起工具栏 | **B** | 折叠为迷你条 |

详见 [top-ppt-html/README.md](./top-ppt-html/README.md#html-header-工具栏) · [SKILL.md 交付物](./top-ppt-html/SKILL.md)。

## 技能一览

| 技能 | 版本 | 做什么 |
|------|------|--------|
| [`top-ppt-html`](./top-ppt-html/) | **0.1.17** | 正式商务演示：HTML 可翻页 + 16:9 可编辑 PPTX；双交付 · MD3 密度克制；三模式 × 九风格；strict 0/0 |

安装器 [`@topmindspace/tms-skills`](https://www.npmjs.com/package/@topmindspace/tms-skills) 同为 **0.1.17**（整仓同 tag 发版）。

## 安装

**npm = 钉版本快照**；**GitHub = 跟仓库 HEAD**。

```bash
npx @topmindspace/tms-skills list
npx @topmindspace/tms-skills install top-ppt-html
npx @topmindspace/tms-skills install top-ppt-html --to ./.claude/skills
npx @topmindspace/tms-skills@0.1.17 install top-ppt-html   # 钉版本
```

```bash
# 跟 HEAD
npx github:topmindspace/tms-skills install top-ppt-html
```

默认探测：`./.agents` → `./.claude` → `./.cursor` → `./.codex` → `./.mimocode`，再用户级 `~/.claude` 等；也可用 `--to`。不要 `npm install top-ppt-html`（技能 id 不是独立包）。

PPTX 精导需在技能目录 `npm install`（pptxgenjs）。HTML 生成仅 Python 标准库。

## 黄金样张

| 模式 | 文件 |
|------|------|
| A 演示 | [`2026-09-09-presentation-business-blue`](./top-ppt-html/assets/examples/2026-09-09-presentation-business-blue.html) |
| B 研究 | [`2026-09-09-research-mckinsey`](./top-ppt-html/assets/examples/2026-09-09-research-mckinsey.html) |
| C 架构 | [`2026-09-09-architecture-graphite-dark`](./top-ppt-html/assets/examples/2026-09-09-architecture-graphite-dark.html) |
| 产品 Showcase | [`2026-09-26-topmind-tms-skills-showcase`](./top-ppt-html/assets/examples/2026-09-26-topmind-tms-skills-showcase.html)（双交付叙事 · 5 种图表 · Header 工具栏） |

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
# PPTX 冒烟（含 McKinsey）：bash scripts/ci_skill_gates.sh --with-pptx
```

详见 [docs/PUBLISHING.md](./docs/PUBLISHING.md) · [docs/ci.md](./docs/ci.md)。

## 许可证

MIT © TopMindspace — [LICENSE](./LICENSE)
