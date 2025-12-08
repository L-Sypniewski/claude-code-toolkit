#!/bin/bash
# Creates skill directory and SKILL.md
# Usage: bash generate-skill-boilerplate.sh <plugin-name> <skill-name> "<description>"

set -e

if [ $# -lt 3 ]; then
    echo "Error: Requires plugin-name, skill-name, and description"
    echo "Usage: bash generate-skill-boilerplate.sh <plugin-name> <skill-name> \"<description>\""
    exit 2
fi

PLUGIN_NAME="$1"
SKILL_NAME="$2"
DESCRIPTION="$3"
SKILL_DIR="plugins/${PLUGIN_NAME}/skills/${SKILL_NAME}"

# Validate kebab-case formats
if [[ ! "$PLUGIN_NAME" =~ ^[a-z][a-z0-9]*(-[a-z0-9]+)*$ ]]; then
    echo "Error: Plugin name must be in kebab-case"
    exit 2
fi

if [[ ! "$SKILL_NAME" =~ ^[a-z][a-z0-9]*(-[a-z0-9]+)*$ ]]; then
    echo "Error: Skill name must be in kebab-case"
    exit 2
fi

# Create skill directory
mkdir -p "$SKILL_DIR"

# Generate SKILL.md
cat > "$SKILL_DIR/SKILL.md" << EOF
---
name: $SKILL_NAME
description: $DESCRIPTION
---

# ${SKILL_NAME^}

[Comprehensive skill content - AI will fill this in]

## Overview

[What this skill provides]

## [Section 1]

[Content]

## [Section 2]

[Content]

## Integration Points

Works with:
- \`agent-name\` agent for [purpose]
- \`/command-name\` command for [purpose]
EOF

echo "✅ Skill created at $SKILL_DIR/SKILL.md"
exit 0
