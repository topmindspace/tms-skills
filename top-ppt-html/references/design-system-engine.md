# 设计系统 · 引擎 CSS 实现目录（维护者 / 深挖时读）

> 顶栏 / 卡片 / 列表 / 表格 / 章节头 / 页脚 / Agenda / 动效等**类实现细节**。
> 生成报告请用 `components-atoms.md` / `layouts-*.md` 的写法；本文件对应
> `assets/templates/engine.css` 注入源，改 CSS 后必跑 `sync_runtime.py`。
> **禁止**把本文件当生成时的默认阅读对象。

## 5. 顶栏 + 主题切换

```css
.bar{position:sticky;top:0;z-index:50;height:var(--bar-h);
  background:color-mix(in srgb,var(--bg) 86%,transparent);
  backdrop-filter:saturate(160%) blur(14px);-webkit-backdrop-filter:saturate(160%) blur(14px);
  border-bottom:1px solid var(--border-soft)}
.bar__in{height:100%;display:flex;align-items:center;justify-content:space-between;gap:var(--sp-4)}
.brand{display:flex;align-items:center;gap:var(--sp-3);min-width:0}
.brand__mark{width:34px;height:34px;flex:none;border-radius:10px;background:var(--accent);
  color:var(--accent-on);display:grid;place-items:center;font-size:13px;font-weight:700}
.brand__title{font-size:var(--fs-sm);font-weight:600;color:var(--text);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.brand__sub{font-size:var(--fs-xs);color:var(--text-3);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.nav{display:flex;align-items:center;gap:var(--sp-1)}
.nav a{padding:8px 14px;border-radius:var(--r-full);color:var(--text-2);text-decoration:none;
  font-size:var(--fs-sm);font-weight:500;white-space:nowrap;transition:background-color .18s,color .18s}
.nav a:hover{background:var(--surface-2);color:var(--text)}
@media (max-width:1120px){.nav{display:none}}
.iconbtn{width:40px;height:40px;flex:none;display:grid;place-items:center;
  border:1px solid var(--border);border-radius:var(--r-full);background:transparent;
  color:var(--text-2);cursor:pointer;transition:background-color .18s,color .18s}
.iconbtn:hover{background:var(--surface-2);color:var(--text)}
.iconbtn svg{width:19px;height:19px}
.icon-sun,.icon-moon{display:none}
html[data-theme="light"] .icon-moon{display:block}
html[data-theme="dark"] .icon-sun{display:block}
```

## 6. 卡片 / 按钮 / 徽标 / 指标卡

```css
.card{background:var(--surface);border:1px solid var(--border-soft);border-radius:var(--r-lg);
  padding:clamp(20px,2vw,30px);transition:border-color .2s,box-shadow .2s,background-color .28s}
.card:hover{border-color:var(--border);box-shadow:var(--shadow-1)}
.card--flat{background:var(--surface-1);border-color:transparent}
.card--flat:hover{background:var(--surface-2)}
.card--accent{background:var(--accent-soft);border-color:transparent}
.card__hd{display:flex;align-items:center;gap:var(--sp-3);margin-bottom:var(--sp-3)}
.card__ico{width:34px;height:34px;flex:none;border-radius:10px;background:var(--accent-soft);
  color:var(--accent-text);display:grid;place-items:center}
.card__ico svg{width:18px;height:18px}

.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:48px;
  padding-inline:26px;border-radius:var(--r-full);font-size:var(--fs-sm);font-weight:500;
  text-decoration:none;cursor:pointer;white-space:nowrap;border:1px solid transparent;
  transition:background-color .2s,box-shadow .2s,transform .2s}
.btn:hover{transform:translateY(-1px)}
.btn--primary{background:var(--accent);color:var(--accent-on)}
.btn--primary:hover{box-shadow:var(--shadow-2)}
.btn--soft{background:var(--accent-soft);color:var(--accent-text)}
.btn--ghost{background:transparent;color:var(--text);border-color:var(--border)}
.btn--onDark{background:var(--surface);color:var(--text)}

.chip{display:inline-flex;align-items:center;gap:6px;height:30px;padding-inline:13px;
  border-radius:var(--r-full);background:var(--surface-2);color:var(--text-2);
  font-size:var(--fs-xs);font-weight:500;white-space:nowrap}
.chip--accent{background:var(--accent-soft);color:var(--accent-text)}
.chip--line{background:transparent;border:1px solid var(--border);color:var(--text-2)}

.metric{background:var(--surface);border:1px solid var(--border-soft);border-radius:var(--r-lg);
  padding:clamp(18px,1.7vw,26px);display:flex;flex-direction:column;gap:var(--sp-2)}
.metric:hover{border-color:var(--border);box-shadow:var(--shadow-1)}
.metric__v{display:flex;align-items:baseline;gap:4px;color:var(--text)}
.metric__v small{font-size:.42em;font-weight:500;letter-spacing:0;color:var(--text-3)}
.metric__k{font-size:var(--fs-sm);color:var(--text-2);font-weight:500}
.metric__n{font-size:var(--fs-xs);color:var(--text-3);line-height:1.5}
.metric--warn .metric__v{color:var(--accent)}
```

## 7. 列表（含流程箭头 / 对勾 / 序号）

```css
.ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:var(--sp-4)}
.ul li{position:relative;padding-left:30px;color:var(--text-2);font-size:var(--fs-body);line-height:1.65}
.ul li::before{content:"";position:absolute;left:0;top:.52em;width:7px;height:7px;
  border-radius:50%;background:var(--accent)}
.ul li strong{color:var(--text);font-weight:600}
.ul--flow li::before{content:"→";width:auto;height:auto;background:none;color:var(--accent);
  font-weight:700;top:0;left:0}
.ul--check li::before{width:18px;height:18px;top:.18em;background:var(--accent-soft);
  color:var(--accent-text);content:"✓";font-size:11px;font-weight:700;display:grid;place-items:center}
.ul--num{counter-reset:n}.ul--num li{padding-left:34px;counter-increment:n}
.ul--num li::before{content:counter(n);width:22px;height:22px;top:.06em;border-radius:50%;
  background:var(--accent-soft);color:var(--accent-text);font-size:11px;font-weight:700;
  display:grid;place-items:center}
```

## 8. 表格 / 引言 / 时间线 / 图示

```css
.tbl-wrap{border:1px solid var(--border-soft);border-radius:var(--r-lg);overflow:hidden;
  background:var(--surface);overflow-x:auto}
table{width:100%;border-collapse:collapse;min-width:min(720px,100%)}
thead th{background:var(--surface-1);color:var(--text-2);font-size:var(--fs-xs);font-weight:600;
  letter-spacing:.04em;text-transform:uppercase;text-align:left;padding:15px 20px;
  border-bottom:1px solid var(--border);white-space:nowrap}
tbody td{padding:17px 20px;border-bottom:1px solid var(--border-soft);font-size:var(--fs-sm);
  color:var(--text-2);vertical-align:top;line-height:1.6}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:var(--surface-1)}
td strong{color:var(--text);font-weight:600}
td.k{color:var(--text);font-weight:500;white-space:nowrap}
td.num{font-variant-numeric:tabular-nums}

.note{display:flex;gap:var(--sp-4);padding:clamp(20px,2vw,28px);border-radius:var(--r-lg);
  background:var(--accent-soft);border-left:3px solid var(--accent)}
.note__ico{width:26px;height:26px;flex:none;border-radius:50%;background:var(--accent);
  color:var(--accent-on);display:grid;place-items:center;font-size:13px;font-weight:700;font-style:normal}
.note__t{font-size:var(--fs-h3);font-weight:600;color:var(--text);margin-bottom:6px}

.tl{position:relative;padding-left:30px}
.tl::before{content:"";position:absolute;left:7px;top:10px;bottom:10px;width:2px;
  background:var(--border);border-radius:2px}
.tl__i{position:relative;padding-bottom:var(--sp-6)}
.tl__i:last-child{padding-bottom:0}
.tl__d{position:absolute;left:-30px;top:5px;width:16px;height:16px;border-radius:50%;
  background:var(--surface);border:3px solid var(--border)}
.tl__i--now .tl__d{border-color:var(--accent);background:var(--accent)}
.tl__i--done .tl__d{border-color:var(--accent)}
.tl__t{font-size:var(--fs-h3);font-weight:600;color:var(--text);margin-bottom:6px}
.tl__l{font-size:var(--fs-xs);font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  color:var(--accent-text);margin-bottom:2px}

.fig{background:var(--surface);border:1px solid var(--border-soft);border-radius:var(--r-xl);
  padding:clamp(20px,2.2vw,36px);overflow:hidden}
.fig__cap{text-align:center;margin-bottom:var(--sp-4);font-size:var(--fs-sm);
  color:var(--text-3);font-weight:500}
.fig svg{display:block;width:100%;height:auto}
```

## 10. 章节头 / 页脚 / 动效 / 打印

```css
.shead{margin-bottom:clamp(28px,3.4vh,48px);max-width:940px}
.shead__title{margin-block:var(--sp-3) var(--sp-4)}
.shead__desc{max-width:900px}
.shead--center{margin-inline:auto;text-align:center}
.shead--center .shead__desc{margin-inline:auto}
.band--deep .t-lead,.band--deep .t-body{color:var(--deep-fg-2)}
.band--deep .t-eyebrow{color:color-mix(in srgb,var(--accent) 40%,#fff)}

.foot{padding-block:clamp(40px,5vh,64px);border-top:1px solid var(--border-soft);
  background:var(--surface-1)}
.foot__in{display:flex;align-items:center;justify-content:space-between;gap:var(--sp-5);flex-wrap:wrap}

@media (prefers-reduced-motion:no-preference){.rv{opacity:0;transform:translateY(14px)}
  .rv.in{opacity:1;transform:none;transition:opacity var(--dur-long) var(--ease-emphasized),
    transform var(--dur-long) var(--ease-emphasized)}}
@media (prefers-reduced-motion:reduce){.rv{opacity:1;transform:none}html{scroll-behavior:auto}}
@media print{.rv{opacity:1!important;transform:none!important}
  .band{padding-block:24px;break-inside:avoid}body{background:#fff;color:#000}
  .pager{display:none!important}}
```

## 11. PPT 翻页导航（页码指示）

右侧固定页码圆点 + 计数，点击跳转；方向键翻页由公共 UI 脚本（`assets/templates/ui.js`，注入各模板）驱动。

```css
/* 页码指示（固定右侧） */
.pager{position:fixed;right:clamp(10px,1.6vw,26px);top:50%;transform:translateY(-50%);
  z-index:60;display:flex;flex-direction:column;align-items:center;gap:10px}
.pager__count{font-size:var(--fs-xs);font-weight:600;color:var(--text-3);
  font-variant-numeric:tabular-nums;letter-spacing:.04em}
.pager__dots{display:flex;flex-direction:column;gap:8px}
.pager__dot{width:9px;height:9px;border-radius:50%;border:1px solid var(--border);
  background:transparent;cursor:pointer;padding:0;transition:background-color .2s,transform .2s,border-color .2s}
.pager__dot:hover{transform:scale(1.3);border-color:var(--accent)}
.pager__dot.on{background:var(--accent);border-color:var(--accent);transform:scale(1.25)}
@media (max-width:760px){.pager{right:6px;gap:6px}.pager__dot{width:7px;height:7px}}
@media (prefers-reduced-motion:reduce){.pager__dot{transition:none}}
```

> 结构：`<aside class="pager"><div class="pager__count">3 / 10</div><div class="pager__dots">…每页一个 .pager__dot…</div></aside>`，由脚本生成。

## 12. Agenda 大纲页（第二页）

首页后必须是 Agenda。大编号 + 标题 + 一句话说明，整行可点击跳转。

```css
.agenda{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.agenda__i{border-top:1px solid var(--border-soft)}
.agenda__i:last-child{border-bottom:1px solid var(--border-soft)}
.agenda__a{display:grid;grid-template-columns:auto 1fr auto;align-items:center;
  gap:clamp(16px,2.4vw,36px);padding:clamp(18px,2.2vh,26px) clamp(4px,.6vw,12px);
  text-decoration:none;color:inherit;transition:background-color .18s}
.agenda__a:hover{background:var(--surface-1)}
.agenda__n{font-size:clamp(1.4rem,2vw,1.9rem);font-weight:var(--fw-display);
  color:var(--accent);font-variant-numeric:tabular-nums;line-height:1;min-width:2.2em}
.agenda__t{font-size:var(--fs-h3);font-weight:var(--fw-title);color:var(--text);margin-bottom:3px}
.agenda__d{font-size:var(--fs-sm);color:var(--text-3)}
.agenda__go{color:var(--text-3);transition:color .18s,transform .18s}
.agenda__a:hover .agenda__go{color:var(--accent);transform:translateX(4px)}
.agenda__go svg{width:20px;height:20px;display:block}
```

> 结构：`<ol class="agenda"><li class="agenda__i"><a class="agenda__a" href="#why"><span class="agenda__n">01</span><span><span class="agenda__t">周期意义</span><span class="agenda__d">治理为何进入智能增长周期</span></span><span class="agenda__go">→</span></a></li>…</ol>`

## 13. 图表尺寸与优雅规范

> 丰富但克制：一屏 1–2 个图，图表服务数据，不堆砌。
> 完整图表代码（含漏斗/甘特/散点/瀑布/双向条形/多段环形）见 `components.md` 第二部分；尺寸下限的**硬约束与校验规则**见 `components.md` 第 35 节（校验脚本按 `data-chart` 类型核对）。

| 图表 | 用途 | 建议高度 / 占比 |
|------|------|----------------|
| 环形/仪表盘 | 占比、达成度 | 直径 140–180px，配中心大数字 |
| 柱状图 | 分阶段目标、对比 | 高 200–240px，柱圆角 5–6px |
| 横向条形 / 棒棒糖 | 排名、覆盖率 | 行高 28–34px，条圆角 |
| 折线/面积 | 时间趋势 | 高 200–240px，面积用 `fill-opacity:.12` 的 accent |
| 斜率图 | 两期升降（谁升谁降） | 高 180–220px，两端都标数值 |
| 雷达图 / 玫瑰图 | 多维能力 | 直径 220–260 / 180–220px，≤ 6 维 |
| 堆叠条 / 马赛克图 | 构成（马赛克含规模维度） | 条高 24–32px；马赛克高 160–200px |
| 瀑布图 | 增减归因 | 高 200–230px |
| 漏斗图 / 桑基图 | 转化、流向归因 | 高 200–240px，≤ 5 层 / ≤ 8 带 |
| 甘特图 | 计划排期 | 高 160–200px |
| 散点/气泡 | 双维分布 | 高 220–260px |
| 哑铃图 | 前后 / 两地对比 | 高 160–200px，行高 34–38px |
| 子弹图 | 目标 vs 实际（含区间） | 高 140–180px，行高 32–36px |
| 点图 | 分布 / 离散度 | 高 120–160px，行高 28px |

**通用**：图表标签 `.f-txt3`（弱化），数值 `.f-txt` 加粗（突出）；网格线 `.s-bds` 细线；数据系列用 `f-acc`（强调）+ `f-s3`（次要），多系列时同族明度递减、**不引入第二色相**。图与图之间留白 ≥ `--sp-6`。
**信息量纪律**：系列 >5 合并"其他"；类别 >8 取 Top 7 + 附录密表；时间点 >8 改折线/按季聚合；一屏一图一重心。完整规则见 `components.md` `charts.md` §64。

## 14. 主题切换 + 翻页脚本（与风格无关）

见任一模式模板（`assets/templates/*.html`）底部注入的公共 UI 脚本（源文件 `assets/templates/ui.js`，由 `sync_runtime.py` 注入），含主题切换、滚动显现、方向键翻页、页码指示生成。
