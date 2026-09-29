# topmind-cover · Cover Art Generation

**[中文](./README.md)** | English

A reusable skill for generating cover art for X long-form posts and WeChat articles. Goal: **striking, eye-catching, theme-focused**.

## Install

```bash
npx @topmindspace/tms-skills install topmind-cover
```

## Usage

0. **Pick a style (3 steps, required)**: choose 1 of 6 styles from `references/cover-styles.md` by topic
   → check `assets/examples/<style>.png` to confirm the visual language
   → compose the prompt from that style's recipe (replace `{TITLE}` with the real title).
1. Input: article title + 3 theme keywords + platform (x / wechat / both, default both).
2. Generate with the agent's image-generation capability (landscape 16:9, 8% margin on all sides).
3. Eyeball check (required): title text correct word for word, subject complete, theme legible at a glance;
   title text and key subject stay inside the central vertical 60% safe zone (so the 900×383 center crop never cuts the title).
4. Crop and save:

```bash
python3 scripts/crop-cover.py <main-image> --out-dir <package>/images/
# produces 00-封面.png (1200×675) + 00-封面-公众号.png (900×383, center crop)
```

## Style library & examples

- **Style library** `references/cover-styles.md`: 6 styles (bold poster / futuristic tech / editorial magazine / minimalist / guochao illustration / cyber glitch art), each with use cases, hex palettes, font suggestions, Chinese+English prompt recipes, and pitfalls.
- **Example images** [assets/examples/](./assets/examples/): 12 (6 styles × 1200×675 master + 900×383 WeChat center-crop, ~6.4MB), shipped with the package, free to reuse or adapt (manifest + safe-zone notes + reuse terms in [assets/examples/README.md](./assets/examples/README.md)).
- **Safe-zone rule**: title text and key subject must stay inside the central vertical 60% safe zone (keep the top/bottom 13%+ free of title text), or the WeChat center crop will cut the title.

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
