# Skills Summary

Quick reference for all Claude Code Skills in the toolkit.

## By Plugin

### Context Engineering (2 skills)

| Skill                     | Description                         | Use When                          |
| ------------------------- | ----------------------------------- | --------------------------------- |
| `prp-structure`           | Standard PRP document format        | Creating/formatting PRP documents |
| `github-issue-processing` | Extract actionable info from issues | Analyzing GitHub issues           |

### Development Workflow (10 skills)

| Skill                        | Description                                          | Use When                                            |
| ---------------------------- | ---------------------------------------------------- | --------------------------------------------------- |
| `feature-planning`           | End-to-end feature implementation workflow           | Feature development from requirements to completion |
| `requirements-extraction`    | Extract requirements from various sources            | Processing GitHub issues, prompts, or files         |
| `requirements-normalization` | Normalize requirements to standard format            | Converting raw input to structured requirements     |
| `requirements-clarification` | Ask clarifying questions for incomplete requirements | Resolving gaps in requirements                      |
| `complexity-scoring`         | 0-8 point complexity assessment                      | Evaluating feature complexity                       |
| `plan-validation-checklist`  | Validate plans for completeness and feasibility      | Quality-gating implementation plans                 |
| `code-review-checklist`      | Comprehensive code review                            | Performing code reviews                             |
| `refactoring-patterns`       | Code refactoring techniques                          | Planning/executing refactoring                      |
| `workflow-orchestration`     | Multi-step workflow coordination                     | Managing complex workflows                          |
| `ui-design-guidelines`       | Frontend UI design methodology and spec templates    | Designing UI layouts and visual systems             |

### Git & Project Management (1 skill)

| Skill                   | Description           | Use When                            |
| ----------------------- | --------------------- | ----------------------------------- |
| `git-worktree-patterns` | Git worktree patterns | Parallel development with worktrees |

### Documentation Templates (2 skills)

| Skill                     | Description               | Use When                       |
| ------------------------- | ------------------------- | ------------------------------ |
| `agent-documentation`     | AGENTS.md for AI agents   | Creating AI agent instructions |
| `claude-delegation-rules` | Agent delegation patterns | Designing agent systems        |

### UI/UX Audit (1 skill)

| Skill                    | Description                          | Use When                        |
| ------------------------ | ------------------------------------ | ------------------------------- |
| `ui-ux-audit-guidelines` | Professional UI/UX audit methodology | Conducting visual design audits |

## By Use Case

### Code Quality

- `code-review-checklist` - Systematic review process
- `refactoring-patterns` - Safe refactoring techniques

### Development Workflow

- `feature-planning` - End-to-end feature implementation
- `requirements-extraction` - Extract requirements from sources
- `requirements-normalization` - Standardize requirement formats
- `requirements-clarification` - Resolve requirement gaps
- `workflow-orchestration` - Complex workflow coordination
- `prp-structure` - Structured problem-solving
- `git-worktree-patterns` - Parallel development with worktrees

### Documentation

- `agent-documentation` - AGENTS.md for AI coding agents
- `claude-delegation-rules` - Agent coordination patterns

### UI/UX Design Quality

- `ui-ux-audit-guidelines` - Professional audit methodology and design vocabulary
- `ui-design-guidelines` - Frontend UI design methodology and spec templates

### Issue & Code Analysis

- `github-issue-processing` - Issue analysis
- `code-review-checklist` - Code quality review

## Quick Stats

- **Total Skills**: 16
- **Total Plugins with Skills**: 5
- **Average Skills per Plugin**: 3.2
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
