# Skill Template

Use this template as the foundation for creating new skill files.

```markdown
---
name: skill-name
description: [Knowledge domain description]. Use when: [scenarios]. Do NOT use for: [anti-patterns].
# Optional fields (Claude Code 2.1+):
# context: fork                  # Run in isolated subagent context (optional)
# allowed-tools:                 # Pre-approved tools for this skill (optional)
#   - Read
#   - Grep
# license: MIT                   # Skill license (optional)
# metadata:                      # Custom metadata (optional)
#   author: "Author Name"
#   version: "1.0.0"
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

## Key Guidelines

- **Description Pattern**: Follow WHEN + WHEN NOT pattern for clarity
- **Line Count**: Target 300-500 lines (comprehensive reference)
- **Organization**: Use clear sections and subsections
- **Examples**: Include both good and bad examples with explanations
- **DRY Principle**: Skills are the single source of truth - agents reference them
- **Templates**: Include reusable templates agents can reference
- **Integration**: Document how other components use this skill

## Optional Fields (Claude Code 2.1+)

| Field | Purpose | When to Use |
|-------|---------|-------------|
| `context: fork` | Run skill in isolated subagent context | Resource-intensive operations, safe experimentation |
| `allowed-tools` | Pre-approve specific tools for the skill | When skill needs specific tool access |
| `license` | Specify skill license | For open-source or shared skills |
| `metadata` | Custom key-value pairs | Organization, versioning, categorization |

## Forked Context Decision Guide

Use `context: fork` when:
- Skill performs resource-intensive operations
- Skill might pollute main session state
- Skill needs to run in parallel with others
- Skill is experimental or might fail destructively

Do NOT use forked context when:
- Skill is lightweight reference material
- Skill needs to share state with main session
- Simplicity is preferred over isolation
