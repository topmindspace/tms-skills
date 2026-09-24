#!/usr/bin/env bash
# Deprecate obsolete @topmindspace/tms-skills 2.x line on npm.
# Prefer: GitHub Actions workflow "Deprecate npm 2.x" (uses NPM_TOKEN).
# Or run manually after `npm login` / with NPM_TOKEN in env.
set -euo pipefail

MSG_EN="Obsolete after repo reset. Use @topmindspace/tms-skills@0.1.x (or latest on the 0.1 line). Do not install ^2."
MSG_ZH="仓库重置后 2.x 已废弃。请使用 @topmindspace/tms-skills@0.1.x（或当前 0.1 线 latest）。不要安装 ^2。"
MSG="${MSG_ZH} / ${MSG_EN}"

echo "Deprecating @topmindspace/tms-skills@2.x ..."
npm deprecate "@topmindspace/tms-skills@2.x" "$MSG"

for v in 2.0.0 2.0.1 2.0.2 2.1.0 2.1.1; do
  echo "Deprecating @topmindspace/tms-skills@${v} ..."
  npm deprecate "@topmindspace/tms-skills@${v}" "$MSG" || true
done

echo "Done. Verify with: npm view @topmindspace/tms-skills"
