# Skills Summary

Quick reference for all Claude Code Skills in the toolkit.

## By Plugin

### Context Engineering (2 skills)

| Skill | Description | Use When |
|-------|-------------|----------|
| `prp-structure` | Standard PRP document format | Creating/formatting PRP documents |
| `github-issue-processing` | Extract actionable info from issues | Analyzing GitHub issues |

### Development Workflow (3 skills)

| Skill | Description | Use When |
|-------|-------------|----------|
| `code-review-checklist` | Comprehensive code review | Performing code reviews |
| `refactoring-patterns` | Code refactoring techniques | Planning/executing refactoring |
| `workflow-orchestration` | Multi-step workflow coordination | Managing complex workflows |

### Git & Project Management (1 skill)

| Skill | Description | Use When |
|-------|-------------|----------|
| `git-workflow-patterns` | Git worktree patterns | Parallel development with worktrees |

### Documentation Templates (2 skills)

| Skill | Description | Use When |
|-------|-------------|----------|
| `agent-documentation` | AGENTS.md for AI agents | Creating AI agent instructions |
| `claude-delegation-rules` | Agent delegation patterns | Designing agent systems |

## By Use Case

### Code Quality
- `code-review-checklist` - Systematic review process
- `refactoring-patterns` - Safe refactoring techniques

### Development Workflow
- `workflow-orchestration` - Complex workflow coordination
- `prp-structure` - Structured problem-solving
- `git-workflow-patterns` - Parallel development with worktrees

### Documentation
- `agent-documentation` - AGENTS.md for AI coding agents
- `claude-delegation-rules` - Agent coordination patterns

### Issue & Code Analysis
- `github-issue-processing` - Issue analysis
- `code-review-checklist` - Code quality review

## Quick Stats

- **Total Skills**: 8
- **Total Plugins with Skills**: 4
- **Average Skills per Plugin**: 2
- **Specification**: Anthropic Agent Skills v1.0

## How Skills Work

Skills are automatically loaded by Claude when relevant context is detected. They provide:

- 📚 **Procedural Knowledge**: Step-by-step processes and workflows
- 📋 **Templates**: Reusable structures and formats
- ✅ **Checklists**: Comprehensive verification criteria
- 🎯 **Best Practices**: Proven patterns and techniques

Unlike agents (which do work) or commands (which trigger actions), skills provide reference knowledge that Claude accesses contextually.

## Further Reading

See [docs/SKILLS.md](docs/SKILLS.md) for complete documentation.
