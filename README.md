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

X 长文与公众号共用的封面图：震撼、醒目、主题突出。内置 **6 种封面风格库**（震撼大字报 / 科技未来感 / 杂志编辑风 / 极简留白 / 国潮插画 / 赛博故障艺术，含适用场景、配色 hex、字体建议、中英 prompt 配方）+ **12 张双尺寸示例图**（`assets/examples/`，随包发布）：**选风格 → 看示例 → 按配方组 prompt** 三步出图，`crop-cover.py` 一键裁出双平台尺寸（X 1200×675、公众号 900×383）。

```bash
npx @topmindspace/tms-skills install topmind-cover
```

> 让 idea 飞，好想法被看见。

<p align="center">
  <img src="docs/assets/tms-skills-banner.png" alt="tms-skills · top-ppt-html — formal business presentations" width="960" />
</p>

> **警告**：不要安装 `@topmindspace/tms-skills@^2`（2.0.0–2.1.1 已弃用）。当前线 **0.2.x**（`latest`）。

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
| [`top-ppt-html`](./top-ppt-html/) | **0.1.19** | 正式商务演示：HTML 可翻页 + 16:9 可编辑 PPTX；双交付 · MD3 密度克制；三模式 × 九风格；strict 0/0 |
| [`topmind-wechat-post`](./topmind-wechat-post/) | **0.1.0** | 公众号文章全生命周期：交付包、审校改写、质量三关、微信内联排版与发布清单 |
| [`topmind-x-article`](./topmind-x-article/) | **0.1.0** | X 长文一键发布：Markdown 原稿转可直接粘贴的纯文本 + 封面图 + 发布清单 |
| [`topmind-cover`](./topmind-cover/) | **0.1.0** | 文章封面配图（X / 公众号共用）：震撼醒目主题突出；6 风格封面风格库 + 12 张双尺寸示例图，尺寸规范 + 裁剪落盘 |

安装器 [`@topmindspace/tms-skills`](https://www.npmjs.com/package/@topmindspace/tms-skills) 为 **0.3.0**（整仓同 tag 发版）。

### topmind-cover · 封面风格库

| 风格 | 一句话 | 典型题材 |
|------|--------|----------|
| 震撼大字报 `big-poster` | 一句话立场，冲击力拉满 | 观点评论、热点快评 |
| 科技未来感 `tech-future` | 霓虹蓝/电光紫，深空藏青底 | AI / 大模型 / 智能体 |
| 杂志编辑风 `magazine` | 克制高级，质感与信任感 | 深度访谈、人物特写 |
| 极简留白 `minimal` | 大面积留白，给版面呼吸感 | 随笔、书评、轻观点 |
| 国潮插画 `guochao` | 朱红/黛青/鎏金，文化感 | 传统文化、节气、非遗 |
| 赛博故障艺术 `cyber-glitch` | RGB 错位，数字 decay 美学 | 网络文化、赛博朋克 |

**三步出图**：① 按题材从 6 风格选 1 → ② 看 [`topmind-cover/assets/examples/`](./topmind-cover/assets/examples/) 对应示例图 → ③ 按 [`references/cover-styles.md`](./topmind-cover/references/cover-styles.md) 该风格的 prompt 配方组 prompt。12 张示例图（6 风格 × 1200×675 主图 + 900×383 公众号中央裁剪版，约 6.4MB）随 npm 包发布；**安全区铁律**：标题字与关键主体必须落在画面中央垂直 60% 安全区内。

## 安装

**npm = 钉版本快照**；**GitHub = 跟仓库 HEAD**。

```bash
npx @topmindspace/tms-skills list
npx @topmindspace/tms-skills install top-ppt-html
npx @topmindspace/tms-skills install top-ppt-html --to ./.claude/skills
npx @topmindspace/tms-skills@0.3.0 install top-ppt-html   # 钉版本
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
