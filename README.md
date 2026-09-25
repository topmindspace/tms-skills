# tms-skills

**TopMindspace 智能体技能 monorepo** — 可安装的智能体技能集合，当前包含 **top-ppt-html**（优雅、大气、正式场合演讲/汇报演示文稿）。

让 idea 飞，好想法被看见。

## 技能一览

| 技能 | 版本 | 做什么 |
|------|------|--------|
| [`top-ppt-html`](./top-ppt-html/) | 0.1.5 | 优雅大气的正式场合演讲/汇报演示文稿：单文件 HTML + 版式保真可编辑 16:9 PPTX |

安装器包 [`@topmindspace/tms-skills`](https://www.npmjs.com/package/@topmindspace/tms-skills) 亦为 **0.1.5**（整仓发版：安装器与当前技能同 tag；未来多技能仍可各自演进，默认随仓库 release）。

更多技能以仓库根目录下的技能目录加入（每个目录含 `SKILL.md`）。

## 安装

两条通道，装出来同一套技能。**npm = 钉版本快照**；**GitHub = 跟仓库 HEAD**。


> **警告 / Warning**：不要安装 `@topmindspace/tms-skills@^2`。npm 上的 **2.0.0–2.1.1** 已弃用（仓库重置前的过时线）；当前线是 **0.1.x**（`latest` 指向 0.1.x）。请安装 `@topmindspace/tms-skills@0.1.x`。
>
> Do **not** install `^2`. Versions **2.0.0–2.1.1 are deprecated**; use **0.1.x** (`latest` tracks 0.1.x).


### npm（推荐）

```bash
npx @topmindspace/tms-skills list
npx @topmindspace/tms-skills install top-ppt-html
npx @topmindspace/tms-skills install top-ppt-html --to ./.claude/skills
npx @topmindspace/tms-skills@0.1.5 install top-ppt-html   # 钉版本
```

### GitHub 直装

```bash
npx github:topmindspace/tms-skills install top-ppt-html

git clone https://github.com/topmindspace/tms-skills.git
node tms-skills/bin/tms-skills.js install top-ppt-html
```

### 手工

解压 GitHub Release 的 `top-ppt-html.zip` 到技能目录。

安装器把根目录下的技能目录 `<id>/`（含 `SKILL.md`）复制到目标目录；智能体通过 frontmatter（`name` + `description`）发现技能。

默认探测顺序（`resolveDefaultTarget`）：项目级 `./.agents` → `./.claude` → `./.cursor` → `./.codex` → `./.mimocode`；再用户级 `~/.claude` → `~/.agents` → `~/.cursor` → `~/.codex`；都没有则落 `./.agents/skills`。也可用 `--to` 显式指定。

| 宿主 | 项目级 | 用户级 |
|------|--------|--------|
| 通用 / Codex | `.agents/skills` | `~/.agents/skills` |
| Claude Code | `.claude/skills` | `~/.claude/skills` |
| Cursor | `.cursor/skills`（兼读 `.agents`） | `~/.cursor/skills` |
| Codex 兼容 | `.codex/skills` | `~/.codex/skills` |
| 本仓库另含 | `.mimocode/skills` | — |

> **排错**：不要 `npm install <skill-id>`（技能 id 不是独立 npm 包）。「找不到包」→ 换 GitHub 直装，或 `--registry https://registry.npmjs.org/`。

### 可选依赖（仅 PPTX 精导）

HTML 生成零第三方依赖（Python 标准库）。PPTX 导出需要 Node + pptxgenjs：

```bash
cd <install-dir>/top-ppt-html
npm install
```

## 仓库结构

```
tms-skills/
├─ top-ppt-html/             # 技能（SKILL.md + assets + references + scripts + evals）
├─ bin/tms-skills.js         # CLI：list / install
├─ docs/                     # 发布规范
├─ scripts/                  # 仓库级工具（隐私扫描）
├─ .github/workflows/        # CI + Release
├─ package.json              # @topmindspace/tms-skills
├─ LICENSE · CHANGELOG.md · README.md
```

## 发布与同步

| 动作 | GitHub | npm |
|------|:------:|:---:|
| push 到 main | 立即可见 | **不变** |
| tag `vX.Y.Z` | Release + zip | **自动 publish** |

- **push 不会更新 npm**；必须 bump 版本并打 tag。
- **Release 只保留最近 2 个**（CI 只删旧 Release，**git tags 保留**）；npm 可钉任意历史版本。
- 安装器与技能 **版本各自独立**；默认 patch/minor，major 仅破坏性变更。

详见 [docs/PUBLISHING.md](./docs/PUBLISHING.md)。

## CI

| 工作流 | 触发 | 做什么 |
|--------|------|--------|
| `ci.yml` | push / PR | 打包门禁、审计、隐私扫描、CLI 冒烟 |
| `release.yml` | tag `v*` | 门禁 → zip → Release → npm publish（已存在则跳过）→ prune Release 留 2（tags 保留） |

```bash
npm run check && npm run audit && npm run privacy
```

## 开发新技能

1. 根目录建 `<skill-id>/`，`SKILL.md` 的 `name` 与目录一致。
2. 人类说明写 `README.md`；智能体入口保持 `SKILL.md`。
3. 发布前 `scripts/package_skill.py --check`。
4. 登记：根 README、`npm run sync:files`、`CHANGELOG.md`（CI 按发现的技能跑门禁，无需再硬编码）。

## 许可证

MIT © TopMindspace — [LICENSE](./LICENSE)
