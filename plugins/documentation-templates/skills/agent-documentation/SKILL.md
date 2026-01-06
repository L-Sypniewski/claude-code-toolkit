---
name: agent-documentation
description: Standards for creating AGENTS.md files that guide AI coding agents. Use when writing AGENTS.md, documenting project conventions for AI, creating agent instructions, or establishing coding standards for AI assistants.
---

# AGENTS.md Documentation

Standards for creating AGENTS.md files - dedicated instructions for AI coding agents working with your codebase.

## What is AGENTS.md?

AGENTS.md is the "README for AI agents" - a machine-readable guide that provides explicit instructions for AI coding tools (like Claude, Copilot, Cursor) working with your project. Unlike README.md (for humans), AGENTS.md gives AI agents unambiguous, step-by-step guidance.

**Important**: For large projects or monorepos, use modular organization (nested AGENTS.md files and referenced detail files) to save context window space. See the `agents-md-organization` skill for patterns.

## Purpose

- **Centralized Instructions**: Single source of truth for all AI agents
- **Explicit Guidance**: Clear setup commands, coding standards, testing workflows
- **Project Context**: Architecture decisions, conventions, constraints
- **Consistency**: Ensures AI-generated code matches project standards
- **Efficiency**: Modular organization saves context window space in complex projects

## AGENTS.md Structure

**For the complete template with all sections**, see [templates/basic-agents-md.md](templates/basic-agents-md.md).

**Required sections**:
1. **Title and Metadata** - Stack, Principles at top
2. **Project Overview** - Brief architectural summary
3. **Repository Structure** - Directory map with descriptions
4. **Key Commands** - Copy-paste ready build/test/lint commands
5. **Quality Gates** - Code quality, testing requirements, review standards

**Optional sections**: Coding Conventions, Testing Guidelines

## Best Practices

### Start with Essentials
Include at minimum: Stack, Principles, Project Overview, Repository Structure, and Key Commands.

### Be Explicit and Specific
- "Set up the environment" → `npm install && cp .env.example .env`
- "Write good tests" → "Write integration tests for all API endpoints, test real collaborations"

### Use Exact Commands
Provide copy-paste ready commands. AI agents will execute them literally.

### Keep It Updated
Review and update AGENTS.md when project structure or conventions change.

## Integration with Claude Code

AGENTS.md works alongside Claude Code agents:
- Claude Code agents can reference AGENTS.md for project context
- Use AGENTS.md for project-specific conventions
- Use agent specifications (.md files) for agent-specific behavior

## Examples

**For a complete real-world example**, see [examples/stocktoolset-agents-md.md](examples/stocktoolset-agents-md.md).

## Further Reading

- [AGENTS.md Specification](https://agents.md/)
- [GitHub's AGENTS.md Guide](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [OpenAI AGENTS.md Repo](https://github.com/openai/agents.md)
- **Organization patterns**: See `agents-md-organization` skill for modular structure
- **Complete example**: See `examples/ORGANIZED-STRUCTURE-EXAMPLE.md` for organized structure

**For large AGENTS.md files (>500 lines)**: Use `/organize-agents-md` command to reorganize into efficient modular structure.
