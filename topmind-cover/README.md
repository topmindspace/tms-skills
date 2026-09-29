# topmind-cover · 封面配图生成

[English](./README.en.md) | 中文

为 X 长文和公众号文章生成封面图的可复用技能。目标：**震撼、醒目、主题突出**。

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

## 安装

```bash
npx @topmindspace/tms-skills install topmind-cover
```

## 用法

0. **选风格（三步，必做）**：按题材从 `references/cover-styles.md` 选 1 种风格（8 选 1）
   → 看 `assets/examples/<风格>.png` 示例图，确认视觉语言符合预期
   → 按该风格的 prompt 配方组 prompt（把 `{TITLE}` 换成实际标题）。
1. 输入文章标题 + 3 个主题关键词 + 平台（x / wechat / both，默认 both）。
2. 用 agent 的图片生成能力出图（横构图 16:9，四周留白 8%）。
3. 肉眼检查（必做）：标题字逐字正确、主体完整、一眼能说出主题；标题字与关键主体
   落在中央垂直 60% 安全区内（900×383 中央裁剪不切字）。
4. 裁剪落盘：

```bash
python3 scripts/crop-cover.py <主图> --out-dir <包>/images/
# 产出 00-封面.png (1200×675) + 00-封面-公众号.png (900×383，中央裁剪)
```

## 风格库与示例图

- **风格库** `references/cover-styles.md`：8 种风格（爆款干货 / 巨字宣言 / 品牌发布 / 教程步骤 / IP 趣味 / 资讯快报 / 极简留白 / 杂志编辑），每种含适用场景、配色 hex、字体建议、中英 prompt 配方、避坑。
- **示例图** [assets/examples/](./assets/examples/)：17 张（8 风格 × 1200×675 主图 + 900×383 公众号中央裁剪版 + `overview.png` 8 宫格总览，约 7.5MB），随包发布，可直接拿去用/改（清单 + 安全区说明 + 复用声明见 [assets/examples/README.md](./assets/examples/README.md)）。
- **安全区铁律**：标题字与关键主体必须落在画面中央垂直 60% 安全区内（上下各预留 13%+ 不放标题字），否则公众号中央裁剪会切掉标题。

## 尺寸

| 平台 | 尺寸 | 比例 |
|------|------|------|
| X Article 封面 | 1200×675 | 16:9（主图） |
| 公众号封面大图 | 900×383 | 2.35:1（中央裁） |

## 设计铁律

一图一主题；主体占画面 40%+；大标题 ≤10 字高对比；忌元素堆砌、小字密排、多主体打架。

## 开发

```bash
python3 scripts/package_skill.py --check
python3 scripts/negative_tests.py
```
