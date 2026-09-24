#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TopPPT HTML · 门禁反向验证（故障注入）

校验器最容易退化成「只会说 OK 的摆设」。本脚本往合格产物里**注入已知缺陷**，
断言对应门禁必须报错——门禁抓不到即视为失败。

覆盖：
  N1  Exhibit 框漏编号（旧实现只校验已编号者的连续性 → 静默通过）
  N2  参考资料两位数编号错配（旧正则 `ref-\\d` 两侧同时落空 → 静默通过）
  N3  参考资料编号跳号
  N4  PPTX 演讲者备注被剔离（dataTable=notes 声称数据入备注，不核对就只是一句承诺）
  N5  模型图表数值篡改（cross_verify 数值核对）
  N6  行动标题判断词鉴别力（正则本身）
  N7  PPTX 字号越出比例尺
  N8  data-chart 未登记类型（登记表白名单）
  N9  图表多样性塌陷（全篇压成同型 → 不同类型数 < 模式下限）
  N10 图片外链（零外链铁律）
  N11 待核实有标色无图例（.tbd 必须配 .tbd-legend/.flagbar）
  N12 模型 theme 与 data-theme 矛盾
  N13 模型 mode 与 data-mode 矛盾
  N14 内部锚点断裂（链接目标 id 不存在）

用法: python scripts/negative_tests.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist' / 'negtest'
PY = sys.executable


def run_validate(path: Path) -> tuple[int, str]:
    r = subprocess.run([PY, str(ROOT / 'scripts' / 'validate_report.py'), str(path), '--strict'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def expect_fail(name: str, path: Path, keyword: str) -> bool:
    code, out = run_validate(path)
    # --strict 下 WARN 同样计失败（退出码 1），故 [WARN] 行也算「门禁抓到」
    hit = [ln for ln in out.splitlines()
           if keyword in ln and ('[FAIL]' in ln or '[WARN]' in ln)]
    ok = code != 0 and bool(hit)
    print(f'  [{"OK" if ok else "FAIL"}] {name}')
    if hit:
        print(f'        抓到: {hit[0].strip()[:120]}')
    elif not ok:
        print(f'        门禁未触发（期望 FAIL 含「{keyword}」）')
    return ok


def main() -> int:
    base = ROOT / 'assets' / 'examples' / '2026-09-09-research-mckinsey.html'
    if not base.exists():
        print(f'SKIP：基准示例缺失 {base}')
        return 0
    txt = base.read_text(encoding='utf-8')
    OUT.mkdir(parents=True, exist_ok=True)

    code, out = run_validate(base)
    if code != 0:
        print('[FAIL] 基准示例本身未通过 strict，反向验证失去意义')
        return 1
    print('基准示例 strict 通过，开始故障注入：')

    cases: list[tuple[str, str, str]] = []

    # N1 抹掉一个 Exhibit 编号（框仍在）
    cases.append(('N1 Exhibit 框漏编号',
                  txt.replace('class="exhibit__no"', 'class="exhibit__no--x"', 1),
                  'Exhibit 框均已编号'))

    # N2 参考资料改成两位数编号，与正文引用错配
    cases.append(('N2 引用编号两位数错配',
                  re.sub(r'id="ref-1"', 'id="ref-10"', txt, count=1),
                  '双向对齐'))

    # N3 编号跳号（两侧同时改，集合仍对齐，但 1..N 不连续）
    t3 = txt.replace('ref-2"', 'ref-9"')
    cases.append(('N3 参考资料编号跳号', t3, '编号连续'))

    # N8 data-chart 用了登记表外的类型
    cases.append(('N8 图表类型未登记',
                  txt.replace('data-chart="hbar"', 'data-chart="hbarx"', 1),
                  '登记表内'))

    # N9 图表多样性塌陷（全部压成 bar → 不同类型数 1 < research 下限 6）
    t9 = txt
    for ct in ('hbar', 'donut', 'waterfall', 'sankey', 'treemap', 'boxplot',
               'network', 'marimekko', 'streamgraph', 'gantt', 'rose', 'candlestick'):
        t9 = t9.replace(f'data-chart="{ct}"', 'data-chart="bar"')
    cases.append(('N9 图表多样性塌陷', t9, '图表多样性'))

    # N10 外链图片（零外链铁律）
    cases.append(('N10 图片外链',
                  txt.replace('</body>',
                              '<img src="https://example.com/x.png" alt="外链注入"></body>', 1),
                  '图片源无外链'))

    # N11 待核实有标色无图例（改名不得包含原串——校验是子串判断）
    t11 = txt.replace('tbd-legend', 'tbd-leg').replace('flagbar', 'flag-bar')
    cases.append(('N11 待核实无图例', t11, '待核实标注'))

    # N12 模型 theme 与页面 data-theme 矛盾
    cases.append(('N12 模型主题不一致',
                  txt.replace('"theme": "light"', '"theme": "dark"', 1),
                  'data-theme 一致'))

    # N13 模型 mode 与页面 data-mode 矛盾
    cases.append(('N13 模型模式不一致',
                  txt.replace('"mode": "research"', '"mode": "presentation"', 1),
                  'data-mode 一致'))

    # N14 内部锚点断裂（链接目标 id 不存在）
    cases.append(('N14 锚点断裂',
                  txt.replace('href="#s1"', 'href="#s404"'),
                  '锚点闭环'))

    # N15 HTML 标签泄漏进可见文本（截图级：转义标签当字面量显示）
    cases.append(('N15 标签泄漏',
                  txt.replace('</p>',
                              ' &lt;a class="cite" href="#ref-1"&gt;[1]&lt;/a&gt;。</p>', 1),
                  'HTML_TAG_IN_TEXT'))

    # N16 极偏 donut（0.5% vs 99.5% 应改 KPI，禁环图）
    t16 = txt
    if '"type": "donut"' in t16 or '"type":"donut"' in t16:
        t16 = re.sub(
            r'("type"\s*:\s*"donut"[\s\S]{0,200}?"values"\s*:\s*\[)[^\]]*(\])',
            r'\g<1>0.5, 99.5\g<2>', t16, count=1)
        cases.append(('N16 极偏 donut', t16, 'CHART_SKEW'))

    # N17 模型字段夹带 HTML 标签（extract 净化 + validate 扫描 REPORT_MODEL）
    t17 = re.sub(
        r'("soWhat"\s*:\s*")',
        r'\g<1><a class=\\"cite\\" href=\\"#ref-1\\">[1]</a> ',
        txt, count=1)
    if t17 == txt:
        t17 = txt.replace(
            '"footnote":',
            '"footnote": "<strong>x</strong> ', 1)
    cases.append(('N17 模型夹带标签', t17, 'HTML_TAG_IN_TEXT'))

    ok = True
    for name, content, keyword in cases:
        if content == txt:
            print(f'  [SKIP] {name}（基准示例无对应结构）')
            continue
        p = OUT / (name.split()[0] + '.html')
        p.write_text(content, encoding='utf-8')
        ok = expect_fail(name, p, keyword) and ok

    ok = _pptx_notes_case() and ok
    ok = _chart_data_case() and ok
    ok = _title_pattern_case() and ok
    ok = _font_scale_case() and ok

    print('反向验证通过：注入的缺陷都被门禁抓住。' if ok
          else '反向验证失败：存在抓不到的缺陷，门禁有假阴性。')
    return 0 if ok else 1


def _font_scale_case() -> bool:
    """N7：往 PPTX 里塞一个比例尺外的字号 → FONT_SIZE_OFF_SCALE 必须报。"""
    name = '2026-09-09-research-mckinsey'
    src = ROOT / 'dist' / 'regression' / f'{name}.pptx'
    model = ROOT / 'assets' / 'examples' / f'{name}.model.json'
    if not src.exists() or not model.exists():
        print('  [SKIP] N7 字号越出比例尺（需先跑 regression）')
        return True
    out = OUT / 'N7-off-scale.pptx'
    patched = False
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if not patched and item.filename == 'ppt/slides/slide4.xml':
                text = data.decode('utf-8')
                new = re.sub(r'sz="\d+"', 'sz="1234"', text, count=1)  # 12.34pt：任何档位都没有
                if new != text:
                    data = new.encode('utf-8')
                    patched = True
            zout.writestr(item, data)
    if not patched:
        print('  [SKIP] N7 字号越出比例尺（未找到可改写的 sz 属性）')
        return True
    report = OUT / 'N7.json'
    subprocess.run([PY, str(ROOT / 'scripts' / 'validate_pptx.py'), str(out),
                    '--strict', '--model=' + str(model), '--json-out', str(report)],
                   capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        data = json.loads(report.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        print('  [FAIL] N7 字号越出比例尺：校验报告不可解析')
        return False
    codes = {i.get('code') for i in (data.get('errors') or []) + (data.get('warnings') or [])}
    ok = 'FONT_SIZE_OFF_SCALE' in codes
    print(f'  [{"OK" if ok else "FAIL"}] N7 字号越出比例尺')
    if not ok:
        print(f'        门禁未触发（期望 FONT_SIZE_OFF_SCALE，实际 {sorted(codes)[:6]}）')
    return ok


def _title_pattern_case() -> bool:
    """N6：主题词式长标题必须被判为「无判断信号」，结论句标题必须放行。"""
    lc = json.loads((ROOT / 'scripts' / 'layout-constants.json').read_text(encoding='utf-8'))
    pat = ((lc.get('contentQuality') or {}).get('researchTitle') or {}).get('judgmentPattern')
    if not pat:
        print('  [SKIP] N6 行动标题判断词（未配置 judgmentPattern）')
        return True
    topic = ['智能体平台的应用架构与技术选型说明', '关于数据治理需求的整体情况介绍',
             '企业知识库建设的相关背景与范围', '平台能力地图与模块组成一览表',
             '项目实施过程中的应急预案汇总', '面向未来的技术路线图规划说明']
    claim = ['投入产出比在第 3 季度首次转正', '三成团队已把智能体纳入日常流程',
             '数据质量是当前最大的落地瓶颈', '推理成本一年内下降 62%',
             '从试点到规模化：关键卡在治理', '自建方案的总成本高于采购方案']
    leaked = [t for t in topic if re.search(pat, t)]
    hurt = [t for t in claim if not re.search(pat, t)]
    ok = not leaked and not hurt
    print(f'  [{"OK" if ok else "FAIL"}] N6 行动标题判断词鉴别力'
          f'（漏放主题词 {len(leaked)}/{len(topic)} · 误伤结论句 {len(hurt)}/{len(claim)}）')
    for t in (leaked + hurt)[:3]:
        print(f'        {t}')
    return ok


def _chart_data_case() -> bool:
    """N5：篡改模型里的图表数值 → cross_verify 的数值核对必须报不符。"""
    name = '2026-09-09-research-mckinsey'
    pptx = ROOT / 'dist' / 'regression' / f'{name}.pptx'
    mp = ROOT / 'assets' / 'examples' / f'{name}.model.json'
    if not pptx.exists() or not mp.exists():
        print('  [SKIP] N5 图表数值篡改（需先跑 regression）')
        return True
    sys.path.insert(0, str(ROOT / 'scripts'))
    try:
        from pptx import Presentation           # noqa: PLC0415
        import cross_verify as CV               # noqa: PLC0415
    except ImportError:
        print('  [SKIP] N5 图表数值篡改（python-pptx 未安装）')
        return True
    model = json.loads(mp.read_text(encoding='utf-8'))
    touched = False
    for sec in (model.get('sections') or []):
        c = CV._model_chart(sec) if isinstance(sec, dict) else None
        if c and isinstance(c.get('values'), list) and c['values']:
            c['values'] = [(v + 777) if isinstance(v, (int, float)) else v for v in c['values']]
            touched = True
            break
    if not touched:
        print('  [SKIP] N5 图表数值篡改（基准模型无可改图表）')
        return True
    issues = CV.chart_data_verify(Presentation(str(pptx)), model, name)
    ok = bool(issues)
    print(f'  [{"OK" if ok else "FAIL"}] N5 模型图表数值被篡改')
    if ok:
        print(f'        抓到: {issues[0][:120]}')
    else:
        print('        门禁未触发（数值核对形同虚设）')
    return ok


def _pptx_notes_case() -> bool:
    """N4：剥离演讲者备注 → dataTable=notes 的图表数据不可追溯，必须被 strict 抓住。"""
    name = '2026-09-09-research-mckinsey'
    src = ROOT / 'dist' / 'regression' / f'{name}.pptx'
    model = ROOT / 'assets' / 'examples' / f'{name}.model.json'
    if not src.exists() or not model.exists():
        print('  [SKIP] N4 备注剥离（需先跑 regression 生成 PPTX）')
        return True
    stripped = OUT / 'N4-no-notes.pptx'
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(stripped, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename.startswith('ppt/notesSlides/'):
                continue
            zout.writestr(item, zin.read(item.filename))
    report = OUT / 'N4.json'
    subprocess.run([PY, str(ROOT / 'scripts' / 'validate_pptx.py'), str(stripped),
                    '--strict', '--model=' + str(model), '--json-out', str(report)],
                   capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        data = json.loads(report.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        print('  [FAIL] N4 备注剥离：校验报告不可解析')
        return False
    codes = {i.get('code') for i in (data.get('errors') or []) + (data.get('warnings') or [])}
    ok = 'MODEL_CHART_NOTES_MISSING' in codes
    print(f'  [{"OK" if ok else "FAIL"}] N4 演讲者备注被剥离')
    if not ok:
        print(f'        门禁未触发（期望 MODEL_CHART_NOTES_MISSING，实际 {sorted(codes)[:6]}）')
    return ok


if __name__ == '__main__':
    sys.exit(main())
