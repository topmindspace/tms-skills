#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TopPPT HTML · 布局选型建议（Batch 2）

用法:
  python scripts/recommend_layout.py --mode B --intent "经营分析 占比极偏" --pages 10
  python scripts/recommend_layout.py --mode A --intent "路演" --intent "趋势" --json
  python scripts/recommend_layout.py --mode C --from-model path/to.model.json
  echo '{"mode":"research","intents":["架构"]}' | python scripts/recommend_layout.py --stdin

输出 JSON 页序列：{pageType, skel, chart?, rationale, v?}
启发式：playbook V1–V4 / sizeByComplexity / 极偏禁 donut / layoutSystem.defaultCharts。
不列入 package REQUIRED（可选工具；Batch 3 再定是否纳入）。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).resolve().parent
LC = json.loads((ROOT / 'layout-constants.json').read_text(encoding='utf-8'))
LS = LC.get('layoutSystem') or {}
PAGE_TO_PRESET = dict(LS.get('pageToPreset') or {})
DEFAULT_CHARTS = list(LS.get('defaultCharts') or
                      ['bar', 'hbar', 'line', 'donut', 'progress', 'area', 'stack', 'dualline'])
SIZE_BANDS = list(((LC.get('charts') or {}).get('sizeByComplexity') or {}).get('bands') or [])
V_MAP = dict(LS.get('vMap') or {'V1': 'P1', 'V2': 'P2', 'V3': 'P3', 'V4': 'P4'})

MODE_ALIAS = {
    'a': 'presentation', 'presentation': 'presentation', '演示': 'presentation',
    'b': 'research', 'research': 'research', '研究': 'research',
    'c': 'architecture', 'architecture': 'architecture', '架构': 'architecture',
}

# 模式默认节奏（页型序列）；cover/closing 由调用方决定是否保留
DEFAULT_SEQ = {
    'presentation': [
        'cover', 'agenda', 'kpi', 'points', 'bar', 'points', 'donut', 'quote', 'closing',
    ],
    'research': [
        'cover', 'agenda', 'metrics', 'exhibit', 'twocol', 'halftable',
        'exhibit', 'threecol', 'matrix', 'flags', 'closing',
    ],
    'architecture': [
        'cover', 'diagram', 'lane', 'diagram', 'points', 'closing',
    ],
}

INTENT_RULES: list[tuple[tuple[str, ...], dict]] = [
    (('极偏', '占比失衡', '长尾', '0.5%'), {
        'pageType': 'kpi', 'chart': None, 'v': 'V3',
        'rationale': '极偏占比禁 donut/pie → V3 大数+佐证',
    }),
    (('占比', '构成', '份额', '结构'), {
        'pageType': 'donut', 'chart': 'donut', 'v': 'V1',
        'rationale': '构成类默认 donut（非极偏）；演示配 V1 右注解',
    }),
    (('趋势', '爬坡', '时间序列', '同比', '环比'), {
        'pageType': 'bar', 'chart': 'line', 'v': 'V2',
        'rationale': '时间趋势 → line；演示用 V2 上图下带',
    }),
    (('排名', '对比', '谁高谁低', '对标'), {
        'pageType': 'bar', 'chart': 'hbar', 'v': 'V1',
        'rationale': '排名/对比 → hbar',
    }),
    (('架构', '拓扑', '分层', '泳道', '流程'), {
        'pageType': 'diagram', 'chart': 'network', 'v': None,
        'rationale': '结构图为王；skel P10/P11',
    }),
    (('路演', '融资', 'pitch', '发布'), {
        'pageType': 'points', 'chart': None, 'v': 'V1',
        'rationale': '演示节奏；简单图禁全幅',
    }),
    (('经营', '复盘', '分析', '调研'), {
        'pageType': 'exhibit', 'chart': 'bar', 'v': None,
        'rationale': '研究证据页 exhibit + bar',
    }),
]


def _norm_mode(m: str) -> str:
    return MODE_ALIAS.get((m or 'b').lower().strip(), 'research')


def _skel(page_type: str, v: str | None = None) -> str:
    if page_type in ('cover', 'closing'):
        return 'P1'
    if page_type in ('agenda',):
        return 'P2'
    if v and v in V_MAP:
        return V_MAP[v]
    return PAGE_TO_PRESET.get(page_type, 'P4')


def _chart_ok(chart: str | None, n_cats: int, n_pts: int) -> str | None:
    """Apply sizeByComplexity forbid list; return possibly replaced chart."""
    if not chart:
        return None
    for band in SIZE_BANDS:
        if n_cats <= int(band.get('maxCats') or 99) and n_pts <= int(band.get('maxPts') or 99):
            forbid = set(band.get('forbid') or [])
            if chart in forbid:
                prefer = list(band.get('prefer') or ['kpi'])
                return None if prefer[0] in ('kpi', 'progress', 'vsbar') else prefer[0]
            return chart
    return chart if chart in DEFAULT_CHARTS else DEFAULT_CHARTS[0]


def _complexity(sec: dict) -> tuple[int, int]:
    ch = sec.get('chart') if isinstance(sec.get('chart'), dict) else {}
    vals = ch.get('values') or ch.get('data') or []
    labels = ch.get('labels') or []
    pts = sec.get('points') or sec.get('items') or []
    n_pts = len(vals) if vals else len(pts)
    n_cats = len(labels) if labels else (len(vals) if vals else (1 if pts else 0))
    return max(n_cats, 0), max(n_pts, 0)


def _skew(sec: dict) -> bool:
    ch = sec.get('chart') if isinstance(sec.get('chart'), dict) else {}
    vals = [float(v) for v in (ch.get('values') or []) if isinstance(v, (int, float))]
    vals = [v for v in vals if v >= 0]
    if len(vals) < 2:
        return False
    total = sum(vals) or 1.0
    pcts = [v / total * 100 for v in vals]
    mn, mx = min(pcts), max(pcts)
    return mn < 5.0 or (mn > 0 and mx / mn > 20)


def _match_intent(text: str) -> dict | None:
    for keys, hint in INTENT_RULES:
        if any(k in text for k in keys):
            return dict(hint)
    return None


def recommend(
    mode: str,
    intents: list[str] | None = None,
    pages: int | None = None,
    model: dict | None = None,
) -> list[dict]:
    mode = _norm_mode(mode)
    intents = intents or []
    blob = ' '.join(intents)

    if model and isinstance(model.get('sections'), list) and model['sections']:
        out = []
        for i, sec in enumerate(model['sections'], 1):
            if not isinstance(sec, dict):
                continue
            pt = str(sec.get('type') or 'points')
            n_cats, n_pts = _complexity(sec)
            ch = None
            if isinstance(sec.get('chart'), dict):
                ch = sec['chart'].get('type')
            elif pt in DEFAULT_CHARTS:
                ch = pt if pt != 'bar' else 'bar'
            rationale = 'from-model'
            v = None
            if _skew(sec) and (ch in ('donut', 'pie', 'multidonut') or pt == 'donut'):
                pt, ch, v = 'kpi', None, 'V3'
                rationale = 'model 极偏占比 → V3 KPI（禁 donut）'
            else:
                ch = _chart_ok(ch, n_cats or 3, n_pts or 3)
                if mode == 'presentation':
                    if n_cats <= 2 and n_pts <= 3:
                        v = 'V3'
                        rationale = '演示·简单数据 → V3 大数，禁全幅简单图'
                    elif n_pts >= 8:
                        v = 'V2'
                        rationale = '演示·复杂序列 → V2 上图下带'
                    else:
                        v = 'V1'
                        rationale = '演示·默认 V1 主视觉+右注解'
            if blob:
                hit = _match_intent(blob)
                if hit and i == min(3, len(model['sections'])):
                    pt = hit.get('pageType', pt)
                    ch = hit.get('chart', ch)
                    v = hit.get('v', v)
                    rationale = hit.get('rationale', rationale)
            skel = sec.get('layoutPreset') or _skel(pt, v)
            row = {'page': i, 'pageType': pt, 'skel': skel, 'chart': ch,
                   'rationale': rationale}
            if v:
                row['v'] = v
            out.append(row)
        return out

    seq = list(DEFAULT_SEQ.get(mode, DEFAULT_SEQ['research']))
    if pages and pages > 0:
        mid = seq[1:-1] if len(seq) > 2 else seq
        if pages <= 2:
            seq = seq[:1] + seq[-1:]
        else:
            need = pages - 2
            body = (mid * ((need // max(len(mid), 1)) + 1))[:need]
            seq = [seq[0]] + body + [seq[-1]]

    out = []
    intent_hit = _match_intent(blob) if blob else None
    for i, pt in enumerate(seq, 1):
        ch = pt if pt in DEFAULT_CHARTS else (DEFAULT_CHARTS[(i - 1) % len(DEFAULT_CHARTS)]
                                             if pt in ('bar', 'exhibit', 'donut') else None)
        if pt == 'bar':
            ch = 'bar'
        if pt == 'donut':
            ch = 'donut'
        if pt == 'exhibit':
            ch = 'bar'
        v = 'V1' if mode == 'presentation' and pt not in ('cover', 'agenda', 'closing', 'quote') else None
        rationale = f'default {mode} rhythm'
        skel = _skel(pt, v)
        row = {'page': i, 'pageType': pt, 'skel': skel, 'chart': ch, 'rationale': rationale}
        if v:
            row['v'] = v
        out.append(row)

    if intent_hit and out:
        idx = 2 if len(out) > 2 else 0
        if out[idx]['pageType'] in ('cover', 'agenda'):
            idx = min(idx + 1, len(out) - 1)
        out[idx]['pageType'] = intent_hit.get('pageType', out[idx]['pageType'])
        out[idx]['chart'] = intent_hit.get('chart')
        if intent_hit.get('v'):
            out[idx]['v'] = intent_hit['v']
        out[idx]['skel'] = _skel(out[idx]['pageType'], out[idx].get('v'))
        out[idx]['rationale'] = intent_hit.get('rationale', '')
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description='Recommend pageType/skel/chart sequence')
    ap.add_argument('--mode', default=None, help='A|B|C or presentation|research|architecture')
    ap.add_argument('--intent', action='append', default=[], help='repeatable intent phrases')
    ap.add_argument('--pages', type=int, default=None)
    ap.add_argument('--from-model', default=None, help='path to REPORT_MODEL JSON')
    ap.add_argument('--stdin', action='store_true', help='read JSON {mode,intents,pages,model} from stdin')
    ap.add_argument('--json', action='store_true', help='machine-readable (default when --stdin/--from-model)')
    args = ap.parse_args()

    model = None
    intents = list(args.intent or [])
    mode = args.mode
    pages = args.pages

    if args.stdin:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
        mode = mode or data.get('mode')
        intents = intents or list(data.get('intents') or [])
        pages = pages if pages is not None else data.get('pages')
        model = data.get('model') or data if 'sections' in data else None

    if args.from_model:
        model = json.loads(Path(args.from_model).read_text(encoding='utf-8'))
        mode = mode or model.get('mode')

    if not mode:
        ap.error('--mode is required (or provide via --from-model/--stdin)')

    rows = recommend(mode, intents, pages, model)
    as_json = args.json or args.stdin or bool(args.from_model)
    payload = {'mode': _norm_mode(mode), 'pages': rows}
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"# recommend_layout · mode={payload['mode']}"
              + (f" · intents={intents!r}" if intents else '')
              + (f" · pages={pages}" if pages else ''))
        print(f"{'#':>3}  {'pageType':<14} {'skel':<6} {'chart':<12} {'v':<4} rationale")
        for r in rows:
            print(f"{r['page']:>3}  {r['pageType']:<14} {r['skel']:<6} "
                  f"{str(r.get('chart') or '—'):<12} {str(r.get('v') or '—'):<4} "
                  f"{r.get('rationale') or ''}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
