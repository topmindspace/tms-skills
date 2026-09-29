# 封面风格库（6 种）

选风格先看题材，再看系列延续性。同一系列固定一个模板，只换主体与标题字。
选风格三步走：**先选风格 → 看 `assets/examples/` 对应示例图 → 按本库配方组 prompt**。

每种风格的 prompt 配方都是中英双语模板：`{TITLE}` 为标题文字占位符（≤10 字，
示例图上用 2~6 字短标题），尺寸固定 1200×675、横构图 16:9。

## 安全区铁律（所有风格通用）

900×383 公众号版是从 1200×675 主图**中央裁剪**（上下各裁约 12.2%）：
**标题字与关键主体必须落在画面中央垂直 60% 安全区内**
（上下各预留 13%+ 不放标题字），否则公众号版会被裁掉。
选风格、组 prompt、检查成图时都要先过这一条；以下各风格的标题位置描述
均已按此约束书写。

---

## 1. big-poster · 震撼大字报

- **适用场景**：观点评论、行业观察、热点快评；X 长文首图、公众号头图都适用，
  是"一句话立场"类文章的默认选择。
- **配色方案**：主色深红 `#C8102E`（或墨黑 `#111111` 做深色版），
  辅色明黄 `#FFC400`（点缀线条/印章），文字色纯白 `#FFFFFF`。
- **字体建议**：中文标题用 Noto Sans SC Black / 思源黑体 Heavy，
  标题字号占画面高度 28%~35%，字距紧凑，可做轻微倾斜或描边增强冲击力。
- **prompt 配方**：
  ```
  中文：震撼中文大字报风格封面，纯深红底色配黑色斜切色块，纸张颗粒质感，
  画面中央巨型白色粗黑标题"{TITLE}"，占画面一半，极简构图，高对比，
  横构图16:9，尺寸1200×675，除标题外无其他文字。

  EN: Bold Chinese big-character poster style cover, solid crimson red
  background with black diagonal bands, subtle paper grain. Giant bold white
  Chinese title "{TITLE}" dominates the center, half the frame. Minimal
  composition, high contrast, landscape 16:9, 1200x675, no other text.
  ```
- **避坑**：
  - 标题超过 10 个字必翻车——大字报风格下长标题会被模型挤成小字或错字；
    长标题先压缩再生成。
  - 忌加副标题/英文小字/日期：模型极易在小字上造错别字，且破坏冲击力。
  - 深色版（墨黑底）配白字时，检查文字与背景对比度，边缘加细描边防"糊"。

## 2. tech-future · 科技未来感

- **适用场景**：AI/大模型/智能体/前沿技术题材；X 长文科技类默认风格，
  Manus / Cue / Agent 这类题材首选。
- **配色方案**：主色深空藏青 `#0A1628`（近黑），辅色霓虹蓝 `#38BDF8`、
  电光紫 `#A78BFA`（渐变光效），文字色纯白 `#FFFFFF`。
- **字体建议**：中文标题用 Noto Sans SC Bold，字号占画面高度 18%~24%，
  落在画面上部、中央垂直安全区内；英文/数字点缀可用 Rajdhani 或 DIN 风格细体（仅作装饰字，
  必须人工核对拼写）。
- **prompt 配方**：
  ```
  中文：科技未来感封面，深空藏青近黑背景，霓虹蓝色电路线条与细颗粒星空，
  中央主体为发光的抽象AI核心光球，边缘光干净，画面上部、中央垂直安全区内
  白色粗黑中文标题"{TITLE}"，电影感光影，极简不堆砌，横构图16:9，尺寸1200×675，
  除标题外无其他文字。

  EN: Futuristic tech cover, deep navy-black space background with glowing
  neon-blue circuit lines and fine starfield particles. A sleek abstract
  glowing AI core orb as central subject with clean rim light. Bold white
  Chinese title "{TITLE}" in the upper third. Cinematic lighting, minimal,
  landscape 16:9, 1200x675, no other text.
  ```
- **避坑**：
  - 霓虹元素别超过 2 种颜色，三色以上画面立刻变"杀马特"。
  - 主体（光球/芯片/机器人）必须完整不被裁切，且占画面 40% 以上，
    否则标题和背景会"各说各话"。
  - 星空颗粒开太大容易显脏：要求"细颗粒"而非"密集星空"。

## 3. magazine · 杂志编辑风

- **适用场景**：深度访谈、人物特写、商业分析、年度盘点；公众号长文首选，
  需要"质感/信任感"时用它。
- **配色方案**：主色暖灰 `#E8E4DC`（浅底）或墨黑 `#141414`（深底版），
  辅色砖红 `#B03A2E`（细线/点缀），文字色炭黑 `#2B2B2B`（浅底）/
  米白 `#F5F1E8`（深底）。
- **字体建议**：中文标题用 Noto Serif SC Bold（宋体感）或思源黑体 Bold，
  字号占画面高度 14%~20%，落在左侧下方、中央垂直安全区内；标题上方配一条细色线，
  杂志感立刻出来。
- **prompt 配方**：
  ```
  中文：杂志编辑风封面，暖灰色影棚背景，右侧三分之一处黑白质感人物肖像，
  左侧大面积留白，左侧下方（中央垂直安全区内）炭黑色典雅粗体中文标题"{TITLE}"，标题上方一条砖红
  色细线，克制高级，杂志封面美学，横构图16:9，尺寸1200×675，除标题外无其他文字。

  EN: Editorial magazine style cover, warm light-gray studio background,
  dramatic black-and-white portrait in the right third, generous negative
  space on the left. Dark charcoal elegant bold Chinese title "{TITLE}" at
  lower left, with a thin brick-red rule line above it. Refined, minimal,
  magazine cover aesthetic, landscape 16:9, 1200x675, no other text.
  ```
- **避坑**：
  - 人物肖像必须用"泛指"描述（商务人士/学者剪影），不得出现可识别的真实人物长相；
    隐私红线。
  - 留白区别手痒加装饰字——杂志风的力量全在克制，加元素必俗。
  - 深底版和浅底版不要混用：同一系列固定一种底色。

## 4. minimal · 极简留白

- **适用场景**：随笔、书评、轻观点、生活感悟；公众号"轻阅读"类文章，
  或系列中需要"呼吸感"的穿插封面。
- **配色方案**：主色米白 `#F7F4EC`（或冷白 `#F2F4F6`），
  辅色淡墨 `#9AA0A6`（小面积点缀），文字色深灰 `#3A3A3A`。
- **字体建议**：中文标题用 Noto Sans SC Medium（不要用 Black，太重），
  字号占画面高度 8%~12%，落在左下角、中央垂直安全区内，留白 ≥60%。
- **prompt 配方**：
  ```
  中文：极致极简主义封面，暖米白背景，大面积留白，一处微小的水墨笔触
  （如孤鸟剪影）点缀在画面右侧中央（中央垂直安全区内），左下角（中央垂直安全区内）
  小字号深灰色中文标题"{TITLE}"，呼吸感强，禅意，横构图16:9，尺寸1200×675，除标题外无其他文字。

  EN: Extreme minimalism cover, warm off-white background with vast empty
  space, one tiny ink-brush stroke (like a lone bird silhouette) near the
  center-right. Small dark-gray Chinese title "{TITLE}" in delicate bold type
  at the lower-left corner. Calm, airy, zen aesthetic, landscape 16:9,
  1200x675, no other text.
  ```
- **避坑**：
  - 极简风对"杂物"零容忍：模型爱加云/山/多余笔触，prompt 里明确"一处""微小""无其他元素"。
  - 标题字别贪大：字一大立刻变"大字报"，极简感全失。
  - 公众号 900×383 中央裁剪会吃掉左右留白——主体和标题尽量往中央安全区放。

## 5. guochao · 国潮插画

- **适用场景**：传统文化、历史、节气、非遗、国货品牌题材；公众号文化类、
  节日特辑首选。
- **配色方案**：主色朱红 `#D43D2A`，辅色黛青 `#2F4F4F`、鎏金 `#C9A86A`
  （标题/纹样），文字色金 `#C9A86A` 或米白 `#F5EFE0`。
- **字体建议**：中文标题用书法感粗体（站酷快乐体/演示佛系体风格描述，
  或 Noto Serif SC Black），字号占画面高度 20%~28%，可竖排，
  落在上方（中央垂直安全区内）或中央。
- **prompt 配方**：
  ```
  中文：国潮插画风封面，朱红与黛青大色块碰撞，祥云海浪传统纹样作暗纹背景，
  中央主体为风格化国风人物或神兽插画，上方（中央垂直安全区内）鎏金书法感
  中文标题"{TITLE}"，浓烈鲜明，文化感，横构图16:9，尺寸1200×675，除标题外无其他文字。

  EN: Guochao Chinese-trendy illustration cover, bold vermilion red and dark
  teal color blocks, traditional cloud-and-wave patterns as subtle background
  texture. Stylized Chinese-style figure or mythical beast illustration as
  central subject. Golden calligraphy-style Chinese title "{TITLE}" at the
  top. Vibrant, cultural, landscape 16:9, 1200x675, no other text.
  ```
- **避坑**：
  - 忌用真实历史人物/文物高精度复刻做主体——一是版权风险，二是模型画不准；
    用"风格化插画"表述。
  - 朱红+黛青+鎏金已是三色上限，别再加第四色。
  - 竖排标题时检查字序：模型偶发把竖排字写成横排或倒序，生成后逐字核对。

## 6. cyber-glitch · 赛博故障艺术

- **适用场景**：网络文化、赛博朋克题材、前沿实验、数字艺术评论；
  X 长文年轻化/亚文化话题，公众号慎用（读者年龄层偏大时跳过）。
- **配色方案**：主色深黑 `#0D0D12`，辅色品红 `#FF2E88`、电青 `#00E5FF`
  （RGB 分离故障色），文字色白 `#FFFFFF`（带品红/青色错位重影）。
- **字体建议**：中文标题用 Noto Sans SC Black，字号占画面高度 18%~25%，
  居中，允许轻微 RGB 错位/扫描线质感，但笔画必须完整可辨认。
- **prompt 配方**：
  ```
  中文：赛博故障艺术风封面，深黑背景，RGB通道分离错位、扫描线与数字噪点，
  霓虹品红与电青色块碎裂，中央主体为像素化消散的全息人脸/城市剪影，
  中央白色粗黑中文标题"{TITLE}"带轻微故障错位，笔画完整可辨认，
  前卫，数字 decay 美学，横构图16:9，尺寸1200×675，除标题外无其他文字。

  EN: Cyberpunk glitch art cover, dark black background with RGB channel-split
  distortion, scanlines and digital noise, neon magenta and cyan shards. A
  fragmented holographic face / city silhouette dissolving into pixels at
  center. Bold white Chinese title "{TITLE}" with slight glitch offset at the
  center, strokes complete and legible. Edgy, digital decay aesthetic,
  landscape 16:9, 1200x675, no other text.
  ```
- **避坑**：
  - 故障特效开度要收：标题笔画一旦被" glitch" 吃掉变成乱码，整张图作废；
    明确要求"笔画完整可辨认"。
  - 噪点/扫描线过密会在公众号小图上糊成一团——要求"适度噪点"。
  - 该风格视觉刺激强，连续多篇使用会疲劳：系列中最多穿插 1~2 次。

---

## 通用组装公式（沿用）

```
{风格模板一句话}，主体：{主体描述}，
画面中央大标题"{≤10字标题}"，{暗底亮字/亮底深字}，
横构图16:9，主体占画面40%以上，四周留白8%，
极简，不堆砌元素，电影感光影
```

标题字逐字写进 prompt；生成后第一件事就是检查标题字。
示例图在 `assets/examples/`（`<style>.png` 1200×675 主图 + `<style>-wechat.png`
900×383 公众号裁剪版），选风格前先看图。
