---
name: agents-md-organization
description: Patterns and best practices for organizing large AGENTS.md files using nested structure and modular references. Use when AGENTS.md is too large, needs reorganization, context window optimization, or splitting into modular files. Applies to monorepos, multi-component projects, and files over 500 lines.
---

# AGENTS.md Organization Patterns

Patterns and best practices for organizing large AGENTS.md files to save context window space and improve maintainability.

## The Problem

Large AGENTS.md files can:
- Consume excessive context window space
- Mix general architecture with implementation details
- Be difficult to maintain and update
- Overwhelm agents with too much information at once

## The Solution: Modular Organization

AGENTS.md supports **nested structure** and **file references**, allowing you to:
1. Keep root AGENTS.md focused on general architecture and standards
2. Place detailed information in separate referenced files
3. Create nested AGENTS.md files for subprojects (backend, frontend, infra)
4. Let agents load only relevant context for their current task

**For detailed organization patterns**, see [patterns/organization-patterns.md](patterns/organization-patterns.md).

## How AI Agents Use Nested AGENTS.md

AI agents (Claude Code, GitHub Copilot, Cursor) automatically:
1. **Load root AGENTS.md** first for general context
2. **Discover nested AGENTS.md files** when working in subdirectories
3. **Merge settings** with more specific (nested) files taking precedence
4. **Follow referenced links** when deeper context is needed

This ensures agents have:
- Right amount of context (not too much, not too little)
- Relevant local knowledge for their current location
- Ability to deep-dive when needed

## Best Practices

### DO
- Keep root AGENTS.md concise and scannable
- Use nested AGENTS.md for distinct subprojects
- Extract detailed information to referenced files
- Maintain clear navigation with links
- Keep quality gates and key commands in root
- Update nested files when local conventions change

### DON'T
- Duplicate information across files
- Create too many nested levels (2-3 max)
- Put all detail in root AGENTS.md
- Create nested AGENTS.md without clear purpose
- Forget to reference nested files from root
- Mix subproject details in root AGENTS.md

## Context Window Efficiency

| State | What Loads | Benefit |
|-------|------------|---------|
| Before (single file) | Entire file every time | All content competes for context |
| After (organized) | Root + relevant nested files | Only relevant context loaded |

**For migration steps**, see [guides/migration-strategy.md](guides/migration-strategy.md).

**For real-world examples**, see [examples/organization-examples.md](examples/organization-examples.md).

**For a root AGENTS.md template**, see [templates/organized-root-agents-md.md](templates/organized-root-agents-md.md).

## Further Reading

- [AGENTS.md Specification](https://agents.md/)
- [GitHub's AGENTS.md Nested Files Support](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)
- [How to Write Great AGENTS.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
