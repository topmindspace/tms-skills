# topmind-briefs · Short-form briefs (WeChat + X)

**[中文](./README.md)** | English

One topic, one chart, then stop. Data-driven short posts: rankings, paper TL;DRs,
product launches — one X post or short thread, ~300–800 words on WeChat,
one-click-copy HTML for both.

- Version: **v0.2.1** (same tag as `@topmindspace/topmind-writing-skills@0.7.9`)

## Install

```bash
npx @topmindspace/topmind-writing-skills install topmind-briefs
```

## Usage

```bash
# X version (image order derived from the WeChat draft; never hand-order --images)
md2x-html.py brief-x.md --out brief-x.html --images-from brief-wechat.md

# WeChat version (images inlined as base64)
md2wechat.py brief-wechat.md --out brief-wechat.html --embed-images
```

The scripts live in the script directories of the `topmind-x-article` and
`topmind-wechat-post` skills (siblings of this skill). See [SKILL.md](./SKILL.md)
for the full workflow.

## Content types

- Data rankings / ranking alerts / paper explainers / mechanism explainers
  (four types calibrated against real posts, see SKILL.md)
- Operating rules: draft only, never auto-post; every number needs a source;
  vendor numbers labeled as vendor claims; no rewriting others' work

## When NOT to use

X long-form → `topmind-x-article`; WeChat long-form → `topmind-wechat-post`;
personal short posts → `topmind-x-posts` (planned, not released).
