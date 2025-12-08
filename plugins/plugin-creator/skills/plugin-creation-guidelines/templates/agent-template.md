# Agent Template

Use this template as the foundation for creating new agent files.

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

## Key Guidelines

- **Description Pattern**: Follow WHEN + WHEN NOT pattern for clarity
- **Line Count**: Target 200-400 lines (optimal: 300)
- **Tools**: Only include tools the agent actually uses
- **Skill References**: Explicitly reference skills rather than duplicating content
- **Error Handling**: Document expected errors and recovery procedures
- **Integration**: Clearly document how agent connects with other components
