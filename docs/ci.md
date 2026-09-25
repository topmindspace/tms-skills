# CI / Release 说明

## 工作流

| 工作流 | 触发 | 做什么 |
|--------|------|--------|
| **CI** (`.github/workflows/ci.yml`) | `push`/`pull_request`（main） | 隐私扫描 · 安装器冒烟 · 技能门禁 |
| **Release** (`.github/workflows/release.yml`) | `push` tag `v*` | 同上技能门禁 → 打包 zip → GitHub Release → npm publish → 修剪旧 Release（留 2） |

并发：CI 同 ref `cancel-in-progress`；Release 不取消（避免发一半被掐）。

## 技能门禁（单一事实源）

`scripts/ci_skill_gates.sh` 被 CI 与 Release **共用**：

```bash
bash scripts/ci_skill_gates.sh --with-pptx
```

对每个发现的技能目录依次：

1. `npm ci`（或 `npm install`）
2. `package_skill.py --check` + `audit_{styles,docs,skill,css}.py`
3. （`--with-pptx`）轻量回归 fixture：`build_pptx.js` 用 `assets/examples/2026-09-09-research-mckinsey.model.json`
4. `negative_tests.py`
5. （`--with-pptx`）`bash scripts/smoke_pptx.sh`（extract → build → `validate_pptx --strict`）
6. （若存在）`test_feedback_gates.py`

`python-pptx` **仅在需要 PPTX 步骤时**安装。完整 `regression.py`（playwright）仍本地跑，不进 CI。

### 本地复现

```bash
# 单技能冒烟（应 exit 0）
cd top-ppt-html && bash scripts/smoke_pptx.sh; echo $?

# 与 CI 同款全门禁
bash scripts/ci_skill_gates.sh --with-pptx

# 仓库级
npm run check && npm run audit && npm run privacy
```

冒烟失败时 stderr 先打 **错误码 / 页码 / 短消息**，完整 JSON 在 `$TMPDIR/top-ppt-html-smoke/*.validate.json`。

## npm publish 幂等

Release 的 publish 步骤：

1. 无 `NPM_TOKEN` → 跳过（exit 0；GitHub Release 仍成功）
2. `npm view pkg@version` 已存在 → 跳过（exit 0）
3. `npm publish` 返回 **E409 / previously staged|published** → 视为成功（exit 0）
4. 其它错误 → 失败

因此「agent 机器已抢先 publish、CI 再跑」不会把 Release job 打红。

## 重跑

- PR / push：GitHub Actions → 对应 workflow → **Re-run failed jobs** / **Re-run all jobs**
- 发版：修好后推新 commit + 新 tag（npm 版本不可覆盖；已发布号走上面的幂等路径）
- 本地：修完再跑 `smoke_pptx.sh` 与 `ci_skill_gates.sh --with-pptx`，确认 exit 0 再推

## 红线（勿为过 CI 而削弱）

- 反截断 / 文本溢出门禁
- 图表多样性地板
- Mode A 大气正式 craft
- runtime SHA 同版本门禁
