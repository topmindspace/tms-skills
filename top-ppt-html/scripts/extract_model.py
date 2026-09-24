#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TopPPT HTML· 从 HTML 报告抽取 PPTX 内容模型
用法:
    python extract_model.py <报告.html> [输出.json]

从报告的 window.REPORT_MODEL（JSON）抽取内容模型，供 build_pptx.js --model= 使用。
保证 PPTX 与页面同源——模型即唯一事实源，不再两处维护。
校验双端同源：页型字段与必填约束读 scripts/model-schema.json（与浏览器端 validateModel
消费同一份 schema，经 sync_runtime.py 注入 assets/pptx-export.js，杜绝漂移）。
含模型-正文一致性抽查（标题/agenda 条数/页数粗对齐），不一致打印警告（硬门禁在 validate_report.py）。
"""
import sys
import re
import json
from pathlib import Path

# Windows GBK 控制台兜底：强制 UTF-8 输出
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

SCHEMA_PATH = Path(__file__).resolve().parent / 'model-schema.json'


def load_schema():
    """DSL schema 单源（model-schema.json）；与浏览器端 validateModel 同一份定义。"""
    try:
        return json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as e:
        print(f"警告: 无法读取 schema 单源 {SCHEMA_PATH}: {e}")
        return None


def schema_get(obj, path):
    cur = obj
    for k in path.split('.'):
        if cur is None or not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return cur


def schema_field_ok(sec, spec):
    """spec = 'a.b:array' / 'a.b:str' / 'a.b'（真值检查）/ 'anyof:a|b:c'（任一满足）。"""
    if spec.startswith('anyof:'):
        return any(schema_field_ok(sec, alt) for alt in spec[len('anyof:'):].split('|') if alt)
    m = re.match(r'^(.*?)(?::(array|str))?$', spec)
    path, kind = m.group(1), m.group(2)
    v = schema_get(sec, path)
    if kind == 'array':
        return isinstance(v, list) and len(v) > 0
    if kind == 'str':
        return isinstance(v, str) and bool(v.strip())
    return bool(v)


def validate_against_schema(model, schema):
    """按 schema 单源校验模型；返回 (缺失列表, 警告列表)。与浏览器端 validateModel 同语义。"""
    missing, warnings = [], []
    if not schema:
        return missing, warnings
    ms = schema.get('model') or {}
    for spec in ms.get('required', []):
        if not schema_field_ok(model, spec):
            missing.append(f"{spec}（顶层必填）")
    mode = model.get('mode') or 'presentation'
    ag = model.get('agenda') or []
    ag_min = (ms.get('agendaMin') or {}).get(mode, 0)
    if ag_min > 0 and len(ag) < ag_min:
        missing.append(f"agenda（大纲 ≥{ag_min} 条）")
    secs = model.get('sections') or []
    if not isinstance(secs, list) or len(secs) < ms.get('sectionsMin', 1):
        missing.append("sections（章节页 ≥1）")
    page_types = schema.get('pageTypes') or {}
    for i, sec in enumerate(secs if isinstance(secs, list) else []):
        t = (sec.get('type') if isinstance(sec, dict) else None) or 'points'
        defn = page_types.get(t)
        if not defn:
            missing.append(f"sections[{i}].type={t!r}（未知页型）")
            continue
        if not (isinstance(sec, dict) and sec.get('title')):
            missing.append(f"sections[{i}].title（第 {i + 1} 章标题）")
        for spec in defn.get('required', []):
            if not schema_field_ok(sec, spec):
                missing.append(f"sections[{i}].{spec}（{defn.get('label', t)}必填）")
        if defn.get('modes') and mode not in defn['modes']:
            warnings.append(f"sections[{i}] 页型 {t!r} 适用于 {'/'.join(defn['modes'])}，当前 mode={mode!r}")
    if schema.get('modes') and model.get('mode') and model['mode'] not in schema['modes']:
        warnings.append(f"mode={model['mode']!r} 未知，按 presentation 处理")
    if secs and len(secs) < ms.get('sectionsRecommended', 3):
        warnings.append(f"章节页仅 {len(secs)} 页，正式报告建议 ≥3")
    if len(ag) > ms.get('agendaComfortMax', 16):
        warnings.append(f"agenda {len(ag)} 条超出单页舒适上限，建议拆分")
    return missing, warnings


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"文件不存在: {path}")
        return 2
    txt = path.read_text(encoding='utf-8')

    m = re.search(r'window\.REPORT_MODEL\s*=\s*(\{[\s\S]*?\})\s*;', txt)
    if not m:
        print("未找到 window.REPORT_MODEL —— 报告未内嵌内容模型。")
        print("请按 references/pptx-export.md 在报告 <script> 中补齐模型后再抽取。")
        return 1
    raw = m.group(1)
    try:
        model = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"REPORT_MODEL 不是合法 JSON: {e}")
        print("注意：模型必须是严格 JSON（双引号、无尾逗号、无注释）。")
        return 1

    # 模型字符串字段净化：禁止把 HTML 标签当纯文本写入（cite 只允许 [n]）。
    # 泄漏标签会在 PPTX/预览里原样露出 <a class="cite"…>，属交付硬缺陷。
    stripped = {'count': 0, 'samples': []}

    def _scrub_assign(obj, path=''):
        if isinstance(obj, dict):
            for k in list(obj.keys()):
                v = obj[k]
                p = f'{path}.{k}' if path else k
                if isinstance(v, str) and re.search(r'</?[a-zA-Z][^>]*>', v):
                    obj[k] = re.sub(r'\s+', ' ', re.sub(r'</?[a-zA-Z][^>]*>', '', v)).strip()
                    stripped['count'] += 1
                    if len(stripped['samples']) < 5:
                        stripped['samples'].append(p)
                else:
                    _scrub_assign(v, p)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                p = f'{path}[{i}]'
                if isinstance(v, str) and re.search(r'</?[a-zA-Z][^>]*>', v):
                    obj[i] = re.sub(r'\s+', ' ', re.sub(r'</?[a-zA-Z][^>]*>', '', v)).strip()
                    stripped['count'] += 1
                    if len(stripped['samples']) < 5:
                        stripped['samples'].append(p)
                else:
                    _scrub_assign(v, p)

    _scrub_assign(model)
    if stripped['count']:
        print(f"[净化] 剥离 {stripped['count']} 处模型字段中的 HTML 标签: {stripped['samples']}")
        print("  注意：引用在模型里写 [n] 纯文本；HTML 正文才用 <a class=\"cite\">。禁止把标签写进模型。")

    # 风格/模式/主题兜底：模型未写时取页面 data-style / data-mode / data-theme
    if not model.get('style'):
        sm = re.search(r'<html[^>]*data-style="([^"]+)"', txt)
        if sm:
            model['style'] = sm.group(1)
    if not model.get('mode'):
        mm = re.search(r'<html[^>]*data-mode="([^"]+)"', txt)
        if mm:
            model['mode'] = mm.group(1)
    if not model.get('theme'):
        tm = re.search(r'<html[^>]*data-theme="([^"]+)"', txt)
        if tm:
            model['theme'] = tm.group(1)

    # schema 单源校验（与浏览器端 validateModel 同一份 model-schema.json）
    schema = load_schema()
    missing, schema_warn = validate_against_schema(model, schema)
    if missing:
        print(f"模型缺字段 {len(missing)} 项（导出的 PPTX 相应页面会为空或跳过）：")
        for msg in missing:
            print(f"  - {msg}")
    for msg in schema_warn:
        print(f"[schema 警告] {msg}")

    # 模型-正文一致性抽查（标题 / agenda 条数 / 页数粗对齐）
    issues = []
    plain = re.sub(r'<[^>]+>', ' ', txt)
    secs = model.get('sections') or []
    miss_titles = [str(s.get('title'))[:14] for s in secs
                   if s.get('title') and str(s.get('title')) not in plain]
    if miss_titles:
        issues.append(f"{len(miss_titles)} 个章节标题未在正文出现: {miss_titles[:3]}")
    n_ag = len(model.get('agenda') or [])
    n_html_ag = txt.count('class="agenda__a"')
    if n_ag and n_html_ag and n_ag != n_html_ag:
        issues.append(f"agenda 条数不一致: model={n_ag} 正文={n_html_ag}")
    n_bands = len(re.findall(r'<section class="band', txt))
    if secs and not (len(secs) + 3 <= n_bands <= len(secs) + 7):
        issues.append(f"页数粗不匹配: 正文 {n_bands} 页 vs 模型 {len(secs)}+3~7")
    for msg in issues:
        print(f"[一致性警告] {msg}")

    out = Path(sys.argv[2]) if len(sys.argv) > 2 else path.with_suffix('.model.json')
    out.write_text(json.dumps(model, ensure_ascii=False, indent=2), encoding='utf-8')
    n_sec = len(model.get('sections', []))
    print(f"已抽取: {out}  (agenda {len(model.get('agenda', []))} 条 · sections {n_sec} 页 · style={model.get('style', 'business-blue')} · theme={model.get('theme', 'light')})")
    if missing:
        print("注意：模型不完整，正式交付前应回 AI 对话补全（页面预览模态含可复制提示词）。")
    print("下一步：")
    print(f'  NODE_PATH=<pptxgenjs 所在 node_modules> <node> scripts/build_pptx.js "报告.pptx" --model="{out}"')
    return 0


if __name__ == '__main__':
    sys.exit(main())
