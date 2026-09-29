#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TopPPT HTML · 模型驱动生成 HTML（消灭双写）

用法:
    python scripts/render_from_model.py report.model.json --template research.html --out report.html
    python scripts/render_from_model.py report.html --inplace     # 用内嵌 REPORT_MODEL 重渲染正文区
    python scripts/render_from_model.py report.model.json --body-only > body.html

定位:
    REPORT_MODEL 是内容唯一事实源。本脚本按锁定版式（layout-grammar P1–P12 / scaffold 同源类名）
    从模型字段渲染 HTML 正文——智能体只填模型，不再手写正文与模型两份。
    引擎标记块（__TOPPPT_*__）原样保留；正文区由模型重建。

纪律:
    · 模型字符串字段必须是纯文本（引用写 [n]）；本脚本负责转义
    · 版式类名与 scaffold_report / components 锁定版式一致，禁止临场发明
    · 渲染后必须跑 validate_report --strict
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / 'assets' / 'templates'
LC = json.loads((ROOT / 'scripts' / 'layout-constants.json').read_text(encoding='utf-8'))
PAGE_TO_PRESET = ((LC.get('layoutSystem') or {}).get('pageToPreset') or {})
IMAGE_SPEC = LC.get('imageSpec') or {}

CONTENT_RE = re.compile(
    r'(<!-- __TOPPPT_CONTENT_START__ -->)[\s\S]*?(<!-- __TOPPPT_CONTENT_END__ -->)')
MODEL_RE = re.compile(r'window\.REPORT_MODEL = \{[\s\S]*?\};')


def esc(s) -> str:
    return (str(s or '')
            .replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;'))


def cite(text: str) -> str:
    """模型里 [n] → HTML 上标引用（模型保持纯文本）。"""
    return re.sub(r'\[(\d+)\]',
                  r'<a class="cite" href="#ref-\1">[\1]</a>',
                  esc(text))


def kp(k, v) -> str:
    k, v = esc(k), cite(v) if isinstance(v, str) else esc(v)
    return f'<li><strong>{k}。</strong>{v}</li>' if k else f'<li>{v}</li>'


def open_sec(i: int, ptype: str, extra: str = '') -> str:
    skel = PAGE_TO_PRESET.get(ptype, 'P4')
    return (f'<section class="band" id="s{i}" data-skel="{skel}" '
            f'data-page-type="{ptype}"{extra}>')


def shead(sec: dict) -> str:
    lead = sec.get('lead') or ''
    lead_html = f'\n    <p class="t-lead shead__desc">{cite(lead)}</p>' if lead else ''
    return (f'    <div class="shead rv">\n'
            f'      <div class="t-eyebrow">{esc(sec.get("eyebrow") or "")}</div>\n'
            f'      <h2 class="t-h1 shead__title">{esc(sec.get("title") or "")}</h2>'
            f'{lead_html}\n    </div>')


def sowhat(sec: dict) -> str:
    t = sec.get('soWhat')
    if not t:
        return ''
    return (f'    <div class="sowhat rv"><span class="sowhat__v">{cite(t)}</span></div>\n')


def footnote(sec: dict) -> str:
    t = sec.get('footnote')
    if not t:
        return ''
    return f'    <div class="footnote">{cite(t)}</div>\n'


def flags_block(sec: dict) -> str:
    fl = sec.get('flags') or []
    if not fl:
        return ''
    items = '\n'.join(f'      <li>{cite(x)}</li>' for x in fl)
    return (f'    <div class="flagbar rv"><div class="flagbar__hd">待核实</div>\n'
            f'      <ul>\n{items}\n      </ul>\n    </div>\n')


def wrap(i: int, ptype: str, body: str, sec: dict, extra: str = '') -> str:
    return (f'{open_sec(i, ptype, extra)}\n  <div class="wrap">\n'
            f'{shead(sec)}\n{body}{sowhat(sec)}{footnote(sec)}{flags_block(sec)}'
            f'  </div>\n</section>')


# ── 语义图标库（高频取码 · 与 references/icons.md 同源；PPTX 侧由 accent 方块路标对应）──
_SVG_OPEN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
             'stroke-linecap="round" stroke-linejoin="round">')
ICONS: dict[str, str] = {
    '增长': _SVG_OPEN + '<path d="M22 7l-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg>',
    '下降': _SVG_OPEN + '<path d="M22 17l-8.5-8.5-5 5L2 7"/><path d="M16 17h6v-6"/></svg>',
    '数据': _SVG_OPEN + '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/></svg>',
    '图表': _SVG_OPEN + '<path d="M3 3v18h18"/><rect x="7" y="12" width="3" height="6" rx="1"/><rect x="12" y="8" width="3" height="10" rx="1"/><rect x="17" y="4" width="3" height="14" rx="1"/></svg>',
    '趋势': _SVG_OPEN + '<path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/><path d="M15 7h4v4"/></svg>',
    '占比': _SVG_OPEN + '<path d="M21.2 15.9A10 10 0 1 1 8 2.8"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>',
    '表格': _SVG_OPEN + '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/></svg>',
    '效率': _SVG_OPEN + '<path d="M12 15l3.5-5.5"/><path d="M20.2 15a8.5 8.5 0 1 0-16.4 0"/></svg>',
    '成果': _SVG_OPEN + '<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/></svg>',
    '安全': _SVG_OPEN + '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
    '权限': _SVG_OPEN + '<rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    '检查': _SVG_OPEN + '<circle cx="12" cy="12" r="10"/><path d="M8 12.5l2.5 2.5L16 9.5"/></svg>',
    '风险': _SVG_OPEN + '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>',
    '团队': _SVG_OPEN + '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    '流程': _SVG_OPEN + '<circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 21V9a9 9 0 0 0 9 9"/></svg>',
    '计划': _SVG_OPEN + '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    '智能': _SVG_OPEN + '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6v6H9zM9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>',
    '洞察': _SVG_OPEN + '<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>',
    '工具': _SVG_OPEN + '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    '清单': _SVG_OPEN + '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg>',
}
_ICONS_ORDER = list(ICONS.keys())


def pick_icon(title: str = '', idx: int = 0) -> str:
    """按标题语义挑图标；未命中则按序轮换（保持同屏同家族、不堆砌）。"""
    t = str(title or '')
    for key, svg in ICONS.items():
        if key in t:
            return svg
    return ICONS[_ICONS_ORDER[idx % len(_ICONS_ORDER)]]


def pick_icon_name(title: str = '', idx: int = 0) -> str:
    """图标名（与 icon_lib.js / PPTX 真导出同名）。"""
    t = str(title or '')
    for key in ICONS:
        if key in t:
            return key
    return _ICONS_ORDER[idx % len(_ICONS_ORDER)]


def card_head(title: str, idx: int = 0, icon_name: str | None = None) -> str:
    """卡片头：图标路标 + 标题（与 scaffold 的 .card__hd + .card__ico 同源）。
    icon_name 写入 data-icon，供 extract_model / build_pptx 真导出同名图标。"""
    name = icon_name or pick_icon_name(title, idx)
    return (f'<div class="card__hd"><div class="card__ico" data-icon="{esc(name)}">{pick_icon(title, idx)}</div>'
            f'<h3 class="t-h3">{esc(title)}</h3></div>')


def pts_list(points) -> str:
    if not points:
        return '<ul class="ul"><li>（待填）</li></ul>'
    lis = []
    for p in points:
        if isinstance(p, (list, tuple)) and len(p) >= 2:
            lis.append(kp(p[0], p[1]))
        elif isinstance(p, dict):
            lis.append(kp(p.get('k') or p.get('t') or '', p.get('v') or p.get('d') or ''))
        else:
            lis.append(f'<li>{cite(p)}</li>')
    return '<ul class="ul">' + ''.join(lis) + '</ul>'


def chart_svg(chart: dict, idx: int, force_type: str | None = None) -> str:
    ct = esc(force_type or (chart or {}).get('type') or 'bar')
    return (f'      <svg class="chart" data-chart="{ct}" viewBox="0 0 560 220">\n'
            f'        <!-- 数据以 REPORT_MODEL.chart 为准；复杂图形用 extract_snippet --chart {ct} -->\n'
            f'        <text x="280" y="110" text-anchor="middle" class="f-txt3" font-size="12">'
            f'{ct} · 见模型数据</text>\n'
            f'      </svg>\n')


# ── 页型渲染器（字段 → 锁定版式 HTML）──────────────────────────────────────────
def r_points(i, sec):
    pts = sec.get('points') or []
    half = (len(pts) + 1) // 2 or 1
    col1, col2 = pts[:half], pts[half:]
    def card(title, items, idx=0):
        return (f'      <div class="card">{card_head(title, idx)}\n'
                f'        {pts_list(items)}</div>')
    body = ('    <div class="grid g-2 rv a-start">\n'
            + card('要点一', col1 or pts[:1], 0) + '\n'
            + card('要点二', col2 or [['', '（第二组要点）']], 1) + '\n'
            + '    </div>\n')
    if sec.get('metrics'):
        body += metrics_row(sec['metrics'])
    return wrap(i, 'points', body, sec)


def metrics_row(metrics) -> str:
    cells = []
    for m in (metrics or [])[:6]:
        if isinstance(m, (list, tuple)):
            val, key = m[0], m[1] if len(m) > 1 else ''
            note = m[2] if len(m) > 2 else ''
        else:
            val, key, note = m.get('v') or m.get('value') or '', m.get('k') or '', m.get('n') or ''
        cells.append(
            f'      <div class="metric"><div class="metric__v t-metric">{esc(val)}</div>'
            f'<div class="metric__k">{esc(key)}</div>'
            f'<div class="metric__n">{cite(note)}</div></div>')
    return f'    <div class="grid g-4 rv a-start">\n' + '\n'.join(cells) + '\n    </div>\n'


def r_metrics(i, sec):
    return wrap(i, 'metrics', metrics_row(sec.get('metrics')), sec, ' band--top')


def r_kpi(i, sec):
    hero = sec.get('hero') or []
    val = hero[0] if hero else ''
    lab = hero[1] if len(hero) > 1 else ''
    delta = hero[2] if len(hero) > 2 else ''
    body = (
        '    <div class="grid g-hero rv a-c">\n'
        f'      <div class="stack gap-3"><div class="t-metric" style="color:var(--accent)">{esc(val)}</div>'
        f'<div class="t-h3">{esc(lab)}</div>'
        + (f'<div class="t-sm" style="color:var(--accent);font-weight:600">{esc(delta)}</div>' if delta else '')
        + '</div>\n'
        + '      <div class="grid g-2">\n'
        + pts_list(sec.get('points') or [['支撑', '一句话。']])
        + '\n      </div>\n    </div>\n')
    return wrap(i, 'kpi', body, sec)


def r_table(i, sec):
    tbl = sec.get('table') or {}
    head = tbl.get('head') or []
    rows = tbl.get('rows') or []
    th = ''.join(f'<th>{esc(h)}</th>' for h in head)
    trs = []
    for row in rows:
        tds = ''.join(f'<td>{cite(c)}</td>' for c in row)
        trs.append(f'<tr>{tds}</tr>')
    body = ('    <div class="tbl-wrap rv"><table><thead><tr>' + th +
            '</tr></thead><tbody>' + ''.join(trs) + '</tbody></table></div>\n')
    extra = ' band--flow' if len(rows) > 10 else ''
    return wrap(i, 'table', body, sec, extra)


def r_bar(i, sec):
    ch = sec.get('chart') or {}
    body = (
        '    <div class="grid g-side rv a-start">\n'
        f'      <div class="fig"><div class="fig__cap">{esc(sec.get("title") or "图表")}</div>\n'
        f'{chart_svg(ch, i)}      </div>\n'
        '      <div class="stack gap-4"><h3 class="t-h3">怎么读这张图</h3>\n'
        f'        {pts_list(sec.get("points") or [["结论一", "一句话。"], ["结论二", "一句话。"]])}\n'
        '      </div>\n'
        '    </div>\n')
    return wrap(i, 'bar', body, sec)


def r_donut(i, sec):
    ch = dict(sec.get('chart') or {})
    ch.setdefault('type', 'donut')
    labels, values = ch.get('labels') or [], ch.get('values') or []
    legend = []
    total = sum(float(v or 0) for v in values) or 1
    for lb, v in zip(labels, values):
        pct = float(v or 0) / total * 100
        legend.append(f'        <li><strong>{esc(lb)}。</strong>{esc(v)}（{pct:.0f}%）</li>')
    body = (
        '    <div class="grid g-side rv a-start">\n'
        f'      <div class="fig" style="text-align:center"><div class="fig__cap">构成占比</div>\n'
        f'{chart_svg(ch, i, "donut")}      </div>\n'
        '      <div class="stack gap-4"><h3 class="t-h3">构成明细</h3>\n'
        '        <ul class="ul">' + ''.join(legend) + '</ul>\n'
        '      </div>\n    </div>\n')
    return wrap(i, 'donut', body, sec)


def r_exhibit(i, sec):
    ch = dict(sec.get('chart') or {})
    st = (sec.get('type') or '').lower()
    if st in ('donut', 'bar', 'halftable') and not ch.get('type'):
        ch['type'] = 'donut' if st == 'donut' else 'bar'
    no = sec.get('exhibitNo') or i
    body = (
        '    <div class="grid g-side rv a-start">\n'
        '      <div class="exhibit rv">\n'
        f'        <div class="exhibit__hd"><span class="exhibit__no">Exhibit {esc(no)}</span>'
        f'<span class="exhibit__t">{esc(sec.get("title") or "")}</span></div>\n'
        f'{chart_svg(ch, i)}'
        f'        <div class="exhibit__src">{cite(sec.get("footnote") or "来源：待补")}</div>\n'
        '      </div>\n'
        f'      {pts_list(sec.get("points") or [["结论", "一句话。"]])}\n'
        '    </div>\n')
    sec = dict(sec)
    sec.pop('footnote', None)  # 已进来源行
    return wrap(i, 'exhibit', body, sec)


def r_twocol(i, sec):
    paras = sec.get('paragraphs') or []
    cols = []
    for p in paras:
        if isinstance(p, (list, tuple)) and len(p) >= 2:
            cols.append(f'      <p class="t-body"><strong>{esc(p[0])}。</strong>{cite(p[1])}</p>')
        else:
            cols.append(f'      <p class="t-body">{cite(p)}</p>')
    body = '    <div class="cols-2 rv">\n' + '\n'.join(cols) + '\n    </div>\n'
    return wrap(i, 'twocol', body, sec)


def r_threecol(i, sec):
    paras = sec.get('paragraphs') or []
    cols = []
    for p in paras[:6]:
        if isinstance(p, (list, tuple)) and len(p) >= 2:
            cols.append(f'      <div class="card"><h3 class="t-h3">{esc(p[0])}</h3>'
                        f'<p class="t-body">{cite(p[1])}</p></div>')
        else:
            cols.append(f'      <div class="card"><p class="t-body">{cite(p)}</p></div>')
    # cols-3 供校验「模型页型 ↔ 版式组件」对齐（TYPE_FEATURE.threecol）
    body = ('    <div class="cols-3 grid g-3 rv a-start">\n' + '\n'.join(cols) + '\n    </div>\n')
    return wrap(i, 'threecol', body, sec)


def r_cards(i, sec):
    cards = sec.get('cards') or []
    n = int(sec.get('columns') or min(3, max(1, len(cards))))
    cls = {1: 'g-2', 2: 'g-2', 3: 'g-3', 4: 'g-4'}.get(n, 'g-3')
    # 纯卡片栅格强制等高（g-2--equal / g-3--equal），与 CSS / layout-grammar「同行卡片 stretch」一致
    if cls in ('g-2', 'g-3', 'g-4'):
        cls = cls + '--equal'
    blocks = []
    for ci, cd in enumerate(cards):
        if isinstance(cd, dict):
            title = cd.get('title')
            points = cd.get('points') or []
            icon_name = cd.get('icon')
        elif isinstance(cd, (list, tuple)) and len(cd) > 1:
            title, points, icon_name = cd[0], [['', cd[1]]], None
        else:
            title, points, icon_name = (cd or ''), [], None
        blocks.append(
            f'      <div class="card">{card_head(str(title), ci, icon_name)}\n'
            f'        {pts_list(points)}</div>')
    body = f'    <div class="grid {cls} rv">\n' + '\n'.join(blocks) + '\n    </div>\n'
    return wrap(i, 'cards', body, sec)


def r_split(i, sec):
    def zone(el, side):
        if not el:
            return '      <div></div>'
        t = (el.get('type') or ('points' if el.get('points') else 'bar'))
        if t == 'table':
            return ('      <div class="tbl-wrap"><table><thead><tr>' +
                    ''.join(f'<th>{esc(h)}</th>' for h in (el.get('head') or [])) +
                    '</tr></thead><tbody>' +
                    ''.join('<tr>' + ''.join(f'<td>{cite(c)}</td>' for c in row) + '</tr>'
                            for row in (el.get('rows') or [])) +
                    '</tbody></table></div>')
        if t == 'image':
            im = el.get('image') or {}
            cap = im.get('caption') or ''
            src = im.get('src') or ''
            ph = bool(im.get('placeholder')) or not src
            fit = im.get('fit') or (IMAGE_SPEC or {}).get('fitDefault') or 'cover'
            fig = _media_figure(src, 'half', fit, '', placeholder=ph,
                                ratio_cls=(IMAGE_SPEC or {}).get('ratioCssClass', {}).get('half') or 'media--r4-3')
            return fig + (f'\n      <div class="media__cap--below">{esc(cap)}</div>' if cap else '')
        if t == 'points' or el.get('points') and t not in ('bar', 'line', 'donut', 'hbar'):
            return f'      <div class="stack gap-4">{pts_list(el.get("points"))}</div>'
        return (f'      <div class="fig"><div class="fig__cap">{esc(el.get("cap") or "图表")}</div>\n'
                f'{chart_svg(el, i)}      </div>')
    body = ('    <div class="grid g-side rv a-start">\n'
            f'{zone(sec.get("left"), "L")}\n{zone(sec.get("right"), "R")}\n'
            '    </div>\n')
    return wrap(i, 'split', body, sec)


def r_comparison(i, sec):
    def panel(d, accent=False):
        style = ' style="background:var(--accent-soft);border-color:transparent"' if accent else ''
        tcol = ' style="color:var(--accent)"' if accent else ''
        return (f'      <div class="card"{style}><h3 class="t-h3"{tcol}>{esc((d or {}).get("title") or "")}</h3>\n'
                f'        {pts_list((d or {}).get("points"))}</div>')
    body = ('    <div class="grid g-half g-2 rv a-start">\n'
            + panel(sec.get('left')) + '\n' + panel(sec.get('right'), True) + '\n'
            + '    </div>\n')
    has_verdict = bool(sec.get('verdict'))
    if has_verdict:
        body += (f'    <div class="sowhat rv"><span class="sowhat__v">{cite(sec["verdict"])}</span></div>\n')
    sec = dict(sec)
    sec.pop('verdict', None)
    # R2：verdict 与 soWhat 共用 .sowhat 槽位——verdict 已渲染时移除 soWhat，禁止同槽双条
    if has_verdict:
        sec.pop('soWhat', None)
    return wrap(i, 'comparison', body, sec)


def r_quote(i, sec):
    body = (
        '    <div class="shead shead--center rv">\n'
        f'      <div style="font-size:clamp(40px,4.6vh,56px);font-weight:700;color:var(--accent)">「</div>\n'
        f'      <p class="t-lead" style="max-width:860px;margin-inline:auto;font-weight:600">{cite(sec.get("quote") or "")}</p>\n'
        f'      <p class="t-sm" style="color:var(--accent-text)">—— {esc(sec.get("author") or "")}'
        + (f' · {esc(sec.get("context"))}' if sec.get('context') else '')
        + '</p>\n    </div>\n')
    return wrap(i, 'quote', body, sec, ' band--accent band--fit')


def _img_ph_label(layout: str, multi: bool = False) -> str:
    """占位标签串——与 PPTX imgPlaceholderLabel 同源（imageSpec 常量拼接，cross_verify 逐页比对）。"""
    spec = IMAGE_SPEC or {}
    label = spec.get('placeholderLabel') or '配图占位'
    if multi:
        return label
    size = (spec.get('recommendedSizePx') or {}).get(layout)
    if not size:
        return label
    prefix = spec.get('placeholderHintPrefix') or '建议 '
    suffix = spec.get('placeholderHintSuffix') or 'px'
    return f'{label} · {prefix}{size}{suffix}'


def _media_figure(src: str, layout: str, fit: str, caption: str = '',
                  placeholder: bool = False, multi: bool = False, ratio_cls: str = '') -> str:
    """单张图 / 占位框（与 PPTX addImageEl 同源：比例锁定 + fit + 占位三要素标签）。"""
    spec = IMAGE_SPEC or {}
    ratio_map = spec.get('ratioCssClass') or {}
    rc = ratio_cls or ratio_map.get(layout) or 'media--r3-1'
    fit_cls = ' media--contain' if str(fit or '').lower() == 'contain' else ''
    if placeholder or not src:
        ph_text = _img_ph_label(layout, multi)
        # 与 PPTX 同串：bold=配图占位，span=建议 …px（单串合并输出，保证 A/B 文本一致）
        parts = ph_text.split(' · ', 1)
        b = esc(parts[0])
        span = esc(parts[1]) if len(parts) > 1 else ''
        inner = f'<div class="media__ph"><b>{b}</b><span>{span}</span></div>'
        return f'<figure class="media {rc} media--ph">{inner}</figure>'
    alt = caption or '配图'
    img = f'<img src="{esc(src)}" alt="{esc(alt)}">'
    cap_html = f'<figcaption class="media__cap--below">{cite(caption)}</figcaption>' if caption else ''
    return f'<figure class="media {rc}{fit_cls}">{img}{cap_html}</figure>'


def r_image(i, sec):
    im = sec.get('image') or {}
    layout = (im.get('layout') or 'full').lower()
    fit = im.get('fit') or (IMAGE_SPEC or {}).get('fitDefault') or 'cover'
    cap = im.get('caption') or ''
    items = im.get('items') or []
    multi_layouts = (IMAGE_SPEC or {}).get('multiLayouts') or ['grid', 'compare', 'wall']

    def one(src, placeholder=False, multi=False, ratio_cls=''):
        return _media_figure(src, layout, fit, cap if not multi else '',
                             placeholder=placeholder, multi=multi, ratio_cls=ratio_cls)

    if layout in multi_layouts and items:
        # 多图版式：grid / compare / wall（与 PPTX imageLayoutShapes 同源）
        cells = []
        ratio_map = (IMAGE_SPEC or {}).get('ratioCssClass') or {}
        for it in items[:6]:
            if not isinstance(it, dict):
                it = {'src': str(it)}
            it_src = it.get('src') or ''
            it_ph = bool(it.get('placeholder')) or not it_src
            it_cap = it.get('caption') or ''
            fig = one(it_src, placeholder=it_ph, multi=True,
                      ratio_cls=ratio_map.get(layout) or 'media--r4-3')
            if it_cap:
                fig += f'    <p class="media__src">{cite(it_cap)}</p>\n'
            cells.append(fig)
        n = len(cells)
        if layout == 'compare':
            grid_cls = 'media-compare'
        elif layout == 'wall':
            grid_cls = 'media-wall'
        else:
            grid_cls = f'media-grid media-grid--{min(4, max(2, n))}'
        media = f'    <div class="{grid_cls} rv">\n' + '\n'.join(cells) + '\n    </div>\n'
    else:
        src = im.get('src') or ''
        ph = bool(im.get('placeholder')) or not src
        media = one(src, placeholder=ph)
        if cap:
            media += f'    <p class="media__src">{cite(cap)}</p>\n'
    body = media
    if layout == 'half' and sec.get('points'):
        body = ('    <div class="grid g-side rv a-start">\n' + media +
                f'      <div class="stack gap-4">{pts_list(sec.get("points"))}</div>\n    </div>\n')
    return wrap(i, 'image', body, sec)


def r_diagram(i, sec):
    layers = sec.get('layers') or []
    rows = []
    for li, lay in enumerate(layers):
        name = lay[0] if lay else ''
        nodes = lay[1] if len(lay) > 1 else []
        focus = len(lay) > 2 and lay[2] == 'focus'
        nds = []
        for nd in nodes[:8]:
            if isinstance(nd, dict):
                nds.append(f'          <div class="arch__node"><div class="arch__nt">{esc(nd.get("t") or "")}</div>'
                           f'<div class="arch__nd">{esc(nd.get("d") or "")}</div></div>')
            else:
                nds.append(f'          <div class="arch__node"><div class="arch__nt">{esc(nd)}</div></div>')
        rows.append(
            f'      <div class="arch__layer{" arch__layer--focus" if focus else ""}">\n'
            f'        <div class="arch__lname">{esc(name)}</div>\n'
            f'        <div class="arch__nodes">\n' + '\n'.join(nds) + '\n        </div>\n      </div>')
        if li < len(layers) - 1:
            rows.append('      <div class="arch__conn" aria-hidden="true">'
                        '<svg width="18" height="22" viewBox="0 0 18 22" fill="none" stroke="currentColor" '
                        'stroke-width="2"><path d="M9 2v14"/><path d="M4 12l5 6 5-6"/></svg></div>')
    legend = ''.join(f'<span class="chip">{esc(x)}</span>' for x in (sec.get('legend') or []))
    body = ('    <div class="arch rv">\n' + '\n'.join(rows) + '\n    </div>\n'
            + (f'    <div class="arch__legend">{legend}</div>\n' if legend else ''))
    return wrap(i, 'diagram', body, sec, ' band--fit')


def r_lane(i, sec):
    lanes = sec.get('lanes') or []
    rows = []
    for ln in lanes:
        hd = ln[0] if ln else ''
        steps = ln[1] if len(ln) > 1 else []
        parts = []
        for si, st in enumerate(steps):
            if isinstance(st, dict):
                cls = 'lane__step lane__step--a' if st.get('accent') else 'lane__step'
                parts.append(f'<span class="{cls}">{esc(st.get("t") or "")}</span>')
            else:
                parts.append(f'<span class="lane__step">{esc(st)}</span>')
            if si < len(steps) - 1:
                parts.append('<span class="lane__arr" aria-hidden="true"></span>')
        rows.append(f'      <div class="lane"><div class="lane__hd">{esc(hd)}</div>'
                    f'<div class="lane__body">' + ''.join(parts) + '</div></div>')
    body = '    <div class="stack rv gap-3">\n' + '\n'.join(rows) + '\n    </div>\n'
    return wrap(i, 'lane', body, sec, ' band--fit')


def r_timeline(i, sec):
    items = []
    for ph in (sec.get('phases') or []):
        if isinstance(ph, (list, tuple)):
            lab, name, desc = (list(ph) + ['', '', ''])[:3]
            state = ph[3] if len(ph) > 3 else ''
        else:
            lab, name, desc, state = ph.get('label', ''), ph.get('name', ''), ph.get('d', ''), ph.get('s', '')
        cls = 'tl__i'
        if state == 'done':
            cls += ' tl__i--done'
        elif state == 'now':
            cls += ' tl__i--now'
        items.append(
            f'        <div class="{cls}"><div class="tl__d"></div>'
            f'<div class="tl__l">{esc(lab)}</div><div class="tl__t">{esc(name)}</div>'
            f'<p class="t-body">{cite(desc)}</p></div>')
    body = '    <div class="fig rv"><div class="tl">\n' + '\n'.join(items) + '\n    </div></div>\n'
    return wrap(i, 'timeline', body, sec)


def r_steps(i, sec):
    items = []
    for si, st in enumerate((sec.get('steps') or [])[:6]):
        if isinstance(st, (list, tuple)):
            t, d = (list(st) + ['', ''])[:2]
            acc = False
        else:
            t, d, acc = st.get('t', ''), st.get('d', ''), bool(st.get('accent'))
        cls = 'step step--a' if acc else 'step'
        items.append(f'      <div class="{cls}"><div class="step__n">{si + 1:02d}</div>'
                     f'<div class="step__t">{esc(t)}</div><div class="step__d">{cite(d)}</div></div>')
    body = '    <div class="steps rv">\n' + '\n'.join(items) + '\n    </div>\n'
    return wrap(i, 'steps', body, sec)


def r_heatmap(i, sec):
    rows, cols, cells = sec.get('rowHeads') or [], sec.get('colHeads') or [], sec.get('cells') or []
    body = f'    <div class="heat rv" style="--heat-cols:{max(1, len(cols))}"><div class="heat__grid">\n'
    body += '      <div></div>' + ''.join(f'<div class="heat__h">{esc(c)}</div>' for c in cols) + '\n'
    for ri, rh in enumerate(rows):
        body += f'      <div class="heat__rh">{esc(rh)}</div>'
        row = cells[ri] if ri < len(cells) else []
        for ci in range(len(cols)):
            v = row[ci] if ci < len(row) else ''
            body += f'<div class="heat__c">{esc(v)}</div>'
        body += '\n'
    body += '    </div></div>\n'
    return wrap(i, 'heatmap', body, sec)


def r_bullet(i, sec):
    items = sec.get('items') or []
    rows = []
    for it in items:
        if isinstance(it, (list, tuple)):
            k, a, t = (list(it) + ['', 0, 0])[:3]
        else:
            k, a, t = it.get('k', ''), it.get('a', 0), it.get('t', 0)
        mx = float(sec.get('max') or 100) or 100
        fw = max(0, min(100, float(a or 0) / mx * 100))
        tw = max(0, min(100, float(t or 0) / mx * 100))
        rows.append(
            f'      <div class="bul__row"><div class="bul__k">{esc(k)}</div>'
            f'<div class="bul__track"><div class="bul__fill" style="width:{fw}%"></div>'
            f'<div class="bul__tgt" style="left:{tw}%"></div></div>'
            f'<div class="bul__v"><b>{esc(a)}</b> / {esc(t)}</div></div>')
    body = '    <div class="bul rv">\n' + '\n'.join(rows) + '\n    </div>\n'
    return wrap(i, 'bullet', body, sec)


def r_pyramid(i, sec):
    levels = sec.get('levels') or []
    n = max(1, len(levels))
    rows = []
    for i2, lv in enumerate(levels):
        if isinstance(lv, (list, tuple)):
            t, d = (list(lv) + ['', ''])[:2]
        else:
            t, d = lv.get('t', ''), lv.get('d', '')
        w = 40 + int(60 * (i2 + 1) / n)
        rows.append(f'      <div class="pyr__lvl" style="--w:{w}%">'
                    f'<div class="pyr__t">{esc(t)}</div><div class="pyr__d">{cite(d)}</div></div>')
    body = '    <div class="pyr rv">\n' + '\n'.join(rows) + '\n    </div>\n'
    return wrap(i, 'pyramid', body, sec)


def r_halftable(i, sec):
    """半表半图：g-half 左表右图（校验 TYPE_FEATURE.halftable）。"""
    tbl = sec.get('table') or {}
    ch = sec.get('chart') or {}
    head = tbl.get('head') or []
    rows = tbl.get('rows') or []
    th = ''.join(f'<th>{esc(h)}</th>' for h in head)
    trs = ''.join('<tr>' + ''.join(f'<td>{cite(c)}</td>' for c in row) + '</tr>' for row in rows)
    body = (
        '    <div class="grid g-half g-2 rv a-start">\n'
        f'      <div class="tbl-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>\n'
        f'      <div class="fig"><div class="fig__cap">{esc(ch.get("cap") or "互证图")}</div>\n'
        f'{chart_svg(ch, i)}      </div>\n'
        '    </div>\n')
    return wrap(i, 'halftable', body, sec)


def r_matrix(i, sec):
    rows, cols, cells = sec.get('rowHeads') or [], sec.get('colHeads') or [], sec.get('cells') or []
    body = f'    <div class="matrix heat rv" style="--heat-cols:{max(1, len(cols))}"><div class="heat__grid">\n'
    body += '      <div></div>' + ''.join(f'<div class="heat__h">{esc(c)}</div>' for c in cols) + '\n'
    for ri, rh in enumerate(rows):
        body += f'      <div class="heat__rh">{esc(rh)}</div>'
        row = cells[ri] if ri < len(cells) else []
        for ci in range(len(cols)):
            v = row[ci] if ci < len(row) else ''
            if isinstance(v, dict):
                v = v.get('t') or v.get('v') or ''
            body += f'<div class="heat__c">{esc(v)}</div>'
        body += '\n'
    body += '    </div></div>\n'
    return wrap(i, 'matrix', body, sec)


def r_info(i, sec):
    t = sec.get('type') or 'sankey'
    body = (f'    <div class="fig rv"><div class="fig__cap">{esc(t)} 信息图</div>\n'
            f'      <svg class="chart" data-chart="{esc(t)}" viewBox="0 0 900 400">\n'
            f'        <text x="450" y="200" text-anchor="middle" class="f-txt3">{esc(t)} · 按 infographics 规格绘制</text>\n'
            f'      </svg>\n    </div>\n')
    return wrap(i, t, body, sec)


RENDERERS = {
    'points': r_points, 'metrics': r_metrics, 'kpi': r_kpi, 'table': r_table,
    'bar': r_bar, 'donut': r_donut, 'exhibit': r_exhibit, 'twocol': r_twocol,
    'threecol': r_threecol, 'cards': r_cards, 'split': r_split, 'comparison': r_comparison,
    'quote': r_quote, 'image': r_image, 'diagram': r_diagram, 'lane': r_lane,
    'timeline': r_timeline, 'steps': r_steps, 'heatmap': r_heatmap, 'bullet': r_bullet,
    'pyramid': r_pyramid, 'halftable': r_halftable, 'matrix': r_matrix,
    'sankey': r_info, 'treemap': r_info, 'boxplot': r_info, 'network': r_info,
    'marimekko': r_info, 'streamgraph': r_info,
}


def render_body(model: dict) -> str:
    parts = []
    # 封面
    parts.append(f'''<!-- 封面 -->
<section class="band band--fit" id="cover">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">{esc(model.get("meta") or "")}</div>
      <h1 class="t-display shead__title">{esc(model.get("title") or "")}</h1>
      <p class="t-lead shead__desc">{esc(model.get("subtitle") or "")}</p>
    </div>
  </div>
</section>''')
    agenda = model.get('agenda') or []
    secs = [s for s in (model.get('sections') or []) if isinstance(s, dict)]

    def _chapter_key(sec, idx):
        """从 eyebrow 的 `NN ·` 前缀或 chapter 字段取章键；无则退回页码。"""
        ch = sec.get('chapter')
        if ch not in (None, ''):
            return str(ch)
        eb = (sec.get('eyebrow') or '').strip()
        m = re.match(r'^(\d{1,2})\s*[·・\-—]', eb)
        if m:
            return m.group(1).zfill(2)
        return f'{idx:02d}'

    def _chapter_title(sec):
        """章标题 = eyebrow 去掉 `NN ·` 前缀；无则退回页标题。"""
        eb = (sec.get('eyebrow') or '').strip()
        m = re.match(r'^\d{1,2}\s*[·・\-—]\s*(.+)$', eb)
        if m and m.group(1).strip():
            return m.group(1).strip()
        return sec.get('title') or ''

    # Agenda = 章节大纲（3–7 章），不是逐页标题罗列。
    # 模型给了合法 agenda（≤8 条）就原样用；否则按 eyebrow 章前缀归并，而不是按页重建。
    MAX_CH = 8
    if not agenda or len(agenda) > MAX_CH or len(agenda) == len(secs) and len(secs) > MAX_CH:
        chapters = {}
        order = []
        for i, s in enumerate(secs, 1):
            key = _chapter_key(s, i)
            if key not in chapters:
                chapters[key] = {'num': key, 'title': _chapter_title(s), 'desc': (s.get('eyebrow') or ''),
                                 'first': i, 'pages': 0}
                order.append(key)
            chapters[key]['pages'] += 1
        model['agenda'] = [[c['num'], c['title'], c['desc']] for c in (chapters[k] for k in order)]
        agenda = model['agenda']
        chapter_first = {c['num']: c['first'] for c in (chapters[k] for k in order)}
    else:
        # 模型 agenda 已是章级：锚点落到该章第一页（按 eyebrow 对齐）
        chapter_first = {}
        for i, s in enumerate(secs, 1):
            key = _chapter_key(s, i)
            chapter_first.setdefault(key, i)
            # 同时用序号兜底
            chapter_first.setdefault(f'{i:02d}', i)
        for gi, ag in enumerate(agenda, 1):
            if isinstance(ag, (list, tuple)) and ag:
                num = str(ag[0]).zfill(2) if str(ag[0]).isdigit() else str(ag[0])
                chapter_first.setdefault(num, gi)

    if agenda or not (model.get('mode') == 'architecture' and len(secs) <= 4):
        lis = []
        for gi, ag in enumerate(agenda, 1):
            num = ag[0] if isinstance(ag, (list, tuple)) and ag else f'{gi:02d}'
            title = ag[1] if isinstance(ag, (list, tuple)) and len(ag) > 1 else ''
            desc = ag[2] if isinstance(ag, (list, tuple)) and len(ag) > 2 else ''
            href_i = chapter_first.get(str(num).zfill(2)) or chapter_first.get(str(num)) or gi
            lis.append(
                f'      <li class="agenda__i"><a class="agenda__a" href="#s{href_i}">'
                f'<span class="agenda__n">{esc(num)}</span>'
                f'<span><span class="agenda__t">{esc(title)}</span>'
                f'<div class="agenda__d">{esc(desc)}</div></span></a></li>')
        parts.append(f'''<section class="band band--top" id="agenda">
  <div class="wrap">
    <div class="shead rv"><div class="t-eyebrow">目录</div>
      <h2 class="t-h1 shead__title">报告大纲</h2></div>
    <ol class="agenda rv">{''.join(lis)}</ol>
  </div>
</section>''')
    ex_n = 0
    for i, sec in enumerate(secs, 1):
        t = (sec.get('type') or 'points').lower()
        is_research_exhibit = (model.get('mode') == 'research'
                               and t in ('exhibit', 'bar', 'halftable', 'donut'))
        if is_research_exhibit:
            ex_n += 1
            sec = dict(sec)
            sec['exhibitNo'] = ex_n
        fn = RENDERERS.get(t, r_points)
        if is_research_exhibit:
            fn = r_exhibit
        try:
            parts.append(fn(i, sec))
        except Exception as e:
            parts.append(wrap(i, t, f'    <p class="t-body">渲染失败 {esc(e)}</p>', sec))
    closing = model.get('closing') or {}
    cpts = closing.get('points') or []
    body = '    <div class="grid g-3 rv a-start">\n' + pts_list(cpts) + '\n    </div>\n'
    parts.append(f'''<section class="band band--accent" id="closing">
  <div class="wrap">
    <div class="shead rv"><div class="t-eyebrow">下一步</div>
      <h2 class="t-h1 shead__title">{esc(closing.get("title") or "收尾")}</h2></div>
{body}  </div>
</section>''')
    # 参考资料：只列模型给的真实来源；无真实来源整节省略（禁止占位条目）
    refs_src = model.get('refs') or model.get('references') or []
    real_refs = []
    for r in refs_src:
        if isinstance(r, dict):
            name = (r.get('name') or r.get('title') or '').strip()
            time_ = (r.get('time') or r.get('date') or '').strip()
            caliber = (r.get('caliber') or r.get('note') or '').strip()
            url = (r.get('url') or r.get('link') or '').strip()
        elif isinstance(r, (list, tuple)) and r:
            name = str(r[0]).strip() if r[0] else ''
            time_ = str(r[1]).strip() if len(r) > 1 and r[1] else ''
            caliber = str(r[2]).strip() if len(r) > 2 and r[2] else ''
            url = str(r[3]).strip() if len(r) > 3 and r[3] else ''
        else:
            name = str(r or '').strip()
            time_ = caliber = url = ''
        # 拦占位串：宁缺毋假
        if not name or any(p in name for p in ('来源名称', '替换为真实来源', '来源 N', '某行业报告')):
            continue
        if time_ and any(p in time_ for p in ('YYYY-MM', 'YYYY', '2026-01；口径')):
            time_ = ''
        real_refs.append((name, time_, caliber, url))
    if real_refs:
        lis = []
        for n, (name, time_, caliber, url) in enumerate(real_refs, 1):
            meta = '，'.join(x for x in (time_, caliber) if x)
            label = esc(name)
            if url and url.startswith(('http://', 'https://', './', '../')) and 'example.com' not in url:
                label = f'<a class="ref-link" href="{esc(url)}" target="_blank" rel="noopener">{esc(name)}</a>'
            lis.append(f'      <li id="ref-{n}">[{n}] {label}' + (f'，{esc(meta)}' if meta else '') + '。</li>')
        parts.append(f'''<section class="band band--flow" id="refs">
  <div class="wrap">
    <div class="shead rv"><div class="t-eyebrow">附录</div>
      <h2 class="t-h1 shead__title">参考资料</h2></div>
    <ol class="refs">{''.join(lis)}</ol>
  </div>
</section>''')
    # 无真实来源 → 不渲染 #refs 整节（也不写占位）
    return '\n\n'.join(parts)


def load_model(path: Path) -> dict:
    txt = path.read_text(encoding='utf-8')
    if path.suffix.lower() == '.json':
        return json.loads(txt)
    m = re.search(r'window\.REPORT_MODEL\s*=\s*(\{[\s\S]*?\})\s*;', txt)
    if not m:
        raise SystemExit('未找到 window.REPORT_MODEL')
    return json.loads(m.group(1))


def _strip_refs_nav(html: str, body: str) -> str:
    """无真实来源（正文不含 #refs 节）时，摘掉导航/收尾的「参考资料」入口，避免悬空锚点。"""
    if 'id="refs"' in body:
        return html
    html = re.sub(r'\s*<a[^>]*href="#refs"[^>]*>[\s\S]*?</a>', '', html)
    return html


def main() -> int:
    ap = argparse.ArgumentParser(description='从 REPORT_MODEL 渲染 HTML 正文（模型驱动生成）')
    ap.add_argument('src', help='model.json 或含 REPORT_MODEL 的 .html')
    ap.add_argument('--template', help='模式模板名 presentation|research|architecture 或路径')
    ap.add_argument('--out', help='输出 HTML')
    ap.add_argument('--inplace', action='store_true', help='就地替换 src 的 CONTENT 区')
    ap.add_argument('--body-only', action='store_true', help='只打印正文片段')
    args = ap.parse_args()

    src = Path(args.src)
    model = load_model(src)
    body = render_body(model)

    if args.body_only:
        sys.stdout.write(body)
        return 0

    if args.inplace:
        t = src.read_text(encoding='utf-8')
        if not CONTENT_RE.search(t):
            print('错误：--inplace 需要 __TOPPPT_CONTENT__ 标记', file=sys.stderr)
            return 2
        t = CONTENT_RE.sub(
            r'\1\n' + body.replace('\\', '\\\\') + r'\n\2', t, count=1)
        # 同步模型（确保与渲染源一致）
        t = MODEL_RE.sub('window.REPORT_MODEL = ' +
                         json.dumps(model, ensure_ascii=False, indent=2) + ';', t, count=1)
        t = _strip_refs_nav(t, body)
        src.write_text(t, encoding='utf-8')
        print(f'已按模型重渲染正文：{src}（{len(body)} 字符）')
        print(f'  下一步: python scripts/validate_report.py "{src}" --strict')
        return 0

    mode = model.get('mode') or 'presentation'
    tpl = args.template or mode
    tpl_path = Path(tpl) if Path(tpl).exists() else TPL / f'{tpl}.html'
    if not tpl_path.exists():
        print(f'错误：模板不存在 {tpl_path}', file=sys.stderr)
        return 2
    t = tpl_path.read_text(encoding='utf-8')
    if not CONTENT_RE.search(t):
        print('错误：模板缺少 CONTENT 标记', file=sys.stderr)
        return 2
    t = CONTENT_RE.sub(r'\1\n' + body.replace('\\', '\\\\') + r'\n\2', t, count=1)
    t = MODEL_RE.sub('window.REPORT_MODEL = ' +
                     json.dumps(model, ensure_ascii=False, indent=2) + ';', t, count=1)
    t = _strip_refs_nav(t, body)
    out = Path(args.out or (src.with_suffix('.html')))
    out.write_text(t, encoding='utf-8')
    print(f'已从模型生成：{out}  sections={len(model.get("sections") or [])}')
    print(f'  下一步: python scripts/validate_report.py "{out}" --strict')
    return 0


if __name__ == '__main__':
    sys.exit(main())
