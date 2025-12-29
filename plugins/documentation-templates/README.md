# Documentation Templates Plugin

Templates and examples for creating comprehensive project documentation including AGENTS.md organization, nested structure, and Claude Code delegation rules with best practices.

## Features

### Agents

- **agents-md-organizer** - Analyzes and reorganizes large AGENTS.md files into efficient modular structure with nested files and references to save context window space

### Commands

- **`/organize-agents-md [path]`** - Analyze and reorganize AGENTS.md files to improve organization and reduce context window consumption

### Prompts

- **AGENTS_MD_CREATION_PROMPT.md** - Comprehensive template for generating AGENTS.md files that document project development guidelines, quality standards, and autonomous agent workflows

### Skills

- **agents-md-organization** - Patterns and best practices for organizing large AGENTS.md files using nested structure, modular references, and separation of concerns
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
/plugin marketplace add https://github.com/L-Sypniewski/claude-code-toolkit.git
/plugin install documentation-templates
```

## Usage

### Organizing Existing AGENTS.md

When your AGENTS.md file becomes too large (>500 lines) or difficult to maintain:

```bash
# Analyze and reorganize AGENTS.md in current directory
/organize-agents-md

# Organize AGENTS.md in specific directory
/organize-agents-md path/to/project
```

The agent will:
1. Analyze your current AGENTS.md structure
2. Propose a reorganization plan (nested files, extracted details, subproject separation)
3. Show expected context window savings (typically 50-79% reduction)
4. Execute reorganization with your approval
5. Validate all content is preserved

**Common Scenarios:**
- **Large File**: AGENTS.md >500 lines → Extract detailed sections to `docs/` files
- **Monorepo**: Multiple subprojects → Create nested `backend/AGENTS.md`, `frontend/AGENTS.md`
- **Extensive Tests**: Testing guidelines >30% of content → Move to `tests/AGENTS.md`
- **Mixed Tech Stacks**: Different technologies → Separate into component-specific files

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

- **Context Window Efficiency**: Save 50-79% context window space with organized structure
- **Better Organization**: Nested AGENTS.md files for subprojects, extracted details for clarity
- **Consistency**: Standardized documentation across projects
- **Onboarding**: New team members quickly understand project standards
- **Automation**: Claude Code agents follow documented patterns automatically
- **Quality**: Clear quality gates and acceptance criteria
- **Efficiency**: Reusable templates save documentation time
- **Maintainability**: Easier to update and maintain modular structure

## Best Practices

### For AGENTS.md Organization

- **Keep Root Concise**: Target 200-400 lines for root AGENTS.md
- **Use Nested Structure**: Create subdirectory AGENTS.md for subprojects (backend, frontend, infra)
- **Extract Details**: Move detailed conventions to referenced files (docs/coding-standards.md, docs/testing-guide.md)
- **Maintain Navigation**: Add "Quick Links" section with references to detailed files
- **Context Window Efficiency**: Reduce typical context window usage by 50-79%
- **Preserve Content**: Never delete, always extract or move to appropriate location

### For AGENTS.md Creation

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
