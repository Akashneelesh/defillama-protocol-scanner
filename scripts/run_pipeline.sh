#!/usr/bin/env bash
# End-to-end pipeline: fetch → filter → verify → render.
#
# Env:
#   GH_TOKEN   GitHub token for higher rate limit (gh auth token works)
#   TVL_MIN    minimum TVL in USD (default 300000)
#   TVL_MAX    maximum TVL in USD (default 5000000)
set -euo pipefail

cd "$(dirname "$0")/.."

TVL_MIN="${TVL_MIN:-300000}"
TVL_MAX="${TVL_MAX:-5000000}"

if [ -z "${GH_TOKEN:-}" ] && command -v gh >/dev/null 2>&1; then
    if gh auth status >/dev/null 2>&1; then
        GH_TOKEN="$(gh auth token)"
        export GH_TOKEN
    fi
fi

echo "[$(date -u +%FT%TZ)] starting pipeline (TVL ${TVL_MIN}-${TVL_MAX})"
python3 scripts/01_fetch_protocols.py
python3 scripts/02_filter_tvl_band.py --min "$TVL_MIN" --max "$TVL_MAX"
python3 scripts/03_verify_github.py
python3 scripts/04_render_report.py
echo "[$(date -u +%FT%TZ)] done"
