# topmind-cover · Cover Art Generation

**[中文](./README.md)** | English

A reusable skill for generating cover art for X long-form posts and WeChat articles. Goal: **striking, eye-catching, theme-focused**.

## Style gallery

<p align="center">
  <img src="https://github.com/topmindspace/tms-skills/raw/main/topmind-cover/assets/examples/overview.png" alt="topmind-cover · 8 cover-style overview" width="960" />
</p>

| Style | Best for |
|-------|----------|
| Viral dry-goods `gan-huo` | Tested picks, reviews, roundups; default for first-person "I tried it all for you" posts |
| Giant-type manifesto `big-type` | Opinion pieces, deep essays, launch manifestos; default for one-sentence-stance pieces |
| Brand launch `brand-launch` | Product launches, version updates, official best practices / whitepapers; first choice when a brand is the subject |
| Tutorial steps `tutorial-steps` | Tutorials, onboarding guides, step-by-step walkthroughs, beginner-proof recipes |
| Fun IP `ip-fun` | Case studies, data recaps, retrospectives, series (part 1 / part 2) |
| News flash `news-flash` | News, flashes, hot-topic explainers, interview teasers, "myth-busting" angles |
| Minimal `minimal` | Essays, book reviews, light takes, lifestyle musings; WeChat "light reading" pieces |
| Editorial magazine `magazine` | In-depth interviews, profiles, business analysis, year-in-review; when "craft / trust" matters |

## Install

```bash
npx @topmindspace/tms-skills install topmind-cover
```

## Usage

0. **Pick a style (3 steps, required)**: choose 1 of 8 styles from `references/cover-styles.md` by topic
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

- **Style library** `references/cover-styles.md`: 8 styles (viral dry-goods / giant-type manifesto / brand launch / tutorial steps / fun IP / news flash / minimalist / editorial magazine), each with use cases, hex palettes, font suggestions, Chinese+English prompt recipes, and pitfalls.
- **Example images** [assets/examples/](./assets/examples/): 17 (8 styles × 1200×675 master + 900×383 WeChat center-crop + `overview.png` 8-grid overview, ~7.5MB), shipped with the package, free to reuse or adapt (manifest + safe-zone notes + reuse terms in [assets/examples/README.md](./assets/examples/README.md)).
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
