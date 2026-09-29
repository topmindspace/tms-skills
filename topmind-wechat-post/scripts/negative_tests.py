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

    if fails:
        print(f"\n[negative_tests] {len(fails)} 项失败")
        sys.exit(1)
    print("\n[negative_tests] 全部通过")


if __name__ == "__main__":
    main()
