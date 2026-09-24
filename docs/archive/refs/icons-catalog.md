# 图标库（内联 SVG · currentColor · 随主题变色）

全部 24×24、描边风格（stroke 1.8，圆角线帽），用 `currentColor`，自动继承所在元素颜色。

> **PPTX 通道**：内联 SVG 图标不跨通道导出。PPTX 侧卡片头用 **accent 小方块路标**（与 HTML `.card__ico` 的 accent 底同语义）；要点列表用 accent 实心方块标记（已有）。**不要在模型里期待图标 ID 进 PPT**——路标语义靠 accent 色块 + 标题对齐完成。若某页必须视觉区分类型，用标题前缀（如「数据 ·」「风险 ·」）而不是图标。

## 使用准则（克制而合理 · 先读再用）

**图标是信息的路标，不是装饰。** 该用的地方用好，不该用的地方一个都别放。

### 哪里用（四个正当位置）

| 位置 | 做法 | 效果 |
|------|------|------|
| **卡片头** `.card__ico` | 每张要点卡一个小图标 | 卡片类型一眼可辨，最推荐 |
| **关键列表** `.ul--ico` | 每行行首一个小图标（见 `components.md` 第 7 节） | 清单可扫读，适合 3–5 条的关键列表 |
| **指标卡** `.metric__ico` | 指标卡右上角小图标 | 指标类别区分（规模/效率/质量） |
| **提示条** `.note__ico` | 把 `i` 字母换成真图标 | 结论/警告/信息三类提示 |

### 哪里不用

- **Agenda 大纲**——大编号已是路标，再加图标是噪音
- **表格单元格**——表格靠文字对齐取胜，图标破坏栅格
- **图表内部**——数据系列用色不用图标
- **正文行内**——打断阅读流（引用标记除外）

### 密度与一致性

- **每屏 3–8 个图标**；一屏全是图标 = 新噪音；连续两三屏零图标 = 单调，给要点卡补一个。
- **克制 ≠ 不用**：全文零图标的报告会"没有路标"，可扫读性差——长报告（≥6 页）至少要点卡（`.card__ico`）或关键列表（`.ul--ico`）有一处图标（校验器 WARN 提醒）。**目标：够用即止，不多不少。**
- **research 模式例外**：图标密度减半（每屏 2–4 个）——咨询版式以 Exhibit 图表与论证结构为视觉主角，图标更克制；`.exhibit` 图表框内不放图标。
- **architecture 模式例外**：主图内不放图标（节点短标签已足够）；图标只允许出现在图例区旁（≤2 个）。
- **一套报告只用描边风**（本库全部是），stroke-width 统一 1.8，不混用填充风。
- **尺寸**：`.card__ico` 内 18px；`.ul--ico` 内 17px；`.metric__ico` 20px；行内特殊场景 `width:1em`。
- **对齐**：图标与标题垂直居中（组件类已处理）；自定义时 `display:grid;place-items:center`。

### 颜色

- 不改 `stroke="currentColor"`——颜色由容器决定（`.card__ico` 自动是 accent 底 + accent 图标）。
- 深色收尾章里容器是半透明亮底，图标容器加 `color:var(--text-inv)`。
- spectrum 风格也不给图标单独上色——**彩色只属于数据系列**。

---

## 数据与图表

**数据库**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/></svg>
```

**柱状图**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><rect x="7" y="12" width="3" height="6" rx="1"/><rect x="12" y="8" width="3" height="10" rx="1"/><rect x="17" y="4" width="3" height="14" rx="1"/></svg>
```

**趋势/折线**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/><path d="M15 7h4v4"/></svg>
```

**环形/占比**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21.2 15.9A10 10 0 1 1 8 2.8"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>
```

**表格/网格**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/></svg>
```

**仪表盘/效率**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 15l3.5-5.5"/><path d="M20.2 15a8.5 8.5 0 1 0-16.4 0"/></svg>
```

**漏斗/转化**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16l-6 8v6l-4 2v-8L4 4z"/></svg>
```

---

## 增长与经营

**增长/上升**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 7l-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg>
```

**下降/回落**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 17l-8.5-8.5-5 5L2 7"/><path d="M16 17h6v-6"/></svg>
```

**成本/财务**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/></svg>
```

**目标/靶心**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
```

**奖章/成果**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/></svg>
```

**旗帜/里程碑**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><path d="M4 22v-7"/></svg>
```

**火箭/启动**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>
```

---

## 治理与安全

**盾牌/安全**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
```

**锁/权限**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
```

**钥匙/密钥**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/></svg>
```

**齿轮/引擎**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33h.01a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51h.01a1.65 1.65 0 0 0 1.82-.33l.06.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82v.01a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
```

**天平/合规**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18"/><path d="M5 21h14"/><path d="M7 7l-4 7a4.5 4.5 0 0 0 8 0L7 7z"/><path d="M17 7l-4 7a4.5 4.5 0 0 0 8 0l-4-7z"/><path d="M5 7h14"/></svg>
```

**链接/血缘**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
```

**检查/对勾**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12.5l2.5 2.5L16 9.5"/></svg>
```

**警告**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>
```

**信息**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
```

**眼睛/可视**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/></svg>
```

---

## 组织与流程

**用户/团队**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>
```

**单人/角色**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
```

**架构/层级**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="16" y="16" width="6" height="6" rx="1"/><path d="M12 8v4M5 16v-2a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v2"/></svg>
```

**图层/架构**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
```

**网络/节点**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 10.6 15.4 6.4M8.6 13.4l6.8 4.2"/></svg>
```

**分支/流程**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="8" r="3"/><path d="M6 9v6M18 11a9 9 0 0 1-9 4"/></svg>
```

**循环/飞轮**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-2.64-6.36"/><path d="M21 3v6h-6"/></svg>
```

**刷新/迭代**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/><path d="M3 21v-5h5"/></svg>
```

**拼图/集成**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 7V4a2 2 0 0 0-4 0v3H7a2 2 0 0 0-2 2v3h3a2 2 0 1 1 0 4H5v3a2 2 0 0 0 2 2h3v-3a2 2 0 1 1 4 0v3h3a2 2 0 0 0 2-2v-3h3a2 2 0 0 0 0-4h-3V9a2 2 0 0 0-2-2h-3z"/></svg>
```

---

## 时间与效率

**时钟/时间**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
```

**日历/计划**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
```

**闪电/高效**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8z"/></svg>
```

**罗盘/方向**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
```

---

## 文档与工具

**文档/报告**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>
```

**文件夹/资产**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg>
```

**搜索/洞察**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
```

**扳手/工具**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
```

**灯泡/洞察**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.2 1 2V17h6v-.3c0-.8.4-1.5 1-2A7 7 0 0 0 12 2z"/></svg>
```

**书签/收藏**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
```

**编辑/撰写**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/></svg>
```

---

## 平台与智能

**云/平台**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>
```

**芯片/AI**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>
```

**机器人/Agent**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="8" width="16" height="12" rx="2"/><path d="M12 8V4M8 4h8"/><circle cx="9" cy="14" r="1"/><circle cx="15" cy="14" r="1"/><path d="M9 18h6"/></svg>
```

**筛选/过滤**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 3H2l8 9.46V19l4 2v-8.54L22 3z"/></svg>
```

**加号/新增**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v8M8 12h8"/></svg>
```

**消息/协同**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
```

---

## 图表语义 / 布局 / 待核实

**待核实/待确认**（`.flagbar` / `.tbd-legend` 专用，与"警告"区分：警告=风险，此=待补）
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>
```

**流向 / 桑基**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h5c4 0 4 12 8 12h3"/><path d="M4 18h5c4 0 4-12 8-12h3"/><path d="M17 3l3 3-3 3M17 15l3 3-3 3"/></svg>
```

**斜率 / 升降对比**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5M20 19V5"/><path d="M6 15 18 8"/><path d="M6 11 18 16"/></svg>
```

**哑铃 / 前后对比**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h16"/><circle cx="6" cy="12" r="2.4"/><circle cx="18" cy="12" r="2.4"/></svg>
```

**分布 / 点图**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18"/><circle cx="7" cy="8" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="16" cy="7" r="1.6"/><circle cx="19" cy="15" r="1.6"/></svg>
```

**目标线 / 子弹图**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="8" rx="2"/><path d="M16 5v14"/></svg>
```

**图片 / 素材图**（也是**配图占位** `.media__ph` 的标准图标——占位块统一用这一个）
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.6"/><path d="m4 17 5-5 4 4 3-3 4 4"/></svg>
```
> 占位块内**不要**给 svg 加 `class="f-*"`：`.media__ph svg` 已用 `stroke:var(--accent); fill:none` 随风格/主题自动取色（写成 `fill` 实心会在深色主题下发灰）。

**拼贴 / 布局**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="10" rx="1.5"/><rect x="13" y="3" width="8" height="5" rx="1.5"/><rect x="13" y="10" width="8" height="11" rx="1.5"/><rect x="3" y="15" width="8" height="6" rx="1.5"/></svg>
```

**清单 / 条目**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6h.01M4 12h.01M4 18h.01"/></svg>
```

**构成 / 马赛克**
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="10" height="16" rx="1.5"/><rect x="13" y="4" width="8" height="9" rx="1.5"/><rect x="13" y="13" width="8" height="7" rx="1.5"/></svg>
```

---

## 速查：按语义选图标

| 语义 | 图标 |
|------|------|
| 规模/底座 | 数据库、云、文件夹 |
| 效率/性能 | 仪表盘、闪电、时钟 |
| 增长/成果 | 增长、奖章、火箭、旗帜 |
| 风险/问题 | 警告、下降 |
| 治理/安全 | 盾牌、锁、钥匙、天平 |
| 口径/规则 | 文档、天平、书签 |
| 组织/分工 | 用户、单人、架构 |
| 流程/血缘 | 分支、链接、循环、刷新、流向 |
| 计划/路线 | 日历、罗盘、旗帜 |
| 智能/Agent | 芯片、机器人 |
| 洞察/分析 | 搜索、灯泡、眼睛 |
| 建设/工具 | 扳手、齿轮、拼图 |
| 图表语义 | 柱状图、趋势、环形、表格、分布、斜率、哑铃、构成 |
| 布局/图片 | 拼贴、图片、全幅 |
| 待核实/待补 | 待核实（问号圈） |
| 清单/条目 | 清单 |
