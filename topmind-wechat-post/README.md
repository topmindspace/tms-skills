# topmind-wechat-post · 公众号创作技能

[English](./README.en.md) | 中文

公众号文章全生命周期：交付包、审校改写、质量三关、状态同步、微信内联排版与发布清单。

## 安装

```bash
npx @topmindspace/tms-skills install topmind-wechat-post
```

## 用法

```bash
export TOPMIND_WORKSPACE=/path/to/workspace   # 推荐；或用 --base 指定交付包根

# 新建交付包
python3 scripts/new-article.py --slug demo --title "标题" --direction reverse

# 排版体检 + 自动修复
python3 scripts/lint-wechat.py --input <包>/公众号稿.md --fix

# 去 AI 味扫描（目标 ≥85）
python3 scripts/scan_ai_flavor.py <包>/公众号稿.md

# Markdown → 全内联 HTML（必加 --embed-images，否则粘贴丢图）
python3 scripts/md2wechat.py --input <包>/公众号稿.md --out-dir <包> --slug demo --embed-images

# 状态同步
python3 scripts/sync-status.py --set 定稿 <包> --apply
```

脚本纯 Python 标准库，零依赖。

## 三条路径

- **forward**：底稿 → 公众号（审校改写）
- **reverse**：选题原创 → 公众号 → 可选回推
- **站外拉取**：在线精选站 → 按 reverse 处理

## 质量三关

事实（一手来源）/ 逻辑（结构一致）/ 文字（去 AI 味 ≥85）。

## 外部依赖

本技能工作流会路由到以下**仓库外**技能（不含于本仓库，一般随用户侧 workbuddy
环境提供）。缺失时对应能力降级/不可用，不影响本仓库脚本的全部功能：

- `humanizer-zh`：中文去 AI 味的保真边界；缺失时「只去 AI 味不排版」路径不可用。
- `qu-aiwei-zh`：中文去 AI 味扫描定位；`scripts/scan_ai_flavor.py` 与其同源，
  缺失时可用仓库内脚本替代，扫描定位能力降级。

## 开发

```bash
python3 scripts/package_skill.py --check
python3 scripts/negative_tests.py
```
