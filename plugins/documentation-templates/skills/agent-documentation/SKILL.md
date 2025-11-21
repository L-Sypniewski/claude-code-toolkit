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

```markdown
# Project Name

Brief description of the project and its purpose.

## Setup

Exact commands to set up the development environment:

```bash
npm install
cp .env.example .env
npm run db:migrate
```

## Build & Test

Commands AI agents should use:

```bash
# Build
npm run build

# Test
npm test
npm run test:integration

# Lint
npm run lint
```

## Project Structure

```
src/
  ├── api/        # REST API endpoints
  ├── models/     # Database models
  ├── services/   # Business logic
  └── utils/      # Helper functions
```

## Coding Conventions

### Code Style
- Use TypeScript strict mode
- Prefer functional programming patterns
- Use async/await (no promise chains)
- Maximum function length: 50 lines

### Naming
- Components: PascalCase
- Functions: camelCase
- Constants: UPPER_SNAKE_CASE
- Files: kebab-case.ts

### Error Handling
- Always use try-catch for async operations
- Throw custom error classes
- Log errors with context

## Testing Guidelines

- Write tests for all public APIs
- Use descriptive test names
- Mock external dependencies
- Aim for 80% coverage minimum

## Commits & PRs

- Use conventional commits: `feat:`, `fix:`, `docs:`
- Keep PRs under 400 lines
- Include tests with code changes
- Update docs when changing APIs

## What NOT to Touch

- Do not modify `/config/secrets.json`
- Do not change database migrations once merged
- Leave `/legacy` folder unchanged

## Additional Context

- We use JWT for authentication
- Database: PostgreSQL with TypeORM
- API follows REST conventions
- Frontend: React with TypeScript
```

## Key Sections

### 1. Setup Commands
Provide exact, copy-paste commands for environment setup. Be explicit.

### 2. Build & Test Commands
List all commands AI agents need to validate their changes.

### 3. Project Structure
Explain directory organization so agents know where to put new code.

### 4. Coding Conventions
Specify code style, naming conventions, patterns to follow.

### 5. Testing Guidelines
Define testing expectations and requirements.

### 6. Boundaries
Explicitly state what files/folders agents should never modify.

## Best Practices

### Be Explicit
- Don't assume agents know conventions
- Provide examples for complex patterns
- Use exact commands, not descriptions

### Keep Updated
- Update when conventions change
- Sync with actual project state
- Remove outdated information

### Be Specific
- "Use TypeScript strict mode" not "Use TypeScript properly"
- "Maximum 50 lines per function" not "Keep functions short"
- "npm test && npm run lint" not "Make sure tests pass"

### Provide Context
- Explain architectural decisions
- Note performance considerations
- Highlight security requirements

## Integration with Claude Code

AGENTS.md works alongside Claude Code agents:
- Claude Code agents can reference AGENTS.md for project context
- Use AGENTS.md for project-specific conventions
- Use agent specifications (.md files) for agent-specific behavior

## Example Templates

### Minimal AGENTS.md
```markdown
# MyApp

Node.js API project.

## Setup
```bash
npm install
```

## Test
```bash
npm test
```

## Style
- Use ESLint config
- Prefer async/await
- Write JSDoc for public functions
```

### Comprehensive AGENTS.md
Include all sections above plus:
- Database schema notes
- API authentication details
- Deployment instructions
- Performance targets
- Security considerations

## Common Pitfalls

### Too Vague
❌ "Write good tests"
✅ "Write unit tests for all services, integration tests for APIs, coverage >80%"

### Missing Commands
❌ "Set up the environment"
✅ "npm install && cp .env.example .env && npm run db:migrate"

### Outdated Information
- Review AGENTS.md quarterly
- Update when major changes occur
- Remove deprecated patterns

## Further Reading

- [AGENTS.md Specification](https://agents.md/)
- [GitHub's AGENTS.md Guide](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [OpenAI AGENTS.md Repo](https://github.com/openai/agents.md)
