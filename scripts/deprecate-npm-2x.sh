#!/usr/bin/env bash
# Deprecate obsolete @topmindspace/tms-skills 2.x line on npm.
# Run manually after `npm login` — this box / CI may not have npm auth.
#
# 弃用 npm 上过时的 2.x 线。须在已 npm login 的环境下由维护者手工执行。
set -euo pipefail

MSG_EN="Obsolete after repo reset. Use @topmindspace/tms-skills@0.1.x (or latest on the 0.1 line). Do not install ^2."
MSG_ZH="仓库重置后 2.x 已废弃。请使用 @topmindspace/tms-skills@0.1.x（或当前 0.1 线 latest）。不要安装 ^2。"
MSG="${MSG_ZH} / ${MSG_EN}"

echo "Deprecating @topmindspace/tms-skills@\"2.x\" ..."
npm deprecate "@topmindspace/tms-skills@\"2.x\"" "$MSG"

# Also deprecate concrete 2.x versions if they remain listed.
for v in 2.0.0 2.0.1 2.1.0 2.1.1; do
  echo "Deprecating @topmindspace/tms-skills@${v} ..."
  npm deprecate "@topmindspace/tms-skills@${v}" "$MSG" || true
done

echo "Done. Verify with: npm view @topmindspace/tms-skills versions --json"
