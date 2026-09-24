#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TopPPT HTML · 布局选型建议（Batch 1 stub · Batch 2 扩展）

用法:
    python scripts/recommend_layout.py --mode research
    python scripts/recommend_layout.py --mode presentation --intent "占比构成 极偏"
    python scripts/recommend_layout.py --mode architecture --pages 6

输出每页建议的 pageType / skel(P#) / chart（启发式，供智能体与 QA；非强制门禁）。
本脚本暂不列入 package REQUIRED（Batch 2 定稿后再纳入）。
"""
from __future__ import annotations

import argparse
import json
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# mode → 默认页型节奏（极简启发式；Batch 2 接内容特征）
DEFAULTS = {
    'presentation': [
        ('cover', 'P1', None),
        ('agenda', 'P2', None),
        ('kpi', 'P3', None),
        ('points', 'P4', None),
        ('bar', 'P5', 'hbar'),
        ('points', 'P6', None),
        ('donut', 'P7', 'donut'),
        ('quote', 'P8', None),
        ('closing', 'P1', None),
    ],
    'research': [
        ('cover', 'P1', None),
        ('agenda', 'P2', None),
        ('metrics', 'P3', None),
        ('exhibit', 'P5', 'bar'),
        ('twocol', 'P6', None),
        ('halftable', 'P7', None),
        ('exhibit', 'P5', 'line'),
        ('threecol', 'P9', None),
        ('matrix', 'P8', None),
        ('flags', 'P4', None),
        ('closing', 'P1', None),
    ],
    'architecture': [
        ('cover', 'P1', None),
        ('diagram', 'P10', 'network'),
        ('lane', 'P11', None),
        ('diagram', 'P10', None),
        ('points', 'P4', None),
        ('closing', 'P1', None),
    ],
}

# 意图关键词 → 覆盖建议
INTENT_HINTS = [
    (('极偏', '占比失衡', '0.5%'), {'pageType': 'kpi', 'skel': 'P3', 'chart': None,
                                    'note': '极偏占比禁 donut→V3 KPI'}),
    (('占比', '构成', '份额'), {'pageType': 'donut', 'skel': 'P7', 'chart': 'donut'}),
    (('趋势', '爬坡', '时间序列'), {'pageType': 'bar', 'skel': 'P5', 'chart': 'line'}),
    (('排名', '对比', '谁高谁低'), {'pageType': 'bar', 'skel': 'P5', 'chart': 'hbar'}),
    (('架构', '拓扑', '分层'), {'pageType': 'diagram', 'skel': 'P10', 'chart': 'network'}),
    (('泳道', '流程', '协作'), {'pageType': 'lane', 'skel': 'P11', 'chart': None}),
    (('路演', '融资', 'pitch'), {'pageType': 'points', 'skel': 'P4', 'chart': None,
                                 'note': '演示节奏；简单图禁全幅'}),
]


def recommend(mode: str, intent: str = '', pages: int | None = None) -> list[dict]:
    mode = {'a': 'presentation', 'b': 'research', 'c': 'architecture',
            'presentation': 'presentation', 'research': 'research',
            'architecture': 'architecture'}.get(mode.lower(), mode)
    seq = list(DEFAULTS.get(mode, DEFAULTS['research']))
    if pages and pages > 0:
        # cover + closing 固定，中间按需裁剪/循环
        mid = seq[1:-1] if len(seq) > 2 else seq
        if pages <= 2:
            seq = seq[:1] + seq[-1:]
        else:
            need = pages - 2
            body = (mid * ((need // max(len(mid), 1)) + 1))[:need]
            seq = [seq[0]] + body + [seq[-1]]
    out = []
    for i, (pt, skel, chart) in enumerate(seq, 1):
        row = {'page': i, 'pageType': pt, 'skel': skel, 'chart': chart}
        out.append(row)
    # 意图覆盖：改写首个内容页（page 3 或 page 2）
    if intent:
        for keys, hint in INTENT_HINTS:
            if any(k in intent for k in keys):
                idx = 2 if len(out) > 2 else 0
                out[idx].update({k: v for k, v in hint.items() if k != 'note'})
                if hint.get('note'):
                    out[idx]['note'] = hint['note']
                break
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description='Recommend pageType/skel/chart sequence')
    ap.add_argument('--mode', required=True, help='presentation|research|architecture|A|B|C')
    ap.add_argument('--intent', default='', help='free-text intent for heuristics')
    ap.add_argument('--pages', type=int, default=None, help='target page count')
    ap.add_argument('--json', action='store_true', help='machine-readable output')
    args = ap.parse_args()
    rows = recommend(args.mode, args.intent, args.pages)
    if args.json:
        print(json.dumps({'mode': args.mode, 'pages': rows}, ensure_ascii=False, indent=2))
    else:
        print(f'# recommend_layout · mode={args.mode}'
              + (f' · intent={args.intent!r}' if args.intent else '')
              + (f' · pages={args.pages}' if args.pages else ''))
        print(f'{"#":>3}  {"pageType":<14} {"skel":<6} {"chart":<12} note')
        for r in rows:
            print(f'{r["page"]:>3}  {r["pageType"]:<14} {r["skel"]:<6} '
                  f'{str(r.get("chart") or "—"):<12} {r.get("note") or ""}')
        print('\n(stub · Batch 2 will add content-aware complexity / V1–V4 matching)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
