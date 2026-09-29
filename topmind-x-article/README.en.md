# topmind-x-article · One-Click X Long-Form Publishing

**[中文](./README.md)** | English

Turn a Markdown draft into a "copy → paste → publish" X long-form (Article) package.

## Install

```bash
npx @topmindspace/tms-skills install topmind-x-article
```

## Usage

```bash
# 1. Draft → paste-ready plain text (the heart of one-click copying)
python3 scripts/md2x.py <draft>.md --out <package>/X发布稿.txt

# 2. Cover: generate a 1200×675 cover with topmind-cover

# 3. Follow references/publish-checklist.md item by item
```

## Conversion rules

The X Article editor has weak, unstable markdown support, so `md2x.py` converts to plain text per `references/x-format.md`: headings → plain text lines, bold/italic markers removed, links → `text（url）`, images → `[图N]` (image list appended at the end), tables → "item: value" lists.

Read the result through once by hand after converting.

## Publishing

X long-form posts are currently published by hand-pasting into the X Article editor; the API does not publish long-form. After publishing, do per the checklist: pin a first comment with the extra info, fetch the full text back for verification.

## Development

```bash
python3 scripts/package_skill.py --check   # pre-publish check
python3 scripts/negative_tests.py          # bad-input tests
```
