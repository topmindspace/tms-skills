# topmind-briefs · 干货短文（公众号 + X 双平台）

[English](./README.en.md) | 中文

一件事，一张图，讲完就停。干货向短文：数据榜单、论文一句话解读、新品速递——
X 一帖或短 thread，公众号约 300–800 字，双版一键复制 HTML。

- 版本：**v0.2.1**（与 `@topmindspace/topmind-writing-skills@0.7.6` 同 tag）

## 安装

```bash
npx @topmindspace/topmind-writing-skills install topmind-briefs
```

## 用法

```bash
# X 版（图片顺序从公众号稿派生，禁止手工拼 --images）
md2x-html.py X短文.md --out X短文.html --images-from 公众号短文.md

# 公众号版（图片 base64 内嵌）
md2wechat.py 公众号短文.md --out 公众号版.html --embed-images
```

脚本分别在 `topmind-x-article` 与 `topmind-wechat-post` 两个技能的脚本目录下
（与本技能同级目录）。工作流细节见 [SKILL.md](./SKILL.md)。

## 内容类型

- 数据榜单型 / 榜单速报型 / 论文解读型 / 机制讲解型（见 SKILL.md，四种按真实帖子校准）
- 运营铁律：只起草不代发、数字必有来源、厂商数字标口径、不洗稿

## 何时不用

X 长文 → `topmind-x-article`；公众号长文 → `topmind-wechat-post`；
个人向短帖 → `topmind-x-posts`（规划中，未发布）。
