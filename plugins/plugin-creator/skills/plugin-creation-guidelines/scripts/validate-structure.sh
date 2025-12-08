#!/bin/bash
# Checks if all required files and directories exist
# Usage: bash validate-structure.sh <plugin-path>
# Outputs JSON with validation results

set -e

if [ $# -eq 0 ]; then
    echo '{"valid": false, "issues": ["No plugin path provided"]}'
    exit 1
fi

PLUGIN_PATH="$1"
ISSUES=()

# Check if path exists
if [ ! -d "$PLUGIN_PATH" ]; then
    echo "{\"valid\": false, \"issues\": [\"Plugin directory does not exist: $PLUGIN_PATH\"]}"
    exit 1
fi

# Check required files
if [ ! -f "$PLUGIN_PATH/.claude-plugin/plugin.json" ]; then
    ISSUES+=("Missing .claude-plugin/plugin.json")
fi

if [ ! -f "$PLUGIN_PATH/README.md" ]; then
    ISSUES+=("Missing README.md")
fi

# Check for at least one component directory
HAS_COMPONENTS=false
if [ -d "$PLUGIN_PATH/agents" ] && [ "$(ls -A "$PLUGIN_PATH/agents" 2>/dev/null)" ]; then
    HAS_COMPONENTS=true
fi
if [ -d "$PLUGIN_PATH/commands" ] && [ "$(ls -A "$PLUGIN_PATH/commands" 2>/dev/null)" ]; then
    HAS_COMPONENTS=true
fi
if [ -d "$PLUGIN_PATH/skills" ] && [ "$(ls -A "$PLUGIN_PATH/skills" 2>/dev/null)" ]; then
    HAS_COMPONENTS=true
fi

if [ "$HAS_COMPONENTS" = false ]; then
    ISSUES+=("No component directories found (agents/, commands/, or skills/)")
fi

# Check agent files have .md extension
if [ -d "$PLUGIN_PATH/agents" ]; then
    for file in "$PLUGIN_PATH/agents"/*; do
        if [ -f "$file" ] && [[ ! "$file" =~ \.md$ ]]; then
            ISSUES+=("Agent file without .md extension: $(basename "$file")")
        fi
    done
fi

# Check skills have SKILL.md in subdirectory
if [ -d "$PLUGIN_PATH/skills" ]; then
    for skill_dir in "$PLUGIN_PATH/skills"/*; do
        if [ -d "$skill_dir" ]; then
            if [ ! -f "$skill_dir/SKILL.md" ]; then
                ISSUES+=("Skill directory missing SKILL.md: $(basename "$skill_dir")")
            fi
        fi
    done
fi

# Check commands have .md extension
if [ -d "$PLUGIN_PATH/commands" ]; then
    for file in "$PLUGIN_PATH/commands"/*; do
        if [ -f "$file" ] && [[ ! "$file" =~ \.md$ ]]; then
            ISSUES+=("Command file without .md extension: $(basename "$file")")
        fi
    done
fi

# Build JSON output
if [ ${#ISSUES[@]} -eq 0 ]; then
    echo '{"valid": true, "issues": []}'
else
    # Escape quotes in issues and build JSON array
    JSON_ISSUES=""
    for issue in "${ISSUES[@]}"; do
        # Escape backslashes and quotes
        ESCAPED=$(echo "$issue" | sed 's/\\/\\\\/g' | sed 's/"/\\"/g')
        if [ -n "$JSON_ISSUES" ]; then
            JSON_ISSUES="$JSON_ISSUES, \"$ESCAPED\""
        else
            JSON_ISSUES="\"$ESCAPED\""
        fi
    done
    echo "{\"valid\": false, \"issues\": [$JSON_ISSUES]}"
fi

exit 0
