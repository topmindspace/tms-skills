#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TopPPT HTML · HTML 检查公共库（单源：承载正则 / 图表通道 / 多样性下限 / 组合版式）

消费方：validate_report.py · quality_gate.py · evals/run_evals.py
禁止在消费方再手抄 CARRIERS / 多样性公式 / 组合版式判定。
阈值仍读 layout-constants.json（charts.variety / charts.registry）。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_LC_PATH = ROOT / 'scripts' / 'layout-constants.json'

# 承载类型正则（组合版式：一页是否含 ≥2 种承载）
CARRIERS = [
    r'<svg\b[^>]*data-chart=',
    r'class="tbl-wrap',
    r'class="card[\s"]',
    r'class="metric[\s"]',
    r'class="media[\s"]',
    r'class="arch[\s"]',
    r'class="lane[\s"]',
    r'class="matrix[\s"]',
    r'class="heat[\s"]',
    r'class="bul[\s"]',
    r'class="pyr[\s"]',
    r'class="steps[\s"]',
    r'class="exhibit[\s"]',
    r'class="cols-2',
    r'class="cols-3',
]

SKIP_BAND_IDS = ('agenda', 'cover', 'refs', 'appendix', 'next')


def load_lc() -> dict:
    return json.loads(_LC_PATH.read_text(encoding='utf-8'))


def chart_registry(lc: dict | None = None) -> dict:
    lc = lc or load_lc()
    return {k: v for k, v in ((lc.get('charts') or {}).get('registry') or {}).items()
            if isinstance(v, dict)}


def chart_variety(lc: dict | None = None) -> dict:
    lc = lc or load_lc()
    return (lc.get('charts') or {}).get('variety') or {}


def bands(html: str) -> list[str]:
    return re.split(r'(?=<section class="band)', html)[1:]


def content_bands(html: str, skip_ids: tuple[str, ...] = SKIP_BAND_IDS) -> list[str]:
    out = []
    for b in bands(html):
        head = b[:240]
        if any(f'id="{i}"' in head for i in skip_ids):
            continue
        out.append(b)
    return out


def chart_types_per_page(html: str) -> list[list[str]]:
    return [re.findall(r'data-chart="([^"]+)"', b) for b in bands(html)]


def distinct_chart_types(html: str) -> list[str]:
    used = [t for ts in chart_types_per_page(html) for t in ts]
    return sorted(set(used))


def variety_floor(mode: str, n_chart_pages: int, variety: dict | None = None) -> int:
    """类型数下限 = min(模式上限, max(1, ⌈图表页数 × ratio⌉))"""
    v = variety if variety is not None else chart_variety()
    floor = int((v.get('minTypes') or {}).get(mode, 4) or 4)
    ratio = float(v.get('minTypesRatio') or 0.6)
    return min(floor, max(1, int(-(-n_chart_pages * ratio // 1))))


def adjacent_same_type(pages: list[list[str]]) -> list[str]:
    """相邻图表页同型告警文案列表。"""
    adj, prev, prev_i = [], None, 0
    for i, ts in enumerate(pages):
        if not ts:
            continue
        if prev and set(ts) & set(prev):
            adj.append(f'第 {prev_i + 1}/{i + 1} 页同型 {sorted(set(ts) & set(prev))}')
        prev, prev_i = ts, i
    return adj


def carrier_count(band: str) -> int:
    return sum(1 for pat in CARRIERS if re.search(pat, band))


def composite_pages(html: str) -> tuple[int, int]:
    """返回 (含 ≥2 种承载的内容页数, 内容页总数)。"""
    content = content_bands(html)
    multi = sum(1 for b in content if carrier_count(b) >= 2)
    return multi, len(content)


def composite_required(mode: str, variety: dict | None = None) -> float:
    """组合版式比例下限；非 compositeModes 返回 0。"""
    v = variety if variety is not None else chart_variety()
    if mode not in (v.get('compositeModes') or ['research']):
        return 0.0
    return float(v.get('compositeMinRatio') or 0)


def chart_channel(chart_type: str, reg: dict | None = None) -> str:
    reg = reg if reg is not None else chart_registry()
    spec = reg.get(str(chart_type or 'bar').lower()) or {}
    return str(spec.get('pptx') or 'native')


def chart_datatable_mode(chart: dict, reg: dict | None = None) -> str:
    reg = reg if reg is not None else chart_registry()
    spec = reg.get(str(chart.get('type') or 'bar').lower()) or {}
    mode = str(chart.get('dataTable') or spec.get('dataTable') or 'notes').lower()
    return 'inline' if mode == 'appendix' else mode
