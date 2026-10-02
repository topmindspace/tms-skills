---
name: topmind-wechat-post
version: 0.2.5
description: "管一篇公众号文章从选题/底稿到发布的完整生命周期：交付包搭建、审校改写、质量三关（事实/逻辑/去AI味）、状态同步、微信内联排版与发布清单。Use when 写公众号、公众号排版、公众号定稿、发公众号。Do NOT use for 只改错别字、小红书/知乎、纯网页发布。"
action_category: write
triggers:
  - 公众号
  - 微信排版
  - 公众号排版
  - 公众号稿
  - 排版这篇文章
  - 定稿
  - 发公众号
  - 公众号交付
  - wechat
  - mp format
triggers_cn:
  - 写公众号文章
  - 公众号排版定稿
  - 公众号发布清单
author: TopMindspace
license: MIT
homepage: https://github.com/topmindspace/topmind-writing-skills#readme
updated: 2026-09-29
---

# topmind-wechat-post · 公众号创作技能

**公众号专用写作技能**。管一篇公众号文章从选题/底稿到发布清单的完整生命周期。

```
选题/底稿 → 创作 → 质量三关 → 定稿(状态+目录) → 排版 → 发布清单 →（可选）回推 notes
```

> 用户明确说公众号 / 微信排版时进本技能；通用长文写作不在本技能范围内。

## 语言铁律

- **默认中文**：标题、正文、配图文案一律用中文写作，这是默认行为，不需要用户每次声明。
- **英文是例外**：只有用户**明确说**"写英文文章"时才用英文。用户消息里夹杂英文词、
  给英文参考素材、引用英文原文，都不算"要求写英文"。
- 引用英文一手素材（官方公告、模型卡、论文标题）时保留英文原文，正文主体仍是中文，
  必要时在旁给中文翻译。

## 脚本（真源）

| 脚本 | 用途 |
|------|------|
| `scripts/new-article.py` | 建交付包（骨架稿 + frontmatter + images/diagrams） |
| `scripts/sync-status.py` | 状态 ⇄ 目录名 ⇄ 字数（草稿 / 定稿 / 已发布） |
| `scripts/sync-mapping.py` | 映射一致性（frontmatter + 目录 + 可选 notes + topic 总表） |
| `scripts/push-to-topstream.py` | 可选回推：公众号稿降级为纯 Markdown notes |
| `scripts/lint-wechat.py` | 排版体检 + 自动修复（中英文间距、段长、AI 腔…） |
| `scripts/md2wechat.py` | Markdown → 全内联 HTML；**必加 `--embed-images`** |
| `scripts/scan_ai_flavor.py` | 中文去 AI 味扫描（与 `qu-aiwei-zh` 同源） |

```bash
# 路径解析：CLI --base/--workspace → env TOPMIND_WECHAT_BASE / TOPMIND_WORKSPACE / TOPSTREAM_ROOT → 惯例
export TOPMIND_WORKSPACE=/path/to/workspace   # 推荐
python3 scripts/new-article.py --slug demo --title "标题" --direction reverse
python3 scripts/lint-wechat.py --input <包>/公众号稿.md --fix
python3 scripts/scan_ai_flavor.py <包>/公众号稿.md          # 目标 ≥85
python3 scripts/md2wechat.py --input <包>/公众号稿.md --out-dir <包> --slug demo \
  --asset-root <素材根> --embed-images
python3 scripts/sync-status.py --set 定稿 <包> --apply
```

细节见 [`references/workflow.md`](references/workflow.md) · [`references/known-pits.md`](references/known-pits.md)。

## 路径默认

| 用途 | 解析 |
|------|------|
| 交付包根 | `--base` → `TOPMIND_WECHAT_BASE` → `{ws}/40-创作/2026-公众号` 或 `{ws}/20-专题/2026-公众号` |
| 工作区 | `TOPMIND_WORKSPACE` |
| 底稿/回推 | `--topstream` → `TOPSTREAM_ROOT` → 可选；不存在则跳过 notes 校验 |
| 终稿交付 | 可 `save-output` 拷贝到 role:delivery（`88-交付/`），包仍留在创作类专题 |

## 三条路径

### forward（底稿 → 公众号）

```
底稿 notes/*.md → 审校改写 → 质量三关 → 定稿 → 排版 → 发布
```

`new-article.py --direction forward --source-file notes/xxx.md`

### reverse（选题原创）

```
选题包 → 调研素材 → 多轮改稿 → 三关 → 定稿 → 排版 → 发布 →（可选）push-to-topstream
```

`new-article.py --direction reverse`（`target_file: pending`）

### 站外拉取（转载整合 / 在线精选站）

源不在本工作区、也不在 topstream `notes/` 时，**仍落 `reverse` + `target_file: pending`**。  
**不要用 `forward`**：它要求 `source_file` 以 `notes/` 开头且文件真实存在，站外源必然过不了 `sync-mapping.py`。

```bash
python3 scripts/new-article.py --slug <中文短名> --title "<标题>" --direction reverse
```

取源坑（RSC 载荷、图片 hash 映射、`md5` 去重、截图裁切）见 `references/workflow.md`「站外拉取取源注意」；差异与口径写进包内 `README.md`。

**回推纪律**：notes 保持纯 Markdown（`:::` 容器 / 徽章 / `==高亮==` 只进公众号稿）；回推**务必带 `--assets`**（否则 GitHub 上 `images/` 死链）。命令串见 `references/workflow.md`「收尾」。

## 交付包与状态

```text
YYYY-MM-DD-<中文短名>            # 草稿
YYYY-MM-DD-<中文短名>-released   # 定稿 / 已发布
├── 公众号稿.md                  # 唯一改稿入口
├── <slug>-公众号版.html         # 浏览器打开 → 复制正文 → 粘贴后台
├── 图片上传清单.md
├── images/  diagrams/
└── README.md                    # 包说明（可选）
```

**frontmatter（映射真源）**

```yaml
status: 草稿            # 草稿 | 定稿 | 已发布
direction: reverse      # forward | reverse
source_file: ""         # forward 填 notes/xxx.md
target_file: pending    # reverse：pending | notes/xxx.md
word_count: 0           # 纯中文字数，sync-status 维护
```

**交付铁律**：发布/分享时直接用交付包里的 HTML 原文件原样呈现，
不临时重新生成版本；`公众号稿.md` 是唯一改稿入口，改稿后重建 HTML 再交付。

状态与目录名**不要手改**：

```bash
python3 scripts/sync-status.py --set 定稿 <包> --apply
```

## 质量三关（定稿前必过）

### 关 1 · 事实

- 承重数字回**一手来源**；厂商口径 / 据报道 分开写  
- 查不到一手来源的传闻**删**  
- 改稿续写：正文已有数字**回源重核**（上一轮文本最不可信）  
- 多口径（主轮/复跑）显式拆开；表格从数据源生成，禁止手抄  
- 外部工具改过的稿：**先核数字再动文字**；「比值对但绝对值错」= 全段重核  

### 关 2 · 逻辑

- 单边结论旁配反方证据  
- 结构前后一致；同一事实多处同值  

### 关 3 · 文字（去 AI 味）

```bash
python3 scripts/scan_ai_flavor.py <包>/公众号稿.md   # ≥85（人话）
```

- 删套话/黑话/工程圈行话；降调段末加粗金句  
- **满分 ≠ 有人味**：再查「段末金句癖 / 节奏过分整齐 / 没有场景与我 / 报告体标注」  
- **口语化 ≠ 有人味**：删社交垫词（元叙述、空转过渡、姿态句）  
- 判据：**这句话删掉之后，读者少知道了什么？**  

详见 [`references/writing-quality.md`](references/writing-quality.md)。

## 排版要点（写稿时）

- 开头 150 字内钩子；单段 ≤110 字；列表项 ≤70 字  
- 二级标题不手写序号（排版层自动生成）；容器：`::: stat|pull|note|tip|warn|danger|dialogue`  
- **`::: stat` 内必须是 `数值 | 说明` 管道行**，否则静默丢弃  
- 评测稿：**图承担数据，正文只解读**；健康密度 **300–450 字/图**  
- 个股用词红线：禁用 买入/推荐/目标价…；文末投资声明  

更多：[`references/typography-rules.md`](references/typography-rules.md) · [`references/wechat-constraints.md`](references/wechat-constraints.md)。

## 排版与导出（必读）

```bash
python3 scripts/md2wechat.py \
  --input <包>/公众号稿.md --out-dir <包> --slug <slug> \
  --asset-root <素材根> --embed-images \
  [--theme assets/themes/minimal-ink.json]
```

1. **永远 `--embed-images`**，否则粘贴丢图（相对路径被序列化成 file://）  
2. **图片 basename 铁律**：正文引用名 = `images/` 目标名；禁止两套同名图共处  
3. 合规自检出现 `✗` 改生成器，不要手改 HTML  
4. **配图位置铁律**（2026-10-01 九月全景教训）：图片必须紧跟它证明的那段文字
   （最多隔一段）；改稿移动段落时图片行一起搬。构建后必跑：嵌入图数量=文档图数量、
   嵌入图顺序=文档出现顺序（逐张解码与源文件比对）；每张图前后 6 行做主题关键词
   邻近检查，不通过则人工核对。
5. **双版一致性校验**（2026-10-01 九月全景教训 B）：同一选题出 X 版后，
   必跑 X 内嵌图序列 vs 公众号内嵌图序列的逐字节/逐像素比对（X 去掉封面后应完全一致）。
   X 侧图片顺序必须用 `--images-from 公众号稿.md` 派生，禁止手工拼 `--images`
   （曾因文件名排序 ≠ 文档顺序，导致 X 版从第六节起整段配图错位）。

坑清单：[`references/known-pits.md`](references/known-pits.md)。

## 主题

| 文件 | 风格 | 适用 |
|------|------|------|
| `assets/themes/md3-business-blue.json`（默认） | MD3 商务蓝：Material Design 3 设计语言，大圆角，tonal 配色 | 通用 / 商务 / AI 技术 |
| `assets/themes/minimal-ink.json` | 黑白灰 + 砖红 | 深度研析 / 观点 / 随笔 |
| `assets/themes/tech-blue.json` | 科技蓝 | AI/技术 |
| `assets/themes/newsprint.json` | 报纸衬线 | 人文评论 |
| `assets/themes/graphite.json` | 石墨克制 | 严肃报告 |
| `assets/themes/amber-review.json` | 琥珀评测 | 产品评测 |

`md2wechat.py --list-themes` 看全部；`--theme genre:评测` 可按题材自动选。  
渲染规格见 [`references/element-spec.md`](references/element-spec.md) · 主题映射见 [`references/theme-map.md`](references/theme-map.md)。

**平台红线速查**（详见 [`references/wechat-constraints.md`](references/wechat-constraints.md)）：禁 `div`/`pre`/`h1`/`figure`/`thead`/flex/float/gradient/shadow；表格 `table-layout` 不写 fixed；列数 ≥4 转卡片。

## 与 Desktop「公众号创作」

可视化工作流伴面（若有）：包列表 → 改稿 → 三关 → 预览 → 导出。脚本语义以本技能为准。

## 外部依赖

以下技能**不在本仓库**（一般随用户侧 workbuddy 环境提供）；缺失时对应路由能力不可用，
本仓库脚本（交付包、排版、发布清单等）功能不受影响：

- `humanizer-zh`：中文去 AI 味的保真边界（「只去 AI 味不排版」路径用）。
- `qu-aiwei-zh`：中文去 AI 味扫描定位；本仓库 `scan_ai_flavor.py` 与其同源，
  缺失时可用仓库内脚本替代，扫描定位能力降级。

## When NOT to use

- 只想改几个句子 → 直接编辑  
- 小红书 / 知乎 / 掘金 → 平台约束不同  
- 通用长文交付 → 不在本技能范围
- 封面配图 → `topmind-cover`；X 长文 → `topmind-x-article`
- 只去 AI 味不排版 → 中文走 `humanizer-zh`（先立保真边界）+ `qu-aiwei-zh`（再扫描定位）；英文走 `humanizer`

## 实战沉淀（2026-10-01 九月全景项目）

- **文字精炼原则**：月度盘点类文章，文字只给"看图能看清的简单结论或事实"，
  不发散论述。删掉的典型："9 月没发生的那件事可能是最重要的"（评论腔）、
  "是同一道题的两种解法"（比喻发散）。每段压到 1–2 句，只留时间、主体、数字、来源。
- **第三方客观素材优先**：官方产品截图 > 官方基准图 > 第三方榜单截图 > 自制图表。
  自制图只用于时间线、价格对比、总结盘点。9 月项目新增：OpenAI DevDay 官方
  Codex 四图（CLI/Cloud/Code Review/Security）、DeepSeek Harness 官方图标+
  第三方实测截图。
- **模型信息核实**：Muse Spark、Step 5 Preview 等新模型，分数/价格必须回官方模型卡
  或 Artificial Analysis 原页，不直接采用二手报告数字。榜单文字与榜单截图日期对齐
  （如 AA 9/28 快照），分数不跨期比较。
- **frontmatter 状态诚实**：`status: 定稿` 必须等事实/逻辑/文字三关全过才写，
  构建流水线跑通不等于定稿；`word_count` 用脚本实算，不手填。

## 实战沉淀（2026-10-02 插件化/RSI 项目）

- **论文图直取 arXiv 源包**：`curl https://arxiv.org/e-print/<id>` 拿源包（可能是 tar.gz
  也可能是单 PDF），`tar tzf` 列出 `figures/*.pdf`，`pdftoppm -png -r 150` 转 PNG；
  单 PDF 用 `pdfimages` 提取嵌入图，矢量图则按 caption 定位页码后 `pdftoppm -f N -l N`
  整页渲染再裁剪。每张图打开验一眼再用。
- **配图丰富度是主动挖掘出来的**：不要等"有图就用"。论文图、工具截图、评测原图、
  关键帖子截图都要主动找；X 帖子截图走浏览器任务（DevTools 整页截图下载）。
  有信息量的段落尽量配图，装饰图一律不要。
- **"概要+列表"**：信息密集的节先给一句概要再列表展开；标题问号表示判断未定，
  正文用证据把问号讲透（见 `references/writing-principles.md` 二、5 / 二点五、3 / 一、5）。
- **v2 措辞整改（用户亲手改稿）**："两条帖子，一个判断"→平实描述；"一句话"→"简单来说"/删；
  "从来不是…而是"/"真正的 RSI"→弱化断言（"现在看起来""最关键的可能还是"）；
  "我的判断"→"现在看起来"；"同一份报告"→"报告中 XXX"；"坑"→"挑战"；
  删"弧线很经典"这类读者看不懂的梗。完整清单见
  `references/writing-principles.md` 五。
- **结尾总结插图**：PIL + Noto Sans CJK 直接画（无 rsvg/chromium 时），三段式状态图
  （进行时/未发生）收束全文判断，MD3 蓝配色与正文主题呼应。
- **封面走 topmind-cover**：big-type 巨字宣言风（浅色奶油底+墨黑大字+一处烫金），
  1500×600 主图 + `crop-cover.py` 裁 900×383 公众号版。

## 发文铁律

精炼客观 + 素材优先 + 研究深度，见 [references/writing-principles.md](references/writing-principles.md)。触发本技能时默认执行。
