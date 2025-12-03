---
name: plugin-creation-guidelines
description: Comprehensive plugin creation best practices, architecture patterns, and security guidelines. Use when: creating plugins, validating plugin structure, refactoring plugin architecture, generating plugin components. Do NOT use for: application development, debugging user code, or non-plugin tasks.
---

# Plugin Creation Guidelines

Comprehensive best practices for building production-ready Claude Code plugins.

## Architecture Patterns

### 1. Single Agent Pattern
**When to Use**: Simple, focused plugins with one clear responsibility
**Example**: A formatter plugin, a simple validator

**Structure**:
- 1 Agent (does all work)
- 0-1 Skills (optional reference knowledge)
- 1 Command (entry point)

**Token Budget**: 200-400 lines for agent

### 2. Orchestrator-Worker Pattern
**When to Use**: Plugins requiring parallel execution or coordination of multiple tasks
**Example**: UI/UX audit (crawl + parallel page analysis), Multi-step workflows

**Structure**:
- 1 Orchestrator Agent (coordinates)
- N Worker Agents (execute in parallel)
- 1+ Skills (shared knowledge)
- 1 Command (entry point)

**Token Budget**:
- Orchestrator: 250-350 lines
- Workers: 100-200 lines each

### 3. Pipeline Pattern
**When to Use**: Sequential processing with specialized stages
**Example**: Code analysis → Planning → Implementation → Review

**Structure**:
- N Agents (sequential pipeline)
- 1+ Skills (domain knowledge)
- 1-2 Commands (entry + shortcuts)

**Token Budget**: 200-350 lines per agent

### 4. Skill-Augmented Pattern
**When to Use**: Agents need extensive domain knowledge or templates
**Example**: Documentation generation, Code review with checklists

**Structure**:
- 1-2 Agents (execution)
- 1-2 Skills (comprehensive reference)
- 1 Command (entry point)

**Token Budget**:
- Agents: 150-300 lines (lean, references skill)
- Skills: 300-500 lines (comprehensive)

## Component Templates

### Agent Template

```markdown
---
name: agent-name
description: [What it does]. Use PROACTIVELY for [specific triggers]. Do NOT use for: [anti-patterns].
tools: [comma-separated tool list]
color: [blue|green|purple|orange|red]
model: [sonnet|opus|haiku]
---

You are [role description]. You [primary responsibility].

## Core Responsibility

[Numbered list of primary responsibilities]

## Skill Reference (if applicable)

Reference the `skill-name` skill for:
- [What to reference from skill]
- [Specific sections/knowledge areas]

## Workflow

### Step 1: [Step Name]

[Detailed instructions]

**Key Actions**:
- Action 1
- Action 2

### Step 2: [Step Name]

[Continue workflow steps]

## Error Handling

- **[Error Type]**: [How to handle]
- **[Error Type]**: [How to handle]

## Output Format

[Expected output structure]

## Communication Protocol

- **Progress Updates**: [When and how]
- **Error Reporting**: [How to report issues]
- **Completion Signal**: [How to indicate completion]

## Quality Standards

- [Quality metric 1]
- [Quality metric 2]

## Integration Points

Works with:
- `other-agent-name` for [purpose]
- `skill-name` skill for [purpose]
- `/command-name` command as [purpose]

## Statelessness Note

**One-Shot Execution**: [Describe completion expectations]
```

### Skill Template

```markdown
---
name: skill-name
description: [Knowledge domain description]. Use when: [scenarios]. Do NOT use for: [anti-patterns].
---

# Skill Title

Brief description of what this skill provides.

## [Knowledge Section 1]

### [Subsection 1.1]

[Detailed procedural knowledge, checklists, or templates]

**Key Points**:
- Point 1
- Point 2

### [Subsection 1.2]

[Continue with organized knowledge]

## [Knowledge Section 2]

[Continue with comprehensive sections]

## Examples

### Good Example
[Positive example with explanation]

### Bad Example
[Anti-pattern with explanation]

## Integration Points

Works with:
- `agent-name` for [how agent uses this skill]
- `/command-name` command for [how command references this]

## Additional Resources

- [Link to blog post 1]
- [Link to documentation]
- [Link to example repository]
```

### Command Template

```markdown
# Command Title

Brief description of what this command does.

## Target: $ARGUMENTS

Default behavior if no arguments provided: [default]

Argument format: [describe expected arguments]

## Workflow

1. **Step 1**: [What happens first]
2. **Step 2**: [What happens next]
3. **Step 3**: [Expected outcome]

## Delegation

Use the `agent-name` agent to execute this workflow. The agent will:
- [Agent responsibility 1]
- [Agent responsibility 2]

## Additional Instructions

- [Special consideration 1]
- [Special consideration 2]
- Reference the `skill-name` skill for [what to reference]

## Examples

### Example 1: [Scenario]
```
/command-name [arguments]
```
Expected result: [outcome]

### Example 2: [Scenario]
```
/command-name [arguments]
```
Expected result: [outcome]
```

### plugin.json Template

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Brief, comprehensive description of plugin capabilities and features",
  "author": {
    "name": "Author Name"
  },
  "keywords": [
    "keyword1",
    "keyword2",
    "keyword3",
    "keyword4"
  ],
  "license": "MIT",
  "repository": "https://github.com/username/repository",
  "homepage": "https://github.com/username/repository/tree/master/plugins/plugin-name"
}
```

### README Template

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

## Best Practices from Research Sources

### Token Optimization (Blog Posts)

**Target Line Counts**:
- Agents: 300-400 lines (optimal performance)
- Skills: 300-500 lines (comprehensive reference)
- Commands: 50-150 lines (concise entry points)

**DRY Principles**:
- Skills = single source of truth for domain knowledge
- Agents reference skills, don't duplicate content
- Templates in skills, not inline in agents

**Evidence**: Blog post showed 803-line agent scored 62/100, refactored 281-line version scored 82-85/100

### Description Engineering (Blog Posts)

**WHEN + WHEN NOT Pattern**:

✅ **Good**:
```yaml
description: Orchestrates UI/UX audits by coordinating parallel page auditors. Use PROACTIVELY for `/ui-ux-audit` command. Do NOT use for: single-page audits, code analysis, or accessibility testing.
```

❌ **Bad**:
```yaml
description: Handles UI/UX auditing tasks.
```

**Key Elements**:
1. **What it does** (clear action)
2. **Use PROACTIVELY for** (explicit triggers)
3. **Do NOT use for** (clear boundaries)

**Benefits**:
- Prevents false positive auto-invocation
- Explicit scope boundaries
- Better context matching

### Naming Conventions (Anthropic Examples)

**Standards**:
- **Format**: `kebab-case` for all components
- **Agents**: Descriptive role names
- **Skills**: Domain or methodology names
- **Commands**: Action verb + object

**Prefixing**:
- Multi-agent plugins: Use plugin name prefix
  - `ui-ux-audit-orchestrator`, `ui-ux-page-auditor`
- Single-agent plugins: Descriptive name
  - `senior-engineer`, `code-reviewer`

**File Names**:
- Agents: `agent-name.md`
- Skills: `SKILL.md` inside `skill-name/` directory
- Commands: `command-name.md`

### Tool Access Patterns

**Common Tool Categories**:

1. **File Operations**: Read, Write, Edit, Glob, Grep
2. **Execution**: Bash, TodoWrite
3. **Coordination**: Task (spawning agents)
4. **Thinking**: mcp__sequentialthinking__sequentialthinking
5. **Research**: WebFetch, WebSearch
6. **MCP Integrations**: mcp__playwright__*, mcp__github__*, etc.

**Best Practices**:
- Only grant tools the agent actually uses
- Orchestrators need Task for spawning
- Workers don't need Task (they ARE spawned)
- Use AskUserQuestion for interactive workflows

### Integration Patterns

**Command → Agent**:
```markdown
Use the `agent-name` agent to execute this workflow.
```

**Agent → Skill**:
```markdown
## Skill Reference

Reference the `skill-name` skill for:
- [Specific knowledge area]
- [Templates or checklists]
```

**Agent → Agent** (Spawning):
```markdown
Use the `Task` tool to spawn `worker-agent-name` agents for parallel execution.
```

**Skill → Components** (Documentation):
```markdown
## Integration Points

Works with:
- `agent-name` agent for [purpose]
- `/command-name` command as [entry point]
```

## Security Validation Checklist

### Bash Script Security

**Issues to Check**:
- ✅ Input sanitization for user-provided arguments
- ✅ No direct shell injection vulnerabilities (`eval`, unquoted `$VAR`)
- ✅ Proper quoting for file paths with spaces
- ✅ Validation of file existence before operations
- ✅ No destructive operations without confirmation
- ✅ Use of `set -euo pipefail` for safety
- ✅ Restricted to necessary permissions

**Example Good Practice**:
```bash
#!/bin/bash
set -euo pipefail

# Validate input
if [[ -z "${1:-}" ]]; then
  echo "Error: Argument required"
  exit 1
fi

# Sanitize and quote
FILE_PATH="${1}"
if [[ ! -f "$FILE_PATH" ]]; then
  echo "Error: File not found: $FILE_PATH"
  exit 1
fi

# Safe operation with quoting
cat "$FILE_PATH"
```

**Example Bad Practice**:
```bash
#!/bin/bash
# No input validation
# No quoting (breaks with spaces)
cat $1
```

### Python Script Security

**Issues to Check**:
- ✅ Input validation and type checking
- ✅ No `eval()` or `exec()` on user input
- ✅ Proper exception handling
- ✅ Safe file operations (no arbitrary writes)
- ✅ No command injection via `os.system()` or `subprocess` with `shell=True`
- ✅ Use of `subprocess.run()` with list arguments
- ✅ Path validation (no directory traversal)

**Example Good Practice**:
```python
import subprocess
import sys
from pathlib import Path

def process_file(file_path: str) -> None:
    """Process file safely with validation."""
    # Validate input
    if not file_path:
        raise ValueError("File path required")

    # Path validation
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # Safe subprocess call (no shell=True)
    result = subprocess.run(
        ["cat", str(path)],
        capture_output=True,
        text=True,
        check=True
    )
    print(result.stdout)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <file_path>")
        sys.exit(1)

    try:
        process_file(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
```

**Example Bad Practice**:
```python
import os
import sys

# No validation, command injection vulnerability
os.system(f"cat {sys.argv[1]}")
```

### Agent Prompt Security

**Issues to Check**:
- ✅ No direct execution of user-provided code without validation
- ✅ Explicit warnings about destructive operations
- ✅ Confirmation gates for sensitive actions
- ✅ GET-only navigation for web crawling (no POST/PUT/DELETE)
- ✅ Rate limiting for API calls
- ✅ No hardcoded credentials or secrets
- ✅ Validation of external URLs before fetching

**Example Good Practice**:
```markdown
## Safety Protocol

**Critical Safety Rules**:
- **Never** execute destructive operations without user confirmation
- **Always** use GET-only requests for web navigation
- **Always** validate and sanitize user input
- **Never** store or log sensitive information
- **Always** rate limit external API calls

**Confirmation Gates**:
Before performing destructive actions (delete, modify production data), use AskUserQuestion:
- Describe the action clearly
- Show what will be affected
- Require explicit confirmation
```

### Skill Content Security

**Issues to Check**:
- ✅ No example code with security vulnerabilities
- ✅ Templates include input validation
- ✅ Best practices emphasize security
- ✅ Warning about common pitfalls
- ✅ Safe defaults in examples

### Command Security

**Issues to Check**:
- ✅ Argument validation before delegation
- ✅ No direct shell execution of arguments
- ✅ Clear warnings about required permissions
- ✅ Documentation of sensitive operations

## Decision Trees

### When to Create a Skill vs Inline Documentation?

**Create a Skill When**:
- ✅ Knowledge is >200 lines
- ✅ Multiple agents need the same information
- ✅ Contains templates, checklists, or structured data
- ✅ Domain-specific expertise
- ✅ May be updated independently

**Use Inline When**:
- ✅ Agent-specific workflow steps
- ✅ <100 lines of guidance
- ✅ Tightly coupled to agent logic
- ✅ Not reusable by other agents

### When to Use Orchestrator Pattern?

**Use Orchestrator When**:
- ✅ Multiple pages/items need parallel processing
- ✅ Coordination of heterogeneous tasks
- ✅ Results need aggregation
- ✅ Workflow has distinct phases

**Use Single Agent When**:
- ✅ Sequential, single-threaded work
- ✅ Simple input → output transformation
- ✅ No coordination needed
- ✅ Work cannot be parallelized

### When to Split into Multiple Agents?

**Split When**:
- ✅ Agent exceeds 400 lines
- ✅ Two distinct responsibilities
- ✅ Different tool requirements
- ✅ Independent reuse needed
- ✅ Different expertise domains

**Keep Single When**:
- ✅ Tightly coupled workflow
- ✅ Sequential dependencies
- ✅ Context needs to persist
- ✅ Total <400 lines

## Validation Checklist

### File Structure
- [ ] `.claude-plugin/plugin.json` exists
- [ ] `README.md` exists
- [ ] At least one of: agents/, commands/, skills/ exists
- [ ] All agent files have `.md` extension
- [ ] All skill directories contain `SKILL.md`
- [ ] All command files have `.md` extension

### Metadata Validation
- [ ] plugin.json has all required fields (name, version, description, author)
- [ ] Plugin name is kebab-case
- [ ] Version follows semantic versioning (X.Y.Z)
- [ ] Description is comprehensive (50-200 chars)
- [ ] Keywords array has 4-8 relevant keywords
- [ ] Repository and homepage URLs are valid

### Agent Validation
- [ ] Agent files have YAML frontmatter
- [ ] Frontmatter includes: name, description, tools, color, model
- [ ] Description follows WHEN + WHEN NOT pattern
- [ ] Agent name matches filename (without .md)
- [ ] Line count: 100-400 lines (target: 300)
- [ ] Tools list is appropriate (no unnecessary tools)
- [ ] Explicit skill references if applicable
- [ ] Clear workflow sections
- [ ] Error handling documented
- [ ] Integration points documented
- [ ] No security vulnerabilities in prompts

### Skill Validation
- [ ] Skill directory name is kebab-case
- [ ] Contains `SKILL.md` file
- [ ] SKILL.md has YAML frontmatter
- [ ] Frontmatter includes: name, description
- [ ] Description follows WHEN + WHEN NOT pattern
- [ ] Skill name matches directory name
- [ ] Line count: 300-500 lines (comprehensive reference)
- [ ] Organized into clear sections
- [ ] Contains examples (good and bad)
- [ ] Integration points documented
- [ ] No security vulnerabilities in example code

### Command Validation
- [ ] Command file name is kebab-case
- [ ] Contains clear title (# heading)
- [ ] Documents arguments ($ARGUMENTS or $1, $2, etc.)
- [ ] Describes default behavior if no args
- [ ] Includes workflow steps
- [ ] Delegates to specific agent(s)
- [ ] Includes usage examples
- [ ] Line count: 50-150 lines

### README Validation
- [ ] Has clear title matching plugin name
- [ ] Brief one-line description at top
- [ ] Overview section explaining purpose
- [ ] Features list (bullets or numbered)
- [ ] Components tables (agents, commands, skills)
- [ ] Installation instructions
- [ ] Usage examples with actual commands
- [ ] Best practices section
- [ ] Integration section (if applicable)
- [ ] Requirements section (if applicable)
- [ ] License section

### Naming Conventions
- [ ] All component names use kebab-case
- [ ] Multi-agent plugins use consistent prefix
- [ ] Agent names are descriptive of role
- [ ] Skill names indicate domain/methodology
- [ ] Command names are verb + object
- [ ] No spaces in any names

### Integration Patterns
- [ ] Commands explicitly delegate to agents
- [ ] Agents explicitly reference skills (if applicable)
- [ ] Agent-to-agent spawning uses Task tool
- [ ] All references use exact component names
- [ ] Integration points documented in all components

### Security Validation
- [ ] Bash scripts: Input validation present
- [ ] Bash scripts: Proper quoting for paths
- [ ] Bash scripts: No shell injection vulnerabilities
- [ ] Python scripts: No eval/exec on user input
- [ ] Python scripts: Safe subprocess usage
- [ ] Python scripts: Path validation present
- [ ] Agent prompts: Confirmation gates for destructive ops
- [ ] Agent prompts: GET-only for web navigation
- [ ] Skills: Example code has no vulnerabilities
- [ ] Commands: Argument validation before delegation

### Token Optimization
- [ ] No content duplication between components
- [ ] Skills used as single source of truth
- [ ] Agent descriptions are concise
- [ ] No unnecessary verbosity
- [ ] Templates extracted to skills, not inline
- [ ] DRY principles applied throughout

## Additional Resources

### Blog Posts (Best Practices)
- [Claude Code: Skills, Commands, Subagents & Plugins](https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins)
  - WHEN/WHEN NOT pattern for descriptions
  - Token optimization: 281 lines scored 82-85/100
  - DRY principles and refactoring guidance
  - Hybrid execution pattern

- [Understanding Claude Code Full Stack](https://alexop.dev/posts/understanding-claude-code-full-stack/)
  - Layered context strategy
  - MCP + Skills synergy
  - CLAUDE.md hierarchy
  - Token efficiency patterns

### Anthropic Examples
- [Anthropic Skills Repository](https://github.com/anthropics/skills/tree/main/skills)
  - Reference skill structures
  - Naming conventions
  - Component organization patterns
  - Example implementations

### Official Documentation
- [Claude Code Plugins Documentation](https://code.claude.com/docs/en/plugins)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Claude Code Sub-agents Documentation](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Slash Commands Documentation](https://code.claude.com/docs/en/slash-commands)
