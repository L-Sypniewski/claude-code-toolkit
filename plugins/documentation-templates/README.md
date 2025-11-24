# Documentation Templates Plugin

Templates and examples for creating comprehensive project documentation including AGENTS.md and Claude Code delegation rules with best practices.

## Features

### Prompts

- **AGENTS_MD_CREATION_PROMPT.md** - Comprehensive template for generating AGENTS.md files that document project development guidelines, quality standards, and autonomous agent workflows

### Skills

- **agent-documentation** - Standards and templates for documenting Claude Code agents including AGENTS.md structure, agent specifications, and delegation patterns
- **claude-delegation-rules** - Rules and patterns for effective agent delegation including handoff protocols, coordination patterns, and best practices

### Examples

- **AGENTS.md** - Real-world example of a complete AGENTS.md file from the ConvoClarity project, demonstrating:
  - TL;DR project overview
  - Quality gates and acceptance criteria
  - Coding standards and conventions
  - Testing expectations
  - Agent roles and responsibilities
  - Workflow patterns

- **CLAUDE.md** - Claude Code delegation rules documentation showing:
  - Mandatory agent delegation hierarchy
  - Automatic agent invocation protocols
  - Common delegation scenarios
  - Best practices for agent coordination

## Installation

This plugin is part of the Claude Code Toolkit marketplace. Install via:

```bash
/plugin marketplace add <marketplace-url>
/plugin install documentation-templates
```

## Usage

### Creating AGENTS.md for Your Project

1. Review the **AGENTS_MD_CREATION_PROMPT.md** template
2. Examine the **AGENTS.md** example for structure and content ideas
3. Adapt the template to your project's specific needs:
   - Define your quality standards
   - Document coding conventions
   - Specify testing requirements
   - Outline agent responsibilities
   - Establish workflow patterns

### Implementing Claude Code Delegation Rules

1. Review the **CLAUDE.md** example
2. Define your agent hierarchy and delegation rules
3. Document when agents should be automatically invoked
4. Create clear scenarios for common tasks
5. Ensure agents have appropriate tool access

## Benefits

- **Consistency**: Standardized documentation across projects
- **Onboarding**: New team members quickly understand project standards
- **Automation**: Claude Code agents follow documented patterns automatically
- **Quality**: Clear quality gates and acceptance criteria
- **Efficiency**: Reusable templates save documentation time

## Best Practices

### For AGENTS.md

- Start with a concise TL;DR that captures project essence
- Define clear, measurable quality gates
- Document architectural decisions and rationale
- Specify testing requirements explicitly
- Include examples for complex patterns
- Keep it updated as the project evolves
- Use agent-documentation skill for comprehensive agent specs

### For CLAUDE.md

- Establish clear agent delegation hierarchy
- Document automatic invocation triggers
- Provide concrete scenario examples
- Specify required tool permissions
- Balance automation with flexibility
- Review and refine based on usage
- Leverage claude-delegation-rules skill for coordination patterns

### For Skills

- Skills are automatically loaded by Claude when relevant context matches
- Each skill provides procedural knowledge and templates
- Skills complement agents by providing reusable patterns and standards
- Keep skills focused on specific domains for optimal auto-loading

## Template Customization

Both templates are designed to be customized:

1. **Project-Specific**: Adapt to your tech stack and methodologies
2. **Team Culture**: Reflect your team's values and practices
3. **Workflow Integration**: Align with your development process
4. **Incremental Improvement**: Start simple, expand over time

## Real-World Examples

The included examples are from actual projects and demonstrate:
- How to structure comprehensive development documentation
- Balancing detail with readability
- Integrating quality standards with practical guidance
- Creating actionable delegation rules

## License

MIT
