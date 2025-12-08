# Create Plugin

Interactively create a new, production-ready Claude Code plugin with best-practice architecture, security validation, and comprehensive documentation.

## Arguments: $ARGUMENTS

**Format**: `/create-plugin [plugin-name] [description]`

**Examples**:
- `/create-plugin api-tester`
- `/create-plugin api-tester "Plugin for testing REST APIs with automated validation"`

**Requirements**:
- plugin-name: Required, must be kebab-case
- description: Optional, brief plugin purpose

**Default**: If no description provided, interactive workflow will collect requirements

## Workflow

1. **Validation**: Check plugin name format and directory availability
2. **Requirements**: Interactive questions about plugin purpose and architecture
3. **Generation**: Create plugin structure with all components
4. **Validation**: Automated best practices and security validation
5. **Summary**: Present generated plugin with next steps

## Delegation

Use the `plugin-creator` agent to execute this workflow. The agent will:
- Gather requirements interactively using AskUserQuestion
- Plan plugin architecture using sequential thinking and best practices
- Generate all components (plugin.json, agents, skills, commands, README)
- Validate security and best practices compliance
- Apply automated fixes where possible
- Provide comprehensive summary with token counts and validation results

## Additional Instructions

- Use sequential thinking to plan the plugin architecture
- Reference the `plugin-creation-guidelines` skill for all templates and best practices
- Apply WHEN/WHEN NOT pattern to all agent descriptions
- Ensure security validation passes before completion
- Target 300-400 lines per agent for optimal performance
- Include TODO comments for user customization points

## Output

Generated plugin will be created at: `plugins/{plugin-name}/`

The plugin will include:
- Complete directory structure (.claude-plugin/, agents/, commands/, skills/)
- plugin.json with complete metadata
- Agents with YAML frontmatter and WHEN/WHEN NOT descriptions
- Skills with comprehensive knowledge and examples
- Commands with clear delegation and usage examples
- README with full documentation
- Validation report showing compliance

## Examples

### Example 1: Simple Plugin
```
/create-plugin code-formatter "Format code using opinionated style guides"
```

**Result**: Single-agent plugin with formatting skill

**Generated Components**:
- 1 agent: `code-formatter` (formats code)
- 1 skill: `formatting-guidelines` (style rules)
- 1 command: `/format-code` (entry point)
- Complete README with usage examples

### Example 2: Complex Plugin
```
/create-plugin security-auditor
```

**Result**: Interactive workflow creates orchestrator-worker plugin

**Interactive Questions**:
1. Purpose: Code Analysis
2. Architecture: Orchestrator-Worker
3. Components: Agents, Skills, Commands
4. Tools: File System

**Generated Components**:
- 2 agents: `security-audit-orchestrator`, `security-rule-checker`
- 1 skill: `security-audit-rules`
- 1 command: `/audit-security`
- Comprehensive README

### Example 3: Integration Plugin
```
/create-plugin github-issue-tracker "Track and analyze GitHub issues with automated categorization"
```

**Result**: Single-agent plugin with GitHub MCP integration

**Generated Components**:
- 1 agent: `github-issue-tracker` (uses GitHub MCP tools)
- 1 skill: `issue-categorization-patterns`
- 1 command: `/track-issues`
- README with GitHub setup instructions
