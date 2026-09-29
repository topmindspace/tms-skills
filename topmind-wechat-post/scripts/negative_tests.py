#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""topmind-wechat-post 异常输入测试：各脚本错误路径干净（任一失败 → 退出码 1）。"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
PY = sys.executable
fails: list[str] = []


def run(script: str, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run([PY, str(SCRIPTS / script), *args], capture_output=True, text=True, timeout=60)


def check(name: str, cond: bool, detail: str = "") -> None:
    print(("  ✓ " if cond else "  ✗ ") + name + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        fails.append(name)


def main() -> None:
    print("[negative_tests] topmind-wechat-post")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        # 1. lint 空文件不崩溃
        (td / "empty.md").write_text("", encoding="utf-8")
        r = run("lint-wechat.py", ["--input", str(td / "empty.md")])
        check("lint 空文件不崩溃", r.returncode == 0 and "Traceback" not in r.stderr, r.stderr[:100])

        # 2. md2wechat 缺失输入 → 非零干净报错
        r = run("md2wechat.py", ["--input", str(td / "nope.md"), "--out-dir", str(td), "--slug", "t"])
        check("md2wechat 缺失输入干净报错", r.returncode != 0 and "Traceback" not in r.stderr, r.stderr[:100])

        # 3. scan 空文件不崩溃
        r = run("scan_ai_flavor.py", [str(td / "empty.md")])
        check("scan 空文件不崩溃", r.returncode == 0 and "Traceback" not in r.stderr, r.stderr[:100])

        # 4. new-article --help 正常
        r = run("new-article.py", ["--help"])
        check("new-article --help 正常", r.returncode == 0, r.stderr[:100])

        # 5. sync-status 缺失包 → 非零干净报错
        r = run("sync-status.py", ["--set", "定稿", str(td / "nope-pkg")])
        check("sync-status 缺失包干净报错", r.returncode != 0 and "Traceback" not in r.stderr, r.stderr[:100])

        # 6. md2wechat 行内图片走图片管线（复制/embed/清单/计数）
        png = ("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk"
               "+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==")
        import base64 as _b64
        (td / "a.png").write_bytes(_b64.b64decode(png))
        (td / "inline.md").write_text(
            "# t\n\n段落 ![行内图](a.png) 后续文字。\n", encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "inline.md"),
                                 "--out-dir", str(td / "o6"), "--slug", "t6",
                                 "--embed-images"])
        html = (td / "o6" / "t6-公众号版.html").read_text(encoding="utf-8")
        manifest = (td / "o6" / "图片上传清单.md").read_text(encoding="utf-8")
        check("md2wechat 行内图片被内嵌", r.returncode == 0 and
              "data:image/png;base64," in html, r.stdout[:200])
        check("md2wechat 行内图片进清单", "a.png" in manifest)

        # 7. md2wechat 大写数字序号同样被剥离
        (td / "num.md").write_text(
            "# t\n\n## 第叁章 大写序号\n\n正文。\n", encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "num.md"),
                                 "--out-dir", str(td / "o7"), "--slug", "t7"])
        html = (td / "o7" / "t7-公众号版.html").read_text(encoding="utf-8")
        check("md2wechat 大写数字序号剥离",
              "第叁章" not in html and ">01</span>" in html)

        # 8. md2wechat 分隔线不触发自家合规 WARN（inline-block）
        (td / "hr.md").write_text("# t\n\n---\n\n正文。\n", encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "hr.md"),
                                 "--out-dir", str(td / "o8"), "--slug", "t8"])
        check("md2wechat 分隔线无 inline-block 告警",
              "inline-block" not in r.stdout, r.stdout[:200])

        # 9. 括号 URL 不被截断（链接与图片；历史 bug：`![a](img(1).png)` 被截成
        #    `img(1` 导致真实文件记成缺失；`[维基](…/猫_(动物))` 的 URL 被截断、
        #    正文多个悬挂 `)`；`[t](url "title")` 被原样保留）
        (td / "img(1).png").write_bytes(_b64.b64decode(png))
        (td / "paren.md").write_text(
            "# t\n\n![括号图](img(1).png)\n\n"
            "[维基](https://zh.wikipedia.org/wiki/猫_(动物)) 与 "
            "[带title](https://example.com/a \"标题文字\")。\n",
            encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "paren.md"),
                                 "--out-dir", str(td / "o9"), "--slug", "t9",
                                 "--no-toc", "--signature", "off"])
        html = (td / "o9" / "t9-公众号版.html").read_text(encoding="utf-8")
        check("md2wechat 括号图片不截断",
              'src="images/img(1).png"' in html and (td / "o9" / "images" / "img(1).png").exists(),
              r.stdout[:200])
        check("md2wechat 括号链接不截断",
              "猫_(动物)" in html and ")</sup>" not in html,
              r.stdout[:200])
        check("md2wechat title 链接被转换",
              "https://example.com/a" in html and '[带title](' not in html,
              r.stdout[:200])

        # 10. 脚注 URL 的 & 不双重转义（历史 bug：显示成 &amp;）
        (td / "amp.md").write_text(
            "# t\n\n[和号](https://x.com/?a=1&b=2)\n", encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "amp.md"),
                                 "--out-dir", str(td / "o10"), "--slug", "t10",
                                 "--no-toc", "--signature", "off"])
        html = (td / "o10" / "t10-公众号版.html").read_text(encoding="utf-8")
        check("md2wechat 脚注 URL 不双重转义",
              "a=1&amp;b=2" in html and "&amp;amp;" not in html)

        # 11. 坏主题 JSON 干净报错（历史 crash：json Traceback）
        (td / "bad-theme.json").write_text("{bad json", encoding="utf-8")
        (td / "t11.md").write_text("# t\n\n正文。\n", encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "t11.md"),
                                 "--out-dir", str(td / "o11"), "--slug", "t11",
                                 "--theme", str(td / "bad-theme.json")])
        check("md2wechat 坏主题 JSON 干净报错",
              r.returncode != 0 and "Traceback" not in r.stderr, r.stderr[:100])

        # 12. 目录当输入：文案明确（与 md2x 一致），非零干净退出
        r = run("md2wechat.py", ["--input", str(td),
                                 "--out-dir", str(td / "o12"), "--slug", "t12"])
        check("md2wechat 目录输入文案正确",
              r.returncode != 0 and "输入是目录不是文件" in r.stderr
              and "Traceback" not in r.stderr, r.stderr[:100])

        # 13. yaml/diff 代码块不高亮 crash（历史 crash：(?m) 拼进 alternation
        #     报 "global flags not at the start"，任何 ```yaml 块都 Traceback）
        (td / "hl.md").write_text(
            "# t\n\n```yaml\nkey: value\n```\n\n```diff\n+add\n-del\n```\n",
            encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "hl.md"),
                                 "--out-dir", str(td / "o13"), "--slug", "t13"])
        html = (td / "o13" / "t13-公众号版.html").read_text(encoding="utf-8")
        check("md2wechat yaml/diff 代码块不崩溃",
              r.returncode == 0 and "Traceback" not in r.stderr
              and "key" in html, r.stderr[:100])

        # 14. 嵌套围栏：```` 开栏不被内层 ``` 提前闭合
        (td / "nest.md").write_text(
            "# t\n\n````markdown\n外层\n```python\nprint(1)\n```\n结束\n````\n",
            encoding="utf-8")
        r = run("md2wechat.py", ["--input", str(td / "nest.md"),
                                 "--out-dir", str(td / "o14"), "--slug", "t14",
                                 "--no-toc", "--signature", "off"])
        html = (td / "o14" / "t14-公众号版.html").read_text(encoding="utf-8")
        body = html.split('<article id="wx-body"')[1]
        check("md2wechat 嵌套围栏不提前闭合",
              r.returncode == 0 and "````markdown" not in body
              and body.count("MARKDOWN</section>") == 1, r.stderr[:100])

    if fails:
        print(f"\n[negative_tests] {len(fails)} 项失败")
        sys.exit(1)
    print("\n[negative_tests] 全部通过")


if __name__ == "__main__":
    main()
