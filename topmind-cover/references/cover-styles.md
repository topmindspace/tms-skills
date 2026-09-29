# 封面风格库（8 种）

> **原创铁律**：本库示例图均为原创，只演示抽象设计原则（标题是视觉重心、信息分层、留白呼吸感、数字与关键词强调），不临摹任何第三方封面；复用时版式与配色不得与第三方封面构成实质相似——只学原则，不学版式。

选风格先看题材，再看系列延续性。同一系列固定一个模板，只换主体与标题字。
选风格三步走：**先选风格 → 看 `assets/examples/` 对应示例图 → 按本库配方组 prompt**。

prompt 配方为中英双语模板：`{TITLE}` 为标题文字占位符（短标题 4~8 字）、其余占位符见各风格说明。尺寸固定 1200×675、横构图 16:9。标题字逐字写进 prompt；生成后第一件事就是检查标题字。

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
- **标题文案提炼公式**：实测数字 + 翻车/打脸结果 + 省时间承诺。
  示例（虚构演示）："实测18篇：避开7个坑"。
- **prompt 配方**：
  ```
  中文：爆款干货风中文封面。字体量级：全图只有一个视觉重心——中央米白色超粗黑中文标题"{TITLE}"（逐字准确），标题字高占画面 1/3，与深底形成最大明度差；顶部小字眉题"{EYEBROW}"（筛选口径，如"18篇 · 逐条实测"）只做开场，字号约为标题的 1/3。配色系统：深炭灰 #2B2B30 全幅深底（沉稳可信，走极端明度）；暖橙 #FF8A3D 只做细线框点缀；朱红 #E6392B 方形印章（右上角，内写白色小字"{NUMBER}"）是全图唯一的跳色、唯一的记忆点。构图能量：一条纵向主阅读动线——眉题（为什么信）→ 大标题（这是什么）→ 印章（数据背书）；左下角一只小巧原创小形象（{CHARACTER}，占画面约15%）做动线落点，绝不遮挡标题。质感细节：深底必须加一层细腻胶片噪点颗粒 + 一道极淡的斜向光影，拒绝死平纯色的塑料感。除标题、眉题、印章、形象外无其他文字；所有文字与关键元素落在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: High-impact Chinese viral-listicle cover. Type scale: exactly one visual anchor — a centered off-white extra-bold Chinese title "{TITLE}" (exact), glyph height 1/3 of the frame, maximum brightness contrast against the dark ground; a small top eyebrow "{EYEBROW}" (selection criteria, e.g. "18 posts, tested one by one") opens the read at ~1/3 of the title size. Color system: full-bleed deep charcoal #2B2B30 ground (steady, credible, extreme-dark value); warm-orange #FF8A3D hairline frame accents only; one vermilion #E6392B square seal at top-right with white micro-text "{NUMBER}" — the single hot-color accent and the single memorable element on the page. Composition energy: one vertical reading path — eyebrow (why trust) → giant title (what it is) → seal (data proof); a tiny original mascot ({CHARACTER}, ~15% of frame) sits bottom-left as the path's landing point, never covering the title. Texture: the dark ground must carry one layer of fine film grain plus one faint diagonal light sweep — flat lifeless solid color is forbidden. No other text. All text and key elements within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{EYEBROW}` 眉题（≤10 字）、`{NUMBER}` 印章内数字（如"18篇"，必须真实）、
  `{CHARACTER}` 原创小形象描述（如"纸飞机造型蓝色小机器人"），不得照抄任何现有 IP 形象。
- **绝不清单**：
  - 绝不小字标题：标题字高不足画面 1/4，整张作废。
  - 绝不把数字做成彩色大字抢标题：数字只进印章，标题里不再出现第二个数字钩子。
  - 绝不浅底：本风格必须是深底，浅底直接变味。
  - 绝不底部标签条/胶囊条：卖点只进眉题小字。
  - 绝不死平纯色底：无噪点无光影的"塑料底"一律重画。

---

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
- **标题文案提炼公式**：反常识断言（4~6 字）+ 陈述句注解。
  示例（虚构演示）："少，才是多"。
- **prompt 配方**：
  ```
  中文：巨字宣言风中文封面。字体量级：标题即画面——单行超大墨黑中文标题"{TITLE}"（逐字准确），横跨画面约85%宽度，字高占画面 1/3~2/5；{TYPE_STYLE}（墨黑书法体配烫金 #C9A227 描边 / 空心描边字 / 竖排大字三选一），字形本身就是情绪；标题下方深灰色陈述句副标题"{SUBTITLE}"只做注解，字号约为标题的 1/4。配色系统：明亮奶油 #FAF3E7 全幅亮底（宣言的从容感，走极端明度）；墨黑标题字；烫金 #C9A227 只点缀一处笔画或一字，是全图唯一的强调。构图能量：一条横向主阅读动线——巨标题横扫全场（钩子与主题合一）→ 副标题收束落点；背景只留极淡的金色几何线条，全部给标题让路。质感细节：奶油底必须带细腻纸纹 + 书法笔锋的飞白质感，拒绝干净单调的平板底。除标题与副标题外无其他文字；所有文字在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Giant-type manifesto Chinese cover. Type scale: the title IS the image — one single-line oversized ink-black Chinese title "{TITLE}" (exact), spanning ~85% of frame width, glyph height 1/3 to 2/5 of the frame; {TYPE_STYLE} (ink-black calligraphy with gold #C9A227 edge accents / outlined hollow type / vertical type) — the letterforms carry the emotion; a small dark-gray declarative subtitle "{SUBTITLE}" below only annotates, at ~1/4 of the title size. Color system: full-bleed bright cream #FAF3E7 ground (extreme-light value, the calm of a manifesto); ink-black title; gold #C9A227 accents exactly one stroke or one character — the single emphasis on the page. Composition energy: one horizontal reading path — the giant title sweeps the frame (hook and theme in one) → the subtitle lands the read; the background keeps only whisper-faint gold geometric lines, everything yields to the title. Texture: the cream ground must carry fine paper grain plus dry-brush flying-white texture in the calligraphy strokes — a clean flat ground is forbidden. No other text. All text within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{TYPE_STYLE}` 字形处理三选一（书法烫金 / 描边空心 / 竖排），
  `{SUBTITLE}` 陈述句副标题（≤10 字，禁止问句）。
- **绝不清单**：
  - 绝不两行撞色标题：本风格只做单行（或竖排），两行撞色是别人的版式。
  - 绝不暗黑背景：本风格必须是亮底，暗底直接变味。
  - 绝不问句/煽动式副标题：副标题只能是陈述句注解。
  - 绝不标题字高不足 1/4：字一小，宣言感全失。
  - 绝不出现第二处烫金：强调色只给一处，多一处就"吵"。

---

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
- **标题文案提炼公式**：品牌词前置 + 版本号做钩子 + 卖点小字给承诺。
  示例（虚构演示）："曙光 5.0：快三倍"。
- **prompt 配方**：
  ```
  中文：品牌发布风中文封面。字体量级：品牌名就是标题——顶部居中大号白色粗黑中文标题"{TITLE}"（逐字准确），字高占画面 1/4~1/3，其中品牌词"{KEYWORDS}"用荧光绿描边发光、其余纯白，是全图唯一的视觉重心；标题下一条荧光绿细线收束视觉，紧跟一排浅灰白分隔符小字卖点"{SELLING_POINTS}"（如"更快 · 更稳 · 更懂你"）做背书。配色系统：深海军蓝 #0A1F44 全幅深底（深邃专业，走极端明度）；荧光绿 #3DFF88 是唯一的强调色（发光描边、细线、卖点小字都用它，别处不再出现第二种颜色）。构图能量：一条纵向主阅读动线——品牌大标题（定调）→ 细线+卖点小字（背书）→ 中央下方荧光绿发光线条勾勒的抽象产品氛围（{PRODUCT}，线框/光影、无可读文字）做氛围落点；左上预留空白 logo 区。质感细节：深蓝底必须加一层细腻星尘噪点 + 中央一团柔和的荧光绿光晕渐变，拒绝死黑平板底。除标题、卖点小字外无其他文字；所有文字在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Brand-launch Chinese cover. Type scale: the brand name IS the title — a large white extra-bold Chinese title "{TITLE}" (exact) centered at top, glyph height 1/4 to 1/3 of the frame; the brand term "{KEYWORDS}" glows in fluorescent-green outline, the rest pure white — the single visual anchor of the page; one thin fluorescent-green rule cinches the eye below the title, followed by one row of light-gray separator-style selling points "{SELLING_POINTS}" (e.g. "更快 · 更稳 · 更懂你") as proof. Color system: full-bleed deep navy #0A1F44 ground (deep, professional, extreme-dark value); fluorescent green #3DFF88 is the ONLY accent color (glowing outlines, hairlines, selling-point micro-text all use it — no second color anywhere). Composition energy: one vertical reading path — brand title (sets the tone) → rule plus selling points (proof) → an abstract product atmosphere drawn in glowing fluorescent-green lines ({PRODUCT}, wireframe and light, no readable text) lower-center as the atmospheric landing; empty logo area reserved top-left. Texture: the navy ground must carry fine stardust grain plus one soft fluorescent-green halo glow at center — a dead flat black ground is forbidden. No other text. All text within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{KEYWORDS}` 品牌词、`{PRODUCT}` 产品氛围描述、`{SELLING_POINTS}` 分隔符小字（≤12 字）；
  真实 logo 必须后期贴图，绝不用 AI 生成 logo。
- **绝不清单**：
  - 绝不渐变彩虹标题：强调色只用荧光绿一种，第二种颜色出现即杂。
  - 绝不写实产品大图/UI 截图：只要发光线框氛围，可读 UI 文字必出乱码。
  - 绝不图标式卖点条：卖点只用一排分隔符小字。
  - 绝不 AI 生成 logo：真实 logo 必须后期贴图。
  - 绝不死黑无光影的底：无星尘无光晕的平板深底一律重画。

---

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
- **标题文案提炼公式**："从A到B"动词句 + 步数做钩子。
  示例（虚构演示）："3步做出小程序"。
- **prompt 配方**：
  ```
  中文：教程步骤风中文封面。字体量级：标题做视觉锚——顶部中央墨色毛笔书法体大字标题"{TITLE}"（逐字准确），字高占画面约 1/3，一字千钧镇住全场；底部时间线上三个线框空心大数字"{N1}""{N2}""{N3}"是节奏钩子，字号约为标题的 1/2，每数字下方配极简短句"{S1}""{S2}""{S3}"（每句≤4字）；右上角小字点睛"{TIP}"（≤8字）只做注脚。配色系统：宣纸米 #F2EDE0 全幅底（温润，走极端浅明度）；墨黑书法标题；赭石 #B5651D 只给时间线细线与线框数字，是全图唯一的强调色。构图能量：一条"镇场→展开"动线——顶部书法大标题定调 → 右上点睛提示 → 底部横向时间线横向展开三步；大面积宣纸留白，步骤区只占底部一条。质感细节：宣纸底必须带淡墨晕染纹理 + 细腻纸纤维质感，拒绝死白平板底。除上述文字外无其他文字；所有文字在中央垂直60%安全区内，文人气、克制，横构图16:9，尺寸1200×675。

  EN: Tutorial-steps Chinese cover. Type scale: the title is the visual anchor — a large ink-brush calligraphy title "{TITLE}" (exact) top-center, glyph height ~1/3 of the frame, one stroke worth a thousand words holding the whole page; on the bottom timeline, three large wireframe hollow numbers "{N1}" "{N2}" "{N3}" act as rhythm hooks at ~1/2 the title size, each with a minimal short phrase below ("{S1}" "{S2}" "{S3}", max 4 characters each); a small accent note "{TIP}" (max 8 characters) top-right as footnote only. Color system: full-bleed rice-paper beige #F2EDE0 ground (warm, extreme-light value); ink-black calligraphy title; ochre #B5651D reserved for the timeline hairline and hollow numbers — the single accent color on the page. Composition energy: one "command then unfold" path — the calligraphy title sets the tone → the top-right note hints → the horizontal timeline unfolds three steps across the bottom; vast rice-paper negative space, the steps occupy only one bottom band. Texture: the paper ground must carry faint ink-bleed texture plus fine paper-fiber grain — a dead flat white ground is forbidden. No other text. All text within the central vertical 60% safe zone. Scholarly, restrained. Landscape 16:9, 1200×675.
  ```
  占位符：`{N1..N3}` 线框数字（01/02/03）、`{S1..S3}` 短句（每句 ≤4 字，越短越安全）、
  `{TIP}` 右上点睛（≤8 字）。
- **绝不清单**：
  - 绝不红笔刷横条标题：本风格的强调色只有赭石。
  - 绝不纵向步骤卡拼贴+箭头：步骤只沿底部横向时间线展开。
  - 绝不实心圆形序号章：数字只用线框空心。
  - 绝不步骤超过 3 个：超过 3 个立刻变说明书。
  - 绝不无纹理的死白底：无墨韵无纸纤维的平板底一律重画。

---

## 5. ip-fun · IP 趣味

- **适用场景**：实战案例、数据战报、复盘、系列连载（上/下篇）。
  示例图：`assets/examples/ip-fun.png`（原创：狐狸画家 IP + "AI绘画挑战营"）。
- **设计语言（抽象原则）**：
  - 暖色氛围做主角情绪：整张的"热气"是第一眼记忆。
  - 标题顶部叠放压阵：深棕大字在上，IP 形象在下半部做记忆点舞台，
    禁止左右对半分区。
  - 数字收进角落印章：数据是注脚，不是标题。
  - 署名做边角点缀：竖排小字，不进主视觉流。
- **配色故事**：橙黄暖色 `#FF9E2C → #FFC53D` 做主色（阳光、热闹）；
  标题与副标题用深棕 `#4A2C0A`（在暖底上最稳的重色）；
  朱红 `#E6392B` 只做右下印章，是全图唯一的跳色。
- **标题写法规范**：
  - 大标题 4~8 字深棕粗黑顶部叠放，字高占画面 1/4~1/3，如"AI绘画挑战营"；
    下方深棕小字副标题（如"每天一幅 · 进化看得见"）。
  - 数据（如"30天"）放右下角圆形印章内小字，不放大。
  - 署名（如"@阿狐画画"）放左下角竖排小字。
- **标题文案提炼公式**：天数挑战 + 动词结果。
  示例（虚构演示）："21天接单挑战"。
- **prompt 配方**：
  ```
  中文：IP 趣味风中文封面。字体量级：标题压阵——顶部叠放深棕色（#4A2C0A）超大粗黑中文标题"{TITLE}"（逐字准确），字高占画面 1/4~1/3；下方深棕色小字副标题"{SUBTITLE}"（≤12字）只做注解；标题与 IP 形象上下叠放，禁止左右对半分区。配色系统：橙黄暖色 #FF9E2C → #FFC53D 全幅主色（阳光热闹，走高饱和暖色）；深棕 #4A2C0A 标题在暖底上形成对比重心；右下角圆形印章内"{NUMBER}"小字（必须真实）用朱红 #E6392B，是全图唯一的跳色注脚。构图能量：一条对角线动线——顶部大标题（情绪钩子）→ 下半部原创趣味 IP 形象（{CHARACTER}，如戴贝雷帽的狐狸画家在画架前作画，暖色调，约占画面40%）做记忆点舞台 → 右下印章（数据注脚）收束；左下角竖排小字署名"{BYLINE}"做边角点缀，不进主视觉流。质感细节：暖色底必须加一层细腻纸纹颗粒 + 一团柔和的阳光光晕，拒绝塑料感平滑渲染。除上述文字外无其他文字；所有文字在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Fun-IP Chinese cover. Type scale: the title holds the fort — a stacked top dark-brown (#4A2C0A) extra-bold Chinese title "{TITLE}" (exact), glyph height 1/4 to 1/3 of the frame, with a small dark-brown subtitle "{SUBTITLE}" (max 12 characters) below as annotation only; title and IP character stack vertically — a left-right split layout is forbidden. Color system: warm orange-yellow #FF9E2C → #FFC53D full-bleed ground (sunny, high-saturation warmth); the dark-brown #4A2C0A title forms the contrast anchor on the warm ground; a small round seal bottom-right with "{NUMBER}" micro-text (must be factual) in vermilion #E6392B — the single accent footnote on the page. Composition energy: one diagonal reading path — top title (emotion hook) → an original playful IP character ({CHARACTER}, e.g. a beret-wearing fox painter at an easel, warm tones, ~40% of frame) staging the lower half as the memorable element → bottom-right seal (data footnote) closes the read; a small vertical byline "{BYLINE}" bottom-left as a corner garnish, kept out of the main visual flow. Texture: the warm ground must carry fine paper-grain plus a soft sunlight halo — plasticky smooth rendering is forbidden. No other text. All text within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{SUBTITLE}` 副标题（≤12 字）、`{NUMBER}` 印章内数字（如"30天"，必须真实）、
  `{BYLINE}` 边角署名（如"@阿狐画画"）、`{CHARACTER}` 原创趣味 IP 形象描述，
  必须与主题道具绑定（如绘画主题 → 狐狸画家 + 画架），不得照抄任何现有 IP 形象。
- **绝不清单**：
  - 绝不左文右图对半分：标题与形象必须上下叠放/错位，禁止左右镜像分区。
  - 绝不巨型彩色数字做标题：数字只进印章，且必须在正文中有出处。
  - 绝不冷色调主色：本风格必须是暖色，冷底直接变味。
  - 绝不形象遮挡标题字：形象是记忆点舞台，占比可到 40%，但吃字就作废。
  - 绝不塑料感平滑渲染：无纸纹无颗粒的"CG 塑料感"一律重画。

---

## 6. news-flash · 资讯快报

- **适用场景**：资讯、快讯、热点解读、人物专访预告、"祛魅/揭秘"类选题。
  示例图：`assets/examples/news-flash.png`（原创："今日AI速览" + 纸纹底 + 俯视桌面静物）。
- **设计语言（抽象原则）**：
  - 标题是绝对视觉重心：单色大字，一眼即主题，快讯的干脆来自"不加修饰"。
  - 信息分层三层：顶部眉题小字（给栏目/时效）→ 中央大标题（给主题）→
    右下角落生活静物（给"正在发生"的现场感）。
  - 点缀手法：俯视桌面静物（报纸/咖啡/闹钟）给氛围，点缀不进文字区。
  - 纸感来自质感：纸纹米底 + 大面积空旷，留白就是呼吸感。
- **配色故事**：纸纹米 `#F4F1E8` 做主色（纸感、阅读感）；标题纯黑单色
  （快讯的干脆，单色是本风格的魂）；静物保留真实色彩（红闹钟是唯一跳色，小面积）。
- **标题写法规范**：
  - 短标题 4~6 字，纯黑粗黑单行，如"今日AI速览"，字高占画面约 1/3。
  - 顶部眉题小字交代栏目/时效（如"晨间快讯 · 每日更新"），字号约为标题的 25%。
  - 感叹号/问号至多一个；标题里不出现彩色字。
- **标题文案提炼公式**：时间范围 + 领域 + "速览/必看"。
  示例（虚构演示）："一周AI大事"。
- **prompt 配方**：
  ```
  中文：资讯快报风中文封面。字体量级：标题是绝对视觉重心——左上纯黑色单行超大粗黑中文标题"{TITLE}"（逐字准确），字高占画面 1/3；单色即干脆，标题里不出现任何彩色字；标题上方顶部眉题小字"{EYEBROW}"（栏目/时效，如"晨间快讯 · 每日更新"，必须真实）交代上下文，字号约为标题的 1/4。配色系统：纸纹米 #F4F1E8 全幅主色（纸感、阅读感，走极端浅明度）；标题纯黑单色——单色是本风格的魂；右下角俯视桌面静物（{PROPS}，如一叠报纸、一杯冒热气的咖啡、一只红色小闹钟，2~3件）保留真实色彩，其中红色小闹钟是全图唯一的跳色。构图能量：一条"时效→主题→现场"动线——眉题（时效）→ 大标题（主题）→ 右下静物（"正在发生"的现场感落点）；静物只做氛围点缀，绝不进文字区。质感细节：纸底必须带干净细腻的纸纹 + 一处真实的纸张折痕或柔和阴影，拒绝死平无质感的白底，也拒绝做旧脏污。除标题、眉题、静物外无其他文字；所有文字与关键元素落在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: News-flash Chinese cover. Type scale: the title is the absolute visual anchor — a huge solid-black single-line extra-bold Chinese title "{TITLE}" (exact) at upper-left, glyph height 1/3 of the frame; monochrome IS the attitude, zero colored characters inside the title; a small top eyebrow "{EYEBROW}" (column/timeliness, e.g. "晨间快讯 · 每日更新", must be factual) sets context above the title at ~1/4 of the title size. Color system: full-bleed paper-beige #F4F1E8 ground (extreme-light value); pure-black monochrome title; a top-down desk still life bottom-right ({PROPS}, e.g. a stack of newspapers, a steaming coffee cup, a small red alarm clock, 2–3 items), the small red alarm clock the single accent color on the page. Composition energy: one "timeliness → theme → scene" path — eyebrow (timeliness) → big title (theme) → bottom-right still life (the "happening now" landing); the still life is atmosphere only, never entering the text zone. Texture: the paper ground must carry clean fine paper grain plus one real paper crease or soft shadow — a dead flat textureless ground is forbidden, and so is grimy distressed aging. No other text. All text and key elements within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{EYEBROW}` 眉题（栏目/时效，≤10 字）、`{PROPS}` 桌面静物描述（2~3 件，
  与主题相关，如报纸/咖啡/闹钟）。
- **绝不清单**：
  - 绝不两行撞色标题：标题必须单行纯黑，撞色+感叹号是别人的版式。
  - 绝不标题里出现彩色字：单色是铁律。
  - 绝不胶囊形副标题条：时效只进眉题小字。
  - 绝不静物进文字区：静物超过 3 件或压字，整张作废。
  - 绝不做旧脏纸纹：要干净纸纹 + 一处真实折痕，拒绝"脏"和"死平"两个极端。

---

## 7. minimal · 极简留白

- **适用场景**：随笔、书评、轻观点、生活感悟；公众号"轻阅读"类文章，
  或系列中需要"呼吸感"的穿插封面。
  示例图：`assets/examples/minimal.png`（原创："慢思考" + 水墨银杏叶点缀）。
- **设计语言（抽象原则）**：
  - 留白是主角：≥60% 空旷，呼吸感就是信息。
  - 点缀手法：一枚朱红印泥圆点做第一眼点睛，一处微小水墨笔触（银杏叶）
    做呼吸，细节精致、位置克制。
  - 标题写法：中等字号 + 字重 Bold + 字距拉宽，轻、慢、稳里藏着分量——
    "慢"的味道全在字距和字重里。
  - 元素总数 ≤3（点睛+点缀+标题），多一件都是负担。
- **配色故事**：冷白 `#F5F6F4` 做主色（干净、冷静）；淡墨只做点缀；
  一枚朱红 `#C73E2C` 印泥圆点是全图唯一的点睛色；
  标题用深灰，不用纯黑（纯黑太"重"，极简感全失）。
- **标题写法规范**：
  - 短标题 4~8 字，如"慢思考"；字距拉宽；字体用 Noto Sans SC Bold
    （比 Medium 重一级，用字重而非字号制造张力；仍不用 Black，太重则极简感全失）。
  - 不加副标题、不加标签条，克制到底。
- **标题文案提炼公式**：一个"慢/轻/少"字眼 + 一个具体生活词。
  示例（虚构演示）："慢煮生活"。
- **prompt 配方**：
  ```
  中文：极简留白风中文封面。字体量级：克制中的张力——深灰色（#3A3A38，不用纯黑）中文标题"{TITLE}"（逐字准确），字高约占画面 1/6，字重用 Bold（比 Medium 重一级，用字重而非字号制造分量），字距拉宽，"慢"的味道全在字距里；标题置于左下安全区内。配色系统：冷白 #F5F6F4 全幅主色（干净冷静，≥85% 留白，留白本身就是构图）；淡墨只做一处水墨点缀；一枚朱红（#C73E2C）印泥圆点（直径约画面 2%）是全图唯一的点睛色、唯一的记忆点。构图能量：一条极简动线——朱红点睛（第一眼）→ 淡墨银杏叶（呼吸）→ 宽字距标题（落点）；元素总数 ≤3（点睛+点缀+标题），多一件都是负担。质感细节：冷白底必须带一层极淡的宣纸纤维纹理，拒绝死白平板底；水墨笔触保留飞白的手工感。除标题外无其他文字；所有元素在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Minimalist negative-space Chinese cover. Type scale: tension inside restraint — a dark-gray (#3A3A38, never pure black) Chinese title "{TITLE}" (exact), glyph height ~1/6 of the frame, set in Bold weight (one step heavier than Medium — weight, not size, carries the presence), letter-spacing stretched wide; the "slow" feeling lives in the spacing; title sits in the lower-left safe zone. Color system: full-bleed cool white #F5F6F4 ground (clean, calm, at least 85% negative space — the emptiness IS the composition); light ink wash for one brush accent only; one vermilion (#C73E2C) seal-paste dot (~2% of frame diameter) — the single accent color and the single memorable element on the page. Composition energy: one minimal path — vermilion dot (first glance) → light-ink ginkgo leaf (breathing room) → wide-tracked title (landing); at most 3 elements total (dot, accent, title), one more is a burden. Texture: the cool-white ground must carry one whisper-faint layer of rice-paper fiber texture — a dead flat white ground is forbidden; the ink stroke keeps dry-brush flying-white handmadeness. No text besides the title. All elements within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
- **绝不清单**：
  - 绝不元素超过 3 个：对"杂物"零容忍，prompt 明确"一处""微小"，防模型加云加山。
  - 绝不纯黑标题：纯黑太"重"，极简感全失，用深灰。
  - 绝不两种以上的颜色：冷白+淡墨+一处朱红，多一色就"吵"。
  - 绝不标题贴边：留白即构图，标题必须悬在呼吸感里。
  - 绝不死白平板底：无纸纤维纹理的底一律重画。

---

## 8. magazine · 杂志编辑风

- **适用场景**：深度访谈、人物特写、商业分析、年度盘点；需要"质感/信任感"时用它，
  公众号长文首选。
  示例图：`assets/examples/magazine.png`（原创："创造者访谈" + 侧脸剪影 + 砖红细线）。
- **设计语言（抽象原则）**：
  - 质感来自克制：影棚颗粒 + 一条细色线，就是杂志感。
  - 人物手法：侧脸剪影（泛指描述）退为全幅背景氛围，给"人"的存在感但不抢标题。
  - 信息分层三层：人物氛围 → 细色线（定调）→ 标题（给主题），标题与人物上下叠放。
  - 同一色调只用一种底：浅底/深底不混用。
- **配色故事**：暖灰 `#E9E5DB` 做主色（影棚质感）；砖红 `#A63A2A` 只做一条细线点睛；
  标题炭黑，沉稳。
- **标题写法规范**：
  - 短标题 4~8 字，如"创造者访谈"；字体用 Noto Serif SC Bold（宋体感）或思源黑体 Bold。
  - 标题上方一条砖红细线是杂志感的灵魂，别省略。
- **标题文案提炼公式**：身份标签 + 反常识断言。
  示例（虚构演示）："投资人：别追风口"。
- **prompt 配方**：
  ```
  中文：杂志编辑风中文封面。字体量级：标题压前景——炭黑色典雅粗体中文标题"{TITLE}"（逐字准确，Noto Serif SC Bold 宋体感），字高占画面 1/4~1/3，居中偏下压在人物氛围之上，是全图唯一的视觉重心；标题上方一条砖红色（#A63A2A）细线定调，是杂志感的灵魂。配色系统：暖灰 #E9E5DB 全幅主色（影棚质感，走克制的中间偏浅明度）；砖红 #A63A2A 只做细线，是全图唯一的强调色；标题炭黑沉稳。构图能量：一条"氛围→定调→主题"动线——全幅低对比黑白人物侧脸剪影（{SUBJECT}，泛指描述，如穿西装的人物侧脸剪影）退为背景氛围、不抢戏 → 砖红细线（定调）→ 大标题（主题）；标题与人物上下叠放，禁止左右分区。质感细节：暖灰底必须带影棚级的细腻胶片颗粒 + 人物区一处真实的柔光阴影，拒绝塑料平滑的人像渲染。除标题外无其他文字；所有文字在中央垂直60%安全区内，克制高级，横构图16:9，尺寸1200×675。

  EN: Editorial magazine-style Chinese cover. Type scale: the title presses the foreground — an elegant charcoal-black bold Chinese title "{TITLE}" (exact, Noto Serif SC Bold with serif character), glyph height 1/4 to 1/3 of the frame, centered-lower, layered over the portrait atmosphere as the single visual anchor of the page; one thin brick-red (#A63A2A) rule above the title sets the tone — the soul of the magazine feel. Color system: full-bleed warm gray #E9E5DB ground (studio texture, restrained light-mid value); brick red #A63A2A reserved for the rule line only — the single accent color on the page; charcoal-black title, composed. Composition energy: one "atmosphere → tone → theme" path — a full-bleed low-contrast black-and-white profile silhouette ({SUBJECT}, generic description, e.g. a suited figure in profile) recedes as background atmosphere, never stealing the show → brick-red rule (tone) → big title (theme); title and figure stack vertically, a left-right split is forbidden. Texture: the warm-gray ground must carry studio-grade fine film grain plus one patch of real soft-light shadow in the figure zone — plasticky smooth portrait rendering is forbidden. No text besides the title. All text within the central vertical 60% safe zone. Restrained, premium. Landscape 16:9, 1200×675.
  ```
  占位符：`{SUBJECT}` 人物泛指描述（职业/姿态，不得出现可识别的真实人物长相）。
- **绝不清单**：
  - 绝不出现可识别的真实人物长相：人物必须用"泛指"描述。
  - 绝不左右分区：标题与人物必须叠放，禁止左文右图式分区。
  - 绝不浅底深底混用：同一色调只用一种底。
  - 绝不留白处加装饰字：杂志风的力量全在克制。
  - 绝不塑料平滑的人像渲染：无胶片颗粒无真实光影一律重画。

---

## 风格速查

| 风格 | 一句话 | 标题字号占比 | 首选题材 |
|---|---|---|---|
| gan-huo | 深炭灰底 + 米白 1/3 巨标题 + 朱红印章点睛，一眼即干货 | ~1/3 | 干货清单/评测/盘点 |
| big-type | 标题即画面：1/3 幅墨黑书法烫金，奶油亮底一声断言 | 1/3~2/5 | 观点/深度/发布宣言 |
| brand-launch | 深海军蓝 + 荧光绿唯一强调，品牌大标题压阵 | 1/4~1/3 | 产品发布/版本更新 |
| tutorial-steps | 宣纸书法 1/3 镇场 + 底部赭石时间线，三步即上手 | ~1/3 | 教程/上手指南 |
| ip-fun | 暖橙舞台 + 深棕叠放巨标题 + 趣味 IP 记忆点 | 1/4~1/3 | 实战案例/数据战报 |
| news-flash | 纸纹米底 + 纯黑 1/3 单色大标题，快讯的干脆 | ~1/3 | 资讯/快讯/热点解读 |
| minimal | 85% 留白 + 一处朱红点睛 + 宽字距深灰标题，张力拉满 | ~1/6（字重补） | 随笔/书评/轻观点 |
| magazine | 暖灰影棚颗粒 + 人像氛围 + 砖红细线，标题压阵 | 1/4~1/3 | 访谈/人物特写/商业分析 |