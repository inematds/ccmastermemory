#!/usr/bin/env bash
# SessionStart hook — injeta prime.md como additionalContext

set -euo pipefail

PRIME_PATH="$(dirname "$0")/prime.md"

if [[ ! -f "$PRIME_PATH" ]]; then
  echo "{}"
  exit 0
fi

# Le o prime.md e injeta como additionalContext no stdout (JSON)
CONTENT=$(cat "$PRIME_PATH")

# Escapa para JSON (python e mais confiavel que jq para escapar strings arbitrarias)
python3 -c "
import json, sys
content = '''$CONTENT'''
print(json.dumps({'hookSpecificOutput': {'hookEventName': 'SessionStart', 'additionalContext': content}}))
"
