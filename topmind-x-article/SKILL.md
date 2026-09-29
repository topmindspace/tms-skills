---
name: topmind-x-article
version: 0.1.0
description: "X 长文（Article）一键发布：Markdown 原稿 → 可直接粘贴的 X发布稿.txt + 封面图 + 发布清单。沉淀自实战。Use when X 长文、发 X 文章、X article、长文发 X。Do NOT use for 短推文（→ topmind-x）、公众号。"
action_category: write
triggers:
  - X 长文
  - 发 X 文章
  - X article
  - 长文发 X
triggers_cn:
  - 写 X 长文
  - X 长文发布
author: TopMindspace
license: MIT
homepage: https://github.com/topmindspace/tms-skills#readme
updated: 2026-09-29
---

# topmind-x-article · X 长文一键发布

把一篇 Markdown 原稿变成"复制 → 粘贴 → 发"的 X 长文发布包。

```
原稿.md → md2x.py → X发布稿.txt → 封面图(topmind-cover) → 发布清单 → 人工粘贴发布
```

## 工作流

1. **转文本**（一键复制的核心）：
   ```bash
   python3 scripts/md2x.py <原稿>.md --out <包>/X发布稿.txt
   ```
   转换规则见 `references/x-format.md`。转完**通读一遍**：X 不渲染 markdown，
   标记剥离后断句、 emphasis 全靠文字本身，读不顺就回原稿改。
2. **封面图**：调 `topmind-cover`，平台选 `x`，得 1200×675 主图。
3. **发布清单**：按 `references/publish-checklist.md` 逐项过。
4. **发布**：用户在 X Article 编辑器粘贴 `X发布稿.txt` 全文、上传封面与配图，
   人工点发布。**API 不发长文**（topmind-x 的 xurl 只覆盖短推文）。
5. **收尾**：记录发布时间与链接；全文抓回核对一遍（标题、数字、图序）。

## 目录约定

```
<包>/
├── 原稿.md            # 输入（或复用既有原稿）
├── X发布稿.txt        # 唯一复制入口：一键全选复制
├── cover-1200x675.png # 封面（topmind-cover 产出）
└── 发布清单.md        # 本次发布 checklist（含时间、链接）
```

## Manus 2.0 实战沉淀

- 补充信息（邀请码、链接、勘误）**不挤正文**，发在发布后首条评论并置顶
- 长文标题 ≤140 字符，首段 3 行内出钩子
- 配图逐张按 `[图N]` 顺序上传，传完对照清单点一遍
- 事实修正只改发布包，不回头改已发原文（除非勘误）

## When NOT to use

- 280 字短推文 → `topmind-x`
- 公众号 → `topmind-wechat-post`
- 只想存档不发布 → `topmind-capture`

## 外部依赖

以下技能**不在本仓库**（一般随用户侧 workbuddy 环境提供）；缺失时对应路由能力不可用，
本技能核心流程（原稿转文本、封面、发布清单）不受影响：

- `topmind-x`：280 字短推文发布（其 xurl 只覆盖短推文，不发长文）。
- `topmind-capture`：「只想存档不发布」时的收录路由。
