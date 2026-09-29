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

    if fails:
        print(f"\n[negative_tests] {len(fails)} 项失败")
        sys.exit(1)
    print("\n[negative_tests] 全部通过")


if __name__ == "__main__":
    main()
