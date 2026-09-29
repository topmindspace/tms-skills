#!/usr/bin/env python3
"""md2x-html.py — Markdown 原稿 → 可直接复制的 X 长文 HTML（单文件）。

用法：
    python3 md2x-html.py 原稿.md --out X长文.html \\
        --images 样张1.png 样张2.png ... [--cover cover-1200x675.png]

约定（与 md2x.py 对齐）：
- `[图N]` 独占一行 → 按顺序取 --images[N-1]，转成内嵌 data-URI 的 <figure>
- ``` 围栏代码块（直出提示词）→ <blockquote> + 「复制提示词」按钮。
  原因：X 文章编辑器没有"粘贴 <pre> 即代码块"的识别，原生代码块只能走
  Insert 菜单；<blockquote> 粘贴后即 X 原生引用块，格式不丢、读者全选即拷
- `#` → h1（X 标题栏专用，复制全文时自动剔除）；`##`/`###` → h2/h3
  （对应 X 的"标题/副标题"两级）
- `- ` / `1. ` → ul/ol；`**x**` → strong；`` `x` `` → code（X 粘贴后变纯文本）；
  `---` → hr（X 粘贴可能丢弃，需手动 Insert → 分割线，见 references/x-html-format.md）
- GFM 表格 → ul.xtable（X 粘贴会丢弃 <table>，转列表保内容）
- frontmatter（--- ... ---）跳过，只取 title

设计目标（对标 md2wechat 的公众号体验）：
- 文本+格式：页顶「一键复制全文」按钮 → 剪贴板富文本 → 粘贴进 X 文章编辑器。
  复制前自动剔除按钮/UI 与 .no-paste 块（标题、封面预览），只剩 X 可识别的
  语义标签：h2/h3/p/ul/ol/blockquote/a/hr/img
- 图片：data-URI 内嵌（X 若支持则随粘贴带入）；每张图带 [图N] 编号 + 「下载图片」
  按钮保底，图片没跟过去时按编号下载再上传，不用找文件、不用对顺序
- 封面：X 有独立封面上传入口，始终单独文件；HTML 顶部仅作预览 + 下载链接

只用 Python 标准库。
"""

import argparse
import base64
import html
import os
import re
import sys

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body { margin: 0; background: #f7f9fa; color: #0f1419;
       font-family: -apple-system, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif; }
.toolbar { position: sticky; top: 0; z-index: 50; background: rgba(255,255,255,.96);
           border-bottom: 1px solid #eff3f4; padding: 10px 16px;
           display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.toolbar .hint { font-size: 13px; color: #536471; }
.toolbar .steps { font-size: 13px; color: #0f1419; font-weight: 700; }
.btn { appearance: none; border: 1px solid #cfd9de; background: #fff; color: #0f1419;
       border-radius: 9999px; padding: 8px 18px; font-size: 14px; font-weight: 700;
       cursor: pointer; }
.btn.primary { background: #0f1419; color: #fff; border-color: #0f1419; }
.btn:active { transform: scale(.97); }
.article { max-width: 680px; margin: 0 auto; background: #fff;
           padding: 32px 28px 64px; }
.article h1 { font-size: 26px; line-height: 1.4; margin: 0 0 20px; }
.article h2 { font-size: 20px; margin: 34px 0 12px; padding-top: 6px; }
.article h3 { font-size: 18px; margin: 26px 0 10px; }
.article p { font-size: 17px; line-height: 1.85; margin: 0 0 14px; word-break: break-word; }
.article ul, .article ol { font-size: 17px; line-height: 1.85; margin: 0 0 14px; padding-left: 1.4em; }
.article hr { border: none; border-top: 1px solid #eff3f4; margin: 28px 0; }
.article a { color: #1d9bf0; }
.article code { background: #f1f3f4; border-radius: 4px; padding: 1px 6px;
                font-size: .92em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.article ul.xtable { list-style: none; padding-left: 0; }
.article ul.xtable li { background: #f7f9fa; border: 1px solid #eff3f4;
                       border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; }
.cover-note { background: #f7f9fa; border: 1px dashed #cfd9de; border-radius: 12px;
              padding: 14px 16px; font-size: 14px; color: #536471; margin-bottom: 24px; }
.cover-note img { width: 100%; border-radius: 8px; display: block; margin-bottom: 10px; }
figure.ximg { margin: 22px 0; }
figure.ximg img { width: 100%; border-radius: 10px; display: block;
                 border: 1px solid #eff3f4; }
figure.ximg figcaption { display: flex; justify-content: space-between; align-items: center;
                        margin-top: 8px; font-size: 13px; color: #536471; }
.prompt { position: relative; margin: 14px 0 20px; }
.prompt blockquote { margin: 0; background: #f7f9fa; border-left: 4px solid #1d9bf0;
                     border-radius: 0 10px 10px 0; padding: 16px 18px;
                     font-size: 14px; line-height: 1.8; }
.prompt blockquote code { background: none; padding: 0; font-size: 1em;
                         font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.prompt .btn { position: absolute; top: 8px; right: 8px; padding: 5px 12px;
               font-size: 12px; }
.toast { position: fixed; left: 50%; bottom: 40px; transform: translateX(-50%);
         background: #0f1419; color: #fff; font-size: 14px; padding: 10px 20px;
         border-radius: 9999px; opacity: 0; transition: opacity .25s; pointer-events: none; }
"""

JS = """
function toast(msg){ var t=document.getElementById('toast'); t.textContent=msg;
  t.style.opacity=1; setTimeout(function(){ t.style.opacity=0; }, 1800); }
function cleanClone(){
  var el=document.getElementById('article');
  var c=el.cloneNode(true);
  var kill=c.querySelectorAll('button, .no-paste');
  for(var i=0;i<kill.length;i++){ kill[i].parentNode.removeChild(kill[i]); }
  return c;
}
async function copyArticle(){
  var c=cleanClone();
  var htm='<meta charset="utf-8">'+c.innerHTML;
  try{
    var item=new ClipboardItem({
      'text/html': new Blob([htm],{type:'text/html'}),
      'text/plain': new Blob([c.innerText],{type:'text/plain'})
    });
    await navigator.clipboard.write([item]);
    toast('已复制全文（含格式），去 X 粘贴吧');
  }catch(e){
    try{ await navigator.clipboard.writeText(c.innerText); toast('已复制纯文本（富文本复制失败）'); }
    catch(e2){ toast('复制失败，请手动全选复制'); }
  }
}
async function copyPrompt(btn){
  var code=btn.parentElement.querySelector('code').innerText;
  try{ await navigator.clipboard.writeText(code); toast('提示词已复制，去 AI 生图工具粘贴'); }
  catch(e){ toast('复制失败，请手动复制'); }
}
function dlImg(btn){
  var img=btn.closest('figure').querySelector('img');
  var a=document.createElement('a');
  a.href=img.src; a.download=btn.getAttribute('data-fname');
  document.body.appendChild(a); a.click(); a.remove();
  toast('开始下载 '+btn.getAttribute('data-fname'));
}
function dlCover(btn){
  var img=document.querySelector('#coverbox img');
  var a=document.createElement('a');
  a.href=img.src; a.download=btn.getAttribute('data-fname');
  document.body.appendChild(a); a.click(); a.remove();
  toast('封面开始下载');
}
"""

HTML_TMPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="toolbar">
  <span class="steps">1. 标题填入 X 标题栏 → 2. 一键复制全文 → 3. 粘贴到 X 正文</span>
  <button class="btn primary" onclick="copyArticle()">一键复制全文</button>
  <span class="hint">图片随粘贴带入则直接用；没带入就按 [图N] 下载上传。封面始终单独上传。</span>
</div>
<article class="article" id="article">
{body}
</article>
<div class="toast" id="toast"></div>
<script>{js}</script>
</body>
</html>
"""


def data_uri(path):
    with open(path, "rb") as f:
        raw = f.read()
    ext = os.path.splitext(path)[1].lower()
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "webp": "image/webp", "gif": "image/gif"}.get(ext.lstrip("."), "image/png")
    return "data:%s;base64,%s" % (mime, base64.b64encode(raw).decode("ascii"))


def inline_md(s):
    """行内 markdown → html：加粗、行内代码、裸链接。"""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    s = re.sub(r"(https?://[^\s<>()\uff08\uff09\u3010\u3011\u300c\u300d\u300e\u300f]+)",
               r'<a href="\1">\1</a>', s)
    return s


def md_to_html(md_text, images, cover):
    lines = md_text.split("\n")
    out = []
    img_idx = 0
    cover_uri = data_uri(cover) if cover else None

    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1

    in_code = False
    code_buf = []
    in_ul = False
    in_ol = False
    in_table = False
    table_buf = []

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table():
        nonlocal in_table, table_buf
        if not in_table:
            return
        rows = []
        for r in table_buf:
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            rows.append(cells)
        rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", c or "-") for c in r)]
        if rows:
            out.append('<ul class="xtable">')
            for j, r in enumerate(rows):
                cells = " ｜ ".join(inline_md(c) for c in r)
                if j == 0:
                    out.append("<li><strong>%s</strong></li>" % cells)
                else:
                    out.append("<li>%s</li>" % cells)
            out.append("</ul>")
        in_table = False
        table_buf = []

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if s.startswith("```"):
            if not in_code:
                close_lists()
                flush_table()
                in_code = True
                code_buf = []
            else:
                in_code = False
                body = "\n".join(code_buf)
                esc = html.escape(body).replace("\n", "<br>")
                out.append(
                    '<div class="prompt"><blockquote><code>%s</code></blockquote>'
                    '<button class="btn" onclick="copyPrompt(this)">复制提示词</button>'
                    "</div>" % esc
                )
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if re.match(r"^\|.*\|\s*$", s) and "|" in s.strip("|"):
            if not in_table:
                close_lists()
                in_table = True
                table_buf = []
            table_buf.append(s)
            i += 1
            continue
        else:
            flush_table()

        m = re.fullmatch(r"\[图(\d+)\]", s)
        if m:
            close_lists()
            n = int(m.group(1))
            if 1 <= n <= len(images):
                uri = data_uri(images[n - 1])
                fname = "图%d-%s" % (n, os.path.basename(images[n - 1]))
                out.append(
                    '<figure class="ximg"><img src="%s" alt="图%d">'
                    '<figcaption><span class="cap">[图%d]</span>'
                    '<button class="btn" data-fname="%s" '
                    'onclick="dlImg(this)">下载图片</button></figcaption></figure>'
                    % (uri, n, n, html.escape(fname, quote=True))
                )
            else:
                out.append("<p>[图%d]（图片缺失）</p>" % n)
            img_idx = max(img_idx, n)
            i += 1
            continue

        if s.startswith("### "):
            close_lists()
            out.append("<h3>%s</h3>" % inline_md(s[4:]))
            i += 1
            continue
        if s.startswith("## "):
            close_lists()
            out.append("<h2>%s</h2>" % inline_md(s[3:]))
            i += 1
            continue
        if s.startswith("# "):
            close_lists()
            out.append('<h1 class="no-paste">%s</h1>' % inline_md(s[2:]))
            i += 1
            continue

        if s in ("---", "***"):
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append("<li>%s</li>" % inline_md(m.group(2)))
            i += 1
            continue

        if s.startswith("- "):
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append("<li>%s</li>" % inline_md(s[2:]))
            i += 1
            continue

        if not s:
            close_lists()
            i += 1
            continue

        close_lists()
        out.append("<p>%s</p>" % inline_md(s))
        i += 1

    close_lists()
    flush_table()

    body = "\n".join(out)

    cover_html = ""
    if cover_uri:
        cover_html = (
            '<div class="cover-note no-paste" id="coverbox">'
            '<img src="%s" alt="封面预览">'
            '<div>封面图预览（1200×675）。X 文章有独立封面上传入口，'
            '请单独上传，不要随正文粘贴。<br>'
            '<button class="btn" data-fname="cover-1200x675.png" '
            'onclick="dlCover(this)">下载封面图</button></div></div>'
        ) % cover_uri
    return cover_html + "\n" + body


def main():
    ap = argparse.ArgumentParser(description="Markdown 原稿 → X 长文 HTML（一键复制）")
    ap.add_argument("md", help="原稿 markdown 路径")
    ap.add_argument("--out", required=True, help="输出 HTML 路径")
    ap.add_argument("--images", nargs="*", default=[], help="[图N] 对应的图片路径（按顺序）")
    ap.add_argument("--cover", default=None, help="封面图路径（1200×675）")
    args = ap.parse_args()

    if not os.path.isfile(args.md):
        print("输入文件不存在：%s" % args.md, file=sys.stderr)
        sys.exit(1)

    with open(args.md, encoding="utf-8") as f:
        md_text = f.read()

    m = re.search(r"^#\s+(.+)$", md_text, re.M)
    title = m.group(1).strip() if m else "X长文"

    body = md_to_html(md_text, args.images, args.cover)
    page = HTML_TMPL.replace("{title}", html.escape(title), 1) \
                    .replace("{css}", CSS, 1) \
                    .replace("{body}", body, 1) \
                    .replace("{js}", JS, 1)

    out_dir = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(out_dir, exist_ok=True)
    tmp = args.out + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(page)
        os.replace(tmp, args.out)
    except OSError as e:
        print("写入失败：%s" % e, file=sys.stderr)
        sys.exit(1)
    print("已生成：%s" % args.out)


if __name__ == "__main__":
    main()
