# Plugin Creator

Interactive plugin creation, validation, and refactoring workflow with best-practice templates, architecture guidance, security validation, and automated quality checks for building production-ready Claude Code plugins.

## Overview

The Plugin Creator is a meta-plugin that helps you create, validate, and refactor Claude Code plugins following best practices from authoritative sources. It provides interactive workflows, comprehensive templates, security validation, and token optimization guidance to ensure your plugins are production-ready.

**Key Benefits**:
- **Educational**: Learn best practices by example
- **Efficient**: Generate complete plugins in minutes
- **Secure**: Automated security validation for scripts and prompts
- **Optimized**: Token-efficient patterns (300-400 lines per agent)
- **Validated**: Every generated plugin passes quality checks

## Features

- **Interactive Plugin Generation**: Guided workflow with architecture pattern selection
- **Comprehensive Templates**: Production-ready templates for agents, skills, commands, plugin.json, and README
- **Security Validation**: Automated checks for bash/python scripts and agent prompts
- **Token Optimization**: DRY principles and optimal line count targets
- **Best Practices Enforcement**: WHEN/WHEN NOT patterns, naming conventions, integration patterns
- **Plugin Validation**: Standalone validator for existing plugins
- **Plugin Refactoring**: Safe refactoring with backup and validation
- **Research-Backed**: Distills best practices from blog posts, Anthropic examples, and official docs

## Components

### Agents

| Agent | Description |
|-------|-------------|
| `plugin-creator` | Interactive plugin generator creating production-ready plugins with best-practice architecture. Gathers requirements, plans architecture, generates all components, validates security, and provides comprehensive summary. |
| `plugin-validator` | Validates plugin structure, security, and best practices compliance. Systematically checks file structure, metadata, components, security patterns, token optimization, and generates detailed reports with actionable recommendations. |

### Commands

| Command | Description |
|---------|-------------|
| `/create-plugin [name] [description]` | Creates new plugin interactively with guided architecture selection and automatic component generation. |
| `/validate-plugin [path]` | Validates existing plugin against best practices, security guidelines, and architectural patterns. |
| `/refactor-plugin [path] [goals]` | Refactors existing plugin to improve architecture, security, token optimization, or add components. |

### Skills

| Skill | Description |
|-------|-------------|
| `plugin-creation-guidelines` | Comprehensive plugin creation best practices including architecture patterns, component templates, security validation checklist, decision trees, and validation framework. Distills wisdom from blog posts, Anthropic examples, and official documentation. |

## Installation

This plugin is part of the Claude Code Toolkit marketplace. No additional installation required once you have the toolkit.

```bash
# The plugin is automatically available in your toolkit
cd claude-code-toolkit

# Verify plugin exists
ls plugins/plugin-creator
```

## Usage

### Creating a New Plugin

#### Basic Usage
```
/create-plugin my-awesome-plugin
```

**Interactive Workflow**:
1. Answer questions about plugin purpose
2. Select architecture pattern
3. Choose needed components (agents, skills, commands)
4. Specify required tools (Playwright, GitHub, etc.)
5. Watch as plugin is generated with all components
6. Review validation report and next steps

#### With Description
```
/create-plugin api-tester "Plugin for testing REST APIs with automated validation"
```

**Result**: Complete plugin with:
- plugin.json with metadata
- Agents with YAML frontmatter
- Skills with comprehensive knowledge
- Commands with clear delegation
- README with documentation
- Validation report showing compliance

### Validating an Existing Plugin

#### Validate Specific Plugin
```
/validate-plugin plugins/ui-ux-audit
```

**Output**: Comprehensive validation report with:
- File structure check
- Metadata validation
- Component-by-component analysis
- Security vulnerability scan
- Token optimization assessment
- Prioritized recommendations

#### Validate Current Directory
```
/validate-plugin
```

**Use Cases**:
- After manual edits (ensure best practices maintained)
- Before publishing (final quality check)
- Regular audits (stay up-to-date with standards)
- Learning (see how good plugins score)

### Refactoring an Existing Plugin

#### Interactive Refactoring
```
/refactor-plugin plugins/my-plugin
```

**Interactive Questions**:
1. What aspect to improve? (Architecture, Security, Tokens, Documentation)
2. Specific goals?
3. Preserve all functionality?

#### Specific Refactoring Goals

**Token Optimization**:
```
/refactor-plugin plugins/my-plugin "optimize token usage"
```
Result: Extract duplications to skills, shorten prompts, remove unnecessary tools

**Architecture Improvement**:
```
/refactor-plugin plugins/my-plugin "convert to orchestrator pattern"
```
Result: Split monolithic agent into orchestrator + workers for parallelization

**Security Hardening**:
```
/refactor-plugin plugins/my-plugin "add security validation"
```
Result: Add input validation, confirmation gates, safe subprocess patterns

**Feature Addition**:
```
/refactor-plugin plugins/my-plugin "add validator agent"
```
Result: Create new validation agent and skill

## Architecture Patterns

The plugin-creation-guidelines skill teaches four proven patterns:

### 1. Single Agent Pattern
**When**: Simple, focused plugins with one clear responsibility
- 1 Agent (all work)
- 0-1 Skills (optional reference)
- 1 Command (entry point)
- **Token Budget**: 200-400 lines

### 2. Orchestrator-Worker Pattern
**When**: Parallel execution or coordination needed
- 1 Orchestrator (coordinates)
- N Workers (parallel execution)
- 1+ Skills (shared knowledge)
- 1 Command (entry point)
- **Token Budget**: Orchestrator 250-350, Workers 100-200 each

### 3. Pipeline Pattern
**When**: Sequential processing with specialized stages
- N Agents (sequential pipeline)
- 1+ Skills (domain knowledge)
- 1-2 Commands (entry + shortcuts)
- **Token Budget**: 200-350 per agent

### 4. Skill-Augmented Pattern
**When**: Agents need extensive domain knowledge
- 1-2 Agents (execution)
- 1-2 Skills (comprehensive reference)
- 1 Command (entry point)
- **Token Budget**: Agents 150-300, Skills 300-500

## Best Practices

### Token Optimization
- **Target**: 300-400 lines per agent (evidence: 281 lines scored 82-85/100)
- **DRY Principle**: Extract common knowledge to skills
- **Reference Pattern**: Agents reference skills instead of duplicating content
- **Concise Descriptions**: Clear and focused, no unnecessary verbosity

### Description Engineering
- **WHEN/WHEN NOT Pattern**: Always include explicit usage boundaries
- **Example**: "Use PROACTIVELY for X. Do NOT use for: Y, Z."
- **Benefits**: Prevents false positives, improves auto-invocation accuracy

### Naming Conventions
- **Format**: kebab-case for all components
- **Consistency**: Multi-agent plugins use consistent prefix
- **Descriptive**: Names indicate role or domain clearly

### Security Patterns
- **Bash Scripts**: Input validation, proper quoting, `set -euo pipefail`
- **Python Scripts**: No eval/exec, safe subprocess, path validation
- **Agent Prompts**: Confirmation gates, GET-only navigation, input validation

### Integration Patterns
- **Command → Agent**: Explicit delegation statement
- **Agent → Skill**: Explicit reference section
- **Agent → Agent**: Task tool for spawning

### Advanced Skill Features (Claude Code 2.1+)

The plugin-creator supports the latest Claude Code 2.1 skill features for generating modern plugins:

#### Forked Context (`context: fork`)
Generate skills that run in isolated subagent contexts for:
- Resource-intensive operations that shouldn't consume main context
- Safe experimentation without polluting main session state
- Parallel skill execution for speedup

**When to use**: Large codebase analysis, experimental operations, parallel processing.

**When NOT to use**: Simple reference skills, templates, checklists (most cases).

#### Progressive Disclosure
Generate skills with descriptions optimized for progressive disclosure:
- Clear, specific descriptions (under 200 chars) ensure skills are selected when relevant
- Use WHEN/WHEN NOT pattern for accurate skill routing
- Reduces initial context window usage for generated plugins

#### Skills as Commands (Convergence)
Design plugins where skills can also be invoked as slash commands:
- Unified extension model reduces complexity
- Generated skills work both contextually (auto-loaded) and explicitly (invoked)
- Reduced cognitive overhead for end users

#### New Metadata Fields
Generate skills with optional fields for better organization:
- `context: fork` - Isolated execution
- `allowed-tools` - Pre-approved tools list
- `metadata` - Custom key-value pairs (author, version, category)
- `license` - Skill licensing

## Validation Checklist

The plugin-validator checks ~90 criteria across 11 categories:

1. **File Structure**: Required files and directories
2. **Metadata**: plugin.json completeness and correctness
3. **Agents**: Frontmatter, descriptions, line counts, workflow sections
4. **Skills**: Structure, content organization, examples
5. **Commands**: Arguments, delegation, usage examples
6. **README**: All required sections present
7. **Naming**: kebab-case consistency
8. **Integration**: Correct component references
9. **Security**: Script vulnerabilities, prompt safety
10. **Token Optimization**: Line counts, DRY compliance
11. **Advanced Features (2.1+)**: Forked context appropriateness, metadata validation

## Integration

Works seamlessly with other Claude Code plugins:

- **development-workflow**: Use plugin-creator to build development automation plugins
- **ui-ux-audit**: Example of well-architected plugin (validate to learn)
- **context-engineering**: Generate plugins that integrate with PRP workflows

## Requirements

- **Claude Code**: Latest version
- **No MCP servers required**: Plugin-creator works standalone
- **Write Access**: To plugins/ directory for creating new plugins

## Examples

### Example 1: Create Formatter Plugin
```
/create-plugin code-formatter "Format code using opinionated style guides"
```

**Interactive Responses**:
- Purpose: Generation
- Architecture: Single Agent
- Components: Agents, Skills, Commands
- Tools: File System

**Generated**:
- `code-formatter` agent (250 lines)
- `formatting-guidelines` skill (320 lines)
- `/format-code` command (85 lines)
- Complete README

**Time**: ~2 minutes

### Example 2: Create Security Audit Plugin
```
/create-plugin security-auditor
```

**Interactive Responses**:
- Purpose: Code Analysis
- Architecture: Orchestrator-Worker
- Components: Agents, Skills, Commands
- Tools: File System

**Generated**:
- `security-audit-orchestrator` agent (290 lines)
- `security-rule-checker` agent (180 lines)
- `security-audit-rules` skill (420 lines)
- `/audit-security` command (95 lines)
- Complete README

**Validation**: All checks pass, 0 security issues

### Example 3: Validate Plugin After Edits
```
# Make manual edits to plugin
vim plugins/my-plugin/agents/my-agent.md

# Validate changes
/validate-plugin plugins/my-plugin
```

**Report Shows**:
- ✅ Structure: PASS
- ⚠️ Agent: Line count 450 (exceeds 400 target)
- ✅ Security: PASS
- ⚠️ Token Optimization: Could extract duplication to skill

**Recommendations**:
1. Extract repeated validation logic to skill (saves ~150 lines)
2. Consider splitting large agent into orchestrator + worker

### Example 4: Refactor for Token Optimization
```
/refactor-plugin plugins/my-plugin "optimize token usage"
```

**Before**:
- Agent: 450 lines
- Inline templates and repeated logic

**After**:
- Agent: 280 lines (38% reduction)
- Skill: 340 lines (extracted content)
- Same functionality, better organized

**Validation**: Optimal token usage achieved

## Advanced Usage

### Custom Architecture
When interactive questions don't fit your needs:
1. Select closest architecture pattern
2. Generate plugin
3. Use `/refactor-plugin` to customize

### Multiple Agents
For complex plugins:
1. Start with Orchestrator-Worker pattern
2. Plugin-creator will ask how many workers
3. Specify role for each worker
4. Generates all with proper integration

### Learning Best Practices
Validate well-known plugins to learn:
```
/validate-plugin plugins/ui-ux-audit
/validate-plugin plugins/development-workflow
```

Study what scores well and why.

## Research Sources

This plugin distills best practices from authoritative sources:

### Blog Posts
- [Claude Code: Skills, Commands, Subagents & Plugins](https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins)
  - WHEN/WHEN NOT pattern
  - Token optimization (281 lines scored 82-85/100)
  - DRY principles

- [Understanding Claude Code Full Stack](https://alexop.dev/posts/understanding-claude-code-full-stack/)
  - Layered context strategy
  - MCP + Skills synergy
  - Token efficiency patterns

### Anthropic Examples
- [Anthropic Skills Repository](https://github.com/anthropics/skills/tree/main/skills)
  - Naming conventions
  - Component organization
  - Example implementations

### Official Documentation
- [Claude Code Plugins](https://code.claude.com/docs/en/plugins)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Claude Code Sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Commands](https://code.claude.com/docs/en/slash-commands)

### Claude Code 2.1+ Features
- [Subagents, Commands and Skills Convergence](https://vivekhaldar.com/articles/claude-code-subagents-commands-skills-converging/)
  - Unified extension model
  - Forked context for skills
  - Skills as slash commands
- [Claude Code 2.1 Update Overview](https://www.geeky-gadgets.com/claude-code-2-1-update-overview/)
  - Hot reloading
  - Session portability
- [Claude Skills Context Window Guide](https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills)
  - Progressive disclosure
  - Context window management
- [Understanding Skills, Agents, and MCP](https://colinmcnamara.com/blog/understanding-skills-agents-and-mcp-in-claude-code)
  - When to use each extension type

## Troubleshooting

### Plugin Creation Fails
- Check write permissions in plugins/ directory
- Ensure plugin name is kebab-case (no spaces/capitals)
- Verify plugins/ directory exists

### Validation Reports Warnings
- Warnings are improvement suggestions, not failures
- Review recommendations by priority (High → Medium → Low)
- Use `/refactor-plugin` to apply improvements

### Generated Plugin Not Working
- Review TODO comments in generated components
- Customize agent prompts for your specific use case
- Test with simple examples first
- Run `/validate-plugin` to check for issues

## Contributing

Plugin-creator is part of the Claude Code Toolkit. To contribute:
1. Test plugin generation workflows
2. Report issues or enhancement ideas
3. Share plugins you've created
4. Suggest additional templates or patterns

## License

MIT

---

**Generated plugins are ready for immediate use and follow all Claude Code best practices!**

Start creating: `/create-plugin your-plugin-name`
