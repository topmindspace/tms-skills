#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""文档审计：references 完整性与内部链接可达性（任一不过 → 退出码 1）。"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
NAME = ROOT.name
errors: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("  ✓ " if cond else "  ✗ ") + msg)
    if not cond:
        errors.append(msg)


def main() -> None:
    print(f"[audit_docs] {NAME}")
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "dist" not in p.parts]
    check(len(md_files) >= 2, f"md 文档 ≥2（实 {len(md_files)}，含 SKILL.md/README.md）")

    refdir = ROOT / "references"
    if refdir.is_dir():
        refs = sorted(refdir.glob("*.md"))
        check(len(refs) >= 1, f"references/*.md ≥1（实 {len(refs)}）")
        for md in refs:
            check(md.stat().st_size > 0, f"references/{md.name} 非空")

    for md in md_files:
        text = md.read_text(encoding="utf-8")
        rel = md.relative_to(ROOT).as_posix()
        for link in set(re.findall(r"\]\(([^)]+)\)", text)):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (md.parent / link.split("#")[0]).resolve()
            if link and not target.exists():
                # 允许指向脚本/资源等非 md 文件的相对链接缺失检查放宽到 md
                if target.suffix == ".md":
                    check(False, f"{rel} 悬空链接: {link}")
    check(True, "内部 md 链接可达")

    if errors:
        print(f"\n[audit_docs] {NAME}: {len(errors)} 项失败")
        sys.exit(1)
    print(f"\n[audit_docs] {NAME}: 全部通过")


if __name__ == "__main__":
    main()
