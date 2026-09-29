---
name: topmind-cover
version: 0.1.0
description: "文章封面配图生成：X 长文与公众号共用。震撼、醒目、主题突出；平台尺寸规范、风格模板、命名落盘、成图检查全流程覆盖。Use when 封面、封面图、头图、配图、cover。Do NOT use for 正文插图、PPT/报告封面。"
action_category: write
triggers:
  - 封面
  - 封面图
  - 头图
  - 配图
  - 缩略图
  - cover
  - thumbnail
triggers_cn:
  - 公众号封面
  - X 封面
  - 文章封面
author: TopMindspace
license: MIT
homepage: https://github.com/topmindspace/tms-skills#readme
updated: 2026-09-29
---

# topmind-cover · 封面配图生成

为 X 长文和公众号文章生成封面图的可复用技能。目标：**震撼、醒目、主题突出**。

```
标题/主题 → 风格模板 → 生成 → 检查 → 裁剪双尺寸 → 落盘命名
```

## 风格样张

<p align="center">
  <img src="https://github.com/topmindspace/tms-skills/raw/main/topmind-cover/assets/examples/overview.png" alt="topmind-cover · 8 封面风格总览" width="960" />
</p>

| 风格 | 适用场景 |
|------|----------|
| 爆款干货 `gan-huo` | 干货清单、评测、盘点、实测筛选；"我替你试完了/筛完了"类第一人称实测文默认选它 |
| 巨字宣言 `big-type` | 观点评论、深度长文、产品/版本发布宣言；"一句话立场"类文章默认选它 |
| 品牌发布 `brand-launch` | 产品发布、版本更新、官方最佳实践/白皮书；有明确品牌主体的内容首选 |
| 教程步骤 `tutorial-steps` | 教程、上手指南、分步实操、保姆级攻略 |
| IP 趣味 `ip-fun` | 实战案例、数据战报、复盘、系列连载（上/下篇） |
| 资讯快报 `news-flash` | 资讯、快讯、热点解读、人物专访预告、"祛魅/揭秘"类选题 |
| 极简留白 `minimal` | 随笔、书评、轻观点、生活感悟；公众号"轻阅读"类文章 |
| 杂志编辑 `magazine` | 深度访谈、人物特写、商业分析、年度盘点；需要"质感/信任感"时用它 |

单风格大图：`assets/examples/<style>.png`；配方：`references/cover-styles.md`。

## 尺寸表

| 平台 | 尺寸 | 比例 | 备注 |
|------|------|------|------|
| X Article 封面 | 1200×675 | 16:9 | 主尺寸，先按这个生成 |
| 公众号封面大图 | 900×383 | 2.35:1 | 从 16:9 中央裁剪 |

生成 prompt 里写明"横构图 16:9"；公众号版用 `scripts/crop-cover.py` 从主图中央裁出，不重新生成（保系列一致）。

## 工作流

0. **选风格（三步，必做）**：
   ① 按题材从 `references/cover-styles.md` 选 1 种风格（8 选 1）；
   ② 看 `assets/examples/<style>.png` 示例图，确认视觉语言符合预期；
   ③ 按该风格的 prompt 配方组 prompt（把 `{TITLE}` 换成实际标题）。
   示例清单见 `assets/examples/README.md`。
1. **输入**：文章标题、3 个主题关键词、平台（`x` / `wechat` / `both`，默认 both）、
   风格（默认按题材自动选，见 `references/cover-styles.md`）。
   平台只影响生成 prompt 的侧重；裁剪落盘永远产出双尺寸。
2. **组 prompt**：按 `references/cover-styles.md` 对应风格的配方组装
   （标题 ≤10 字逐字写明，防 AI 自造错别字）。
3. **生成**：`media.generate_image`，`name` 用 `<slug>-cover`。
4. **检查**（必做，肉眼看一遍）：
   - 标题字逐字正确，无错别字、无多字少字
   - 主体完整不被裁切，画面不杂乱
   - 一眼能说出主题；说不出就重生成
   - 900×383 版复查：标题字、关键主体不被中央裁剪裁掉（见风格库"安全区铁律"）
5. **裁剪落盘**：
   ```bash
   python3 scripts/crop-cover.py <主图> --out-dir <包>/images/
   ```
   产出 `00-封面.png`（1200×675，X/公众号共用主文件）与 `00-封面-公众号.png`（900×383）。
   公众号包规约：正文引用 `images/00-封面.png`，`图片上传清单.md` 登记两版。
6. **系列感**：同一系列文章固定色系 + 版式语言，prompt 复用同一风格模板。

## 设计铁律

- 一图一主题；主体占画面 40% 以上，居中或三分法
- 大标题 ≤10 字，高对比（暗底亮字 / 亮底深字）
- 四周 8% 安全边距，标题不贴边；标题字另须满足中央垂直 60% 安全区（见风格库"安全区铁律"）
- 忌：元素堆砌、小字密排、多主体打架、标题字错误

## 外部依赖 / 规约来源

- "公众号包规约"（正文引用 `images/00-封面.png`、`图片上传清单.md` 登记两版）
  来自用户侧 workbuddy 环境，仓库内无此文件；缺失时仍按固定命名落盘，
  不阻塞核心流程。

## When NOT to use

- 正文插图：主体是文字说明，按正文配图流程走
- 报告/PPT 封面：走 `top-ppt-html`
- 只想找现成图：走 `image_search` 技能
