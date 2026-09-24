#!/usr/bin/env bash
# TopPPT HTML · PPTX 轻量冒烟（Batch 2）
# extract_model → build_pptx → validate_pptx --strict --model=
# 用法: bash scripts/smoke_pptx.sh [example.html]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
HTML="${1:-assets/examples/2026-09-09-presentation-business-blue.html}"
if [[ ! -f "$HTML" ]]; then
  echo "smoke_pptx: missing $HTML" >&2
  exit 2
fi
STEM="$(basename "$HTML" .html)"
OUT_DIR="${TMPDIR:-/tmp}/top-ppt-html-smoke"
mkdir -p "$OUT_DIR"
MODEL="$OUT_DIR/${STEM}.model.json"
PPTX="$OUT_DIR/${STEM}.pptx"

echo "== smoke_pptx =="
echo "HTML  $HTML"
python3 scripts/extract_model.py "$HTML" "$MODEL"
echo "MODEL $MODEL ($(wc -c < "$MODEL") bytes)"

# Prefer local node_modules pptxgenjs
export NODE_PATH="${ROOT}/node_modules${NODE_PATH:+:$NODE_PATH}"
node scripts/build_pptx.js "$PPTX" --model="$MODEL"
echo "PPTX  $PPTX ($(wc -c < "$PPTX") bytes)"

python3 scripts/validate_pptx.py "$PPTX" --strict --model="$MODEL"
echo "smoke_pptx: OK"
