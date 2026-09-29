#!/usr/bin/env python3
"""md2x-html.py — Markdown 原稿 → 可直接复制的 X 长文 HTML（单文件）。

用法：
    python3 md2x-html.py 原稿.md --out X长文.html \\
        --images 样张1.png 样张2.png ... [--cover cover-1200x675.png]

约定（与 md2x.py 对齐）：
- `[图N]` 独占一行 → 按顺序取 --images[N-1]，转成内嵌 data-URI 的 <figure>
- ``` 围栏代码块 → <pre> + 「复制提示词」按钮（一键复制该块纯文本）
- `#` / `##` → h1/h2；`- ` → ul；`**x**` → strong；`` `x` `` → code；`---` → hr
- frontmatter（--- ... ---）跳过，只取 title

设计目标（对标 md2wechat 的公众号体验）：
- 文本+格式：页顶「一键复制全文」按钮 → 剪贴板富文本 → 粘贴进 X 文章编辑器
- 图片：data-URI 内嵌（X 若支持则随粘贴带入）；每张图带 [图N] 编号 + 「下载图片」
  按钮保底，图片没跟过去时按编号下载再上传，不用找文件、对顺序
- 封面：X 有独立封面上传入口，始终单独文件；HTML 顶部仅作预览 + 下载链接

只用 Python 标准库。
"""

import argparse
import base64
import html
import io
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
.btn { appearance: none; border: 1px solid #cfd9de; background: #fff; color: #0f1419;
       border-radius: 9999px; padding: 8px 18px; font-size: 14px; font-weight: 700;
       cursor: pointer; }
.btn.primary { background: #0f1419; color: #fff; border-color: #0f1419; }
.btn:active { transform: scale(.97); }
.article { max-width: 680px; margin: 0 auto; background: #fff;
           padding: 32px 28px 64px; }
.article h1 { font-size: 26px; line-height: 1.4; margin: 0 0 20px; }
.article h2 { font-size: 20px; margin: 34px 0 12px; padding-top: 6px; }
.article p { font-size: 17px; line-height: 1.85; margin: 0 0 14px; word-break: break-word; }
.article ul { font-size: 17px; line-height: 1.85; margin: 0 0 14px; padding-left: 1.4em; }
.article hr { border: none; border-top: 1px solid #eff3f4; margin: 28px 0; }
.article code { background: #f1f3f4; border-radius: 4px; padding: 1px 6px;
                font-size: .92em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.cover-note { background: #f7f9fa; border: 1px dashed #cfd9de; border-radius: 12px;
              padding: 14px 16px; font-size: 14px; color: #536471; margin-bottom: 24px; }
.cover-note img { width: 100%; border-radius: 8px; display: block; margin-bottom: 10px; }
figure.ximg { margin: 22px 0; }
figure.ximg img { width: 100%; border-radius: 10px; display: block;
                 border: 1px solid #eff3f4; }
figure.ximg figcaption { display: flex; justify-content: space-between; align-items: center;
                        margin-top: 8px; font-size: 13px; color: #536471; }
.prompt-wrap { position: relative; margin: 14px 0 20px; }
.prompt-wrap pre { background: #f7f9fa; border: 1px solid #eff3f4; border-radius: 10px;
                   padding: 16px; font-size: 13.5px; line-height: 1.75; overflow-x: auto;
                   white-space: pre-wrap; word-break: break-word; margin: 0;
                   font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
.prompt-wrap .btn { position: absolute; top: 8px; right: 8px; padding: 5px 12px;
                    font-size: 12px; }
.toast { position: fixed; left: 50%; bottom: 40px; transform: translateX(-50%);
         background: #0f1419; color: #fff; font-size: 14px; padding: 10px 20px;
         border-radius: 9999px; opacity: 0; transition: opacity .25s; pointer-events: none; }
"""

JS = """
function toast(msg){ var t=document.getElementById('toast'); t.textContent=msg;
  t.style.opacity=1; setTimeout(function(){ t.style.opacity=0; }, 1800); }
async function copyArticle(){
  var el=document.getElementById('article');
  var htm='<meta charset=\"utf-8\">'+el.innerHTML;
  try{
    var item=new ClipboardItem({
      'text/html': new Blob([htm],{type:'text/html'}),
      'text/plain': new Blob([el.innerText],{type:'text/plain'})
    });
    await navigator.clipboard.write([item]);
    toast('已复制全文（含格式），去 X 粘贴吧');
  }catch(e){
    try{ await navigator.clipboard.writeText(el.innerText); toast('已复制纯文本（富文本复制失败）'); }
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
  <button class="btn primary" onclick="copyArticle()">一键复制全文</button>
  <span class="hint">复制后去 x.com/compose/articles 粘贴；图片若没跟过去，用每张图下的「下载图片」按编号上传</span>
</div>
<article class="article" id="article">
{cover_block}
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


def inline_md(text):
    """行内：**粗体**、`代码`，先转义再替换。"""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    return text


def convert(md_text, images, cover=None):
    lines = md_text.split("\n")
    # 去 frontmatter
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is not None:
            lines = lines[end + 1:]
    out = []
    i, n = 0, len(lines)
    img_idx = 0
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    while i < n:
        line = lines[i]
        s = line.strip()

        if s.startswith("```"):
            close_list()
            buf = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # 跳过结束围栏
            code = html.escape("\n".join(buf).strip("\n"))
            out.append('<div class="prompt-wrap"><pre><code>%s</code></pre>'
                       '<button class="btn" onclick="copyPrompt(this)">复制提示词</button></div>' % code)
            continue
        if s.startswith("# "):
            close_list()
            out.append("<h1>%s</h1>" % inline_md(s[2:].strip()))
        elif s.startswith("## "):
            close_list()
            out.append("<h2>%s</h2>" % inline_md(s[3:].strip()))
        elif s == "---":
            close_list()
            out.append("<hr>")
        elif re.fullmatch(r"\[图\d+\]", s):
            close_list()
            num = int(re.fullmatch(r"\[图(\d+)\]", s).group(1))
            if 1 <= num <= len(images):
                uri = data_uri(images[num - 1])
                name = os.path.basename(images[num - 1])
                out.append(
                    '<figure class="ximg"><img src="%s" alt="图%d">'
                    '<figcaption><span>[图%d]</span>'
                    '<button class="btn" data-fname="图%d-%s" onclick="dlImg(this)">下载图片</button>'
                    "</figcaption></figure>" % (uri, num, num, num, html.escape(name)))
            else:
                out.append("<p>%s</p>" % html.escape(s))
        elif s.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>%s</li>" % inline_md(s[2:].strip()))
        elif s == "":
            close_list()
        else:
            close_list()
            out.append("<p>%s</p>" % inline_md(s))
        i += 1
    close_list()

    cover_block = ""
    if cover:
        uri = data_uri(cover)
        cover_block = (
            '<div class="cover-note" id="coverbox"><img src="%s" alt="封面">'
            "封面图请在 X 编辑器单独上传（X 有独立封面入口）。"
            '<button class="btn" data-fname="%s" onclick="dlCover(this)">下载封面</button></div>'
            % (uri, html.escape(os.path.basename(cover))))
    return "\n".join(out), cover_block


def main():
    ap = argparse.ArgumentParser(description="Markdown → X 长文 HTML（单文件，一键复制）")
    ap.add_argument("md", help="原稿 Markdown")
    ap.add_argument("--out", required=True, help="输出 HTML 路径")
    ap.add_argument("--images", nargs="*", default=[], help="[图N] 按顺序对应的图片")
    ap.add_argument("--cover", default=None, help="封面图（单独预览+下载，不占用[图N]编号）")
    args = ap.parse_args()

    with open(args.md, encoding="utf-8") as f:
        md_text = f.read()
    m = re.search(r"^title:\s*(.+)$", md_text, re.M)
    title = m.group(1).strip() if m else "X 长文"

    body, cover_block = convert(md_text, args.images, args.cover)
    out_html = HTML_TMPL.format(title=html.escape(title), css=CSS, js=JS,
                                cover_block=cover_block, body=body)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(out_html)

    chars = len(re.sub(r"\s+", "", re.sub(r"```.*?```", "", md_text, flags=re.S)))
    print("OK %s" % args.out)
    print("正文约 %d 字，配图 %d 张，HTML %.1f KB" % (chars, len(args.images), os.path.getsize(args.out) / 1024))


if __name__ == "__main__":
    main()
