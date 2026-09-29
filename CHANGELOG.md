## [0.3.3] - 2026-09-29

> 根包 0.3.2 → **0.3.3**（patch）；4 个技能 `version` 保持不动（top-ppt-html 0.1.19，其余 0.1.0）。
> 注：0.3.2 未发布，已并入本版。

### topmind-cover：6 张样张版式级重设计（差异化纠偏）

- 用户指出第四轮样张仍是"翻版"（版式结构照搬 7 张参考封面，只换文案形象）。
  本轮按**版式级标准**重做：只保留抽象原则（标题是视觉重心/信息分层/留白呼吸感），
  6 张重设计（gan-huo 居中构图+深炭灰暖橙、big-type 单行超大书法字+奶油亮底、
  brand-launch 深海军蓝+荧光绿、tutorial-steps 横向时间线+墨色题字、
  ip-fun 数字改右下角印章+橙黄暖色、news-flash 纯黑单色+纸纹+俯视静物大改），
  2 张保留微调（minimal「慢思考」、magazine「创造者访谈」）。
- 8 张主配色互不相同，且不与 7 张参考图主配色（浅蓝/黑红/粉紫/红白/蓝白）撞车；
  每张过双重目检（中文正确性 + 路人测试：描述画面后追问"像哪张参考图"，答不出才算过）。
- `references/cover-styles.md`：设计语言收紧为抽象原则，删除"左文右图""底部标签条"等
  具体版式描述；**原创铁律升级**：版式与配色也不得与第三方封面构成实质相似，
  只学原则不学版式。

### topmind-wechat-post / topmind-x-article：第二轮深审（质量）

- wechat-post：修 5 处文档与实现/规范打架（`---` 渲染文档落后于实现、主题表 genre 漏项、
  最小示例缺放图前置步骤、`--link-mode note` 档无文档、加粗密度两份规范打架按 lint 对齐）；
  零行为改动。遗留 3 个需改行为候选：缺图是否进合规自检、border-radius WARN 去噪、
  h2 序号剥离残留标点。
- x-article：文档×脚本 14/14 规则实测一致；补 x-format.md 4 处"脚本有行为、文档没写"缺口；
  SKILL.md 触发词补 `X 发长文`/`推特长文`/`twitter 长文`；README.en 表格标点精确化；
  零行为改动。遗留 4 个行为变化候选：无前导 `|` 表格、`~~~` 围栏、标题 140 字符检查
  （超长分段经评估不需要）。

## [0.3.2] - 2026-09-29

> **本版未发布**（未打 tag、未发 npm），全部内容已并入 0.3.3。以下为当时记录：

> 根包 0.3.1 → **0.3.2**（patch）；4 个技能 `version` 保持不动（top-ppt-html 0.1.19，其余 0.1.0）。
> 整仓同 tag 发版，技能 `version` 独立演进（见 docs/PUBLISHING.md）。

### topmind-cover：样张原创重制（纠偏）

- 上一版 16 张样张被指出"照搬参考封面"（文案与形象临摹第三方爆款图），本轮推倒重做：
  设计语言保留（巨型标题字/数字彩色突出/三层文字结构/中央 60% 安全区），
  **8 种风格全部换上原创标题与视觉**："7天玩转提示词"（纸飞机机器人）、"AI效率手册"
  （抽象光影几何）、"星尘 OS 3.0"（虚构品牌发布）、"从想法到产品"（步骤卡片）、
  "30天AI绘画挑战"（狐狸画家 IP）、"AI早报！"（报纸咖啡）、"慢思考"（银杏留白）、
  "创造者访谈"（杂志肖像）。
- `assets/examples/` 16 张（8 主图 + 8 公众号裁剪版）+ `overview.png` 全部重拼重检：
  中文逐字正确、无乱码、与参考图不构成临摹；`README.md` 声明样张为原创设计、
  标题/数字/品牌均为虚构演示。
- `references/cover-styles.md` 新增**原创铁律**：prompt 配方是设计语言，
  禁止照抄任何第三方封面的文案与形象；8 风格示例小节同步换为本轮原创标题。

### topmind-wechat-post：全面优化 + 4 处修复

- `scripts/md2wechat.py` 修复：**行内图片绕过图片管线**（现统一经管线解析、复制到
  `images/`、登记上传清单、可被 `--embed-images` 内嵌）；分隔线不再触发自家合规
  WARN（改用块级 `<section>` 居中，视觉一致）；标题手写序号剥离支持大写数字
  （壹贰叁肆伍陆柒捌玖拾）；图片 `title` 属性（`![a](x "t")`）不再导致整段源码泄漏。
- SKILL.md：主题表"适用"列与各主题 JSON 的 `genre` 声明对齐；补行内图片走图片管线
  说明；补 `--link-mode` 参数说明（默认脚注上标 / `inline` 括号注）。
- README（中/英）：新增 9 行"最小示例"（输入→输出片段）+ `md2wechat` 参数表。
- `negative_tests.py` 5→8 项，全过。

### topmind-x-article：全面优化 + 12 处转换 bug 修复

- `scripts/md2x.py` 修复 12 处：标题/引用/表格内行内标记残留、引用式链接与图片
  （`[文字][ref]`/`![alt][img]` 及定义行）、URL 含括号断裂、`\` 转义符残留、
  Setext 标题残留、带空格分割线（`* * *`）不识别、代码块内 `---` 误判分割线、
  文首 `---` 被 frontmatter 误吞、BOM 头、文档以代码块开头时首行缩进丢失。
- SKILL.md：description 补 `Do NOT use for 公众号（→ topmind-wechat-post）`，与短推文
  路由对称；`references/x-format.md` 转换规则表与脚本行为对齐。
- README（中/英）：转换规则更新 + 新增 10 行"最小示例"（输出经实测逐字一致）。

## [0.3.1] - 2026-09-29

> 根包 0.3.0 → **0.3.1**（patch）；4 个技能 `version` 保持不动（top-ppt-html 0.1.19，其余 0.1.0）。
> 整仓同 tag 发版，技能 `version` 独立演进（见 docs/PUBLISHING.md）。

### topmind-cover：风格库按爆款封面重沉淀 + 样张重制

- `references/cover-styles.md` 按 7 张爆款参考封面 + Manus 实战封面重沉淀为 **8 种风格**：
  爆款干货（`gan-huo`）/ 巨字宣言（`big-type`）/ 品牌发布（`brand-launch`）/
  教程步骤（`tutorial-steps`）/ IP 趣味（`ip-fun`）/ 资讯快报（`news-flash`）/
  极简留白（`minimal`，保留）/ 杂志编辑（`magazine`，保留），
  每种含适用场景、构图公式、配色 hex、标题写法规范（4~8 字、数字/关键词彩色突出）、
  中英 prompt 配方、避坑；删除旧 6 风格。
- `assets/examples/` 样张全部重制：**16 张**（8 风格 × 1200×675 主图 + 900×383 公众号中央裁剪版）
  + `overview.png`（8 宫格总览图），逐张目检（标题逐字准确、无乱码、中央 60% 安全区），
  7 次返工均为"底部元素超出安全区"；旧 12 张移除。
- 提炼规律：标题字巨大化（占画面高 22%~45%）、左文右图通用分区、三层文字结构
  （大标题 + 胶囊/笔刷副标题 + 底部标签条）、数字前置造冲击、背景极简浅色。
- 根 README（中/英）、cover README（中/英）、cover SKILL.md 嵌入总览图（GitHub 绝对 URL）
  + 8 风格一行式索引；用法"6 选 1"→"8 选 1"。

### bug 修复

- topmind-wechat-post `scripts/md2wechat.py`：本地图片文件缺失时未登记进"图片上传清单"
  （用户按清单补图会漏传）；现登记 `⚠ 本地文件缺失` 行并计入"图片 N 张"计数。
  HTML 仍保留断链占位（设计选择），清单已标注。

## [0.3.0] - 2026-09-29

> 根包 0.2.0 → **0.3.0**（minor，新功能）；4 个技能 `version` 保持不动（top-ppt-html 0.1.19，其余 0.1.0）。
> 整仓同 tag 发版，技能 `version` 独立演进（见 docs/PUBLISHING.md）。

### topmind-cover：封面风格库 + 12 张示例图（新功能）

- `references/cover-styles.md` 扩为 **6 种风格库**：震撼大字报（`big-poster`）/ 科技未来感（`tech-future`）/
  杂志编辑风（`magazine`）/ 极简留白（`minimal`）/ 国潮插画（`guochao`）/ 赛博故障艺术（`cyber-glitch`），
  每种含适用场景、配色 hex、字体建议、中英 prompt 配方、避坑。
- `assets/examples/` 新增 **12 张示例图**（6 风格 × 1200×675 主图 + 900×383 公众号中央裁剪版，共约 6.4MB），
  附 `assets/examples/README.md`（清单 + 安全区说明 + 复用声明），随 npm 包发布。
- SKILL.md 工作流新增"**步骤 0 选风格**"（三步必做：按题材 6 选 1 → 看示例图 → 按配方组 prompt）。
- 标题**中央垂直 60% 安全区**上升为设计铁律（风格库新增"安全区铁律"章节）：标题字与关键主体
  上下各预留 13%+，否则 900×383 中央裁剪会切掉标题。

### 最佳实践整改

- top-ppt-html / topmind-wechat-post 的 SKILL.md `description` 改**第三人称**（降误触发）；
  topmind-cover `description` 同步微调（"一次配齐"→"全流程覆盖"），`triggers` 新增 `缩略图` / `thumbnail`。
- topmind-wechat-post：站外取源坑与回推命令串收敛到 `references/workflow.md`，SKILL.md 只留索引；
  新增跨技能路由索引（封面配图 → topmind-cover，X 长文 → topmind-x-article）；
  二级标题序号由排版层自动生成（不再手写）。
- 各技能 README（中/英）与 SKILL.md 对齐：cover 新增风格库与示例图章节、用法改"步骤 0 选风格"；
  x-article 转换规则补"分隔线→空行"。

### bug 修复

- topmind-x-article `scripts/md2x.py`：`---` / `***` / `___` 分隔线转**空行**（原逻辑误当 frontmatter 吞掉）；
  `***粗斜体***` 先去三重星号再处理 `**` / `__` / `*`，不再残留星号。
- topmind-cover `scripts/crop-cover.py`：移除 `--slug` 悬空参数
  （用法与文档统一：`crop-cover.py <主图> --out-dir <包>/images/`）。

## [0.2.0] - 2026-09-29

### 新增三个写作/配图技能

- **topmind-wechat-post `0.1.0`**：公众号文章全生命周期技能（由 topmind-wechat 适配改名）。
  交付包 / 审校改写 / 质量三关（事实·逻辑·去 AI 味 ≥85）/ 状态同步 / 微信内联排版（`md2wechat --embed-images`）/ 发布清单。
  适配点：frontmatter 去 topmind-pack 专有键（`degradation`/`action_category`/`entrypoint`），
  跨 skill 引用改为通用表述，`writing-quality.md` 改用技能自带 `scan_ai_flavor.py`
  （原引用本机 `~/.workbuddy` 路径），`md2wechat.py` 缺失输入改干净报错（原 Traceback）。
- **topmind-x-article `0.1.0`**：X 长文一键发布。`md2x.py` 把 Markdown 转可直接粘贴进
  X Article 编辑器的纯文本（标题→纯文本行、加粗/斜体去标记、链接→`文字（url）`、
  图片→`[图N]`+文末配图清单、表格→"项：值"列表）；`references/publish-checklist.md`
  沉淀实战经验（首评置顶补信息、图序核对、发布后抓回核对）。缺失输入干净报错。
- **topmind-cover `0.1.0`**：文章封面配图，X / 公众号共用。设计铁律（震撼·醒目·主题突出：
  一图一主题、大标题 ≤10 字、四周 8% 留白）+ 5 套风格模板；
  `crop-cover.py` 从 16:9 主图中央裁出公众号 900×383 版（X 用 1200×675），落盘命名规范。
  缺失输入 / 非图片干净报错。
- 每个新技能带轻量 CI 门禁：`package_skill.py --check`（frontmatter/版本/引用完整性/禁用文件）、
  `audit_skill.py` / `audit_docs.py` / `audit_styles.py` / `audit_css.py`、`negative_tests.py`
  （异常输入不崩溃）。`ci_privacy_scan.py` 全仓通过。

## [0.1.19] - 2026-09-28

### 排版修复 · 大纲篇章化 · 参考资料去假 · 图标真导出 · PPTX 高保真增强

> 源起：2026-09-28 用户复盘五类问题（顶栏重叠 / 卡片不齐 / 大纲罗列页标题 / 参考资料占位 / PPTX 格式错乱），并要求「业界怎么解决的，不要闭门造车」。本次对照 Slidev `pptx-editable` / PptxGenJS / think-cell 混合通道模式系统整改。

#### A. HTML 排版硬伤
- **顶栏副标题压住右侧工具钮**：`.brand__txt` 此前无基础样式，flex `min-width:auto` 钉死整行文字宽，省略号永不触发。补 `min-width:0; overflow:hidden`，`.brand` / `.bar__in` / `.nav` 收缩链修复；≤1360px 自动收起副标题。
- **卡片高度不一致**：`.card` 改 flex 列 + 底对齐；`.g-quad` / `.g-half` / `.g-*--equal` 强制等高；`.g-half` 提升进 `engine.css` 并改 `align-items:stretch`（此前 research 专属且 `start` 违反「同构同高」契约）；纯卡片栅格不再误用 `.a-start`。

#### B. 大纲 = 章节大纲（3–7 章），不是页目录
- **结构契约**：`agenda` 条目 = 章（篇/section），每章 1+ 页；页标题逐页出现，章标题只在 Agenda 出现一次。预算 3–7 章（含参考资料 +1 仍 ≤8）。
- **生成器**：`render_from_model` / `scaffold_report` 按 eyebrow `NN ·` 章前缀归并，删掉「agenda 条数 ≠ 页数就按页强制重建」逻辑；锚点落该章第一页。
- **schema / 阈值**：`model-schema` 加 `agendaMax=7` / `agendaHint`；`layout-constants.contentQuality.agenda` 加 `chapterMin/Max`；`agendaComfortMax` 16→8。
- **文档**：`content-rules` §Agenda 重写；`SKILL` 铁律 4；`components-atoms` / `failure-modes` F20 / `layout-grammar` 阈值同步。
- **样张**：showcase 大纲 12 条页标题 → 9 章（`05 · 图表工艺` 下 3 页只占 1 条）。

#### C. 参考资料只列真实来源（宁缺毋假）
- **冒烟枪**：`render_from_model.py:738` 对每个 `[n]` 生成 `「来源名称，时间；口径。」`；scaffold 写「来源 N（替换为真实来源名称）」。
- **新规则**：只列 `model.refs` 真实来源；**无真实来源整节省略**（连导航 `#refs` 入口一并摘掉，避免悬空锚点）。硬拦占位串（`来源名称` / `替换为真实来源` / `某行业报告`）。
- **模板**：三份模式模板参考节改为注释掉的真实样例 + 「无真实来源则删整节」说明；`example.com` 假条目清除。
- **文档**：`content-rules` §五 规则 4 重写；`SKILL` 铁律 10；`layouts-research` / `.ref-link` 示例改真实机构名。

#### D. 图标真导出（SVG→PNG，不再用 accent 方块替代）
- **新模块**：`scripts/icon_lib.js`（20 语义图标单源）· `scripts/build_icon_assets.js`（sharp 栅格化）· `scripts/icon-assets.json`（PNG 缓存，gitignore）· `scripts/icon_raster.js`。
- **链路**：模型 `cards[].icon` / HTML `data-icon` → `extract_model` 回填 → `build_pptx` 嵌 PNG。`objectName: icon:*`，`validate_pptx` 单独计数 `icon_pictures`，**不进** `pictures=0` 内容图门禁。缺 sharp/资产回落 accent 方块。
- **schema**：`cards[].icon` 字段 + 取值说明（`icon_lib.js` 键）。

#### E. PPTX 高保真增强（对照业界混合通道）
- **发射前叠印断言**：`assertNoOverlap` / `rectsOverlap` 在 `addShape` 前自检组合布局（图表∩inline 数据表等），计入 `OVERLAP_PREEMIT`。
- **表格行高自适应**：`addTable` 超容量压到 hardFloor / 整体缩放；表头独立 `headRowH`；`fit:'shrink'`。
- **`regionOf('bar')` 双偏移纠正**：`chartX/chartW` 此前被当偏移再加 `mx`，柱图右移 0.6in 与标题/表格不齐——改与 donut/table/hbar 同口径对齐版心。双引擎同步。
- **图例收进图高**：waffle / marimekko / slope 图例带含在 `h` 内，与 inline 数据表留间隙（几何铁律②）。
- **文本自动收缩**：标题 / 卡片 / 结论条 / 页脚统一 `fit:'shrink'`（PowerPoint 字体度量 ≠ 浏览器）。

#### F. 文档与工程
- `icons.md` / `pptx-export.md` / `high-fidelity.md`（新增「已落地的高保真增强」对照表）/ `failure-modes` F20 / `tech-design`（图标单源登记）/ `package_skill`（三模块进必收）。
- 业界调研纪要：`docs/industry-pptx-research.md`（Slidev pptx-editable / PptxGenJS / think-cell / Marp / reveal.js 路线对比与取舍）。

#### 回归
- 技能审计 ✓ · 文档审计 ✓ · 研究 HTML 94/0/0 ✓ · 展示 HTML 85/2/0 ✓ · 两份 PPTX `errors:[] warnings:[]` ✓ · 打包校验 106 文件 ✓。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none、结论条无「So what」标签、无左侧 accent 装饰轨、双单源 + sync_runtime、strict 0/0 交付。

## [0.1.18] - 2026-09-28

### PPTX 导出质量整改 · 双通道几何收敛 + 门禁盲区补齐

> 源起：2026-09-28 研究报告双通道交付复盘（HTML/PPTX），PPTX 有 4 类硬伤（含两处大面积文字叠印）、HTML 有 4 类空间利用问题、门禁全绿而效果不合格。本次按六类根因（R1–R7）系统整改。

#### A. 几何叠印硬伤（R1/R2 · PPTX 导出）
- **架构节点标题/注解叠印**：注解改为钳制在标题下边（原底对齐 `y=lh-0.5` 在 `lh≈0.59` 时与标题完全重合）；节点高不足降级单框混排。双引擎同步。
- **verdict/soWhat 同槽叠印**：共用 annotation 结论条槽位——渲染器互斥（verdict 优先）、`extract_model` WARN、`model-schema` 加 `mutualExclusionHint`。HTML 同步去重。
- **图例压来源行**：图例改落图区底部（`bodyBottom-0.28`），禁 `PH-0.62` 固定偏移。
- **`sec.note` 压 so-what 带**：`note` 与 `footnote` 合并到 `footnoteY=6.72`，禁用 `note.y=6.55` 绘制。
- **图表类目标签越出图区**：标签带含在图高 `h` 内（原画到 `y+h` 外）。
- **图片底边侵入注释带**：有图注时下界收到 `contentBottomWithNote`。

#### B. 列宽 / 槽位几何（R3）
- **三栏只占半幅（栏宽 1.69in）**：`regionOf('twocol')` 单栏宽被当总宽——改用版心全宽推导。双引擎同步。
- **KPI 支撑指标铺满整页**：A 通道 `regOf('kpi','metrics')` 缺分支——补 dividerX 右侧分栏。
- **halftable 图表越过 so-what**：`regOf('halftable')` 忽略 opts.top/bottom——传导 opts。

#### C. Agenda 分页与列序统一（R4）
- >8 条自动双列（列优先）；**>12 条自动分页**（Agenda I/II）；长标题截断全称沉 notes（`titleMaxChars=36`）。双引擎 + HTML 同步。

#### D. 门禁盲区补齐（R6）
- **新增 `ELEMENT_OVERLAP`**（元素两两重叠 ≥0.05in²）与 **`LAYOUT_FILL`**（版心填充率 <55%）。
- **Agenda 容量契约**：条数 ≤16、标题 ≤36 字、>8 条须双列。
- **图表还原度分级**（`charts.fidelityMap`）：low = area/radar/treemap/sankey/streamgraph/marimekko/boxplot/network；决策树标注 + 改判建议。
- **跨通道一致性**（`cross_verify`）：Agenda 阅读顺序、图片数量、图表数据标签。

#### E. 图标与图片正确使用
- **图标**：`render_from_model` 内置语义图标库 + `card_head()`；PPTX 保持 accent 方块路标。
- **图片**：`r_image` 支持真图渲染、占位同串、`fit=contain`、多图版式（grid/compare/wall）。

#### 文档同步
- `page-type-matrix` 容量契约 + 还原度；`failure-modes` F19/F20；`pptx-export` 几何铁律；`chart-decision-tree` 还原度列；`content-rules` / `components-atoms` / `modes` / `layouts-combo` 契约更新。
- Pages 源同步：`docs/showcase.html` / `docs/style-gallery.html` 与技能侧 assets 副本逐字节一致（meta → v0.1.18）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none、结论条无「So what」标签、无左侧 accent 装饰轨、大纲 >8 → 2col。

## [0.1.17] - 2026-09-26

### Release
- Republish of the **0.1.16 craft** (结论条去左轨 · anti-AI-flavor · Showcase 全页刷新). npm registry left `0.1.16` in a staged/conflict state (`E409 previously staged`); content identical to the `v0.1.16` GitHub Release / docs Pages source.

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none、结论条无「So what」标签、无左侧 accent 装饰轨。

## [0.1.16] - 2026-09-26

### Craft · 结论条去 AI 味：取消左侧 accent 装饰轨

#### 设计决策（硬原则）
- **结论条无 left rail**：用户明确拒绝结论条左侧色条为 AI-flavored chrome。`.sowhat` / PPTX `soWhatBar()` 改为 **MD3 tonal surface 满铺**（`accent-soft` + 细描边）+ 舒适字阶 / `line-height:1.65` / 内边距 `--sp-5`/`--sp-6`；**禁止**竖色条、霓虹边、装饰 chip 当强调。
- 写入 `design-system` §去 AI 味、`content-rules`、`components-atoms`、`SKILL`、`layout-constants.aiFlavor.visual.forbidConclusionLeftRail`。
- 同类收口 `.note` 同步去掉左轨，改 tonal 细描边；`.flagbar`（待核实）保留细强调（功能态，非结论装饰）。

#### 深度同步
- 引擎：`engine.css` · `build_pptx.js` · `pptx-export.js` · `style-gallery` 预览条。
- 样张 / 模板 / `docs/showcase.html`：全量 `sync_runtime`；Showcase 全页刷新（修 s1「要点一/二」占位 → 三主张卡；s2/s4 补结论条；「so-what」用户文案 →「结论条」；meta → v0.1.16）。
- 截图：`docs/showcase/topmind-showcase/*` + `assets/showcase/*` + theme-overview 重截。
- 版本对齐 **0.1.16**（根 + 技能 package / SKILL / README / PUBLISHING / CHANGELOG）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none、结论条无「So what」标签、大纲 >8 → 2col。

## [0.1.15] - 2026-09-26

### Release
- Republish of the **0.1.14 craft overhaul** (MD3 结论条 · 一屏/大纲自适应 · 克制图标). npm registry left `0.1.14` in a staged/conflict state (`E409 previously staged`); content identical to the `v0.1.14` GitHub Release / docs Pages source.

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none。

## [0.1.14] - 2026-09-26

### Craft overhaul · 三支柱：结论条 · 一屏高度/大纲自适应 · 克制图标

#### A. MD3 结论条（原 so-what）
- `.sowhat` 升为 MD3 tonal 衬条（`accent-soft` 底 + 左 4px accent 轨 + `--fw-title` / `fs-h3`）；**默认不显示「So what / SO WHAT」标签**（可选 `.sowhat--labeled`）。
- 与上方主内容呼吸间距 `clamp(28px,3.6vh,48px)`；`:has(>.sowhat)` 时 wrap 纵向 flex，结论条 `flex:none` 防挤压。
- CSS 迁入公共 `engine.css`（三模式共享）；research 模板去掉重复规则。
- PPTX `soWhatBar()` 双通道只画衬底+左轨+正文；`chartBottom` 相对 `soWhatY` 让位 0.12→0.20in。
- 门禁：`EXHIBIT_PAGE_MISSING_SOWHAT` 改检测结论条形状；文案「结论条」。

#### B. 一页一屏 · 大纲自适应
- 高度契约：`section.band` 一屏；主内容不得溢出或压进结论条/注释带；放不下走 `overflowRule`（重构→拆页→换形态→有限缩字），禁静默截断。
- 大纲：**>8 条须 `.agenda--2col`（两列/两排）**；>16 拆篇。阈值入 `contentQuality.agenda`；`validate_report` 只认 `<ol class="…agenda--2col">`（修 CSS 选择器误伤假通过）。
- Showcase 12 条大纲改双列；`layout-grammar` / `components-atoms` / SKILL 同步。

#### C. 图标原则（行业共识 · 非装饰）
- `icons.md` 增补 wayfinding / 同家族 / 有限密度 / 四正当位置 / 禁区（Agenda·表·图内）；Mode A 内容页必做。
- Showcase / 黄金样张落地 `card__ico` / `ul--ico`；`validate_report` 对「≥2 卡且无 `.card__ico`」发 WARN。

#### 发布
- 样张、模板、references、README、PUBLISHING、截图同步；版本对齐 **0.1.14**。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none。

## [0.1.13] - 2026-09-26

### Changed
- Restored the spacious sparse cream/navy/gold banner (1280×360) with the install command as the bordered subtitle: `npx @topmindspace/tms-skills install top-ppt-html`.
- Restored the third-row product line: **TopMindspace Agent Skills · 让 idea 飞 · 正式场合演示文稿**.
- Aligned whole-repo package, skill metadata, and documentation versions to **0.1.13**.

## [0.1.12] - 2026-09-26

### Changed
- Regenerated `docs/assets/tms-skills-banner.png` (1280×360): includes core skill name **top-ppt-html**, formal keynote / presentation stage intent, tagline HTML + PPT.

## 0.1.11 — 2026-09-26

### Positioning · README slim · showcase narrative

- **差异化定位**：根 README / 技能 README（中英）开篇写清——市面 PPT 技能很多，为何还要 top-ppt-html；特色 **HTML + PPT 双交付**；为**演示报告 / 正式商务演示**而生；参考 **MD3** 信息密度与克制；日常 HTML 等同幻灯片，需要时再导出高保真可编辑 PPTX。
- **主题总览只留一张**：默认 `theme-overview.png`（演示·business-blue）；caption 链到 style-gallery / 研究·架构总览路径；正文不再三张并排占屏（落地页同步精简）。
- **Showcase 叙事**：改写「为什么是我们」与「双交付」两页；subtitle / meta → v0.1.11；版本折线含 0.1.11；`validate_report --strict` **0/0**（5 种图表保持）。
- **截图**：刷新 `docs/showcase/topmind-showcase/*` 与 `top-ppt-html/assets/showcase/`（含 positioning / charts / toolbar）。
- **SKILL.md**：开篇与 description 产品句对齐定位；等量删减冗余，体积仍 ≤13KB。
- **Live**：`docs/showcase.html` / Pages 源与 github.io `tms-skills/` 同步本版。
- 版本对齐 **0.1.11**（根 + 技能 package/lock / SKILL metadata / README / PUBLISHING）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none。

## 0.1.10 — 2026-09-26

### Showcase · header toolbar docs · bilingual README

- **产品 Showcase 加厚**：`2026-09-26-topmind-tms-skills-showcase` 扩为 Mode A · 12 内容页；**5 种图表**（`bar` / `donut` / `line` / `waterfall` / `hbar`）经 `render_from_model` + `hydrate_charts` 回填；含 **Header 工具栏专页**（控件 × 快捷键 × 行为表）；`validate_report --strict` **0/0**。
- **Header 工具栏文档**：`SKILL.md` 交付物表（T/P/H/F/B + 9 风格 + Esc/翻页 + `REPORT_MODEL` 同步）；根 README / 技能 README（中英）显著说明。
- **双语 README**：保持 **`README.md` = 中文默认**；新增 **`README.en.md`** 全量英文平行；`top-ppt-html/README.en.md` 用户向摘要；文首互链。
- **截图**：刷新 `docs/showcase/topmind-showcase/*` 与 `top-ppt-html/assets/showcase/`（含 `showcase-toolbar.png`）。
- **维护工具**：新增 `scripts/hydrate_charts.py`（核心图类型占位 SVG → 模型数据绘形，供样张重建）。
- **Live**：`docs/showcase.html` / Pages 源与 github.io `tms-skills/` 同步本版 showcase。
- 版本对齐 **0.1.10**（根 + 技能 package/lock / SKILL metadata / README / PUBLISHING）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版、motion=none。

## 0.1.9 — 2026-09-26

### Docs · banner · theme overview · live showcase

- **主题总览大图**：根 README + `top-ppt-html/README.md` 嵌入三张 Gate 0 `theme-overview*.png`（演示 / 研究 / 架构），保留风格封面与 showcase 样张画廊。
- **Slim banner**：`docs/assets/tms-skills-banner.png` 裁为 **1280×360**；README 展示宽约 960。
- **Badge 行**：对齐 topmind 风格（Release / npm / CI / License）。
- **Live 链接**：指向 `https://topmindspace.github.io/tms-skills/`（落地页 / showcase.html / style-gallery.html）。
- **Pages 源**：`docs/index.html` + `docs/showcase.html` + `docs/style-gallery.html` + `docs/site-assets/`（启用 GitHub Pages → Deploy from branch `main` / `/docs` 即可上线同路径 URL）。
- 模板 / runtime：经 `sync_runtime.py` 校验，无「甲板」；`REPORT_MODEL` 与引擎 SHA 一致。
- 版本对齐 **0.1.9**（根 + 技能 package/lock / SKILL metadata / README / PUBLISHING）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版。

## 0.1.8 — 2026-09-26

### Showcase · docs · release polish

- **产品 Showcase**：新增 Mode A 样张 `top-ppt-html/assets/examples/2026-09-26-topmind-tms-skills-showcase.html`（+ model）——介绍 TopMind / tms-skills / top-ppt-html（三模式·风格主题·质量门禁·Fast Mode）；`validate_report --strict` 与 `smoke_pptx` **0/0**。
- **截图**：刷新 `theme-overview*.png`；新增 `docs/showcase/`（showcase 全页 + 三黄金样张关键页）与精简 `top-ppt-html/assets/showcase/`（进技能包，供 README）。
- **README 吸引力**：根 README + 技能 README 增加 banner、风格/模式画廊、showcase 链接与安装钉版本 **0.1.8**。
- **Banner**：`docs/assets/tms-skills-banner.png`。
- **打包**：`package_skill` 纳入 `assets/showcase/*`；examples 最小数量仍 ≥3（黄金样张 + 可选 showcase）。
- **文档清理**：用户向 README 对齐当前产品面；PUBLISHING 版本线 → 0.1.8；`build_examples` 说明允许 showcase 并存。
- 版本对齐 **0.1.8**（根 + 技能 package/lock / SKILL metadata / README）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语、整仓 npm 发版。

## 0.1.7 — 2026-09-26

### top-ppt-html · defect opt (D8/D9/D11/D13)

- **P0 D8**：`chartBottom(hasSoWhat, hasFootnote)` 不再 footnote 短路；`Math.min(soWhatY, footnoteY, contentBottomWithNote)` 与 flagY 让位同口径。双通道（`build_pptx.js` / `pptx-export.js`）对齐；flagBar 在 withNote 时底边不越过 `contentBottomWithNote`；Agenda 预留 0.25in 避免 severe 误伤。
- **P0 D9**：`annotation_band_overlap_check` 报告页内**全部**侵入者（去掉首条即 `break`）。
- **P1 D11**：有 so-what 时 `band_top = soWhatY`（6.05），捕获 (6.05, 6.40] 侵入；crush = 自带顶之上压下；注释自形状/窄 accent 条豁免保留。
- **P1 D13**：`ci_skill_gates.sh --with-pptx` 必跑 `smoke_pptx` × business-blue **与** research-mckinsey（覆盖 soWhat+footnote）；graphite-dark 可选。
- **CHROME_DRIFT**：页码只认 `N / M`，不再把年份/Exhibit 编号当页脚（research-mckinsey 假阳性清除）。
- **Fast Mode / 效率**：演讲/汇报线索→Mode A；明确跳过 vs 仍须（质检红线不降）；L0+L1 / `extract_snippet` 纪律不变。
- **门禁**：`test_feedback_gates` 锁定 D8/D9/D11/CHROME；research-mckinsey `--strict` **0/0**。
- 版本对齐 **0.1.7**（根 + 技能 package / SKILL metadata / README / PUBLISHING）。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁、中文「演示文稿」术语保持。

## 0.1.6 — 2026-09-25

### CI / Release 硬化
- **根因 A**：`validate_pptx` 的 `ANNOTATION_BAND_OVERLAP` 把全幅背景（底边 7.50in）误判为侵入注释带；改为排除 full-bleed 背景 / 全高装饰条 / chrome 区，同时保留对图例/主图压进 so-what 带的真阳性。
- **根因 A′**：`FONT_SIZE_NOT_SNAPPED` 未收录 `modeTypeScale` 的 **h2=17pt**；改为从 typeScale ∪ 全模式 modeTypeScale ∪ ladder 动态取允许集。
- **冒烟可读性**：`smoke_pptx.sh` 可靠传播 validate 退出码；失败时 stderr 先打错误码/页码短摘要。
- **根因 B**：Release `npm publish` 遇已发布/已 staged 的 **E409** 时改为 exit 0（幂等）；GitHub Release + 资产仍成功。
- **DRY**：`scripts/ci_skill_gates.sh` 为 CI/Release 共用门禁；Release 对齐 CI 的 fixture + `smoke_pptx`；CI concurrency cancel-in-progress；npm cache；python-pptx 仅 PPTX 步骤安装。
- 文档：新增 `docs/ci.md`；版本对齐 **0.1.6**。

### 红线未动
反截断、图表多样性地板、Mode A craft、runtime SHA 同版本门禁保持。

## 0.1.5 — 2026-09-25

### top-ppt-html · defect close-out

- **P0 D1**：环图右栏可见标题去掉作者约束「禁止叠在弧上」→ 读者向「构成明细」。
- **P0 D2**：`sync_runtime.py` 注入 `/* __TOPPPT_RUNTIME_SHA__:<16hex> */`（源 = `assets/pptx-export.js`）；`validate_report` 缺戳/漂移 FAIL；负例 N19。
- **P1 D3**：`cross_verify.NUMERIC_TOKEN` 增补 YB|ZB|EB|PB 与 kWh|Gbps。
- **P1 D4**：CI 轻量生成 `dist/regression` 样张 + `python-pptx`，使 N4/N5/N7 真正跑通（非全量 regression）。
- **P2**：package-lock 对齐 0.1.5；README/PUBLISHING 2.x 弃用改为事实陈述；`deprecate-npm-2x.sh` 精简为 `@2.x` one-shot + verify；双版本口径（包 semver vs schema `0.1`）写入 SKILL/tech-design。
- **术语**：全库「甲板」→ 演示文稿/样页等（保留英文 trigger `deck`）。

### Installer

- `@topmindspace/tms-skills` → **0.1.5**（整仓同 tag）。

## 0.1.4 — 2026-09-25

### top-ppt-html · craft + quality + docs + perf close-out

- **P0 效率 / agent 工作流**（usage-feedback）：
  - 默认交付 **仅 B 通道 PPTX**（`build_pptx.js`）；A 通道（`pptx-export.js` / `gen_channel_a.js`）限预览与 `cross_verify` / 回归。
  - `extract_snippet` 强制 + **整读大 L2 = FAIL / 不合格**（SKILL + playbook）；`audit_skill` 新增对应门禁。
  - `quality_gate` 对互不依赖子进程（HTML strict / PPTX strict / evals）**并行**执行。
  - Fast / 轻量路径强化 **HTML-first**；PPTX 显式 opt-in（用户要 PPT 或交付含 PPTX）。
  - **未削弱**红线：反截断、图表多样性（`minTypes.presentation=4` / registry）、Mode A 大气正式工艺、Gate 0 语义。
- **质量 / 规范**：对齐 SKILL frontmatter、双 `package.json`、README 钉版本、PUBLISHING、安装说明；跑通 check / audit / feedback gates。
- **docs 工艺改写**：定位强调优雅·美观·大气·演讲/正式场合；版式/排版/色彩/内容组织 + 质检与高保真导出；L0 仍瘦、L2 按需。
- **此前 #7（validator / engine）**：`shape_bounds` 读 `p:xfrm`、`TEXT_OVERFLOW_VERTICAL`、`ANNOTATION_BAND_OVERLAP`、`FONT_SIZE_NOT_SNAPPED`、多系列 vbar、streamgraph 图例内收、image caption `capYImg`——随本版一并发布。

### Installer

- `@topmindspace/tms-skills` → **0.1.4**（整仓同 tag）。

### Intentional leftovers

- 不引入 Claude-only `when_to_use` / 跨端风险 `allowed-tools`（同 0.1.3）。
- `skills-ref validate` 仍为可选，非发布硬依赖。
- layout-constants / model-schema 事实源版本线仍为 `0.1`（patch 记在 package / metadata）。

## 0.1.3 — 2026-09-24

### top-ppt-html · QA close-out + docs

- **P2-4 playbook 拆表**：意图→页型穷举 → `references/page-type-matrix.md`；图表决策表+七种误用 → `references/chart-decision-tree.md`。playbook 保留 Mode 契约 / V1–V4 / 组合 / **图表多样性摘要** / **反截断** / 路径·命令·L2 路由（体积 22KB→~17KB）。
- **版本对齐**：根 README / 技能 README / PUBLISHING / `metadata.version` / 双 `package.json` → **0.1.3**（消除残留 0.1.0 横幅）。
- **IMAGE_CAPTION**：配图页亦认 so-what/lead/figcaption；新增 WARN `IMAGE_NEAR_EMPTY`（近图过空）。
- **P2-2/P2-3**：不引入 Claude-only `when_to_use`、不写跨端风险 `allowed-tools`（`skills-ref validate` 已通过开放标准字段；扩展字段留给宿主实验）。
- **P2-5**：可选 `npx skills-ref@0.1.5 validate ./top-ppt-html`（不作为发布硬依赖；主门禁仍 `audit_skill`）。
- **docs**：根 README 安装表/钉版本/`@0.1.3`；技能 README 改为人类维护指南并指向 SKILL；package REQUIRED + MIN refs ≥25。

### Installer

- `@topmindspace/tms-skills` → **0.1.3**（整仓同 tag）。

### 此前 Unreleased（agent-compat，随 0.1.3 一并发布）

- **P0-1 Trigger eval**：`evals/trigger-queries.json` + `scripts/check_triggers.py`；`package_skill.py --check` 门禁。
- **P0-2 Mode A 读预算诚实**：L0+L1=2；Mode A/Fast 可加 L1.5（`default-surface` + `presentation-craft`）。
- **P0-3 反过读**：禁止整读清单 + 强制 `extract_snippet.py`。
- **P1 Frontmatter / 安装路径 / Fast 最小大纲 / 插画 brief**：license·compatibility·metadata；Cursor/Codex 路径；`illustration-layout.md`；`agents/openai.yaml`。


## 0.1.2 — 2026-09-24

### top-ppt-html · P2 cleanup（advanced 按需 · Mode A 次级骨架 · icons 压缩）

- **Advanced charts 按需**：默认读面 = `charts-discipline` + 核图 8；`charts-extended.md` **禁止预读**，仅意图命中 `extract_snippet.py --chart`。`charts.variety.preferCoreFirst` + validate WARN（A/B）；advanced **计入** `minTypes`（不降 `presentation=4`，不缩 registry）。
- **Mode A 骨架分层**：主力 P1–P4+P6/P10；次级 P7–P9/P11–P12（`layoutSystem.modeSkels` + layout-grammar / default-surface / recommend_layout 同口径）；画廊侧重主力。
- **icons.md 压缩**：语义表 + 禁区 + 尺寸档 + 高频 20 SVG（~8.7KB）；完整枚举 → `docs/archive/refs/icons-catalog.md`；package 仍 REQUIRED。
- **docs 对齐**：SKILL / playbook / presentation-craft / modes / charts 门面同步；Fast Mode + 长文溢出序保持不变。

### Installer

- 安装器 `@topmindspace/tms-skills` → **0.1.2**（随技能包内容更新）。



### top-ppt-html · Long-text / Quality round（反截断 + 门禁加深）

- **反截断政策**：Mode A / content-rules / presentation-craft「长文与信息承载」——溢出顺序固定为 重构→拆页/分章→换形态→有限 fontShrink；**禁止**静默截断 / 砍 so-what / 为疏朗删实质。单页字数改预警（presentation char 1800），不为「字多」单独 FAIL。
- **结构引导取代硬砍刀**：列表/卡片 `maxItemChars` 等改为引导 + prefer；checklist 同步。
- **layout-qa 加深**：`LAYOUT_QA_TRUNCATION` / `OVERFLOW_NO_SPLIT` / `HALF_EMPTY` / `ALIGN_RHYTHM`；presentation `--strict` 仍自动 layout-qa。负例 L4–L6。
- **recommend_layout**：高容量意图 → 多页序列（议程→主张→证据卡→明细），禁一页塞爆。
- **P1-3 charts facade**：纪律优先 → 核图 8 → extended 按需；**不降** `minTypes.presentation=4`。
- **P1-4 会场字号**：pptx-export venue 表（小会议室 / 默认 / 礼堂）。
- **P1-6 chrome**：跨页页脚 y 漂移 `CHROME_DRIFT` WARN + 文档说明。

### top-ppt-html · Presentation Craft（Mode A 工艺）

- **P0-1 图表多样性（用户明确保留）**：**不降** `minTypes.presentation`（仍为 **4**）；registry/advanced 图种保留。纪律改为「按内容选型拉开多样」+ 禁反模式（简单全幅 / 极偏 donut / 为过门禁硬上冷门图）；playbook §五 / layout-qa 同步。
- **P0-2 default-surface**：升为 Mode A / Fast 演示主读面（12 页型 + 8 核图 + V1–V4；P5–P12/advanced 按需）；SKILL L2 索引指向。
- **P0-3 layout-qa 默认**：`validate_report --strict` 在 presentation 下自动 `--layout-qa`；`quality_gate` 同口径；B/C 不强制。
- **P0-4 主张标题**：Mode A action/claim title（禁话题标签）写入 content-rules / modes；校验 WARN。
- **P0-5 `presentation-craft.md`**：中英术语一页纸清单（one idea / 3s / whitespace / CRAP / motion=none / WCAG…）；package REQUIRED。
- **P1**：fillTarget A 58–75% + intentional whitespace 豁免；`recommend_layout` 偏 V1–V4、降 donut 默认权重；Fast 路演/汇报/发布/演讲/demo→A；motion=none 铁律短句。

### top-ppt-html · Batch 3（瘦身）

- **归档 L2**：`industry-benchmark.md` / `design-system-engine.md` → `docs/archive/refs/`（生成路径不读）。
- **layoutSlots 单源**：删除 `scripts/layout_slots.json`；`lib_layout_regions.js` / `sync_runtime.py` 只读 `layout-constants.layoutSlots`。
- **示例**：`assets/examples/` 仅留 3 份黄金样张（每模式 1）；其余 → `docs/archive/examples/`；`build_examples.py` 瘦身为自检（全量脚本归档）。
- **主题 PNG**：`theme-overview*.png` 量化压缩约 −70%。
- **default-surface.md**：12 页型 + 8 图 + V1–V4 速查；playbook §五标注默认 8 核心图。
- **package**：MIN refs ≥20、examples ≥3；`recommend_layout.py` 入 REQUIRED；README 缩为安装+命令索引。

### top-ppt-html · Batch 2（布局选型 + layout-qa + PPTX 对齐）

- **recommend_layout.py**：`--mode A|B|C` + `--intent` / `--from-model` / `--stdin` → `{pageType,skel,chart,rationale,v?}`（V1–V4 / 极偏禁 donut / sizeByComplexity）。
- **validate_report.py --layout-qa**：缺 data-skel、连续同骨架、极偏 donut、演示简单全幅、V 契约；negative_tests 增 L1–L3。
- **cross_verify.py** 默认 SKIP，`--full-ab` 才跑；regression 同口径。
- **build_pptx.js** 尊重 `layoutPreset`（缺省由 pageToPreset 回填，写入备注）。
- **smoke_pptx.sh** + CI skill-gates 冒烟：extract_model → build_pptx → validate_pptx --strict。

# Changelog

## Unreleased

### top-ppt-html 0.1.1 — Batch 1（工作流单写 · Fast Mode）

- **模型单写统一**：playbook / SKILL / pptx-export 命令链均为 scaffold → 只填 `REPORT_MODEL` → `render_from_model --inplace` → `validate_report --strict`（禁 HTML/模型双写）。
- **`render_from_model.py` 纳入 package REQUIRED**；references 最小篇数注释对齐实有数量（≥24）。
- **Fast Mode**：触发词跳过 Gate 0 + 六项；默认 B/mckinsey/light 等；标准路径仍为硬门禁；`audit_skill` 适配豁免声明。
- **归档** `references/reform-plan.md` → `docs/archive/reform-plan.md`；硬门禁改指 `qualityGates` + `failure-modes`。
- 技能 `package.json` 版本对齐仓库叙事 `0.1.1`（LC 仍为 `0.1`）。

## 0.1.1 — 2026-09-24

### Fixes (P0 / P1)

- **Release 顺序与稳健性**：Privacy → 技能门禁 → Package → Collect → GitHub Release → **npm publish（已发布则跳过，避免 E409）** → 再 Prune。
- **Prune 策略**：只删旧 GitHub Release（保留 2 个）；**不再删除 git tags**。
- **多技能发现**：`scripts/discover_skills.js` + CI/Release 动态打包/门禁；`npm run sync:files` 同步 `package.json` `files`。
- **CLI**：校验 skill id；目标目录已存在时须 `--force`；文档口径与 README 对齐（npm 推荐 / GitHub 跟 HEAD）。
- **python3**：根与技能 `package.json`、workflows 统一 `python3`。
- **打包门禁**：`references/layout-grammar.md` 纳入 REQUIRED；去掉与 `theme-overview.png` 完全重复的 `theme-overview-presentation.png`。
- **Lockfile**：提交 `top-ppt-html/package-lock.json`；CI 优先 `npm ci --omit=dev`。
- **npm 2.x**：文档警告勿装 `^2`；提供 `scripts/deprecate-npm-2x.sh`（须维护者本地 npm 登录后执行）。

## 0.1.0 — 2026-09-24

首个公开版本。

### 安装

```bash
npx @topmindspace/tms-skills install top-ppt-html
# 或
npx github:topmindspace/tms-skills install top-ppt-html
```

### 包含

- 技能 **top-ppt-html**（品牌 TopPPT HTML）：单文件 HTML 报告 + 可编辑 16:9 PPTX
- 安装器 CLI **tms-skills**（`list` / `install`）
- 双通道分发：npm 钉版本 / GitHub 跟 HEAD
- tag 发版自动：GitHub Release + npm publish；**Release 只保留最近 2 个**

### 版本策略

- 安装器 `@topmindspace/tms-skills` 与技能 `top-ppt-html` **各自独立**按 semver 演进
- 默认 **patch / minor**；**major 仅用于**技能 id、CLI、注入标记等破坏性变更
- 改代码 ≠ 发 npm：必须 bump 版本并打 tag（或手工 publish）
