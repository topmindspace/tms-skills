# topmind-wechat-post · WeChat Article Authoring

**[中文](./README.md)** | English

Full lifecycle for WeChat articles: delivery package, review & rewrite, three quality gates, status sync, WeChat inline typography, and publish checklist.

## Install

```bash
npx @topmindspace/tms-skills install topmind-wechat-post
```

## Usage

```bash
export TOPMIND_WORKSPACE=/path/to/workspace   # recommended; or point the delivery package root with --base

# Create a new delivery package
python3 scripts/new-article.py --slug demo --title "标题" --direction reverse

# Typography lint + auto-fix
python3 scripts/lint-wechat.py --input <package>/公众号稿.md --fix

# De-AI-flavor scan (target ≥ 85)
python3 scripts/scan_ai_flavor.py <package>/公众号稿.md

# Markdown → fully inline HTML (--embed-images is mandatory, or pasted images go missing)
python3 scripts/md2wechat.py --input <package>/公众号稿.md --out-dir <package> --slug demo --embed-images

# Status sync
python3 scripts/sync-status.py --set 定稿 <package> --apply
```

Scripts use Python stdlib only — zero dependencies.

## Three paths

- **forward**: draft → WeChat article (review & rewrite)
- **reverse**: original topic → WeChat article → optional pushback
- **curated web**: online curated sources → handled as reverse

## Three quality gates

Facts (first-hand sources) / logic (structural consistency) / copy (de-AI-flavor ≥ 85).

## Development

```bash
python3 scripts/package_skill.py --check
python3 scripts/negative_tests.py
```
