---
name: agent-documentation
description: Standards for creating AGENTS.md files that guide AI coding agents working with your codebase. Use when creating instructions for AI agents to follow project conventions, setup, and workflows.
---

# AGENTS.md Documentation

This skill provides standards for creating AGENTS.md files - dedicated instructions for AI coding agents working with your codebase.

## What is AGENTS.md?

AGENTS.md is the "README for AI agents" - a machine-readable guide that provides explicit instructions for AI coding tools (like Claude, Copilot, Cursor) working with your project. Unlike README.md (for humans), AGENTS.md gives AI agents unambiguous, step-by-step guidance.

## Purpose

- **Centralized Instructions**: Single source of truth for all AI agents
- **Explicit Guidance**: Clear setup commands, coding standards, testing workflows
- **Project Context**: Architecture decisions, conventions, constraints
- **Consistency**: Ensures AI-generated code matches project standards

## AGENTS.md Structure

Based on real-world examples, a well-structured AGENTS.md follows this pattern:

```markdown
# ProjectName - Development Guide

**Stack**: [Tech stack components]
**Principles**: [Core development principles, e.g., SOLID, KISS, YAGNI]

## Project Overview

[Brief description of architecture and approach]

## Repository Structure

- `path/to/main/`: [Description]
- `path/to/tests/`: [Description]
- `path/to/config/`: [Description]

## Key Commands

```bash
# Core commands
[build command]
[test command]
[format command]

# Additional tools
[migration/deployment commands]
[additional commands]
```

## Quality Gates (Required)

Define the quality standards that must be met:

### Code Quality
- [ ] Build succeeds without errors
- [ ] All tests pass
- [ ] Code formatting/linting passes
- [ ] No compiler warnings

### Testing Requirements
- [ ] Integration tests for key workflows (favor sociable tests over isolated unit tests)
- [ ] Avoid excessive mocking - test real collaborations
- [ ] All edge cases and error paths covered

### Code Review Standards
- [ ] Follows project conventions
- [ ] No code smells or anti-patterns
- [ ] Proper error handling
- [ ] Security considerations addressed

## Coding Conventions (Optional)

[Project-specific coding standards]

## Testing Guidelines (Optional)

[Testing expectations]

## What NOT to Touch (Optional)

[Protected files/folders]
```

## Key Sections Explained

### 1. Title and Metadata (Required)
**Format**: `# ProjectName - Development Guide`

Include **Stack** and **Principles** at the top for quick reference.

### 2. Project Overview (Required)
Brief architectural summary - what type of project, key technologies, approach.

### 3. Repository Structure (Required)
Map of directories with brief descriptions. Helps agents understand where code lives.

### 4. Key Commands (Required)
Copy-paste commands for:
- Building the project
- Running tests
- Formatting code
- Database migrations or other critical operations

### 5. Quality Gates (Required)
Define quality standards that code must meet:
- **Code Quality**: Build, test, lint requirements
- **Testing Requirements**: Coverage thresholds, test types needed
- **Code Review Standards**: Conventions, patterns, security checks

### 6. Optional Sections
Add as needed:
- **Coding Conventions**: Project-specific rules
- **Testing Guidelines**: Coverage expectations, testing approach
- **What NOT to Touch**: Protected files/folders agents should avoid

## Best Practices

### Start with Essentials
Include at minimum: Stack, Principles, Project Overview, Repository Structure, and Key Commands.

### Be Explicit and Specific
❌ "Set up the environment"  
✅ "npm install && cp .env.example .env"

❌ "Write good tests"  
✅ "Write unit tests for all services, aim for >80% coverage"

### Use Exact Commands
Provide copy-paste ready commands. AI agents will execute them literally.

### Keep It Updated
Review and update AGENTS.md when project structure or conventions change.

## Integration with Claude Code

AGENTS.md works alongside Claude Code agents:
- Claude Code agents can reference AGENTS.md for project context
- Use AGENTS.md for project-specific conventions
- Use agent specifications (.md files) for agent-specific behavior

## Complete Example

```markdown
# StockToolset - Development Guide

**Stack**: .NET 10, ASP.NET Core Minimal APIs, .NET Aspire 13, PostgreSQL, PGMQ.
**Principles**: SOLID, KISS, YAGNI. Consistency over innovation.

## Project Overview

Cloud-native .NET 10 modular monolith using Vertical Slice Architecture, 
Aspire 13, PostgreSQL, and PGMQ.

## Repository Structure

- `StockStorage/src/`: Main app (Features/, Database/, Infrastructure/)
- `StockStorage/tests/`: Unified test project (Unit, Integration, System)
- `StockStorage.AppHost/`: .NET Aspire orchestration
- `StockStorage.ServiceDefaults/`: Shared Aspire defaults

## Key Commands

```bash
# Core
dotnet build
dotnet test # Requires Docker
dotnet format

# EF Core
dotnet ef migrations add <MigrationName>
dotnet ef database update
```

## Quality Gates

### Code Quality
- [ ] `dotnet build` succeeds with zero warnings
- [ ] `dotnet format` shows no formatting issues
- [ ] All tests pass (`dotnet test`)

### Testing Requirements
- [ ] Integration tests for all API endpoints (favor sociable tests)
- [ ] Avoid excessive mocking - test real collaborations
- [ ] All edge cases and error paths tested

### Code Review Standards
- [ ] Follows Vertical Slice Architecture
- [ ] SOLID, KISS, YAGNI principles applied
- [ ] No code duplication
- [ ] Proper error handling and logging

## Coding Conventions

- Follow SOLID, KISS, YAGNI principles
- Consistency over innovation
- Use Vertical Slice Architecture per feature
```

## Further Reading

- [AGENTS.md Specification](https://agents.md/)
- [GitHub's AGENTS.md Guide](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [OpenAI AGENTS.md Repo](https://github.com/openai/agents.md)
