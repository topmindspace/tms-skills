# 封面风格示例图

6 种风格 × 2 种尺寸 = 12 张示例（共约 6.4MB，随 npm 包发布，npx 安装即得）：

- `<style>.png`（1200×675，X 长文封面 / 公众号共用主尺寸）
- `<style>-wechat.png`（900×383，公众号封面大图，`scripts/crop-cover.py` 中央裁剪版）

| 文件 | 风格 | 适用场景（一句话） |
|------|------|--------------------|
| `big-poster.png` / `big-poster-wechat.png` | 震撼大字报 | 观点评论、行业观察、热点快评，"一句话立场"类文章默认选它 |
| `tech-future.png` / `tech-future-wechat.png` | 科技未来感 | AI/大模型/智能体/前沿技术题材，X 长文科技类默认风格 |
| `magazine.png` / `magazine-wechat.png` | 杂志编辑风 | 深度访谈、人物特写、商业分析，需要质感与信任感时用它 |
| `minimal.png` / `minimal-wechat.png` | 极简留白 | 随笔、书评、轻观点，给版面"呼吸感"的穿插封面 |
| `guochao.png` / `guochao-wechat.png` | 国潮插画 | 传统文化、历史、节气、非遗、国货品牌，节日特辑首选 |
| `cyber-glitch.png` / `cyber-glitch-wechat.png` | 赛博故障艺术 | 网络文化、赛博朋克、前沿实验，年轻化/亚文化话题 |

详细配方（配色 hex / 字体 / 中英 prompt / 避坑）见 `../references/cover-styles.md`。

## 安全区说明（重要）

所有示例的标题字都落在**中央垂直 60% 安全区**内——这正是 `900×383` 中央裁剪版标题不被裁掉的原因。
自己组 prompt 时务必遵守：标题/关键主体不得超出上下各 13% 的禁区，否则公众号版会被切掉。
反例：标题压在顶部 15% 处时，`-wechat.png` 里只剩半截字（第一版 tech-future/guochao 示例即如此，已修正）。

## 复用声明

**示例图可直接拿去用/改，作封面底图或风格参考。**
拿去用时建议按 `scripts/crop-cover.py` 的流程重新裁剪双尺寸并按包规约命名落盘；
改图时保留原风格的配色与版式语言，只换主体与标题字，以维持系列感。
