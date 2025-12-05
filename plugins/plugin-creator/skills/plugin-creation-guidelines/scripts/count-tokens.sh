#!/bin/bash
# Counts lines in agent files (proxy for token usage)
# Usage: bash count-tokens.sh <agent-file>

set -e

if [ $# -eq 0 ]; then
    echo "Error: Agent file path required"
    exit 1
fi

AGENT_FILE="$1"

if [ ! -f "$AGENT_FILE" ]; then
    echo "Error: File not found: $AGENT_FILE"
    exit 1
fi

# Count lines
LINE_COUNT=$(wc -l < "$AGENT_FILE")

# Provide status based on line count
if [ $LINE_COUNT -ge 300 ] && [ $LINE_COUNT -le 400 ]; then
    echo "$LINE_COUNT lines ✅ Within recommended 300-400 range"
elif [ $LINE_COUNT -lt 300 ]; then
    echo "$LINE_COUNT lines ⚠️ Below 300 lines - may be too minimal"
elif [ $LINE_COUNT -le 500 ]; then
    echo "$LINE_COUNT lines ⚠️ Between 400-500 lines - consider refactoring"
else
    echo "$LINE_COUNT lines ❌ Exceeds 500 lines - strongly consider splitting or refactoring"
fi

exit 0
