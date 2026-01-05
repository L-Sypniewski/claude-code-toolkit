# Template: Organized Root AGENTS.md

Use this template for root AGENTS.md files that reference detailed documentation.

```markdown
# ProjectName - Development Guide

## TL;DR
- Stack: [Technologies]
- Quality Gates: [Commands]
- Structure: [Monorepo/Subprojects]

## Quick Links
- [Architecture](docs/architecture.md)
- [Coding Standards](docs/coding-standards.md)
- [Testing Guide](docs/testing-guide.md)
- [Backend Instructions](backend/AGENTS.md) - if applicable
- [Frontend Instructions](frontend/AGENTS.md) - if applicable

## Repository Structure
- `src/` or `backend/` - [Description]
- `tests/` - [Description]

## Quality Gates
[Essential commands for build/test/lint]

## Core Coding Standards
[High-level principles]

**Detailed conventions**: [docs/coding-standards.md](docs/coding-standards.md)

## Testing Overview
[High-level testing approach]

**Detailed guidelines**: [docs/testing-guide.md](docs/testing-guide.md)

## Agent Workflow Tips
[Key workflow patterns]
```

## Template Guidelines

1. **TL;DR first**: Most important information at the top
2. **Quick Links**: Navigation to all detailed docs
3. **Keep it brief**: Summary of each section, details in referenced files
4. **Stay concise**: Root should be scannable, not comprehensive
5. **Clear references**: Use relative links to detail files
