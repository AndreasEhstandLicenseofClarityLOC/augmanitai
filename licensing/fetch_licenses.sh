#!/usr/bin/env bash
# fetch_licenses.sh — Download canonical license texts for AUGMANITAI
#
# This script fetches the authoritative license text for each license used
# by the AUGMANITAI project and saves them alongside the project's license
# application files.
#
# Usage:
#   cd licensing/
#   ./fetch_licenses.sh
#
# Requires: curl or wget

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

fetch() {
  local url="$1"
  local out="$2"
  echo "Fetching $url → $out"
  if command -v curl >/dev/null 2>&1; then
    curl -sSL "$url" -o "$out"
  elif command -v wget >/dev/null 2>&1; then
    wget -q "$url" -O "$out"
  else
    echo "ERROR: neither curl nor wget is available" >&2
    exit 1
  fi
  if [[ ! -s "$out" ]]; then
    echo "ERROR: download of $url failed or resulted in empty file" >&2
    rm -f "$out"
    exit 1
  fi
}

echo "Fetching canonical license texts for AUGMANITAI..."

fetch "https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.txt" \
      "LICENSE-data-canonical.txt"

fetch "https://www.apache.org/licenses/LICENSE-2.0.txt" \
      "LICENSE-code-apache-canonical.txt"

# MIT license canonical text from OSI
fetch "https://opensource.org/licenses/MIT" \
      "LICENSE-code-mit-canonical.html"
# Note: OSI does not ship a plain-text MIT; you may want to hand-edit a
# canonical MIT text from the HTML, or use the SPDX plain-text variant:
fetch "https://spdx.org/licenses/MIT.txt" \
      "LICENSE-code-mit-canonical.txt" || {
  echo "SPDX MIT plain-text not available; using HTML fallback."
}

echo ""
echo "Done. Downloaded files:"
ls -lh LICENSE-*-canonical.* 2>/dev/null || echo "(none)"

echo ""
echo "NEXT STEPS:"
echo "  1. Commit the canonical files alongside the summary LICENSE files"
echo "  2. Verify that LICENSE-summary.md still matches the canonical texts"
echo "  3. Update NOTICE if the acknowledgments section has changed"
