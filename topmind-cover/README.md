# topmind-cover · 封面配图生成

[English](./README.en.md) | 中文

为 X 长文和公众号文章生成封面图的可复用技能。目标：**震撼、醒目、主题突出**。

## 安装

```bash
npx @topmindspace/tms-skills install topmind-cover
```

## 用法

1. 输入文章标题 + 3 个主题关键词 + 平台（x / wechat / both）
2. 按 `references/cover-styles.md` 选风格模板组 prompt（标题字逐字写进 prompt）
3. 用 agent 的图片生成能力出图（横构图 16:9，四周留白 8%）
4. 肉眼检查：标题字逐字正确、主体完整、一眼能说出主题
5. 裁剪落盘：

```bash
python3 scripts/crop-cover.py <主图> --slug <slug> --out-dir <包>/images/
# 产出 00-封面.png (1200×675) + 00-封面-公众号.png (900×383，中央裁剪)
```

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
