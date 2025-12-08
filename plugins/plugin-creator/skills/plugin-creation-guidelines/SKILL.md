---
name: plugin-creation-guidelines
description: Plugin architecture patterns and best practices for Claude Code plugins. Use when creating/validating plugins. Do NOT use for general coding or debugging.
---

# Plugin Creation Guidelines

Reference for building Claude Code plugins with optimal token efficiency.

## Architecture Patterns

### 1. Single Agent Pattern

One agent handles all plugin responsibilities. Use for simple, sequential workflows (<400 lines).

```
plugin-name/
├── .claude-plugin/plugin.json
├── agents/plugin-name.md (300-400 lines)
├── commands/command-name.md
└── README.md
```

### 2. Orchestrator-Worker Pattern

Orchestrator coordinates parallel workers. Use for independent subtasks requiring parallelization.

```
plugin-name/
├── .claude-plugin/plugin.json
├── agents/
│   ├── plugin-orchestrator.md (250-350 lines)
│   └── plugin-worker.md (100-200 lines)
├── skills/shared-guidelines/SKILL.md (300-500 lines)
└── commands/command-name.md
```

Orchestrator uses `Task` tool to spawn workers. Workers are stateless. Reference: `plugins/ui-ux-audit/`

### 3. Pipeline Pattern

Sequential chain where each agent's output feeds the next. Use for multi-stage workflows with distinct stage boundaries.

```
plugin-name/
├── agents/
│   ├── stage-1-agent.md
│   ├── stage-2-agent.md
│   └── stage-3-agent.md
└── commands/command-name.md
```

First agent delegates to second via Task tool, etc. Each validates input from previous stage.

### 4. Skill-Augmented Pattern

Agents reference shared skills for domain knowledge. Use when >100 lines of reference material needed by multiple agents.

```
plugin-name/
├── agents/agent-name.md (references skill)
├── skills/domain-guidelines/SKILL.md (300-500 lines)
└── commands/command-name.md
```

Skills contain methodology, not workflow logic. Can combine with any pattern.

### Pattern Selection

- Parallelizable → Orchestrator-Worker
- Multi-stage → Pipeline
- >100 lines reference material → Skill-Augmented
- Otherwise → Single Agent

Patterns can be combined.

## Best Practices

### Token Optimization

- **Agents**: 300-400 lines max (loaded with every execution)
- **Skills**: 300-500 lines OK (loaded only when referenced)
- **DRY**: Extract shared knowledge to skills, not duplicated in agents
- Reference templates/docs instead of inlining

### Descriptions

Use WHEN + WHEN NOT pattern: `[What it does]. Use PROACTIVELY for [triggers]. Do NOT use for: [anti-patterns].`

Example: "Orchestrates UI/UX audits. Use PROACTIVELY for `/ui-ux-audit`. Do NOT use for: single-page audits, code analysis."

### Naming

All `kebab-case`, lowercase:
- **Plugins**: `domain-focus` (e.g., `ui-ux-audit`)
- **Agents**: `[plugin-prefix-]role` (e.g., `ui-ux-audit-orchestrator`)
- **Skills**: `domain-guidelines` (e.g., `plugin-creation-guidelines`)
- **Commands**: `verb-object` (e.g., `/create-plugin`)

### Integration

- **Commands → Agents**: Delegate in command markdown
- **Agents → Skills**: Reference explicitly in agent prompt
- **Agents → Agents**: Use `Task` tool for spawning
- **Skills → Scripts**: Reference supporting scripts

### Tool Access

Grant only necessary tools. Common: Read/Write/Edit (files), Grep/Glob (search), TodoWrite (tracking), Task (spawning), Bash (scripts).

**Anti-pattern**: Giving all tools to all agents.

## Templates & Scripts

Templates in `templates/`: plugin.json, agent/skill frontmatter, command/README structures.
Scripts in `scripts/`: generation and validation tools (support `--help`).

## Reference

See `plugins/ui-ux-audit/` for validated Orchestrator-Worker + Skill-Augmented implementation.
