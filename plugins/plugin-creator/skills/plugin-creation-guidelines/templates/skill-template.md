# Skill Template

Use this template as the foundation for creating new skill files.

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

## Key Guidelines

- **Description Pattern**: Follow WHEN + WHEN NOT pattern for clarity
- **Line Count**: Target 300-500 lines (comprehensive reference)
- **Organization**: Use clear sections and subsections
- **Examples**: Include both good and bad examples with explanations
- **DRY Principle**: Skills are the single source of truth - agents reference them
- **Templates**: Include reusable templates agents can reference
- **Integration**: Document how other components use this skill
