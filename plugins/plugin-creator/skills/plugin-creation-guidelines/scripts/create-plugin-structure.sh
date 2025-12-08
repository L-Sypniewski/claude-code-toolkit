#!/bin/bash
# Creates plugin directory skeleton
# Usage: bash create-plugin-structure.sh <plugin-name>

set -e

if [ $# -eq 0 ]; then
    echo "Error: Plugin name required"
    echo "Usage: bash create-plugin-structure.sh <plugin-name>"
    exit 2
fi

PLUGIN_NAME="$1"
BASE_DIR="plugins/${PLUGIN_NAME}"

# Validate kebab-case format
if [[ ! "$PLUGIN_NAME" =~ ^[a-z][a-z0-9]*(-[a-z0-9]+)*$ ]]; then
    echo "Error: Plugin name must be in kebab-case (lowercase, hyphens only)"
    echo "Example: my-plugin, api-tester, code-analyzer"
    exit 2
fi

# Check if plugin already exists
if [ -d "$BASE_DIR" ]; then
    echo "Error: Plugin '$PLUGIN_NAME' already exists at $BASE_DIR"
    exit 1
fi

# Create directory structure
mkdir -p "$BASE_DIR/.claude-plugin"
mkdir -p "$BASE_DIR/agents"
mkdir -p "$BASE_DIR/commands"
mkdir -p "$BASE_DIR/skills"

# Create placeholder README
cat > "$BASE_DIR/README.md" << 'EOF'
# Plugin Name

Brief description of the plugin.

## Components

[To be filled in during generation]

## Installation

[To be filled in during generation]

## Usage

[To be filled in during generation]
EOF

echo "✅ Plugin structure created at $BASE_DIR"
echo ""
echo "Created directories:"
echo "  - $BASE_DIR/.claude-plugin/"
echo "  - $BASE_DIR/agents/"
echo "  - $BASE_DIR/commands/"
echo "  - $BASE_DIR/skills/"
echo "  - $BASE_DIR/README.md (placeholder)"

exit 0
