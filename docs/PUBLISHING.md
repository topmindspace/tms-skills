# 发布与贡献规范

本仓库发布**智能体技能（agent skills）**，须可安全开源。

**双通道分发**（同一套技能）：

| 通道 | 命令 | 特点 |
|------|------|------|
| **npm** | `npx @topmindspace/tms-skills install <skill-id>` | 钉版本、日常推荐 |
| **GitHub** | `npx github:topmindspace/tms-skills install <skill-id>` | 跟 HEAD、可 clone |

- 包：<https://www.npmjs.com/package/@topmindspace/tms-skills>
- 仓库：<https://github.com/topmindspace/tms-skills>

当前线：安装器 **0.1.3** · 技能 top-ppt-html **0.1.3**（整仓同 tag 发版；见 CHANGELOG）。


## npm 2.x 弃用说明（仓库重置）

npm 上仍可能看到 `@topmindspace/tms-skills` 的 **2.0.0–2.1.1**。那是重置前的过时线；**不要安装 `^2`**。当前线是 **0.1.x**（`latest` 指向 0.1.x）。

维护者在已 `npm login` 的机器上执行：

```bash
bash scripts/deprecate-npm-2x.sh
```

（本仓库 CI / 无 npm 登录的环境无法代跑 deprecate。）


## 安装口径（文档与 CLI 一致）

| 优先级 | 命令 | 何时用 |
|--------|------|--------|
| **默认** | `npx @topmindspace/tms-skills install <skill-id>` | 日常 |
| 跟最新源 | `npx github:topmindspace/tms-skills install <skill-id>` | 要 HEAD |
| 备选 | `git clone` + `node tms-skills/bin/tms-skills.js install <skill-id>` | 离线 |
| 手工 | 解压 Release 的 `<skill-id>.zip` | 无 Node |

不要引导 `npm install <skill-id>`（技能 id 不是独立 npm 包）。

## 版本策略（务必遵守）

| 包 | 字段 | 规则 |
|----|------|------|
| 安装器 | 根 `package.json` `version` | **独立** semver |
| 技能 | `<skill-id>/package.json` + `scripts/layout-constants.json` `version`（事实源）+ `model-schema.json` / `layoutSlots` 同值 | **独立** semver |

- **默认只升 patch / minor**（修 bug、加能力、改文案）。
- **major 仅用于破坏性变更**：技能 id、CLI 名、注入标记、安装路径、不兼容模型字段。
- **禁止**无实质变更时跳大版本；禁止用版本号表达心情。
- npm 版本发布后不可覆盖；有变更就要新号。

## GitHub ≠ npm

| 动作 | GitHub | npm |
|------|:------:|:---:|
| `git push` | 更新 | **不变** |
| `git tag vX.Y.Z && git push --tags` | Release + zip | **自动 publish** |

**Release 保留策略：最多 2 个最近版本**（CI 只通过 API 删除更旧 **Release**；**git tags 保留**，便于历史追溯与 npm 对照）。npm 历史版本可钉。

## 发布流程

1. 更新 `CHANGELOG.md`。
2. 按上表 bump 对应包的版本（多处同值）。
3. 门禁：
   ```bash
   npm run check && npm run audit && npm run privacy
   ```
4. 新技能：`npm run sync:files`（把发现的技能目录写入 `package.json` `files`）。
5. 提交并打 tag：
   ```bash
   git tag vX.Y.Z
   git push origin main --tags
   ```
   CI：门禁 → 技能 zip → GitHub Release → `npm publish`（版本已存在则跳过）→ prune Releases（留 2，tags 保留）。
6. 验证：`npm view @topmindspace/tms-skills version`

### 手工 publish

```bash
npm publish --access public --registry https://registry.npmjs.org/
```

Secret **`NPM_TOKEN`**（granular，scope `@topmindspace` 写权限）配置在 GitHub Actions；未配置则跳过 npm 步骤。

## 命名

| 面 | 规则 | 示例 |
|----|------|------|
| 技能 id / 目录 / frontmatter `name` | kebab-case，三处一致 | `top-ppt-html` |
| 品牌展示名 | 简短 | `TopPPT HTML` |
| 环境变量 | `TOP_PPT_*` | `TOP_PPT_NODE_EXE` |
| 注入标记 | `__TOPPPT_*__` | `__TOPPPT_CONSTANTS__` |
| JS API | PascalCase | `TopPptHtml` |
| npm | `@topmindspace/*` | `@topmindspace/tms-skills` |
| CLI | 与仓库名一致 | `tms-skills` |

新代码禁止历史遗留标识（扫描器拦截）；文档不写更名流水账。

## 隐私检查清单

- [ ] 无绝对本地路径 / 用户名 / 主机名 / 凭据
- [ ] 扫描器不硬编码真实机器信息（本地词表 `scripts/.privacy-deny.local`，不入库）
- [ ] 无 IDE / 智能体本机状态、`node_modules`、`dist`、`scripts/_*`
- [ ] `SKILL.md` description ≤ 1024，含「做什么 + 何时用 + 何时不用」
- [ ] 根 `package.json` 的 `files` 覆盖全部技能目录

```bash
npm run privacy
```

## 打包矩阵

| 类别 | 技能 zip | npm 包 | git |
|------|:--------:|:------:|:---:|
| `SKILL.md` / `README.md` / `package.json` | ✅ | ✅ | ✅ |
| `assets/` `references/` `scripts/` `evals/` | ✅ | ✅ | ✅ |
| `bin/` | ❌ | ✅ | ✅ |
| 根 `docs/` | ❌ | ❌ | ✅ |
| `dist/` `node_modules/` 缓存 | ❌ | ❌ | ❌ |
| 临时 `scripts/_*` · `.privacy-deny.local` | ❌ | ❌ | ❌ |

## 新增技能

1. 根目录建 `<new-id>/SKILL.md`，`name` 与目录一致。
2. 附 `README.md`、`package.json`；有工具则 `package_skill.py --check`。
3. 登记 README 技能表、`npm run sync:files`、CHANGELOG（CI/Release 动态发现技能）。
4. 隐私清单全绿。

## 排错

| 现象 | 处理 |
|------|------|
| `ENEEDAUTH` | `npm login --registry https://registry.npmjs.org/` |
| `403` 2FA | granular token 或 `--otp` |
| `403` cannot publish over version | 已存在 → bump |
| Public 但 registry 404 | 索引延迟 / 指定官方 registry |
| 发到镜像站 | publish 只用 `registry.npmjs.org` |
| tag 后 npm 未发 | 查 Actions 与 `NPM_TOKEN` |
