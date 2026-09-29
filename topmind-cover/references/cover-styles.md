# 封面风格库（8 种）

选风格先看题材，再看系列延续性。同一系列固定一个模板，只换主体与标题字。
选风格三步走：**先选风格 → 看 `assets/examples/` 对应示例图 → 按本库配方组 prompt**。

每种风格的 prompt 配方都是中英双语模板：`{TITLE}` 为标题文字占位符（短标题 4~8 字）、
其余占位符见各风格说明。尺寸固定 1200×675、横构图 16:9。标题字逐字写进 prompt；
生成后第一件事就是检查标题字。

## 安全区铁律（所有风格通用）

900×383 公众号版是从 1200×675 主图**中央裁剪**（上下各裁约 12.2%）：
**标题字与关键主体必须落在画面中央垂直 60% 安全区内**
（上下各预留 20% 不放标题字），否则公众号版会被裁掉。
选风格、组 prompt、检查成图时都要先过这一条。

## 原创铁律（所有风格通用）

本库的 prompt 配方沉淀的是**抽象设计原则**——标题是视觉重心、信息分层、
留白与呼吸感、数字与关键词的强调手法——**不是任何具体版式**。
**版式与配色也不得与第三方封面构成实质相似：只学原则，不学版式。**
禁止照抄任何第三方封面的文案、形象、版式结构与配色组合——包括但不限于
标题文字、数字、品牌词、IP 形象、署名，以及"左文右图""底部标签条""两行撞色标题"
这类可辨识的构图公式。`assets/examples/` 中的 16 张示例图均为原创设计，
其标题/数字/品牌/署名（如"深蓝 OS 2.0""提示词避坑指南""AI绘画挑战营""@阿狐画画"）
均为虚构演示内容，仅用于演示设计原则。
用本库组 prompt 时，标题、形象、版式细节必须自己原创；
改图时只换主体与标题字，保留本风格的配色故事与设计原则。

---

## 1. gan-huo · 爆款干货

- **适用场景**：干货清单、评测、盘点、实测筛选类文章；"我替你试完了/筛完了"这类
  第一人称实测文的默认选择。示例图：`assets/examples/gan-huo.png`（原创："提示词避坑指南"）。
- **设计语言（抽象原则）**：
  - 标题是绝对视觉重心：居中大字，一眼即主题。
  - 信息分层三层：顶部眉题小字（给上下文）→ 中央大标题（给主题）→ 角落印章小数字（给数据点）。
  - 数字强调手法：数字不做彩色大字，收进印章/徽章做"小而精"的点睛。
  - 留白与呼吸感：深色底 + 大面积空旷，克制干练。
- **配色故事**：深炭灰 `#2B2B30` 做主色（沉稳、可信）；暖橙 `#FF8A3D` 只做细线点缀；
  朱红印章做一处跳色；标题米白高对比。
- **标题写法规范**：
  - 短标题 4~8 字，如"提示词避坑指南"；标题居中，字号约为画面高度 30%。
  - 顶部眉题小字交代筛选口径（如"12种写法 · 逐条实测"），字号约为标题的 30%。
  - 数据（如"18篇"）放右上角朱红印章内，白字，不放大。
- **prompt 配方**：
  ```
  中文：爆款干货风中文封面，深炭灰色（#2B2B30）背景，暖橙色（#FF8A3D）细线点缀。
  中央米白色超大粗黑中文标题"{TITLE}"（逐字准确），居中构图；标题上方顶部眉题小字"{EYEBROW}"；
  右上角一枚朱红色方形印章，内写白色小字"{NUMBER}"；左侧一只小尺寸原创小形象
  （{CHARACTER}，占画面约15%，小巧不抢戏）。除标题、眉题、印章、形象外无其他文字；
  所有文字与关键元素落在中央垂直60%安全区内，克制干练，横构图16:9，尺寸1200×675。

  EN: Chinese viral-listicle style cover, deep charcoal-gray (#2B2B30)
  background with thin warm-orange (#FF8A3D) line accents. Huge off-white bold
  Chinese title "{TITLE}" (exact) centered, ~30% of frame height; small top
  eyebrow text "{EYEBROW}" above the title; a small vermilion square seal at
  top-right with white text "{NUMBER}"; a small original mascot ({CHARACTER},
  ~15% of frame) on the left, tiny and unobtrusive. No other text. All text
  and key elements within the central vertical 60% safe zone, restrained and
  crisp, landscape 16:9, 1200x675.
  ```
  占位符：`{EYEBROW}` 眉题（≤10 字）、`{NUMBER}` 印章内数字（如"18篇"，必须真实）、
  `{CHARACTER}` 原创小形象描述（如"纸飞机造型蓝色小机器人"），不得照抄任何现有 IP 形象。
- **避坑**：
  - 数字放大上色是旧套路：本风格数字只进印章，标题里不再出现彩色大数字。
  - 形象是配角：超过画面 20% 或挡住标题字，整张作废。
  - 元素总数 ≤4（眉题+标题+印章+形象），多一件都是负担。

## 2. big-type · 巨字宣言

- **适用场景**：观点评论、深度长文、产品/版本发布宣言；"一句话立场"类文章的默认选择。
  示例图：`assets/examples/big-type.png`（原创："慢即是快"）。
- **设计语言（抽象原则）**：
  - 标题即画面：单行超大，字形本身做文章（书法笔意 / 描边 / 烫金质感均可）。
  - 副标题是注解：陈述句，解释标题，不提问、不煽动。
  - 明亮底色反衬：用"亮"制造宣言的从容感，而非暗黑压迫感。
- **配色故事**：奶油底 `#FAF3E7`（温暖、纸感）；墨黑标题字；烫金 `#C9A227`
  只做笔画点缀，一处即够。
- **标题写法规范**：
  - 短标题 4~8 字，单行，横跨画面宽度约 80%，如"慢即是快"。
  - 副标题用陈述句（如"慢公司的效率哲学"），字号约为标题的 25%。
- **prompt 配方**：
  ```
  中文：巨字宣言风中文封面，明亮奶油色（#FAF3E7）背景，细腻纸纹。
  画面中央单行超大中文标题"{TITLE}"（逐字准确），横跨画面约80%，
  {TYPE_STYLE}（如墨黑书法体配烫金#FFD23F描边/空心描边字/竖排大字三选一），
  极具冲击力；标题下方深灰色陈述句副标题"{SUBTITLE}"；背景极淡的金色几何线条点缀，
  不抢字。除标题与副标题外无其他文字；所有文字在中央垂直60%安全区内，
  横构图16:9，尺寸1200×675。

  EN: Giant-type manifesto Chinese cover, bright cream (#FAF3E7) background
  with subtle paper grain. Single-line oversized Chinese title "{TITLE}"
  (exact) at center, spanning ~80% of frame width, {TYPE_STYLE} (ink-black
  calligraphy with gold #C9A227 accents / outlined type / vertical type),
  maximum impact; small dark-gray declarative subtitle "{SUBTITLE}" below;
  very faint gold geometric line accents in background, unobtrusive. No other
  text. All text within central vertical 60% safe zone, landscape 16:9,
  1200x675.
  ```
  占位符：`{TYPE_STYLE}` 字形处理三选一（书法烫金 / 描边空心 / 竖排），
  `{SUBTITLE}` 陈述句副标题（≤10 字，禁止问句）。
- **避坑**：
  - 标题超过 8 个字必翻车——先压缩再生成。
  - 两行撞色标题是别人的版式：本风格只做单行（或竖排），不用两行撞色。
  - 副标题一旦写成问句，整张的气质就垮了。

## 3. brand-launch · 品牌发布

- **适用场景**：产品发布、版本更新、官方最佳实践/白皮书；有明确品牌主体的内容首选。
  示例图：`assets/examples/brand-launch.png`（原创虚构品牌"深蓝 OS 2.0"）。
- **设计语言（抽象原则）**：
  - 标题视觉重心居中置顶：品牌名就是标题，不藏不绕。
  - 氛围代替写实：用发光线条/光影做产品氛围，不画写实产品大图（防 AI 乱码也防呆板）。
  - 卖点信息分层：一排分隔符小字（"更快 · 更稳 · 更懂你"），轻量不做图标条。
- **配色故事**：深海军蓝 `#0A1F44` 做全幅主色（深邃、专业）；荧光绿 `#3DFF88`
  做唯一强调色（发光描边、细线、分隔符小字都用它）。
- **标题写法规范**：
  - 品牌词前置并上色："深蓝"用荧光绿发光描边，其余白字；短标题 4~8 字。
  - 标题下一条荧光绿细线收束视觉。
  - 底部一排分隔符小字卖点，格式 `更快 · 更稳 · 更懂你`，浅灰白小字。
- **prompt 配方**：
  ```
  中文：品牌发布风中文封面，深海军蓝（#0A1F44）全幅背景，荧光绿（#3DFF88）发光点缀。
  顶部居中大号白色粗黑中文标题"{TITLE}"（逐字准确），其中品牌词"{KEYWORDS}"用荧光绿
  描边发光、其余白色；标题下方一条荧光绿细线；画面中央下方一组荧光绿发光线条勾勒的
  抽象产品氛围（{PRODUCT}，线框/光影，无可读文字）；底部中央一排小字卖点
  "{SELLING_POINTS}"（分隔符式，如"更快 · 更稳 · 更懂你"）；左上预留空白 logo 区。
  除标题、卖点小字外无其他文字；所有文字在中央垂直60%安全区内，
  横构图16:9，尺寸1200×675。

  EN: Brand-launch style Chinese cover, full-bleed deep navy (#0A1F44)
  background with fluorescent-green (#3DFF88) glowing accents. Large white bold
  Chinese title "{TITLE}" (exact) centered at top, brand term "{KEYWORDS}" in
  glowing fluorescent-green outline, rest white; a thin fluorescent-green rule
  below the title; lower center an abstract product atmosphere drawn in glowing
  fluorescent-green lines ({PRODUCT}, wireframe/light, no readable text);
  bottom center one row of small separator-style selling points
  "{SELLING_POINTS}" (e.g. "更快 · 更稳 · 更懂你"); empty logo area reserved
  at top-left. No other text. All text within central vertical 60% safe zone,
  landscape 16:9, 1200x675.
  ```
  占位符：`{KEYWORDS}` 品牌词、`{PRODUCT}` 产品氛围描述、`{SELLING_POINTS}` 分隔符小字（≤12 字）；
  真实 logo 必须后期贴图，绝不用 AI 生成 logo。
- **避坑**：
  - 产品界面里的 UI 文字让 AI 生成必出乱码：只要氛围线框，不要可读文字。
  - 图标式卖点条是旧版式：本风格只用一排分隔符小字。
  - 强调色只用荧光绿一种，第二种颜色出现即杂。

## 4. tutorial-steps · 教程步骤

- **适用场景**：教程、上手指南、分步实操、保姆级攻略。
  示例图：`assets/examples/tutorial-steps.png`（原创："从想法到产品"）。
- **设计语言（抽象原则）**：
  - 标题做视觉锚：墨色书法题字，一字千钧，镇住画面。
  - 步骤沿横向时间线展开：一条线串起线框数字，数字是节奏点不是徽章。
  - 东方留白：大面积宣纸空，步骤区只占底部一条。
- **配色故事**：宣纸米 `#F2EDE0` 做底（温润）；墨黑书法标题；赭石 `#B5651D`
  只做时间线与线框数字。
- **标题写法规范**：
  - 大标题 4~8 字，墨色书法体，如"从想法到产品"，占画面高度约 25%。
  - 时间线：赭色水平细线 + 三个线框空心数字 `01 02 03`，每数字下一句极简短句（≤4 字）。
  - 右上角小字点睛（如"先懂逻辑，再动手"）。
- **prompt 配方**：
  ```
  中文：教程步骤风中文封面，宣纸米色（#F2EDE0）背景，淡墨纹理。
  顶部中央墨色毛笔书法体大字标题"{TITLE}"（逐字准确），占画面高度约25%；
  底部一条横向时间线：一根赭色（#B5651D）水平细线横贯画面下部，
  线上三个线框空心数字"{N1}""{N2}""{N3}"，每数字下方配极简短句"{S1}""{S2}""{S3}"；
  右上角小字点睛"{TIP}"。除上述文字外无其他文字；所有文字在中央垂直60%安全区内，
  文人气、克制，横构图16:9，尺寸1200×675。

  EN: Tutorial-steps style Chinese cover, rice-paper beige (#F2EDE0)
  background with faint ink texture. Top center: large ink-brush calligraphy
  title "{TITLE}" (exact), ~25% of frame height. Bottom: a horizontal timeline
  — one thin ochre (#B5651D) horizontal line across the lower frame, with three
  wireframe hollow numbers "{N1}" "{N2}" "{N3}" on it, each with a minimal short
  phrase below ("{S1}" "{S2}" "{S3}"); small accent text "{TIP}" at top-right.
  No other text. All text within central vertical 60% safe zone, scholarly and
  restrained, landscape 16:9, 1200x675.
  ```
  占位符：`{N1..N3}` 线框数字（01/02/03）、`{S1..S3}` 短句（每句 ≤4 字，越短越安全）、
  `{TIP}` 右上点睛（≤8 字）。
- **避坑**：
  - 步骤超过 3 个立刻变说明书。
  - 圆形实心序号章是旧版式：本风格只用线框空心数字。
  - 红色笔刷横条不用：本风格的强调色只有赭石。

## 5. ip-fun · IP 趣味

- **适用场景**：实战案例、数据战报、复盘、系列连载（上/下篇）。
  示例图：`assets/examples/ip-fun.png`（原创：狐狸画家 IP + "AI绘画挑战营"）。
- **设计语言（抽象原则）**：
  - 暖色氛围做主角情绪：整张的"热气"是第一眼记忆。
  - 标题深色压住暖底：深棕/深色字在暖色底上形成对比重心。
  - 数字收进角落印章：数据是注脚，不是标题。
  - 署名做边角点缀：竖排小字，不进主视觉流。
- **配色故事**：橙黄暖色 `#FF9E2C → #FFC53D` 做主色（阳光、热闹）；
  标题与副标题用深棕 `#4A2C0A`（在暖底上最稳的重色）。
- **标题写法规范**：
  - 大标题 4~8 字深棕粗黑，如"AI绘画挑战营"；下方深棕小字副标题（如"每天一幅 · 进化看得见"）。
  - 数据（如"30天"）放右下角圆形印章内小字，不放大。
  - 署名（如"@阿狐画画"）放左下角竖排小字。
- **prompt 配方**：
  ```
  中文：IP 趣味风中文封面，暖橙黄色（#FF9E2C 渐变至 #FFC53D）主色背景，阳光感。
  中央偏左深棕色（#4A2C0A）大号粗黑中文标题"{TITLE}"（逐字准确），
  下方深棕色小字副标题"{SUBTITLE}"；右侧原创趣味 IP 形象（{CHARACTER}，
  如戴贝雷帽的狐狸画家在画架前作画，暖色调），生动，约占画面35%，不遮挡文字；
  右下角一枚圆形印章，内写"{NUMBER}"小字；左下角竖排小字署名"{BYLINE}"。
  除上述文字外无其他文字；所有文字在中央垂直60%安全区内，
  横构图16:9，尺寸1200×675。

  EN: Fun-IP style Chinese cover, warm orange-yellow (#FF9E2C to #FFC53D)
  dominant background, sunny feel. Center-left large dark-brown (#4A2C0A) bold
  Chinese title "{TITLE}" (exact), small dark-brown subtitle "{SUBTITLE}"
  below; right side an original playful IP character ({CHARACTER}, e.g. a
  beret-wearing fox painter at an easel, warm tones), vivid, ~35% of frame,
  never covering text; bottom-right a small round seal with "{NUMBER}"; 
...[truncated 3507 chars]