# Command Template

Use this template as the foundation for creating new command files.

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

## Key Guidelines

- **Line Count**: Target 50-150 lines (concise entry points)
- **Delegation**: Explicitly delegate to specific agent(s)
- **Arguments**: Document expected arguments and defaults
- **Examples**: Provide concrete usage examples
- **Workflow**: Describe high-level steps, let agent handle details
- **Integration**: Reference skills if agents need domain knowledge
