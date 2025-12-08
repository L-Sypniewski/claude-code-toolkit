#!/bin/bash
# Creates command .md file from template
# Usage: bash generate-command-boilerplate.sh <plugin-name> <command-name> "<description>"

set -e

if [ $# -lt 3 ]; then
    echo "Error: Requires plugin-name, command-name, and description"
    echo "Usage: bash generate-command-boilerplate.sh <plugin-name> <command-name> \"<description>\""
    exit 2
fi

PLUGIN_NAME="$1"
COMMAND_NAME="$2"
DESCRIPTION="$3"
COMMAND_FILE="plugins/${PLUGIN_NAME}/commands/${COMMAND_NAME}.md"

# Validate formats (kebab-case or snake_case for commands)
if [[ ! "$PLUGIN_NAME" =~ ^[a-z][a-z0-9]*(-[a-z0-9]+)*$ ]]; then
    echo "Error: Plugin name must be in kebab-case"
    exit 2
fi

if [[ ! "$COMMAND_NAME" =~ ^[a-z][a-z0-9]*([_-][a-z0-9]+)*$ ]]; then
    echo "Error: Command name must be in kebab-case or snake_case"
    exit 2
fi

# Generate command markdown
cat > "$COMMAND_FILE" << EOF
# ${COMMAND_NAME^}

$DESCRIPTION

## Arguments: \$ARGUMENTS

[Document expected arguments here]

Expected format: \`<arg1> [arg2]\`

- **arg1** (required): [Description]
- **arg2** (optional): [Description]

## Examples

\`\`\`bash
# Example 1
/${COMMAND_NAME} <example-input>

# Example 2
/${COMMAND_NAME} <example-input> <optional-arg>
\`\`\`

## Workflow

1. **[Step 1]**: [Description]
2. **[Step 2]**: [Description]
3. **[Step 3]**: [Description]

## Delegation

Use the \`agent-name\` agent to execute this workflow. The agent will:
- [Agent responsibility 1]
- [Agent responsibility 2]
- [Agent responsibility 3]

## Output

[Describe expected output]

## Notes

[Additional notes or special considerations]
EOF

echo "✅ Command created at $COMMAND_FILE"
exit 0
