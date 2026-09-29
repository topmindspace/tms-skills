---
name: topmind-x-article
version: 0.1.0
description: "X 长文（Article）一键发布：Markdown 原稿 → 可直接复制的 X长文.html（富文本一键复制+配图内嵌）/ X发布稿.txt + 封面图 + 发布清单。沉淀自实战。Use when X 长文、发 X 文章、X article、长文发 X。Do NOT use for 短推文（→ topmind-x）、公众号（→ topmind-wechat-post）。"
action_category: write
triggers:
  - X 长文
  - 发 X 文章
  - X article
  - 长文发 X
  - X 发长文
  - 转纯文本
  - X 纯文本
  - 发 article
  - 一键复制
triggers_cn:
  - 写 X 长文
  - X 长文发布
  - 推特长文
  - twitter 长文
author: TopMindspace
license: MIT
homepage: https://github.com/topmindspace/tms-skills#readme
updated: 2026-09-29
---

# topmind-x-article · X 长文一键发布

把一篇 Markdown 原稿变成"复制 → 粘贴 → 发"的 X 长文发布包。

```
原稿.md → md2x-html.py → X长文.html（一键复制全文+配图）→ 封面图(topmind-cover) → 发布清单 → 人工粘贴发布
原稿.md → md2x.py     → X发布稿.txt（纯文本兜底）
```

## 工作流

1. **转 HTML**（一键复制的核心，首选）：
   ```bash
   python3 scripts/md2x-html.py <原稿>.md --out <包>/X长文.html \
     --images <图1> <图2> ... [--cover cover-1200x675.png]
   ```
   单文件 HTML：内联样式 + 配图 base64 内嵌。浏览器打开后点页顶
   「一键复制全文」，富文本（含格式）进剪贴板，去 X 文章编辑器粘贴。
   转换规则见 `references/x-html-format.md`。
   - `#` 首个标题**不进剪贴板**：手动填入 X 标题栏（工具栏有三步话术提示）。
   - 每张配图自动编号 `[图N]`；图片 data-URI 内嵌，能随粘贴带入编辑器最好，
     带不进去时用图下「下载图片」按钮按编号下载再上传——不用找文件、不用对顺序。
   - 每个 ``` 提示词块渲染为引用块（X 可识别）+ 右上角「复制提示词」按钮，
     一键复制该块纯文本。注意 X 原生代码块/表格/分割线只能走 Insert 菜单，
     粘贴流不承诺还原，详见 `references/x-html-format.md` 的语法映射表。
   - 封面走 `--cover` 只在页顶预览 + 提供下载；**封面始终在 X 编辑器单独上传**
     （X 有独立封面入口）。
2. **转纯文本**（兜底）：`python3 scripts/md2x.py <原稿>.md --out <包>/X发布稿.txt`，
   规则见 `references/x-format.md`。HTML 复制异常时的备用入口。
   转完**通读一遍**：X 不渲染 markdown，标记剥离后断句、emphasis 全靠文字本身，
   读不顺就回原稿改。
3. **封面图**：调 `topmind-cover`，平台选 `x`，得 1200×675 主图。
4. **发布清单**：按 `references/publish-checklist.md` 逐项过。
5. **发布**：用户在 X Article 编辑器粘贴全文、上传封面与配图（按 `[图N]` 编号），
   人工点发布。**API 不发长文**（topmind-x 的 xurl 只覆盖短推文）。
6. **收尾**：记录发布时间与链接；全文抓回核对一遍（标题、数字、图序）。

## 目录约定

```
<包>/
├── 原稿.md            # 输入（或复用既有原稿）
├── X长文.html         # 首选复制入口：浏览器打开，一键复制全文
├── X发布稿.txt        # 纯文本兜底入口
├── cover-1200x675.png # 封面（topmind-cover 产出，X 编辑器单独上传）
└── 发布清单.md        # 本次发布 checklist（含时间、链接）
```

## 实战沉淀

- 补充信息（邀请码、链接、勘误）**不挤正文**，发在发布后首条评论并置顶
- 标题 ≤140 字符，首段 3 行内出钩子；配图逐张按 `[图N]` 顺序上传，传完对照清单点一遍
- 事实修正只改发布包，不回头改已发原文（除非勘误）
- X 编辑器对剪贴板 data-URI 图片的处理不稳定：**文本格式一键复制可靠，
  图片按"能带入则带入，带不入则按编号下载上传"处理**，不要承诺用户图片 100% 一键带图

## When NOT to use

- 280 字短推文 → `topmind-x`
- 公众号 → `topmind-wechat-post`
- 只想存档不发布 → `topmind-capture`
- 写稿（只有发布需求、无原稿时）→ 先走写作技能再回本技能

## 外部依赖

以下技能**不在本仓库**（一般随用户侧 workbuddy 环境提供）；缺失时对应路由能力不可用，
本技能核心流程（原稿转文本、封面、发布清单）不受影响：

- `topmind-x`：280 字短推文发布（xurl 只覆盖短推文，不发长文）。
- `topmind-capture`：「只想存档不发布」时的收录路由。
