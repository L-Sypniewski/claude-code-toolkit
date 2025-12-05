#!/usr/bin/env python3
"""
Creates agent .md file with valid YAML frontmatter
Usage: python generate-agent-boilerplate.py --name "agent-name" --description "..." --tools "tool1,tool2" --color "blue" --model "sonnet"
"""

import argparse
import re
import sys

def validate_kebab_case(name):
    """Validate that name is in kebab-case format"""
    pattern = r'^[a-z][a-z0-9]*(-[a-z0-9]+)*$'
    return re.match(pattern, name) is not None

def main():
    parser = argparse.ArgumentParser(description='Generate agent boilerplate with frontmatter')
    parser.add_argument('--name', required=True, help='Agent name (kebab-case)')
    parser.add_argument('--description', required=True, help='Agent description with WHEN/WHEN NOT')
    parser.add_argument('--tools', required=True, help='Comma-separated tool names')
    parser.add_argument('--color', required=True, choices=['blue', 'green', 'purple', 'red', 'yellow', 'orange'], help='Agent color')
    parser.add_argument('--model', required=True, choices=['sonnet', 'opus', 'haiku'], help='Claude model')

    args = parser.parse_args()

    # Validate agent name
    if not validate_kebab_case(args.name):
        print("Error: Agent name must be in kebab-case (lowercase, hyphens only)", file=sys.stderr)
        sys.exit(1)

    # Output agent markdown with frontmatter
    output = f"""---
name: {args.name}
description: {args.description}
tools: {args.tools}
color: {args.color}
model: {args.model}
---

You are [ROLE_DESCRIPTION - AI will fill this in].

## Skill Reference

[If this agent references a skill, document it here. Otherwise remove this section.]

**Use the `skill-name` skill** for:
- [What to reference from the skill]
- [Knowledge areas]

## Core Responsibility

**[Primary Responsibility Name]**: When processing [trigger]:

1. [Primary action]
2. [Secondary action]
3. [Tertiary action]

## Workflow

### Phase 1: [Phase Name]

[Phase description and steps]

### Phase 2: [Phase Name]

[Phase description and steps]

## Tool Usage Notes

- **[Tool 1]**: [When and how to use]
- **[Tool 2]**: [When and how to use]

## Error Handling

- **[Error Type]**: [How to handle]
- **[Error Type]**: [How to handle]

## Integration Points

Works with:
- `agent-name` agent for [purpose]
- `skill-name` skill for [purpose]
- `/command-name` command as [purpose]

## Statelessness Note

**One-Shot Execution**: [Describe completion criteria]
"""

    print(output)
    return 0

if __name__ == '__main__':
    sys.exit(main())
