#!/usr/bin/env python3
"""md → X 长文可粘贴纯文本。

把 Markdown 原稿转成可直接粘贴进 X Article 编辑器的纯文本：
标题/正文保留，排版标记剥离，图片转为 [图N] 占位。

用法：
    python3 md2x.py <输入.md> --out <输出/X发布稿.txt>

规则见 references/x-format.md。
"""
import argparse
import re
import sys
from pathlib import Path


def convert(md: str):
    images = []
    out_lines = []
    in_code = False

    def img_repl(m):
        alt = m.group(1).strip()
        images.append(alt)
        return f"[图{len(images)}]"

    for raw in md.splitlines():
        line = raw.rstrip()

        # 分割线 → 空行（frontmatter 已在 main() 去除，这里只剩正文分隔线）
        if re.match(r"^(\*{3,}|-{3,}|_{3,})\s*$", line):
            out_lines.append("")
            continue

        # 代码块：去围栏，内容缩进保留
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            out_lines.append("    " + line)
            continue

        # 图片占位
        line = re.sub(r"!\[([^\]]*)\]\([^)]*\)", img_repl, line)

        # 标题 → 纯文本行
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out_lines.append("")
            out_lines.append(m.group(2).strip())
            out_lines.append("")
            continue

        # 引用 → 纯文本
        line = re.sub(r"^>\s?", "", line)

        # 分割线 → 空行
        if re.match(r"^(\*{3,}|-{3,}|_{3,})\s*$", line):
            out_lines.append("")
            continue

        # 表格行 → "项：值" 列表
        if "|" in line and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                continue
            label = cells[0]
            rest = "，".join(c for c in cells[1:] if c)
            out_lines.append(f"{label}：{rest}" if rest else label)
            continue

        # 行内标记剥离（先 *** 再 ** 再 *，防残留）
        line = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", line)  # 粗斜体
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)      # 加粗
        line = re.sub(r"__(.+?)__", r"\1", line)
        line = re.sub(r"\*(.+?)\*", r"\1", line)          # 斜体
        line = re.sub(r"`(.+?)`", r"\1", line)            # 行内代码
        line = re.sub(r"~~(.+?)~~", r"\1", line)          # 删除线
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1（\2）", line)  # 链接
        line = re.sub(r"^(\s*)- \[ \]\s+", r"\1- ", line)  # 任务列表
        line = re.sub(r"^(\s*)- \[x\]\s+", r"\1- ", line, flags=re.I)

        out_lines.append(line)

    # 压缩 3+ 空行为 2 个
    text = "\n".join(out_lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    # 文末附图注清单
    if images:
        text += "\n—— 配图清单 ——\n"
        for i, alt in enumerate(images, 1):
            text += f"[图{i}] {alt or '（未写图注）'}\n"

    return text, images


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="输入 Markdown")
    ap.add_argument("--out", required=True, help="输出 X发布稿.txt")
    args = ap.parse_args()

    inp = Path(args.input)
    if not inp.is_file():
        sys.exit(f"错误：找不到输入文件 {inp}")
    md = inp.read_text(encoding="utf-8")
    # 去掉首尾 frontmatter 块
    md = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)
    text, images = convert(md)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")

    chars = len(text.replace("\n", ""))
    print(f"OK {out}")
    print(f"正文约 {chars} 字，配图 {len(images)} 张")


if __name__ == "__main__":
    main()
