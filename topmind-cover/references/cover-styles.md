# 封面风格库（11 种）

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
这类可辨识的构图公式。`assets/examples/` 中的 26 张风格示例图均为原创设计，
其标题/数字/品牌/署名（如"深蓝 OS 2.0""提示词避坑指南""AI绘画挑战营""@阿狐画画"）
均为虚构演示内容，仅用于演示设计原则。
用本库组 prompt 时，标题、形象、版式细节必须自己原创；
改图时只换主体与标题字，保留本风格的配色故事与设计原则。

---

## 9. gan-huo · 爆款干货

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
  中文：爆款干货风中文封面。字体量级：全图只有一个视觉重心——中央米白色超粗黑中文标题"{TITLE}"（逐字准确），标题字高占画面 1/3，与深底形成最大明度差；顶部小字眉题"{EYEBROW}"（筛选口径，如"18篇 · 逐条实测"）只做开场，字号约为标题的 1/3。配色系统：深炭灰 #2B2B30 全幅深底（沉稳可信，走极端明度）；暖橙 #FF8A3D 只做细线框点缀；朱红 #E6392B 方形印章（右上角，内写白色小字"{NUMBER}"）是全图唯一的跳色、唯一的记忆点。构图能量：一条纵向主阅读动线——眉题（为什么信）→ 大标题（这是什么）→ 印章（数据背书）；左下角一只小巧原创小形象（{CHARACTER}，占画面约15%）做动线落点，绝不遮挡标题。质感细节：深底必须加一层细腻胶片噪点颗粒 + 一道极淡的斜向光影，拒绝死平纯色的塑料感。文字特效：标题里挑钩子词做三处装饰，全句只用米白、朱红、暖橙三种颜色——①把一个钩子词（如“翻车”）换成朱红 #E6392B，其余字保持米白；②另一个钩子词下方垫一块朱红 #E6392B 实色矩形，色块高度为字高的 1.2 倍，米白字压在色块上、明暗对立（色块衬底的字不再换色）；③用暖橙 #FF8A3D 马克笔笔触把标题里的数字钩子（如“7”）圈起来，圈略大于字、不压笔画，只圈一处。除标题、眉题、印章、形象外无其他文字；所有文字与关键元素落在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: High-impact Chinese viral-listicle cover. Type scale: exactly one visual anchor — a centered off-white extra-bold Chinese title "{TITLE}" (exact), glyph height 1/3 of the frame, maximum brightness contrast against the dark ground; a small top eyebrow "{EYEBROW}" (selection criteria, e.g. "18 posts, tested one by one") opens the read at ~1/3 of the title size. Color system: full-bleed deep charcoal #2B2B30 ground (steady, credible, extreme-dark value); warm-orange #FF8A3D hairline frame accents only; one vermilion #E6392B square seal at top-right with white micro-text "{NUMBER}" — the single hot-color accent and the single memorable element on the page. Composition energy: one vertical reading path — eyebrow (why trust) → giant title (what it is) → seal (data proof); a tiny original mascot ({CHARACTER}, ~15% of frame) sits bottom-left as the path's landing point, never covering the title. Texture: the dark ground must carry one layer of fine film grain plus one faint diagonal light sweep — flat lifeless solid color is forbidden. Text effects: decorate the hook words with exactly three treatments — only off-white, vermilion, and warm orange in the sentence: ① recolor one hook word (e.g. “翻车”) in vermilion #E6392B, keep the rest off-white; ② slide a solid vermilion #E6392B rectangle under another hook word, block height 1.2× glyph height, off-white type over it with opposing light-dark contrast (block-backed words are not recolored); ③ circle the title's number hook (e.g. “7”) with a warm-orange #FF8A3D marker stroke, the circle slightly larger than the glyphs, never touching strokes, only one circle. No other text. All text and key elements within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{EYEBROW}` 眉题（≤10 字）、`{NUMBER}` 印章内数字（如"18篇"，必须真实）、
  `{CHARACTER}` 原创小形象描述（如"纸飞机造型蓝色小机器人"），不得照抄任何现有 IP 形象。
- **绝不清单**：
  - 绝不小字标题：标题字高不足画面 1/4，整张作废。
  - 绝不把数字做成彩色大字抢标题：数字只进印章，标题里不再出现第二个数字钩子。
  - 绝不浅底：本风格必须是深底，浅底直接变味。
  - 绝不底部标签条/胶囊条：卖点只进眉题小字。
  - 绝不死平纯色底：无噪点无光影的"塑料底"一律重画。
  - 绝不透视/扭曲/弧形排大标题：中文必乱码，要动感用色块和圈注代替。
  - 绝不标题里超 3 种颜色：字色只许米白+朱红，暖橙圈注已是第三种，多一色就"吵"。
  - 绝不竖排+旋转组合：大标题永远水平；旋转只许右上印章≤8°。
  - 绝不色块吞字：色块高度≤1.3 倍字高，米白字压朱红块、明暗对立。
  - 绝不装饰压笔画：圈注只圈标题里一个数字钩子、不压笔画。
  - 绝不装饰超量：单图只用变色+色块+圈注 3 种，多一种即乱。

---

## 5. big-type · 巨字宣言

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
  中文：巨字宣言风中文封面。字体量级：标题即画面——单行超大墨黑中文标题"{TITLE}"（逐字准确），横跨画面约85%宽度，字高占画面 1/3~2/5；{TYPE_STYLE}（墨黑书法体配烫金 #C9A227 描边 / 空心描边字 / 竖排大字三选一），字形本身就是情绪；标题下方深灰色陈述句副标题"{SUBTITLE}"只做注解，字号约为标题的 1/4。配色系统：明亮奶油 #FAF3E7 全幅亮底（宣言的从容感，走极端明度）；墨黑标题字；烫金 #C9A227 只点缀一处笔画或一字，是全图唯一的强调。构图能量：一条横向主阅读动线——巨标题横扫全场（钩子与主题合一）→ 副标题收束落点；背景只留极淡的金色几何线条，全部给标题让路。质感细节：奶油底必须带细腻纸纹 + 书法笔锋的飞白质感，拒绝干净单调的平板底。文字特效：冲击力全在字形上，全句颜色不超过 3 种——①标题里的钩子词（如反常识断言词“暴跌”）字号放大到其余字的 1.5 倍，其余字保持原字号，不换行；②描边按 {TYPE_STYLE} 选型量化：“书法烫金”选型只给一处笔画或一字勾烫金 #C9A227 细描边（描边宽不超过笔画宽的 1/5，防笔画粘连）；“空心描边字”选型用 2px 深灰描边、字内留白；③字后方加一层同字形、浅墨灰色、向右下错位 4px 的字，只错位一层，制造轻微立体感；描边与立体已是两种效果，绝不再加阴影。除标题与副标题外无其他文字；所有文字在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Giant-type manifesto Chinese cover. Type scale: the title IS the image — one single-line oversized ink-black Chinese title "{TITLE}" (exact), spanning ~85% of frame width, glyph height 1/3 to 2/5 of the frame; {TYPE_STYLE} (ink-black calligraphy with gold #C9A227 edge accents / outlined hollow type / vertical type) — the letterforms carry the emotion; a small dark-gray declarative subtitle "{SUBTITLE}" below only annotates, at ~1/4 of the title size. Color system: full-bleed bright cream #FAF3E7 ground (extreme-light value, the calm of a manifesto); ink-black title; gold #C9A227 accents exactly one stroke or one character — the single emphasis on the page. Composition energy: one horizontal reading path — the giant title sweeps the frame (hook and theme in one) → the subtitle lands the read; the background keeps only whisper-faint gold geometric lines, everything yields to the title. Texture: the cream ground must carry fine paper grain plus dry-brush flying-white texture in the calligraphy strokes — a clean flat ground is forbidden. Text effects: all impact lives in the letterforms — at most 3 colors in the line: ① enlarge the hook word (e.g. the contrarian claim word) to 1.5× the other glyphs, keep the rest at base size, no line break; ② quantify the outline per {TYPE_STYLE}: the “gold calligraphy” option outlines only one stroke or one glyph in a gold #C9A227 hairline (outline width ≤ 1/5 of stroke width, no stroke merging); the “hollow outline” option uses 2px dark-gray outline with empty interior; ③ add one same-glyph layer behind the type in light ink-gray, offset 4px down-right, a single offset only, for a subtle 3D lift; outline plus 3D is already two effects — never add a drop shadow. No other text. All text within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{TYPE_STYLE}` 字形处理三选一（书法烫金 / 描边空心 / 竖排），
  `{SUBTITLE}` 陈述句副标题（≤10 字，禁止问句）。
- **绝不清单**：
  - 绝不两行撞色标题：本风格只做单行（或竖排），两行撞色是别人的版式。
  - 绝不暗黑背景：本风格必须是亮底，暗底直接变味。
  - 绝不问句/煽动式副标题：副标题只能是陈述句注解。
  - 绝不标题字高不足 1/4：字一小，宣言感全失。
  - 绝不出现第二处烫金：强调色只给一处，多一处就"吵"。
  - 绝不透视变形大标题：要动感用轻微立体代替。
  - 绝不一句话超 3 种颜色（含描边色、立体层颜色）。
  - 绝不描边+阴影+立体三重叠加：本风格只用描边+轻微立体两种，绝不再加阴影。
  - 绝不竖排+旋转组合：竖排字形不叠加任何旋转；旋转只许印章/标签类小元素≤8°，单行大标题永远水平。
  - 绝不描边过粗：描边宽≤笔画宽 1/5，粗了笔画粘连。
  - 绝不装饰超量：字号对比+描边+轻微立体 3 种封顶。

---

## 10. brand-launch · 品牌发布

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
  中文：品牌发布风中文封面。字体量级：品牌名就是标题——顶部居中大号白色粗黑中文标题"{TITLE}"（逐字准确），字高占画面 1/4~1/3，其中品牌词"{KEYWORDS}"做色块衬底（见"文字特效"段）、其余纯白，是全图唯一的视觉重心；标题下一条荧光绿细线收束视觉，紧跟一排浅灰白分隔符小字卖点"{SELLING_POINTS}"（如"更快 · 更稳 · 更懂你"）做背书。配色系统：深海军蓝 #0A1F44 全幅深底（深邃专业，走极端明度）；荧光绿 #3DFF88 是唯一的强调色（色块衬底、细线、卖点小字都用它，别处不再出现第二种颜色）。构图能量：一条纵向主阅读动线——品牌大标题（定调）→ 细线+卖点小字（背书）→ 中央下方荧光绿发光线条勾勒的抽象产品氛围（{PRODUCT}，线框/光影、无可读文字）做氛围落点；左上预留空白 logo 区。质感细节：深蓝底必须加一层细腻星尘噪点 + 中央一团柔和的荧光绿光晕渐变，拒绝死黑平板底。文字特效：贵气来自克制，全句只用纯白、荧光绿、深海军蓝三种颜色——①品牌词“{KEYWORDS}”下方垫一块荧光绿 #3DFF88 实色矩形，色块高度为字高的 1.2 倍，字换成深海军蓝 #0A1F44 粗体压在色块上、明暗对立（色块替代原荧光绿发光描边写法，不叠加）；②其余纯白标题字加一层向右下 45° 的柔和投影，投影偏移为字高的 1/10，黑色 30% 不透明度、柔和不脏；阴影不加在品牌词上，同一字不同时叠加描边和阴影。除标题、卖点小字外无其他文字；所有文字在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Brand-launch Chinese cover. Type scale: the brand name IS the title — a large white extra-bold Chinese title "{TITLE}" (exact) centered at top, glyph height 1/4 to 1/3 of the frame; the brand term "{KEYWORDS}" glows in fluorescent-green outline, the rest pure white — the single visual anchor of the page; one thin fluorescent-green rule cinches the eye below the title, followed by one row of light-gray separator-style selling points "{SELLING_POINTS}" (e.g. "更快 · 更稳 · 更懂你") as proof. Color system: full-bleed deep navy #0A1F44 ground (deep, professional, extreme-dark value); fluorescent green #3DFF88 is the ONLY accent color (glowing outlines, hairlines, selling-point micro-text all use it — no second color anywhere). Composition energy: one vertical reading path — brand title (sets the tone) → rule plus selling points (proof) → an abstract product atmosphere drawn in glowing fluorescent-green lines ({PRODUCT}, wireframe and light, no readable text) lower-center as the atmospheric landing; empty logo area reserved top-left. Texture: the navy ground must carry fine stardust grain plus one soft fluorescent-green halo glow at center — a dead flat black ground is forbidden. Text effects: premium comes from restraint — only pure white, fluorescent green, and deep navy in the line: ① slide a solid fluorescent-green #3DFF88 rectangle under the brand term “{KEYWORDS}”, block height 1.2× glyph height, type set in deep-navy #0A1F44 bold over it with opposing light-dark contrast (the block replaces the glowing-outline treatment — never stacked); ② the remaining pure-white title glyphs get one soft drop shadow at 45° down-right, offset 1/10 of glyph height, black at 30% opacity, soft and clean; no shadow on the brand term — one glyph never carries outline and shadow together. No other text. All text within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{KEYWORDS}` 品牌词、`{PRODUCT}` 产品氛围描述、`{SELLING_POINTS}` 分隔符小字（≤12 字）；
  真实 logo 必须后期贴图，绝不用 AI 生成 logo。
- **绝不清单**：
  - 绝不渐变彩虹标题：强调色只用荧光绿一种，第二种颜色出现即杂。
  - 绝不写实产品大图/UI 截图：只要发光线框氛围，可读 UI 文字必出乱码。
  - 绝不图标式卖点条：卖点只用一排分隔符小字。
  - 绝不 AI 生成 logo：真实 logo 必须后期贴图。
  - 绝不死黑无光影的底：无星尘无光晕的平板深底一律重画。
  - 绝不透视变形大标题：要动感用轻微阴影代替。
  - 绝不一句话超 3 种颜色：本风格只有纯白、荧光绿、深海军蓝三种。
  - 绝不描边+阴影+立体三重叠加：品牌词用色块（无阴影），纯白字用阴影（无描边），同一字不同时叠加。
  - 绝不竖排+旋转组合：大标题永远水平；旋转只许小元素≤8°。
  - 绝不色块吞字：色块高度≤1.3 倍字高，深蓝字压荧光绿块、明暗对立。
  - 绝不装饰超量：色块+轻微阴影 2 种封顶。

---

## 6. tutorial-steps · 教程步骤

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
  中文：教程步骤风中文封面。字体量级：标题做视觉锚——顶部中央墨色毛笔书法体大字标题"{TITLE}"（逐字准确），字高占画面约 1/3，一字千钧镇住全场；底部时间线上三个线框空心大数字"{N1}""{N2}""{N3}"是节奏钩子，字号约为标题的 1/2，每数字下方配极简短句"{S1}""{S2}""{S3}"（每句≤4字）；右上角小字点睛"{TIP}"（≤8字）只做注脚。配色系统：宣纸米 #F2EDE0 全幅底（温润，走极端浅明度）；墨黑书法标题；赭石 #B5651D 只给时间线细线与线框数字，是全图唯一的强调色。构图能量：一条"镇场→展开"动线——顶部书法大标题定调 → 右上点睛提示 → 底部横向时间线横向展开三步；大面积宣纸留白，步骤区只占底部一条。质感细节：宣纸底必须带淡墨晕染纹理 + 细腻纸纤维质感，拒绝死白平板底。文字特效：教程风靠“划重点”指路，全句只用墨黑、赭石两种颜色——①标题里的关键词（如动词“做出”）换成赭石 #B5651D，其余字保持墨黑；②在关键词下方画一条手绘感波浪下划线，赭石 #B5651D，线宽为笔画宽度的 1/2，略带抖动、不压笔画；装饰只用这 2 种，不再加箭头。除上述文字外无其他文字；所有文字在中央垂直60%安全区内，文人气、克制，横构图16:9，尺寸1200×675。

  EN: Tutorial-steps Chinese cover. Type scale: the title is the visual anchor — a large ink-brush calligraphy title "{TITLE}" (exact) top-center, glyph height ~1/3 of the frame, one stroke worth a thousand words holding the whole page; on the bottom timeline, three large wireframe hollow numbers "{N1}" "{N2}" "{N3}" act as rhythm hooks at ~1/2 the title size, each with a minimal short phrase below ("{S1}" "{S2}" "{S3}", max 4 characters each); a small accent note "{TIP}" (max 8 characters) top-right as footnote only. Color system: full-bleed rice-paper beige #F2EDE0 ground (warm, extreme-light value); ink-black calligraphy title; ochre #B5651D reserved for the timeline hairline and hollow numbers — the single accent color on the page. Composition energy: one "command then unfold" path — the calligraphy title sets the tone → the top-right note hints → the horizontal timeline unfolds three steps across the bottom; vast rice-paper negative space, the steps occupy only one bottom band. Texture: the paper ground must carry faint ink-bleed texture plus fine paper-fiber grain — a dead flat white ground is forbidden. Text effects: the tutorial voice “marks the key point” — only ink black and ochre in the line: ① recolor the title's keyword (e.g. the verb) in ochre #B5651D, keep the rest ink black; ② draw one hand-drawn wavy underline beneath the keyword in ochre #B5651D, line width 1/2 of stroke width, slightly wobbly, never touching strokes; only these 2 treatments — no arrows. No other text. All text within the central vertical 60% safe zone. Scholarly, restrained. Landscape 16:9, 1200×675.
  ```
  占位符：`{N1..N3}` 线框数字（01/02/03）、`{S1..S3}` 短句（每句 ≤4 字，越短越安全）、
  `{TIP}` 右上点睛（≤8 字）。
- **绝不清单**：
  - 绝不红笔刷横条标题：本风格的强调色只有赭石。
  - 绝不纵向步骤卡拼贴+箭头：步骤只沿底部横向时间线展开。
  - 绝不实心圆形序号章：数字只用线框空心。
  - 绝不步骤超过 3 个：超过 3 个立刻变说明书。
  - 绝不无纹理的死白底：无墨韵无纸纤维的平板底一律重画。
  - 绝不透视变形大标题。
  - 绝不标题超 3 种颜色：本风格只用墨黑+赭石两种，多一色就杂。
  - 绝不竖排+旋转组合：大标题永远水平。
  - 绝不装饰压笔画：下划线线宽≤笔画宽 1/2，不压字。
  - 绝不装饰超量：变色+手绘下划线 2 种封顶，不再加箭头。

---

## 11. ip-fun · IP 趣味

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
  中文：IP 趣味风中文封面。字体量级：标题压阵——顶部叠放深棕色（#4A2C0A）超大粗黑中文标题"{TITLE}"（逐字准确），字高占画面 1/4~1/3；下方深棕色小字副标题"{SUBTITLE}"（≤12字）只做注解；标题与 IP 形象上下叠放，禁止左右对半分区。配色系统：橙黄暖色 #FF9E2C → #FFC53D 全幅主色（阳光热闹，走高饱和暖色）；深棕 #4A2C0A 标题在暖底上形成对比重心；右下角圆形印章内"{NUMBER}"小字（必须真实）用朱红 #E6392B，是全图唯一的跳色注脚。构图能量：一条对角线动线——顶部大标题（情绪钩子）→ 下半部原创趣味 IP 形象（{CHARACTER}，如戴贝雷帽的狐狸画家在画架前作画，暖色调，约占画面40%）做记忆点舞台 → 右下印章（数据注脚）收束；左下角竖排小字署名"{BYLINE}"做边角点缀，不进主视觉流。质感细节：暖色底必须加一层细腻纸纹颗粒 + 一团柔和的阳光光晕，拒绝塑料感平滑渲染。文字特效：潮玩感来自“贴纸+徽章”，全句颜色不超过 3 种——①标题里的关键词（如挑战词“接单”）原位下方垫一块深棕 #4A2C0A 实色矩形（色块在字下方、标题总字数不变，严禁把关键词复制一份做成独立元素），色块高度为字高的 1.2 倍，字换成米白色压在色块上、明暗对立；②标题字后方加一层同字形、朱红 #E6392B、向右下错位 4px 的字，只错位一层，做出徽章凸起的轻微立体感；色块与立体已是两种效果，不再加描边和阴影。除上述文字外无其他文字；所有文字在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Fun-IP Chinese cover. Type scale: the title holds the fort — a stacked top dark-brown (#4A2C0A) extra-bold Chinese title "{TITLE}" (exact), glyph height 1/4 to 1/3 of the frame, with a small dark-brown subtitle "{SUBTITLE}" (max 12 characters) below as annotation only; title and IP character stack vertically — a left-right split layout is forbidden. Color system: warm orange-yellow #FF9E2C → #FFC53D full-bleed ground (sunny, high-saturation warmth); the dark-brown #4A2C0A title forms the contrast anchor on the warm ground; a small round seal bottom-right with "{NUMBER}" micro-text (must be factual) in vermilion #E6392B — the single accent footnote on the page. Composition energy: one diagonal reading path — top title (emotion hook) → an original playful IP character ({CHARACTER}, e.g. a beret-wearing fox painter at an easel, warm tones, ~40% of frame) staging the lower half as the memorable element → bottom-right seal (data footnote) closes the read; a small vertical byline "{BYLINE}" bottom-left as a corner garnish, kept out of the main visual flow. Texture: the warm ground must carry fine paper-grain plus a soft sunlight halo — plasticky smooth rendering is forbidden. Text effects: the collectible-toy feel comes from “sticker plus badge” — at most 3 colors in the line: ① slide a solid dark-brown #4A2C0A rectangle under the title's keyword in place (e.g. the challenge word; block sits beneath the glyphs, total character count unchanged — never duplicate the keyword as a separate element), block height 1.2× glyph height, off-white type over it with opposing light-dark contrast; ② add one same-glyph layer behind the title in vermilion #E6392B, offset 4px down-right, a single offset only, for a badge-like subtle 3D lift; block plus 3D is already two effects — never add outline or shadow. No other text. All text within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
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
  - 绝不透视变形大标题：要动感用轻微立体代替。
  - 绝不一句话超 3 种颜色。
  - 绝不描边+阴影+立体三重叠加：本风格只用色块+轻微立体，不再加描边和阴影。
  - 绝不竖排+旋转组合：左下竖排署名保持不转；旋转只许右下印章≤8°，大标题永远水平。
  - 绝不色块吞字：色块高度≤1.3 倍字高，米白字压深棕块、明暗对立。
  - 绝不装饰超量：色块+立体 2 种封顶。

---

## 1. white-clean · 白色清新

- **适用场景**：干货清单、实测盘点、效率/副业/职场类选题；"替你筛好了、看完即用"类
  亲和干货的默认选择。示例图：`assets/examples/white-clean.png`（原创："一人公司起步指南"）。
  设计语言来源：用户 2026-09-29 提供的两张"白色清新"风格代表图
  （`references/ref-white-clean-1.png`、`ref-white-clean-2.png`）；只学抽象设计语言，不抄版式。
- **设计语言（抽象原则）**：
  - 纯白底 + 大面积留白：干净清新，信息流里"透气"。
  - 标题极大：空间允许时字高冲击画面 1/3；1~2 行横跨顶部，关键词撞色。
  - 关键词装饰每次只用 2~3 种：撞色变色 / 马克笔横条衬底 / 色块衬底。
  - 场景化插图：3D 毛绒 / Q 版人物 + 与主题绑定的工作场景（悬浮卡片、工具、桌面），
    插图讲"正在用"的故事，不做无意义装饰。
  - 圆角胶囊标签行：浅色胶囊 + 小图标 + 短词，收束卖点。
  - 小装饰点到为止：星星、感叹号、波浪线，至多 2 处。
- **配色故事**：纯白 `#FFFFFF` 全幅主色（走极端浅明度）；标题墨黑 `#1A1A1A` 打底；
  撞色只给标题关键词（优选组合三选一，见配方）；胶囊用撞色对应的浅色系。
- **标题写法规范**：
  - 短标题 6~10 字，1~2 行，顶部横跨，空间允许时字高冲击 1/3（底线 ≥1/4），
    如"一人公司起步指南"。
  - 每行至多 1 个撞色关键词。
  - 胶囊标签行 3 个短词，`·` 分隔（如"实测筛选 · 长文精选 · 全流程实操"），
    字号约为标题的 1/4。
- **标题文案提炼公式**：人群/场景 + 结果承诺。
  示例（虚构演示）："打工人副业增收课"。
- **prompt 配方**：
  ```
  中文：白色清新风中文封面。字体量级：标题是绝对视觉重心——顶部横跨墨黑色（#1A1A1A）超大粗黑中文标题"{TITLE}"（逐字准确），1~2 行，空间允许时字高冲击画面 1/3（底线≥1/4）；中部一条浅色圆角胶囊标签行"{TAGLINE}"（如"实测筛选 · 长文精选 · 全流程实操"，必须真实）收束卖点，字号约为标题的 1/4。字体优选组合 {FONT_COMBO} 三选一：A 超粗黑体（力量感，笔画粗、字面满）/ B 圆润黑体（亲和感，笔画圆润、字角圆）/ C 黑体正文 + 英文关键词斜体（国际感）。配色系统：纯白 #FFFFFF 全幅主色（极端浅明度，大面积留白）；标题墨黑 #1A1A1A 打底；撞色优选组合 {COLOR_COMBO} 三选一：A 品牌蓝 #2B7FFF + 活力橙红 #FF5A2E / B 电光紫 #7C5CFF + 薄荷青 #00C2A8 / C 墨黑 #1A1A1A + 品牌蓝 #2B7FFF，撞色只给标题关键词（每行至多 1 个撞色词）；胶囊用撞色对应的浅色（如 #EAF2FF 系）。构图能量：一条"主题→背书→场景"动线——顶部大标题横跨全宽（钩子与主题合一）→ 中部胶囊标签行（背书）→ 底部场景化插图舞台（{SCENE}，如毛绒质感 3D 小角色在悬浮卡片与主题工具之间忙碌、带柔和投影，约占画面 35%，必须与主题绑定、讲"正在用"的故事）做记忆点落点；标题与插图上下叠放，禁止左右对半镜像分区。花式优选组合 {FX_COMBO} 每次只用 2~3 种：①关键词变色高亮（撞色，见配色组合）；②黄色 #FFD93B 马克笔横条衬底（横条略宽于字、不压笔画）；③关键词原位垫实色块（色块高度为字高的 1.2 倍，字色与色块明暗对立，标题总字数不变、严禁复制关键词做独立元素）。方向/透视优选组合 {DIR_COMBO} 三选一：A 标题全水平、胶囊轻微错位叠放；B 撞色关键词整体上扬 ≤8°（字不转、整体转）；C 插图轻微俯视透视、标题保持水平。大标题永远水平，绝不透视变形。质感细节：纯白底必须带一层极淡的纸纹 + 插图区一团柔和的浅色光晕，拒绝死白平板底。除标题、胶囊行外无其他文字；所有文字与关键元素在中央垂直 60% 安全区内，横构图 16:9，尺寸 1200×675。

  EN: Clean-white Chinese cover. Type scale: the title is the absolute visual anchor — an oversized ink-black (#1A1A1A) extra-bold Chinese title "{TITLE}" (exact) spanning the top in 1–2 lines, glyph height pushing toward 1/3 of the frame when space allows (floor 1/4); one light rounded-capsule tag row "{TAGLINE}" (e.g. "实测筛选 · 长文精选 · 全流程实操", must be factual) mid-page cinches the selling points at ~1/4 of the title size. Font combo {FONT_COMBO}, pick one of three: A ultra-bold heiti (powerful, heavy strokes, full letterforms) / B rounded heiti (friendly, soft strokes, rounded corners) / C heiti body with italic English keywords (international feel). Color system: full-bleed pure white #FFFFFF ground (extreme-light value, generous negative space); ink-black #1A1A1A title base; accent combo {COLOR_COMBO}, pick one of three: A brand blue #2B7FFF + vivid orange-red #FF5A2E / B electric purple #7C5CFF + mint teal #00C2A8 / C ink black #1A1A1A + brand blue #2B7FFF — accents touch title keywords only (at most one accented word per line); capsules use the matching light tints (e.g. the #EAF2FF family). Composition energy: one "theme → proof → scene" path — the giant title spans the top (hook and theme in one) → the capsule tag row (proof) → a scenario illustration stage at the bottom ({SCENE}, e.g. a fluffy 3D mascot busy among floating cards and topic tools with soft shadows, ~35% of frame, must tie to the topic and tell a "being used" story) as the memorable landing; title and illustration stack vertically — a mirrored left-right split is forbidden. Flourish combo {FX_COMBO}, use only 2–3 per image: ① keyword recolor highlight (accent color per the palette combo); ② yellow #FFD93B marker highlighter bar behind a keyword (bar slightly wider than the glyphs, never touching strokes); ③ solid color block under a keyword in place (block height 1.2× glyph height, opposing light-dark contrast, total character count unchanged — never duplicate the keyword as a separate element). Direction/perspective combo {DIR_COMBO}, pick one of three: A fully horizontal title with slightly offset-stacked capsules; B the accented keyword tilted upward ≤8° as a whole (glyphs not rotated, the block rotated); C illustration in slight top-down perspective while the title stays horizontal. The main title is always horizontal — never warped in perspective. Texture: the white ground must carry one whisper-faint paper grain plus one soft light-tint halo in the illustration zone — a dead flat white ground is forbidden. No text besides the title and capsule row. All text and key elements within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{TAGLINE}` 胶囊标签行（3 短词，`·` 分隔，≤14 字，必须真实）、
  `{SCENE}` 场景化插图描述（必须与主题绑定：角色 + 场景 + 主题道具，讲"正在用"的故事）、
  `{FONT_COMBO}` 字体三选一（A 超粗黑 / B 圆润黑 / C 黑体+英文斜体）、
  `{COLOR_COMBO}` 撞色三选一（A 蓝+橙红 / B 紫+青 / C 黑+品牌蓝）、
  `{FX_COMBO}` 花式每次 2~3 种（变色 / 马克笔横条 / 色块衬底）、
  `{DIR_COMBO}` 方向三选一（A 全水平 / B 关键词上扬≤8° / C 插图俯视）。
- **绝不清单**：
  - 绝不深底/灰底：本风格必须是纯白底，底色一深直接变味。
  - 绝不标题字高不足 1/4：空间允许必须冲击 1/3。
  - 绝不左右对半镜像分区：标题与插图必须上下叠放。
  - 绝不每行超 1 个撞色词：撞色一多就"吵"。
  - 绝不一句话超 3 种颜色：标题内只许墨黑 + 撞色组合的两种。
  - 绝不透视变形大标题：大标题永远水平。
  - 绝不色块吞字：色块高度≤1.3 倍字高，明暗对立。
  - 绝不装饰压笔画：横条/圈注不压字。
  - 绝不装饰超量：花式 2~3 种封顶，小装饰（星星/感叹号）至多 2 处。
  - 绝不无意义插图：插图必须与主题绑定、讲"正在用"的故事，纯装饰角色一律不用。

---

## 2. bg-blur · 背景虚化

- **适用场景**：生活方式、职场日常、运动健康、城市观察；"氛围感 + 主题"类文章的
  默认选择。示例图：`assets/examples/bg-blur.png`（原创："深夜加班自救手册"）。
- **设计语言（抽象原则）**：
  - 虚化摄影背景 + 清晰前景主体：大光圈景深对比本身就是记忆点。
  - 背景走浅色调虚化（明亮、通透），拒绝暗黑压抑。
  - 前景主体锐利清晰，与主题强绑定（人物半身 / 产品特写 / 主题物件三选一）。
  - 大标题压在清晰区：空间允许时字高冲击 1/3，字色与背景明度对立。
  - 光斑/柔光只做氛围，不进文字区。
- **配色故事**：浅色虚化摄影背景（米白 / 浅灰 / 柔光，极端浅明度）；标题深色
  （墨黑 / 深棕）；强调色只给一处（关键词或一处光斑色）。
- **标题写法规范**：
  - 短标题 6~10 字，单行或双行，压在画面清晰区，空间允许时字高冲击 1/3（底线 ≥1/4）。
  - 标题字加浅色光晕衬底或细描边，保证在虚化背景上可读。
- **标题文案提炼公式**：场景 + 痛点/获得。
  示例（虚构演示）："通勤包里的效率术"。
- **prompt 配方**：
  ```
  中文：背景虚化风中文封面。字体量级：大标题压在清晰区——深色超大粗黑中文标题"{TITLE}"（逐字准确），单行或双行，空间允许时字高冲击画面 1/3（底线≥1/4），是全图唯一的视觉重心；标题字加一层浅色光晕衬底（或 2px 浅色描边，描边宽≤笔画宽 1/5），保证在虚化背景上清晰可读。字体优选组合 {FONT_COMBO} 三选一：A 超粗黑体（醒目）/ B 人文黑体（亲和）/ C 粗黑 + 数字/英文斜体混排。配色系统：浅色调虚化摄影背景 {BG_SCENE}（极端浅明度：明亮、通透，拒绝暗黑）；标题深色（墨黑 #1A1A1A / 深棕二选一）；强调色优选组合 {COLOR_COMBO} 三选一：A 暖橙 #FF8A3D（配光斑）/ B 品牌蓝 #2B7FFF / C 朱红 #E6392B，强调色只给标题关键词一处。构图能量：一条"氛围→主体→主题"动线——浅色虚化背景（氛围，大光圈虚化 + 柔和光斑，不进文字区）→ 清晰前景主体（{SUBJECT}，锐利清晰、约占画面 30~40%，必须与主题强绑定）→ 大标题压在主体旁的清晰区（主题）；背景与主体明暗/虚实对立，景深对比就是记忆点。花式优选组合 {FX_COMBO} 每次只用 2 种：①关键词变色高亮（强调色）；②关键词字号放大到其余字的 1.4 倍（不换行）。方向/透视优选组合 {DIR_COMBO} 三选一：A 标题全水平、主体三分法站位；B 标题沿主体轮廓轻微上扬 ≤8°；C 前景主体轻微仰视透视、标题保持水平。大标题不做透视变形。质感细节：背景虚化必须有真实的光斑层次 + 前景主体边缘锐利，拒绝"全图均匀模糊"的假虚化。除标题外无其他文字；所有文字与关键主体在中央垂直 60% 安全区内，横构图 16:9，尺寸 1200×675。

  EN: Background-blur Chinese cover. Type scale: the big title presses the sharp zone — an oversized dark extra-bold Chinese title "{TITLE}" (exact), one or two lines, glyph height pushing toward 1/3 of the frame when space allows (floor 1/4), the single visual anchor of the page; the title carries one light halo backing (or a 2px light outline, outline width ≤ 1/5 of stroke width) so it stays legible over the blur. Font combo {FONT_COMBO}, pick one of three: A ultra-bold heiti (punchy) / B humanist heiti (friendly) / C bold heiti mixed with italic numerals/English. Color system: light-toned blurred photographic background {BG_SCENE} (extreme-light value: bright, airy — dark and moody is forbidden); dark title (ink black #1A1A1A / deep brown, pick one); accent combo {COLOR_COMBO}, pick one of three: A warm orange #FF8A3D (pairs with bokeh) / B brand blue #2B7FFF / C vermilion #E6392B — the accent touches exactly one title keyword. Composition energy: one "atmosphere → subject → theme" path — the light blurred background (atmosphere: wide-aperture blur plus soft bokeh, kept out of the text zone) → the sharp foreground subject ({SUBJECT}, tack-sharp, 30–40% of frame, must tie strongly to the topic) → the big title pressed into the clear zone beside the subject (theme); background and subject oppose in light and in sharpness — the depth-of-field contrast IS the memorable element. Flourish combo {FX_COMBO}, use only 2 per image: ① keyword recolor highlight (accent color); ② keyword enlarged to 1.4× the other glyphs (no line break). Direction/perspective combo {DIR_COMBO}, pick one of three: A fully horizontal title with the subject on a rule-of-thirds position; B the title rising gently ≤8° along the subject's contour; C the foreground subject in slight low-angle perspective while the title stays horizontal. The main title is never warped in perspective. Texture: the background blur must show real bokeh layering, and the foreground subject must have crisp edges — uniformly blurred "fake bokeh" is forbidden. No text besides the title. All text and key subjects within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{BG_SCENE}` 背景虚化场景三选一（明亮办公室虚化 / 城市街景光斑虚化 / 自然柔光虚化，
  必须浅色调）、`{SUBJECT}` 清晰前景主体三选一（人物半身 / 产品特写 / 主题物件，
  必须与主题强绑定）、`{FONT_COMBO}` 字体三选一、`{COLOR_COMBO}` 强调色三选一
  （橙/蓝/朱红，只给一处）、`{FX_COMBO}` 花式 2 种（变色 + 字号对比）、
  `{DIR_COMBO}` 方向三选一。
- **绝不清单**：
  - 绝不暗黑虚化背景：本风格背景必须是浅色调，暗底直接变味。
  - 绝不全图均匀模糊：背景虚化必须有光斑层次，前景主体必须锐利。
  - 绝不标题落在虚化重灾区：标题必须压在清晰区，否则可读性全失。
  - 绝不标题字高不足 1/4：空间允许必须冲击 1/3。
  - 绝不一句话超 3 种颜色：深色标题 + 一处强调色。
  - 绝不透视变形大标题。
  - 绝不光斑进文字区：光斑只做背景氛围。
  - 绝不主体与主题无关：前景主体必须与主题强绑定，无意义摆拍一律不用。
  - 绝不装饰超量：变色 + 字号对比 2 种封顶。

---

## 3. paper-collage · 纸感拼贴

- **适用场景**：手账、整理术、生活灵感、旧物改造、轻教程；"手作感 / 人味"类选题的
  默认选择。示例图：`assets/examples/paper-collage.png`（原创："手账整理术"）。
- **设计语言（抽象原则）**：
  - 浅色底 + 纸片拼贴：撕边 / 圆角 / 便签纸片错位叠放，拼贴本身就是构图。
  - 固定手法三选一：和纸胶带 / 回形针 / 图钉，"贴上去"的真实感。
  - 标题落在最大纸片上（或牛皮纸标签），空间允许时字高冲击 1/3。
  - 小贴纸 / 小标签点缀，元素总数 ≤5。
  - 手工感：撕纸毛边、胶带半透明，拒绝 CG 塑料感。
- **配色故事**：米白 / 浅灰底（极端浅明度）；纸片用马卡龙浅色系优选组合
  （浅蓝 / 浅粉 / 浅黄 / 浅绿三选一）；标题深色；一处跳色（朱红 / 赭石）只给最小的标签。
- **标题写法规范**：
  - 短标题 4~8 字，印在最大纸片中央，空间允许时字高冲击 1/3（底线 ≥1/4），如"手账整理术"。
  - 纸片上不加第二行小字，干净。
- **标题文案提炼公式**：旧物 / 日常 + 动词改造。
  示例（虚构演示）："工位改造计划"。
- **prompt 配方**：
  ```
  中文：纸感拼贴风中文封面。字体量级：标题是视觉重心——深色超大粗黑中文标题"{TITLE}"（逐字准确），印在最大纸片中央，空间允许时字高冲击画面 1/3（底线≥1/4）；纸片上不加第二行小字。字体优选组合 {FONT_COMBO} 三选一：A 超粗黑体（海报感）/ B 手写体（人味，笔画清晰可辨）/ C 黑体 + 英文小字混排。配色系统：米白 / 浅灰底（极端浅明度）；纸片马卡龙浅色系优选组合 {COLOR_COMBO} 三选一：A 浅蓝 #D6E9FF + 浅黄 #FFF3C4 / B 浅粉 #FFDCE5 + 浅绿 #D9F2E2 / C 牛皮纸 #E8DCC8 + 纯白 #FFFFFF；标题深色（墨黑 / 深棕二选一）；跳色只给最小的标签一处（朱红 #E6392B / 赭石 #B5651D 二选一）。构图能量：一条"底→纸片→标题"动线——浅色底（呼吸）→ 3~5 张纸片 {PAPER_COMBO} 错位叠放拼贴（撕边 / 圆角 / 便签三选一，纸片带撕纸毛边与柔和投影）→ 最大纸片上的大标题（主题）；纸片用 {FIX_COMBO} 固定（和纸胶带 / 回形针 / 图钉三选一，半透明/金属质感真实）；1~2 张小贴纸或小标签做点缀（元素总数 ≤5）。花式优选组合 {FX_COMBO} 每次只用 2 种：①标题关键词变色（跳色）；②小标签上手写感圈注（只圈一处）。方向/透视优选组合 {DIR_COMBO} 三选一：A 纸片全水平、错位叠放；B 最大纸片整体倾斜 ≤8°（字不转、纸转）；C 轻微俯视拼贴桌面、标题保持水平。大标题不做透视变形。质感细节：纸片必须有撕纸毛边 + 纸纹 + 柔和投影，胶带半透明，拒绝 CG 塑料感。除标题、小标签短词外无其他文字；所有文字与关键纸片在中央垂直 60% 安全区内，横构图 16:9，尺寸 1200×675。

  EN: Paper-collage Chinese cover. Type scale: the title is the visual anchor — an oversized dark extra-bold Chinese title "{TITLE}" (exact) printed at the center of the largest paper scrap, glyph height pushing toward 1/3 of the frame when space allows (floor 1/4); no second line of small text on the scrap. Font combo {FONT_COMBO}, pick one of three: A ultra-bold heiti (poster feel) / B handwriting style (human touch, strokes clean and legible) / C heiti mixed with small English. Color system: off-white / light-gray ground (extreme-light value); pastel paper palette combo {COLOR_COMBO}, pick one of three: A light blue #D6E9FF + light yellow #FFF3C4 / B light pink #FFDCE5 + light green #D9F2E2 / C kraft #E8DCC8 + pure white #FFFFFF; dark title (ink black / deep brown, pick one); one pop of color reserved for the smallest tag only (vermilion #E6392B / ochre #B5651D, pick one). Composition energy: one "ground → scraps → title" path — the light ground (breathing room) → 3–5 paper scraps {PAPER_COMBO} in offset collage (torn edge / rounded corner / sticky-note, pick one; scraps carry torn fibrous edges and soft shadows) → the big title on the largest scrap (theme); scraps fastened with {FIX_COMBO} (washi tape / paper clip / push pin, pick one, realistic translucent/metal texture); 1–2 small stickers or tags as garnish (at most 5 elements total). Flourish combo {FX_COMBO}, use only 2 per image: ① title keyword recolor (pop color); ② hand-drawn circle on a small tag (only one circle). Direction/perspective combo {DIR_COMBO}, pick one of three: A all scraps horizontal in offset stack; B the largest scrap tilted ≤8° as a whole (glyphs not rotated, the scrap rotated); C slight top-down view of the collage desk while the title stays horizontal. The main title is never warped in perspective. Texture: scraps must show torn fibrous edges plus paper grain plus soft shadows, tape translucent — plasticky CG rendering is forbidden. No text besides the title and small tag words. All text and key scraps within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{PAPER_COMBO}` 纸片三选一（撕边 / 圆角 / 便签）、`{FIX_COMBO}` 固定手法三选一
  （和纸胶带 / 回形针 / 图钉）、`{FONT_COMBO}` 字体三选一、`{COLOR_COMBO}` 纸片配色三选一、
  `{FX_COMBO}` 花式 2 种（变色 + 圈注）、`{DIR_COMBO}` 方向三选一。
- **绝不清单**：
  - 绝不深底：本风格必须是浅色底。
  - 绝不纸片超 5 张：元素总数 ≤5，多一张就碎。
  - 绝不标题字高不足 1/4：空间允许必须冲击 1/3。
  - 绝不 CG 塑料感：无毛边无纸纹无投影的纸片一律重画。
  - 绝不透视变形大标题。
  - 绝不一句话超 3 种颜色。
  - 绝不纸片上加第二行小字。
  - 绝不装饰超量：变色 + 圈注 2 种封顶。

---

## 4. news-flash · 资讯快报

- **适用场景**：资讯、快讯、热点解读、人物专访预告、"祛魅/揭秘"类选题。
  示例图：`assets/examples/news-flash.png`（原创："今日AI速览" + 纸纹底 + 俯视桌面静物）。
- **设计语言（抽象原则）**：
  - 标题是绝对视觉重心：单色大字，一眼即主题，快讯的干脆来自"不加修饰"。
  - 信息分层三层：顶部眉题小字（给栏目/时效）→ 中央大标题（给主题）→
    右下角落生活静物（给"正在发生"的现场感）。
  - 点缀手法：俯视桌面静物（报纸/咖啡/闹钟）给氛围，点缀不进文字区。
  - 纸感来自质感：纸纹米底 + 大面积空旷，留白就是呼吸感。
- **配色故事**：纸纹米 `#F4F1E8` 做主色（纸感、阅读感）；标题以纯黑为主打底、爆点关键词做朱红点睛
  （快讯的干脆来自纯黑的利落，朱红只给爆点词一处）；静物保留真实色彩（红闹钟是唯一跳色，小面积）。
- **标题写法规范**：
  - 短标题 4~6 字，纯黑粗黑单行，如"今日AI速览"，字高占画面约 1/3。
  - 顶部眉题小字交代栏目/时效（如"晨间快讯 · 每日更新"），字号约为标题的 25%。
  - 感叹号/问号至多一个；标题里彩色只给爆点关键词一处（朱红）。
- **标题文案提炼公式**：时间范围 + 领域 + "速览/必看"。
  示例（虚构演示）："一周AI大事"。
- **prompt 配方**：
  ```
  中文：资讯快报风中文封面。字体量级：标题是绝对视觉重心——左上纯黑色单行超大粗黑中文标题"{TITLE}"（逐字准确），字高占画面 1/3；标题以纯黑为主打底，爆点关键词做朱红点睛（见“文字特效”段），其余字一律纯黑；标题上方顶部眉题小字"{EYEBROW}"（栏目/时效，如"晨间快讯 · 每日更新"，必须真实）交代上下文，字号约为标题的 1/4。配色系统：纸纹米 #F4F1E8 全幅主色（纸感、阅读感，走极端浅明度）；标题纯黑单色——单色是本风格的魂；右下角俯视桌面静物（{PROPS}，如一叠报纸、一杯冒热气的咖啡、一只红色小闹钟，2~3件）保留真实色彩，其中红色小闹钟是全图唯一的跳色。构图能量：一条"时效→主题→现场"动线——眉题（时效）→ 大标题（主题）→ 右下静物（"正在发生"的现场感落点）；静物只做氛围点缀，绝不进文字区。质感细节：纸底必须带干净细腻的纸纹 + 一处真实的纸张折痕或柔和阴影，拒绝死平无质感的白底，也拒绝做旧脏污。文字特效：突发感靠“爆点词炸出来”，标题里只用纯黑、朱红两种颜色——①标题里的爆点关键词（如“暴跌”）换成朱红 #E6392B，其余字保持纯黑；②爆点词字号放大到其余字的 1.5 倍，其余字保持原字号，不换行；③从标题向右下静物方向画一条朱红 #E6392B 手绘箭头，只画一条，线条粗细均匀、不压字，制造“正在发生”的现场感。除标题、眉题、静物外无其他文字；所有文字与关键元素落在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: News-flash Chinese cover. Type scale: the title is the absolute visual anchor — a huge solid-black single-line extra-bold Chinese title "{TITLE}" (exact) at upper-left, glyph height 1/3 of the frame; monochrome IS the attitude, zero colored characters inside the title; a small top eyebrow "{EYEBROW}" (column/timeliness, e.g. "晨间快讯 · 每日更新", must be factual) sets context above the title at ~1/4 of the title size. Color system: full-bleed paper-beige #F4F1E8 ground (extreme-light value); pure-black monochrome title; a top-down desk still life bottom-right ({PROPS}, e.g. a stack of newspapers, a steaming coffee cup, a small red alarm clock, 2–3 items), the small red alarm clock the single accent color on the page. Composition energy: one "timeliness → theme → scene" path — eyebrow (timeliness) → big title (theme) → bottom-right still life (the "happening now" landing); the still life is atmosphere only, never entering the text zone. Texture: the paper ground must carry clean fine paper grain plus one real paper crease or soft shadow — a dead flat textureless ground is forbidden, and so is grimy distressed aging. Text effects: breaking-news energy comes from the “exploding” keyword — only pure black and vermilion in the title: ① recolor the title's breaking keyword (e.g. “暴跌”) in vermilion #E6392B, keep the rest pure black; ② enlarge the keyword to 1.5× the other glyphs, keep the rest at base size, no line break; ③ draw one vermilion hand-drawn arrow from the title toward the bottom-right still life, a single arrow with even line weight, never covering glyphs, for the “happening now” feel. No other text. All text and key elements within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
  占位符：`{EYEBROW}` 眉题（栏目/时效，≤10 字）、`{PROPS}` 桌面静物描述（2~3 件，
  与主题相关，如报纸/咖啡/闹钟）。
- **绝不清单**：
  - 绝不两行撞色标题：标题必须单行（纯黑打底、爆点词朱红点睛），撞色+感叹号是别人的版式。
  - 绝不标题里出现第二个彩色：彩色只给爆点关键词一处（朱红），多一处就“吵”。
  - 绝不透视变形大标题：要动感用字号对比+箭头。
  - 绝不一句话超 3 种颜色：标题里只许纯黑+朱红两种。
  - 绝不竖排+旋转组合：大标题永远水平；旋转只许小元素≤8°。
  - 绝不箭头压字或超过 1 条：只画一条手绘箭头，不压笔画。
  - 绝不装饰超量：变色+字号对比+箭头 3 种封顶。
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
  中文：极简留白风中文封面。字体量级：克制中的张力——深灰色（#3A3A38，不用纯黑）中文标题"{TITLE}"（逐字准确），字高约占画面 1/6，字重用 Bold（比 Medium 重一级，用字重而非字号制造分量），字距拉宽，"慢"的味道全在字距里；标题置于左下安全区内。配色系统：冷白 #F5F6F4 全幅主色（干净冷静，≥85% 留白，留白本身就是构图）；淡墨只做一处水墨点缀；一枚朱红（#C73E2C）印泥圆点（直径约画面 2%）是全图唯一的点睛色、唯一的记忆点。构图能量：一条极简动线——朱红点睛（第一眼）→ 淡墨银杏叶（呼吸）→ 宽字距标题（落点）；元素总数 ≤3（点睛+点缀+标题），多一件都是负担。质感细节：冷白底必须带一层极淡的宣纸纤维纹理，拒绝死白平板底；水墨笔触保留飞白的手工感。文字特效：克制到底——标题字本身不加任何装饰（不变色、不描边、不加阴影、不旋转、不下划线）；全图唯一的装饰就是那枚朱红 #C73E2C 印泥圆点点睛（直径约画面 2%，见“配色系统”段），与深灰标题字形成明暗对立；装饰种类只许这 1 种，多一种即破功。除标题外无其他文字；所有元素在中央垂直60%安全区内，横构图16:9，尺寸1200×675。

  EN: Minimalist negative-space Chinese cover. Type scale: tension inside restraint — a dark-gray (#3A3A38, never pure black) Chinese title "{TITLE}" (exact), glyph height ~1/6 of the frame, set in Bold weight (one step heavier than Medium — weight, not size, carries the presence), letter-spacing stretched wide; the "slow" feeling lives in the spacing; title sits in the lower-left safe zone. Color system: full-bleed cool white #F5F6F4 ground (clean, calm, at least 85% negative space — the emptiness IS the composition); light ink wash for one brush accent only; one vermilion (#C73E2C) seal-paste dot (~2% of frame diameter) — the single accent color and the single memorable element on the page. Composition energy: one minimal path — vermilion dot (first glance) → light-ink ginkgo leaf (breathing room) → wide-tracked title (landing); at most 3 elements total (dot, accent, title), one more is a burden. Texture: the cool-white ground must carry one whisper-faint layer of rice-paper fiber texture — a dead flat white ground is forbidden; the ink stroke keeps dry-brush flying-white handmadeness. Text effects: restraint to the end — the title glyphs carry zero decoration (no recolor, no outline, no shadow, no rotation, no underline); the single decorative accent on the page is that vermilion #C73E2C seal-paste dot (~2% of frame diameter, defined in the color system above), set against the dark-gray title with opposing light-dark contrast; exactly 1 decoration type allowed — one more breaks the style. No text besides the title. All elements within the central vertical 60% safe zone. Landscape 16:9, 1200×675.
  ```
- **绝不清单**：
  - 绝不元素超过 3 个：对"杂物"零容忍，prompt 明确"一处""微小"，防模型加云加山。
  - 绝不纯黑标题：纯黑太"重"，极简感全失，用深灰。
  - 绝不两种以上的颜色：冷白+淡墨+一处朱红，多一色就"吵"。
  - 绝不标题贴边：留白即构图，标题必须悬在呼吸感里。
  - 绝不死白平板底：无纸纤维纹理的底一律重画。
  - 绝不使用变色/旋转/手绘装饰：标题字本身零装饰，唯一的装饰是朱红印泥圆点点睛。
  - 绝不装饰超量：装饰种类只许 1 种，多一种即破功。
  - 绝不透视变形大标题。
  - 绝不一句话超 3 种颜色：标题字色只用深灰一种。
  - 绝不竖排+旋转组合：大标题永远水平；本风格连小元素旋转也不用。

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
  中文：杂志编辑风中文封面。字体量级：标题压前景——炭黑色典雅粗体中文标题"{TITLE}"（逐字准确，Noto Serif SC Bold 宋体感），字高占画面 1/4~1/3，居中偏下压在人物氛围之上，是全图唯一的视觉重心；标题上方一条砖红色（#A63A2A）细线定调，是杂志感的灵魂。配色系统：暖灰 #E9E5DB 全幅主色（影棚质感，走克制的中间偏浅明度）；砖红 #A63A2A 只给细线和标题关键词两处，是全图唯一的强调色；标题炭黑沉稳。构图能量：一条"氛围→定调→主题"动线——全幅低对比黑白人物侧脸剪影（{SUBJECT}，泛指描述，如穿西装的人物侧脸剪影）退为背景氛围、不抢戏 → 砖红细线（定调）→ 大标题（主题）；标题与人物上下叠放，禁止左右分区。质感细节：暖灰底必须带影棚级的细腻胶片颗粒 + 人物区一处真实的柔光阴影，拒绝塑料平滑的人像渲染。文字特效：杂志封面的强调全在标题排印上，标题里只用炭黑、砖红两种颜色——①标题里的关键词（如反常识断言词“别追”）换成砖红 #A63A2A，其余字保持炭黑；②关键词字号放大到其余字的 1.5 倍，其余字保持原字号，不换行；装饰只用这 2 种，留白处不加任何装饰字。除标题外无其他文字；所有文字在中央垂直60%安全区内，克制高级，横构图16:9，尺寸1200×675。

  EN: Editorial magazine-style Chinese cover. Type scale: the title presses the foreground — an elegant charcoal-black bold Chinese title "{TITLE}" (exact, Noto Serif SC Bold with serif character), glyph height 1/4 to 1/3 of the frame, centered-lower, layered over the portrait atmosphere as the single visual anchor of the page; one thin brick-red (#A63A2A) rule above the title sets the tone — the soul of the magazine feel. Color system: full-bleed warm gray #E9E5DB ground (studio texture, restrained light-mid value); brick red #A63A2A reserved for the rule line only — the single accent color on the page; charcoal-black title, composed. Composition energy: one "atmosphere → tone → theme" path — a full-bleed low-contrast black-and-white profile silhouette ({SUBJECT}, generic description, e.g. a suited figure in profile) recedes as background atmosphere, never stealing the show → brick-red rule (tone) → big title (theme); title and figure stack vertically, a left-right split is forbidden. Texture: the warm-gray ground must carry studio-grade fine film grain plus one patch of real soft-light shadow in the figure zone — plasticky smooth portrait rendering is forbidden. Text effects: a magazine cover's emphasis lives in the title typography — only charcoal black and brick red in the title: ① recolor the title's keyword (e.g. the contrarian claim) in brick red #A63A2A, keep the rest charcoal black; ② enlarge the keyword to 1.5× the other glyphs, keep the rest at base size, no line break; only these 2 treatments — no decorative words in the negative space. No text besides the title. All text within the central vertical 60% safe zone. Restrained, premium. Landscape 16:9, 1200×675.
  ```
  占位符：`{SUBJECT}` 人物泛指描述（职业/姿态，不得出现可识别的真实人物长相）。
- **绝不清单**：
  - 绝不出现可识别的真实人物长相：人物必须用"泛指"描述。
  - 绝不左右分区：标题与人物必须叠放，禁止左文右图式分区。
  - 绝不浅底深底混用：同一色调只用一种底。
  - 绝不留白处加装饰字：杂志风的力量全在克制。
  - 绝不塑料平滑的人像渲染：无胶片颗粒无真实光影一律重画。
  - 绝不透视变形大标题。
  - 绝不标题超 3 种颜色：只用炭黑+砖红两种。
  - 绝不竖排+旋转组合：大标题永远水平。
  - 绝不装饰超量：变色+字号对比 2 种封顶。

---

## 风格速查（浅色优先：1~8 浅色，9~11 深色/高饱和）

| 风格 | 一句话 | 标题字号占比 | 首选题材 |
|---|---|---|---|
| white-clean | 纯白底 + 冲击 1/3 的撞色巨标题 + 场景化插图 + 胶囊标签，清新透气 | 冲击 1/3 | 干货清单/实测盘点/效率职场 |
| bg-blur | 浅色虚化摄影背景 + 锐利前景主体，大标题压清晰区 | 冲击 1/3 | 生活方式/职场日常/运动健康 |
| paper-collage | 马卡龙纸片拼贴 + 和纸胶带/回形针，标题印最大纸片上 | 冲击 1/3 | 手账/整理术/旧物改造 |
| news-flash | 纸纹米底 + 纯黑大标题 + 朱红爆点词点睛，快讯的干脆 | ~1/3 | 资讯/快讯/热点解读 |
| big-type | 标题即画面：1/3 幅墨黑书法烫金，奶油亮底一声断言 | 1/3~2/5 | 观点/深度/发布宣言 |
| tutorial-steps | 宣纸书法 1/3 镇场 + 底部赭石时间线，三步即上手 | ~1/3 | 教程/上手指南 |
| minimal | 85% 留白 + 一处朱红点睛 + 宽字距深灰标题，张力拉满 | ~1/6（字重补） | 随笔/书评/轻观点 |
| magazine | 暖灰影棚颗粒 + 人像氛围 + 砖红细线，标题压阵 | 1/4~1/3 | 访谈/人物特写/商业分析 |
| gan-huo | 深炭灰底 + 米白 1/3 巨标题 + 朱红印章点睛，一眼即干货 | ~1/3 | 干货清单/评测/盘点 |
| brand-launch | 深海军蓝 + 荧光绿唯一强调，品牌大标题压阵 | 1/4~1/3 | 产品发布/版本更新 |
| ip-fun | 暖橙舞台 + 深棕叠放巨标题 + 趣味 IP 记忆点 | 1/4~1/3 | 实战案例/数据战报 |