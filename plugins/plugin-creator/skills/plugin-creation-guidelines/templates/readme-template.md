# README Template

Use this template as the foundation for creating plugin README files.

```markdown
# Plugin Name

Brief one-line description matching plugin.json

## Overview

Comprehensive explanation of plugin purpose, capabilities, and use cases.

## Features

- Feature 1 with brief explanation
- Feature 2 with brief explanation
- Feature 3 with brief explanation

## Components

### Agents

| Agent | Description |
|-------|-------------|
| `agent-name` | What it does and when to use it |

### Commands

| Command | Description |
|---------|-------------|
| `/command-name` | What it does and arguments |

### Skills

| Skill | Description |
|-------|-------------|
| `skill-name` | Knowledge domain it provides |

## Installation

This plugin is part of the Claude Code Toolkit marketplace. Install via:

```bash
# Clone or navigate to marketplace
cd claude-code-toolkit

# Plugin is automatically available once repository is cloned
```

## Usage

### [Primary Use Case]

1. Step-by-step instructions
2. With expected outcomes
3. And example commands

**Example**:
```
/command-name arguments
```

### [Secondary Use Case]

[Additional usage scenarios]

## Best Practices

- Recommendation 1
- Recommendation 2
- Recommendation 3

## Integration

Works with:
- **[Other Plugin Name]**: How they integrate
- **[MCP Server Name]**: What functionality it provides

## Requirements

- Claude Code
- [Any MCP servers required]
- [Any system dependencies]

## License

MIT
```

## Key Guidelines

- **Structure**: Match this structure for consistency across plugins
- **Description**: One-line description should match plugin.json exactly
- **Components**: Use tables to clearly document all agents, commands, and skills
- **Examples**: Provide concrete, working examples
- **Integration**: Document dependencies and integrations with other plugins/MCPs
- **Installation**: Follow standard marketplace installation pattern
