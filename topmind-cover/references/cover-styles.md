# 封面风格库（8 种）

选风格先看题材，再看系列延续性。同一系列固定一个模板，只换主体与标题字。
选风格三步走：**先选风格 → 看 `assets/examples/` 对应示例图 → 按本库配方组 prompt**。

每种风格的 prompt 配方都是中英双语模板：`{TITLE}` 为标题文字占位符（短标题 4~8 字）、
`{KEYWORDS}` 为需要彩色突出的数字/关键词占位符，其余占位符见各风格说明。
尺寸固定 1200×675、横构图 16:9。标题字逐字写进 prompt；生成后第一件事就是检查标题字。

## 安全区铁律（所有风格通用）

900×383 公众号版是从 1200×675 主图**中央裁剪**（上下各裁约 12.2%）：
**标题字与关键主体必须落在画面中央垂直 60% 安全区内**
（上下各预留 13%+ 不放标题字），否则公众号版会被裁掉。
选风格、组 prompt、检查成图时都要先过这一条；以下各风格的标题位置描述
均已按此约束书写。

---

## 1. gan-huo · 爆款干货

- **适用场景**：干货清单、评测、盘点、实测筛选类文章；"我替你试完了/筛完了"这类
  第一人称实测文的默认选择。参考样张：Muse 爆款干货、Manus 2.0 封面。
- **构图公式**：左右分区。左侧 60% 为文案堆叠区（自上而下：短引子行 → 巨型标题 →
  底部胶囊标签条）；右侧 40% 为萌物/IP 形象（抱着主题物品，如帖子、产品），
  形象顶部不超过标题区、不遮挡任何文字。标题字占画面高度 25%~32%。
- **配色方案**：暖白底 `#FFF9F0`（或米白 `#FAF6EF`）；主标题炭黑 `#1A1A1A`；
  数字/品牌词用亮蓝 `#2B7FFF`；篇数类数字可用橙红 `#FF4D2E`；
  关键词下垫黄色笔刷底 `#FFD23F`；底部标签条为蓝色胶囊 `#2B7FFF` 配白字。
- **标题写法规范**：
  - 短标题 4~8 字，如"爆款干货""实测报告"；上方加 1~2 行引子小字
    （"刷了3天时间线/我从上百个帖子里"），引子字号约为标题的 55%。
  - 数字必须放大并上色："26篇"中的 26 用橙红，"3天"中的 3 用蓝色；
    品牌词（如 Muse、Manus）用蓝色。
  - 底部标签条：蓝色圆角胶囊，内放 3 个标签，格式 `⚡四字词 | 📋四字词 | 📊四字词`
    （如"实测筛选 | 长文精选 | 全流程实操"），字号约为标题的 30%。
- **prompt 配方**：
  ```
  中文：爆款干货风中文封面，暖白色干净背景，左侧文案区：上方小字引子行，
  中央巨型炭黑色粗黑标题"{TITLE}"，其中数字与关键词"{KEYWORDS}"用亮蓝色与橙红色突出，
  关键词下方垫黄色笔刷底色；底部一条蓝色圆角胶囊标签条；右侧一只毛茸茸的可爱
  IP 萌物抱着与主题相关的物品，萌物占画面右侧三分之一、不遮挡文字，
  画面中央垂直安全区内，星星小点缀，亲切活泼，横构图16:9，尺寸1200×675。

  EN: Chinese viral-listicle style cover, clean warm-white background. Left
  text zone: small intro lines on top, giant bold charcoal-black Chinese
  title "{TITLE}" at center, with numbers and keywords "{KEYWORDS}" highlighted
  in bright blue and orange-red, a yellow brush stroke behind keywords; a blue
  rounded capsule tag bar at the bottom. On the right third, a fluffy cute IP
  mascot holding a theme-related item, never overlapping the text. All key
  elements within the central vertical safe zone, tiny star accents, friendly
  and lively, landscape 16:9, 1200x675.
  ```
  占位符：`{CHARACTER}` 可替换萌物描述（如"蓝色毛绒小怪物""戴墨镜的猫导演"），
  必须与文章主题相关。
- **避坑**：
  - 萌物是配角：占画面不超过 40%，一旦挡住标题字整张作废。
  - 彩色字不要超过 2 种颜色，三色以上立刻变杂。
  - 胶囊标签条必须整体落在中央安全区内，上下留白防裁切。
  - 元素总数 ≤5（引子+标题+标签条+萌物+小点缀），多一件都是负担。

## 2. big-type · 巨字宣言

- **适用场景**：观点评论、深度长文、产品/版本发布宣言；"一句话立场"类文章的默认选择。
  参考样张：Skill 指南封面。
- **构图公式**：标题即画面。巨型标题字占画面高度 35%~45%，横跨画面三分之二以上，
  分两行：上行品牌词/关键词（白色或黑色），下行宣言（品牌色/红色，可做 3D 立体字）；
  背景为场景化配图（巨型书、建筑、空间纵深），人物极小仅作比例参照；
  底部一条白色横条放问题式副标题，横条压在画面底部安全区内。
- **配色方案**：深底版：近黑 `#101014` 底 + 纯白 `#FFFFFF` 字 + 强调红 `#E63B2E`
  （或品牌色）；浅底版：白底 + 黑字 + 红字。同一系列固定一种底色。
- **标题写法规范**：
  - 短标题 4~8 字，分两行断句，如"Skill指南：/从入门到精通"；下行宣言用彩色。
  - 底部白横条用问句引出内容："如何从0开始构建一个属于自己的Skill?"，
    字号约为标题的 35%，左对齐。
  - 右侧可加竖排小字装饰（如一句 slogan），字号小、不抢戏。
- **prompt 配方**：
  ```
  中文：震撼巨字宣言风中文封面，深色场景化背景（{SCENE}，如巨型书本/建筑纵深，
  一位小小人物作比例参照），画面中央巨型中文标题"{TITLE}"占画面近一半，
  上行白色下行红色粗黑体，可做轻微3D立体质感，极具冲击力；底部一条白色横条，
  内写黑色问句副标题；标题与横条均在中央垂直安全区内，高对比，
  横构图16:9，尺寸1200×675。

  EN: Bold giant-type manifesto Chinese cover, dark scenic background
  ({SCENE}, e.g. gigantic books / architectural depth, a tiny human figure for
  scale). Enormous bold Chinese title "{TITLE}" dominates the center, nearly
  half the frame, white on the first line and red on the second, subtle 3D
  extruded type feel, maximum impact; a white horizontal bar at the bottom
  with a black question-style subtitle. Title and bar inside the central
  vertical safe zone, high contrast, landscape 16:9, 1200x675.
  ```
  占位符：`{SCENE}` 为场景化配图描述，必须与主题强相关（如 Skill 主题用"巨型操作手册"）。
- **避坑**：
  - 标题超过 10 个字必翻车——先压缩成 4~8 字再生成。
  - 3D 立体字与背景对比度不够会"糊"：深底配白字、浅底配黑字，边缘加细描边。
  - 背景人物只是比例参照，放大抢戏就喧宾夺主。
  - 字不能顶到画面边缘：四周至少留 5% 空气，否则公众号裁剪会切字。

## 3. brand-launch · 品牌发布

- **适用场景**：产品发布、版本更新、官方最佳实践/白皮书；有明确品牌主体的内容首选。
  参考样张：typesafe AI Jev 封面、Manus 2.0 封面（品牌区部分）。
- **构图公式**：左文右图。左上品牌 logo 区（AI 不画 logo，prompt 里留空位、后期贴真实 logo）；
  左侧大标题（品牌词用品牌色渐变 + 其余黑字），标题下手写感副标题 + 品牌色下划线；
  右侧 50% 为产品/界面展示（深色控制台、App 界面、产品渲染图）；
  底部 3~4 个卖点图标条：图标 + 中文 + 英文小字。标题字占画面高度 20%~28%。
- **配色方案**：以品牌主色为准（示例：品红 `#E8408C` 渐变至 `#B02860`）；
  浅底 `#FDF6F9`（或品牌浅色 tint）；文字炭黑 `#1A1A1A`；
  图标底色用品牌色 10% 浅底。
- **标题写法规范**：
  - 品牌词前置并上色："Jev"用品牌色渐变，"最佳实践"用黑字；短标题 4~8 字。
  - 副标题口语化、手写感，如"手把手教你改进现有工作流"，下方加品牌色笔刷下划线。
  - 卖点条格式：`图标 / 中文四字 / 英文小字`（如"更高效率 / Make it faster"），
    3~4 个，中文在上英文在下，英文仅装饰。
- **prompt 配方**：
  ```
  中文：品牌发布风中文封面，品牌浅色背景（{BRAND_TINT}），左上预留空白 logo 区，
  左侧大标题"{TITLE}"，其中品牌词"{KEYWORDS}"用品牌主色（{BRAND_COLOR}）渐变突出、
  其余字炭黑色粗黑体；标题下方手写感副标题配品牌色下划线；
  右侧一半为产品展示（{PRODUCT}，深色界面、发光细节）；底部 3~4 个卖点图标条
  （图标+中文+英文小字）；干净高级，横构图16:9，尺寸1200×675。

  EN: Brand-launch style Chinese cover, light brand-tinted background
  ({BRAND_TINT}), empty logo area reserved at top-left. Large title "{TITLE}"
  on the left, brand term "{KEYWORDS}" in gradient brand color
  ({BRAND_COLOR}), remaining characters in bold charcoal black; handwritten-feel
  subtitle below with a brand-color underline. Right half shows the product
  ({PRODUCT}, dark UI with glowing details). Bottom row of 3-4 selling-point
  icon chips (icon + Chinese + small English). Clean and premium, landscape
  16:9, 1200x675.
  ```
  占位符：`{BRAND_COLOR}`/`{BRAND_TINT}` 为品牌色 hex，`{PRODUCT}` 为产品展示描述；
  真实 logo 必须后期贴图，绝不用 AI 生成 logo。
- **避坑**：
  - 产品界面里的 UI 文字让 AI 生成必出乱码：要求"界面文字模糊/占位块"，
    或只展示界面氛围不展示可读文字。
  - 卖点条超过 4 个立刻变说明书；英文小字必须人工核对拼写。
  - 品牌色渐变只用在品牌词上，全标题上色等于没重点。

## 4. tutorial-steps · 教程步骤

- **适用场景**：教程、上手指南、分步实操、保姆级攻略。参考样张：Reddit 上手教程封面。
- **构图公式**：左文右卡。左侧：顶部彩色笔刷横条（写起点，如"从0到1"）→
  大黑标题（4~8 字）→ 底部彩色笔刷横条（内容总结，如"搞懂规则×发帖实操"）；
  右侧：2~3 张步骤卡片纵向拼贴（撕纸/便签质感），每张含彩色圆章序号（01/02）+
  小图标 + 短句，卡片间用箭头连接；右上小字点睛（如"先懂规则，再动手"）。
  标题字占画面高度 22%~30%。
- **配色方案**：纸白底 `#F7F4EC`；笔刷/序号章用强调红 `#E8401F`
  （或品牌色）；标题字炭黑 `#1A1A1A`；卡片描边浅灰。
- **标题写法规范**：
  - 顶部笔刷条：白字写起点/承诺，"从0到1""7天上手"，4 字以内最有力。
  - 大标题 4~8 字，如"Reddit上手/保姆级教程"，分两行断句。
  - 底部笔刷条：白字总结全文骨架，"搞懂规则×发帖实操"，用 × 连接两个关键词。
  - 步骤卡片内文字极简：序号 + 8 字以内短句（如"看懂平台与社区规则"）。
- **prompt 配方**：
  ```
  中文：教程步骤风中文封面，纸白色温暖背景，左侧：顶部红色笔刷横条白字写"{HOOK}"，
  中央大号炭黑色粗黑标题"{TITLE}"，底部红色笔刷横条白字写"{SUMMARY}"；
  右侧两张撕纸质感便签卡片纵向排列，卡片上有红色圆形序号章（01/02）、
  简笔画小图标与极简短句，卡片间黑色箭头连接；右上角小字点睛；
  红黑白三色，对比鲜明，横构图16:9，尺寸1200×675。

  EN: Tutorial-steps style Chinese cover, warm paper-white background. Left
  side: red brush-stroke banner with white text "{HOOK}" on top, large bold
  charcoal-black Chinese title "{TITLE}" at center, red brush banner with white
  text "{SUMMARY}" at the bottom. Right side: two torn-paper memo cards
  stacked vertically, each with a red circular number badge (01/02), a small
  line icon and minimal short text, connected by a black arrow; small accent
  text at top-right. Red-black-white palette, crisp contrast, landscape 16:9,
  1200x675.
  ```
  占位符：`{HOOK}` 顶部钩子（≤4 字）、`{SUMMARY}` 底部总结（≤10 字）、
  卡片短句直接写进 prompt 且每张 ≤8 字（模型小字易错，越短越安全）。
- **避坑**：
  - 步骤卡片最多 3 张，第 4 张起画面必乱。
  - 卡片内一个字都不能多：小字是 AI 错别字重灾区，生成后逐字核对。
  - 箭头方向必须明确向下/向右，别让模型自由发挥画成回路。
  - 笔刷横条别压住标题字，上下留 breathing room。

## 5. ip-fun · IP 趣味

- **适用场景**：实战案例、数据战报、复盘、系列连载（上/下篇）。参考样张：AI 视频制作实战封面。
- **构图公式**：左文右图。左侧：巨型彩色数字行（数字占画面高度 20%+，如"600万播放"，
  数字彩色、单位黑字）→ 大黑标题（4~8 字）→ 灰色副标题 + 署名（左下小字）；
  右侧 50% 为趣味 IP 形象：拟人动物/角色 + 主题道具（如猫导演 + 放映机 + 胶片），
  形象生动、与主题强绑定。
- **配色方案**：纯白底 `#FFFFFF`；数字用亮蓝 `#2B7FFF`（或品牌色）；
  标题炭黑 `#1A1A1A`；副标题/署名用中灰 `#9AA0A6`。
- **标题写法规范**：
  - 数字前置造冲击："600万播放"中数字放大 1.5 倍并上色，单位用黑字；
    数字必须真实，严禁编造数据。
  - 大标题 4~8 字黑粗体，如"AI视频制作实战"。
  - 副标题灰字说明结构："从想法到成片 · 下篇"；署名 "@Xanderwow" 放左下角小字。
- **prompt 配方**：
  ```
  中文：IP 趣味风中文封面，纯白干净背景，左侧：巨型亮蓝色数字"{NUMBER}"
  配炭黑色单位字，下方大号炭黑色粗黑标题"{TITLE}"，再下方灰色小字副标题与署名；
  右侧一半为趣味 IP 形象（{CHARACTER}，如戴墨镜的猫导演操作复古放映机、
  胶片环绕），形象生动、细节丰富但不遮挡文字；所有文字在中央垂直安全区内，
  横构图16:9，尺寸1200×675。

  EN: Fun-IP style Chinese cover, clean pure-white background. Left side: huge
  bright-blue number "{NUMBER}" with charcoal-black unit characters, large
  bold charcoal-black Chinese title "{TITLE}" below, small gray subtitle and
  byline underneath. Right half features a playful IP character ({CHARACTER},
  e.g. a sunglasses-wearing cat director operating a vintage film projector
  with film reels swirling around), vivid and detailed but never covering the
  text. All text within the central vertical safe zone, landscape 16:9,
  1200x675.
  ```
  占位符：`{NUMBER}` 为真实数据（"600万"）、`{CHARACTER}` 为 IP 形象描述，
  必须与主题道具绑定（如视频主题 → 导演猫 + 放映机）。
- **避坑**：
  - 数字造假是红线：封面上的每个数字必须在正文中有出处。
  - IP 形象再可爱也不能抢字：右侧边界止于画面 55% 处。
  - 白底最怕"脏"：要求"纯白干净背景"，防模型加渐变/纹理。
  - 连载标注（上篇/下篇）放副标题里，别进大标题。

## 6. news-flash · 资讯快报

- **适用场景**：资讯、快讯、热点解读、人物专访预告、"祛魅/揭秘"类选题。
  参考样张：算法工程师祛魅封面。
- **构图公式**：左文右图。左侧：两行大字标题（上行黑字 4 字、下行品牌色 4~5 字 +
  感叹号）→ 下方彩色胶囊副标题（问句/悬念）；右侧 35%~50% 为人物或主题元素点缀
  （二次元人物、产品小物、场景物件），点缀丰富但不进文字区。
  标题字占画面高度 22%~30%。
- **配色方案**：白底 `#FFFFFF`；标题黑 `#1A1A1A` + 品牌蓝 `#2B7FFF`
  （或品牌色）；胶囊副标题用品牌色底 + 白字。
- **标题写法规范**：
  - 标题两行、上黑下彩，如"带你祛魅/算法工程师！"，每行 4~6 字；
    感叹号是点睛，一个就够。
  - 胶囊副标题用问句制造悬念："薪资？日常？统统告诉你"，问号 + 陈述收尾；
    问句必须在正文中有答案，不做无答案的标题党。
  - 右侧点缀可加小标签云（如书脊上的"Machine Learning/PyTorch"），丰富主题氛围。
- **prompt 配方**：
  ```
  中文：资讯快报风中文封面，纯白背景，左侧两行大字标题，上行炭黑色"{TITLE_TOP}"、
  下行品牌蓝色"{TITLE_BOTTOM}"加感叹号，粗黑体；标题下方蓝色圆角胶囊副标题，
  白字问句"{SUBTITLE}"；右侧人物/主题元素点缀（{CHARACTER}，如专注的二次元
  少年、笔记本电脑、代码屏幕、书堆小物），生动但不遮挡文字；
  所有文字在中央垂直安全区内，横构图16:9，尺寸1200×675。

  EN: News-flash style Chinese cover, white background. Left side: two-line
  bold headline, charcoal-black "{TITLE_TOP}" on top and brand-blue
  "{TITLE_BOTTOM}" with exclamation mark below; a blue rounded capsule
  subtitle with a white question-style "{SUBTITLE}" underneath. Right side
  decorative figure / theme elements ({CHARACTER}, e.g. a focused anime-style
  youth, laptop, code screen, book stack props), lively but never covering the
  text. All text within the central vertical safe zone, landscape 16:9,
  1200x675.
  ```
  占位符：`{TITLE_TOP}` 上行（黑字）、`{TITLE_BOTTOM}` 下行（彩色）、
  `{SUBTITLE}` 胶囊问句、`{CHARACTER}` 右侧点缀描述。
- **避坑**：
  - 感叹号/问号各一个，多了变地摊文学。
  - 右侧点缀元素别超过 4 件，多了就抢标题的风头。
  - 胶囊问句的字数 ≤12 字，太长胶囊装不下会被模型挤小。
  - 热点人物用"泛指"描述，不画可识别真人。

## 7. minimal · 极简留白

- **适用场景**：随笔、书评、轻观点、生活感悟；公众号"轻阅读"类文章，
  或系列中需要"呼吸感"的穿插封面。
- **构图公式**：大面积留白（≥60%）。一处微小点缀落在右侧中央安全区内
  （如水墨笔触、孤鸟剪影）；标题小字号放左下角安全区内，不与点缀打架。
  标题字占画面高度 8%~12%。
- **配色方案**：主色米白 `#F7F4EC`（或冷白 `#F2F4F6`），
  辅色淡墨 `#9AA0A6`（小面积点缀），文字色深灰 `#3A3A3A`。
- **标题写法规范**：短标题 4~8 字即可，字体用 Noto Sans SC Medium（不用 Black，
  太重则极简感全失）；不加副标题、不加标签条，克制到底。
- **prompt 配方**：
  ```
  中文：极致极简主义封面，暖米白背景，大面积留白，一处微小的水墨笔触
  （如孤鸟剪影）点缀在画面右侧中央（中央垂直安全区内），左下角（中央垂直安全区内）
  小字号深灰色中文标题"{TITLE}"，呼吸感强，禅意，无其他元素，
  横构图16:9，尺寸1200×675，除标题外无其他文字。

  EN: Extreme minimalism cover, warm off-white background with vast empty
  space, one tiny ink-brush stroke (like a lone bird silhouette) near the
  center-right. Small dark-gray Chinese title "{TITLE}" in delicate bold type
  at the lower-left corner. Calm, airy, zen aesthetic, no other elements,
  landscape 16:9, 1200x675, no other text.
  ```
- **避坑**：
  - 对"杂物"零容忍：prompt 明确"一处""微小""无其他元素"，防模型加云加山。
  - 标题字别贪大：字一大立刻变大字报。
  - 主体和标题尽量往中央安全区放，防公众号裁剪吃掉左右留白。

## 8. magazine · 杂志编辑风

- **适用场景**：深度访谈、人物特写、商业分析、年度盘点；需要"质感/信任感"时用它，
  公众号长文首选。
- **构图公式**：三分法。右侧三分之一为黑白质感人物肖像（泛指描述）；
  左侧大面积留白；标题放左侧下方安全区内，标题上方一条品牌色/砖红细线。
  标题字占画面高度 14%~20%。
- **配色方案**：主色暖灰 `#E8E4DC`（浅底）或墨黑 `#141414`（深底版），
  辅色砖红 `#B03A2E`（细线/点缀），文字色炭黑 `#2B2B2B`（浅底）/
  米白 `#F5F1E8`（深底）。
- **标题写法规范**：短标题 4~8 字，字体用 Noto Serif SC Bold（宋体感）或思源黑体 Bold；
  标题上方一条细色线是杂志感的灵魂，别省略；深底/浅底同一系列只用一种。
- **prompt 配方**：
  ```
  中文：杂志编辑风封面，暖灰色影棚背景，右侧三分之一处黑白质感人物肖像，
  左侧大面积留白，左侧下方（中央垂直安全区内）炭黑色典雅粗体中文标题"{TITLE}"，
  标题上方一条砖红色细线，克制高级，杂志封面美学，
  横构图16:9，尺寸1200×675，除标题外无其他文字。

  EN: Editorial magazine style cover, warm light-gray studio background,
  dramatic black-and-white portrait in the right third, generous negative
  space on the left. Dark charcoal elegant bold Chinese title "{TITLE}" at
  lower left, with a thin brick-red rule line above it. Refined, minimal,
  magazine cover aesthetic, landscape 16:9, 1200x675, no other text.
  ```
- **避坑**：
  - 人物肖像必须用"泛指"描述（商务人士/学者剪影），不得出现可识别的真实人物长相。
  - 留白处别手痒加装饰字——杂志风的力量全在克制。
  - 深底版和浅底版不要混用。

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

## 风格速查

| 风格 | 一句话 | 标题字号占比 | 首选题材 |
|---|---|---|---|
| gan-huo | 萌物 + 巨型标题 + 彩色数字 + 胶囊标签条 | 25%~32% | 干货清单/评测/盘点 |
| big-type | 标题即画面，字占近半，分两行撞色 | 35%~45% | 观点/深度/发布宣言 |
| brand-launch | 品牌色大标题 + 产品展示 + 卖点图标条 | 20%~28% | 产品发布/版本更新 |
| tutorial-steps | 笔刷横条标题 + 步骤卡片拼贴 + 序号章 | 22%~30% | 教程/上手指南 |
| ip-fun | 巨型彩色数字 + 趣味 IP + 署名 | 数字 20%+ | 实战案例/数据战报 |
| news-flash | 两行大字 + 胶囊问句 + 人物点缀 | 22%~30% | 资讯/解读/快讯 |
| minimal | 大面积留白，一处点缀，小字标题 | 8%~12% | 随笔/书评/轻阅读 |
| magazine | 三分法 + 人物肖像 + 细线标题 | 14%~20% | 访谈/商业分析/盘点 |
