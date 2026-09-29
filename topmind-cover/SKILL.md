---
name: topmind-cover
version: 0.1.0
description: "文章封面配图生成：X 长文与公众号共用。震撼、醒目、主题突出；平台尺寸规范、风格模板、命名落盘、成图检查全流程覆盖。Use when 文章封面、封面图、头图、题图、cover。Do NOT use for 正文插图、PPT/报告封面。"
action_category: write
triggers:
  - 封面
  - 封面图
  - 头图
  - 题图
  - 首图
  - 配图
  - 缩略图
  - banner
  - cover
  - thumbnail
triggers_cn:
  - 公众号封面
  - 公众号题图
  - X 封面
  - X 首图
  - 文章封面
author: TopMindspace
license: MIT
homepage: https://github.com/topmindspace/tms-skills#readme
updated: 2026-09-29
---

# topmind-cover · 封面配图生成

为 X 长文和公众号文章生成封面图。目标：**震撼、醒目、主题突出**。

```
标题/主题 → 风格模板 → 生成 → 检查 → 裁剪双尺寸 → 落盘命名
```

## 风格索引

风格总览图见 `assets/examples/overview.png`（8 宫格，离线可看）。

| 风格 | 首选题材 |
|------|----------|
| 爆款干货 `gan-huo` | 干货清单、评测、盘点、实测筛选 |
| 巨字宣言 `big-type` | 观点评论、深度长文、发布宣言 |
| 品牌发布 `brand-launch` | 产品发布、版本更新、官方白皮书 |
| 教程步骤 `tutorial-steps` | 教程、上手指南、分步实操 |
| IP 趣味 `ip-fun` | 实战案例、数据战报、复盘、连载 |
| 资讯快报 `news-flash` | 资讯快讯、热点解读、揭秘类选题 |
| 极简留白 `minimal` | 随笔、书评、轻观点 |
| 杂志编辑 `magazine` | 深度访谈、人物特写、商业分析 |

适用场景细则、配色故事、prompt 配方见 `references/cover-styles.md`；单风格大图 `assets/examples/<style>.png`。

> 示例图为原创演示：只学设计原则，不临摹第三方版式（详见 `references/cover-styles.md` 顶部"原创铁律"）。

## 尺寸表

| 平台 | 尺寸 | 比例 | 备注 |
|------|------|------|------|
| X Article 封面 | 1200×675 | 16:9 | 主尺寸，先按这个生成 |
| 公众号封面大图 | 900×383 | 2.35:1 | 从 16:9 中央裁剪 |

生成 prompt 里写明"横构图 16:9"；公众号版用 `scripts/crop-cover.py` 从主图中央裁出，不重新生成（保系列一致）。

## 工作流

0. **选风格（三步，必做）**：① 按题材从 `references/cover-styles.md` 选 1 种（8 选 1）→ ② 看 `assets/examples/<style>.png` 确认视觉语言 → ③ 按该风格配方组 prompt（`{TITLE}` 换实际标题）。
1. **输入**：文章标题、3 个主题关键词、平台（`x` / `wechat` / `both`，默认 both，平台只影响 prompt 侧重；裁剪落盘永远产出双尺寸）。
2. **组 prompt**：按风格配方组装（标题 ≤10 字逐字写明，防 AI 自造错别字）。
3. **生成**：`media.generate_image`，`name` 用 `<slug>-cover`。
4. **检查**（必做，肉眼看一遍）：标题字逐字正确无错别字；主体完整不杂乱；一眼能说出主题；900×383 版标题字与关键主体不被中央裁剪裁掉（风格库"安全区铁律"）。
5. **裁剪落盘**：
   ```bash
   python3 scripts/crop-cover.py <主图> --out-dir <包>/images/
   ```
   产出 `00-封面.png`（1200×675，X/公众号共用主文件）与 `00-封面-公众号.png`（900×383）。
   公众号包规约：正文引用 `images/00-封面.png`，`图片上传清单.md` 登记两版。
6. **系列感**：同一系列固定色系 + 版式语言，prompt 复用同一风格模板。

## 设计铁律

- 一图一主题；主体占画面 40% 以上，居中或三分法
- 大标题 ≤10 字，高对比（暗底亮字 / 亮底深字）
- 四周 8% 安全边距，标题不贴边；标题字另须满足中央垂直 60% 安全区（见风格库"安全区铁律"）
- 忌：元素堆砌、小字密排、多主体打架、标题字错误

## 外部依赖 / 规约来源

"公众号包规约"（正文引用 `images/00-封面.png`、`图片上传清单.md` 登记两版）来自用户侧
workbuddy 环境，仓库内无此文件；缺失时仍按固定命名落盘，不阻塞核心流程。

## When NOT to use

- 正文插图：主体是文字说明，按正文配图流程走
- 报告/PPT 封面：走 `top-ppt-html`
- 只想找现成图：走 `image_search` 技能
