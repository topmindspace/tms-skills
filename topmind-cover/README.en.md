# topmind-cover · Cover Art Generation

**[中文](./README.md)** | English

A reusable skill for generating cover art for X long-form posts and WeChat articles. Goal: **striking, eye-catching, theme-focused**.

## Install

```bash
npx @topmindspace/tms-skills install topmind-cover
```

## Usage

1. Input: article title + 3 theme keywords + platform (x / wechat / both)
2. Pick a style template from `references/cover-styles.md` and compose the prompt (write the title text into the prompt word for word)
3. Generate the image with the agent's image-generation capability (landscape 16:9, 8% margin on all sides)
4. Eyeball check: title text correct word for word, subject complete, theme legible at a glance
5. Crop and save:

```bash
python3 scripts/crop-cover.py <main-image> --slug <slug> --out-dir <package>/images/
# produces 00-封面.png (1200×675) + 00-封面-公众号.png (900×383, center crop)
```

## Sizes

| Platform | Size | Aspect |
|----------|------|--------|
| X Article cover | 1200×675 | 16:9 (master image) |
| WeChat cover large image | 900×383 | 2.35:1 (center crop) |

## Design rules

One image, one theme; subject fills 40%+ of the frame; big title ≤ 10 chars, high contrast; avoid clutter, tiny dense text, and competing subjects.

## Development

```bash
python3 scripts/package_skill.py --check
python3 scripts/negative_tests.py
```
