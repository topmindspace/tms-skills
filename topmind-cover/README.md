# topmind-cover · 封面配图生成

[English](./README.en.md) | 中文

为 X 长文和公众号文章生成封面图的可复用技能。目标：**震撼、醒目、主题突出**。

- 版本：**v0.1.0**（与 `@topmindspace/tms-skills@0.3.8` 同 tag）

## 风格样张

<p align="center">
  <img src="https://github.com/topmindspace/tms-skills/raw/main/topmind-cover/assets/examples/overview.png" alt="topmind-cover · 8 封面风格总览" width="960" />
</p>

8 种风格（爆款干货 / 巨字宣言 / 品牌发布 / 教程步骤 / IP 趣味 / 资讯快报 / 极简留白 / 杂志编辑）：适用场景、配色故事、抽象设计原则、中英 prompt 配方见 [`references/cover-styles.md`](./references/cover-styles.md)；单风格大图在 [`assets/examples/`](./assets/examples/)。

## 安装

```bash
npx @topmindspace/tms-skills install topmind-cover
```

## 用法

0. **选风格**：按题材从 `references/cover-styles.md` 选 1 种（8 选 1）→ 看示例图确认视觉语言。
1. **标题提炼**：先定标题文案（一般 ≤10 字），用该风格章节的标题写法规范；不满意重写，不先画图。
2. **构图简报**：一句话 brief（主题/受众/情绪/视觉隐喻/配色方向），组 prompt 前先写。
3. 输入文章标题 + 3 个主题关键词 + 平台（x / wechat / both，默认 both）。
4. 用 agent 的图片生成能力出图（横构图 16:9，四周留白 8%）。
5. **冲击力自检**（必做）：按 [SKILL.md 冲击力自检清单](./SKILL.md#冲击力自检清单) 逐项过；不通过→调 prompt 重生成，最多 3 次。
6. 裁剪落盘：

```bash
python3 scripts/crop-cover.py <主图> --out-dir <包>/images/
# 产出 00-封面.png (1200×675) + 00-封面-公众号.png (900×383，中央裁剪)
```

## 尺寸

| 平台 | 尺寸 | 比例 |
|------|------|------|
| X Article 封面 | 1200×675 | 16:9（主图） |
| 公众号封面大图 | 900×383 | 2.35:1（中央裁） |

## 设计铁律

一图一主题；主体占画面 40%+；大标题 ≤10 字高对比；忌元素堆砌、小字密排、多主体打架。**安全区铁律**：标题字与关键主体必须落在画面中央垂直 60% 安全区内。

## 开发

```bash
python3 scripts/package_skill.py --check
python3 scripts/negative_tests.py
```
