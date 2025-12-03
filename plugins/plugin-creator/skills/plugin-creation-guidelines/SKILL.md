---
name: plugin-creation-guidelines
description: Comprehensive plugin creation best practices, architecture patterns, and security guidelines. Use when: creating plugins, validating plugin structure, refactoring plugin architecture, generating plugin components. Do NOT use for: application development, debugging user code, or non-plugin tasks.
---

# Plugin Creation Guidelines

Comprehensive best practices for building production-ready Claude Code plugins.

## Architecture Patterns

### 1. Single Agent Pattern
**When to Use**: Simple, focused plugins with one clear responsibility

**Structure**:
- 1 Agent (does all work)
- 0-1 Skills (optional reference knowledge)
- 1 Command (entry point)

**Token Budget**: 200-400 lines for agent

### 2. Orchestrator-Worker Pattern
**When to Use**: Plugins requiring parallel execution or coordination of multiple tasks

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

**Structure**:
- N Agents (sequential pipeline)
- 1+ Skills (domain knowledge)
- 1-2 Commands (entry + shortcuts)

**Token Budget**: 200-350 lines per agent

### 4. Skill-Augmented Pattern
**When to Use**: Agents need extensive domain knowledge or templates

**Structure**:
- 1-2 Agents (execution)
- 1-2 Skills (comprehensive reference)
- 1 Command (entry point)

**Token Budget**:
- Agents: 150-300 lines (lean, references skill)
- Skills: 300-500 lines (comprehensive)

## Best Practices Summary

### Token Optimization

**Target Line Counts**:
- Agents: 300-400 lines (optimal performance)
- Skills: 300-500 lines (comprehensive reference)
- Commands: 50-150 lines (concise entry points)

**DRY Principles**:
- Skills = single source of truth for domain knowledge
- Agents reference skills, don't duplicate content
- Templates in skills, not inline in agents

**Evidence**: Blog post showed 803-line agent scored 62/100, refactored 281-line version scored 82-85/100

### Description Engineering

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

### Naming Conventions

**Standards**:
- **Format**: `kebab-case` for all components
- **Agents**: Descriptive role names
- **Skills**: Domain or methodology names
- **Commands**: Action verb + object

**Prefixing**:
- Multi-agent plugins: Use plugin name prefix (`ui-ux-audit-orchestrator`, `ui-ux-page-auditor`)
- Single-agent plugins: Descriptive name (`senior-engineer`, `code-reviewer`)

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

## Templates & References

For detailed templates and checklists, reference these files in the skill directory:

### Component Templates

Use Read tool to access complete templates with guidelines:

- `templates/agent-template.md` - Complete agent structure with frontmatter and all sections
- `templates/skill-template.md` - Skill file structure and organization patterns
- `templates/command-template.md` - Command file with delegation patterns and examples
- `templates/plugin-json-template.json` - Plugin metadata schema with all required fields
- `templates/readme-template.md` - Comprehensive README structure with all sections

### Validation Checklists

Use Read tool to access detailed validation criteria:

- `checklists/security-validation.md` - Security patterns for bash/python/agents with examples
- `checklists/component-validation.md` - Complete validation checklist for all components

**Progressive Disclosure**: Use Read tool to access these files when generating or validating specific plugin components. This keeps the main skill concise while providing comprehensive reference material on demand.

## Quick Reference: Component Requirements

### Agent Requirements
- YAML frontmatter: name, description, tools, color, model
- WHEN + WHEN NOT description pattern
- 100-400 lines (optimal: 300)
- Explicit skill references if applicable
- Clear workflow sections
- Error handling documented

### Skill Requirements
- YAML frontmatter: name, description
- WHEN + WHEN NOT description pattern
- 300-500 lines
- Clear sections and subsections
- Examples (good and bad)
- Integration points documented

### Command Requirements
- Clear title (# heading)
- Documents arguments and defaults
- Workflow steps
- Explicit delegation to agent(s)
- Usage examples
- 50-150 lines

### Plugin Requirements
- `.claude-plugin/plugin.json` with all required fields
- `README.md` with standard structure
- At least one component directory (agents/, commands/, or skills/)
- Kebab-case naming throughout
- Semantic versioning (X.Y.Z)

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
