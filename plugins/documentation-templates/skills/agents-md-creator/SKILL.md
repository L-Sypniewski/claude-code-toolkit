---
name: agents-md-creator
description: Create comprehensive AGENTS.md files following the agents.md standard. Use when users need to create "README for agents" documentation providing context, commands, and conventions for autonomous coding agents. Follows official format standards from agents.md, includes discovery phase, validation checkpoints, and ensures accuracy over assumptions. Generates living documentation with quality gates, coding standards, and agent-specific workflows.
---

# AGENTS.md Creator

Specialized skill for creating comprehensive AGENTS.md files that serve as "README for agents" - providing detailed context, commands, and conventions for autonomous coding agents.

## When to Use

- Creating AGENTS.md files for repositories
- Documenting agent-specific workflows and conventions
- Establishing quality gates for autonomous agents
- Providing structured guidance for AI coding assistants
- Complementing human-focused README documentation

## What is AGENTS.md?

AGENTS.md provides everything an autonomous coding agent needs to work effectively in a repository:
- Technology stack and setup instructions
- Build, test, and deployment commands
- Quality gates and validation requirements
- Coding standards and patterns
- Common pitfalls and edge cases

**Official Standard**: https://agents.md/

## Creation Methodology

### Phase 1: Planning

**Create Detailed Plan** before starting:

```markdown
# AGENTS.md Creation Plan

## Discovery Steps
- [ ] Analyze project structure
- [ ] Identify technology stack
- [ ] Find build/test commands
- [ ] Review existing documentation

## Sections to Include
- [ ] TL;DR
- [ ] Repository structure
- [ ] Environment setup
- [ ] Quality gates
- [ ] Coding standards
- [ ] Testing expectations

## Validation Checkpoints
- [ ] Verify all commands work
- [ ] Cross-reference with codebase
- [ ] Validate tool versions
- [ ] Test quality gates

## Timeline
- Discovery: [time estimate]
- Structure creation: [time estimate]
- Validation: [time estimate]
- Finalization: [time estimate]
```

### Phase 2: Discovery

**Understand Project Structure**:
- Use semantic search to explore codebase
- Read README.md and contributing guidelines
- Check package files (package.json, requirements.txt, etc.)
- Examine configuration files
- Look for existing agent documentation

**Identify Technology Stack**:
- Primary languages and frameworks
- Build tools and package managers
- Testing frameworks
- Deployment methods
- Development tools

**Find Quality Gates**:
- Build commands
- Test commands
- Lint commands
- Type checking
- Security scanning

### Phase 3: Validation (Critical)

**Cross-Reference with Codebase**:
- Verify package manager by checking lock files
- Confirm testing framework from dependencies
- Validate build commands in config files
- Check actual directory structure
- Test that commands actually work

**Accuracy Requirements**:
- Never guess tool or framework names
- Always verify commands execute successfully
- Cross-check version numbers
- Validate file paths and directory names

### Phase 4: Structure Creation

## AGENTS.md Template Structure

### TL;DR Section

```markdown
## TL;DR
- Primary stack: [Key technologies - be specific]
- Essential quality gates: [Critical commands agents must run]
  - Build: `[exact command]`
  - Test: `[exact command]`
  - Lint: `[exact command]`
- Key constraints: [Important limitations]
- Critical rules: [Most important rules agents must follow]
```

### Repository at a Glance

```markdown
## Repository at a Glance

├── frontend/          # [Brief description]
├── backend/           # [Brief description]
├── tests/             # [Test organization]
└── docs/              # [Documentation location]

Primary workflows:
- Development: [workflow description]
- Testing: [testing approach]
- Deployment: [deployment process]
```

### Environment & Setup

```markdown
## Environment & Setup

### Required Tooling
- Node.js: ^18.0.0 (verified in .nvmrc)
- Python: 3.11+ (verified in pyproject.toml)
- [Other tools with versions]

### Repository Configuration
1. Copy `.env.example` to `.env`
2. Install dependencies: `[exact command]`
3. [Additional setup steps]

### [Technology-Specific Setup]
[Framework-specific configuration]
```

### Running the App

```markdown
## Running the App

### Frontend
```bash
cd frontend
npm run dev
# Runs on http://localhost:3000
```

### Backend
```bash
cd backend
python manage.py runserver
# Runs on http://localhost:8000
```

### Tooling & Automation
- Hot reload: Enabled by default
- Debug mode: `[command]`
- [Other development tools]
```

### Quality Gates ✅

```markdown
## Quality Gates ✅

**Agents must run ALL quality gates before marking work complete.**

### Frontend
```bash
cd frontend
npm run build      # Build must succeed
npm run lint       # Zero errors/warnings
npm run type-check # Zero type errors
npm test           # All tests must pass
```

### Backend
```bash
cd backend
pytest                    # All tests pass
ruff check .             # Zero lint errors
mypy .                   # Zero type errors
```

### Reporting
Agents must report quality gate results as **PASS/FAIL** in completion summary:
- Build: PASS/FAIL
- Lint: PASS/FAIL
- Tests: PASS/FAIL
```

### Coding Standards & Patterns

```markdown
## Coding Standards & Patterns

### General Principles
- Follow existing code patterns - consistency over innovation
- Understand before modifying - search, read, research first
- KISS and YAGNI - avoid overengineering
- Ask for clarification when uncertain

### [Language] Conventions
- Naming: [conventions]
- Organization: [structure rules]
- Documentation: [doc requirements]

### Architecture Principles
- [Pattern 1]: [description and rationale]
- [Pattern 2]: [description and rationale]

### Performance Considerations
- [Important performance rules]
- [Common bottlenecks to avoid]
```

### Testing Expectations

```markdown
## Testing Expectations

### Unit Tests
- Framework: [Jest, Pytest, etc.]
- Location: [test file organization]
- Naming: `*.test.ts` or `test_*.py`
- Coverage: Minimum [X]% (measured by [tool])

### Integration Tests
- Framework: [specific framework]
- Location: [where integration tests live]
- Run with: `[exact command]`

### E2E Tests
- Framework: [Playwright, Cypress, etc.]
- Location: [e2e test location]
- Run with: `[exact command]`

### General Guidance
- Add tests for new features
- Update tests for changes
- Ensure all tests pass before completion
- Write tests that clearly describe behavior
```

### Data & Integrations

```markdown
## Data & Integrations

### Database
- Type: [PostgreSQL, MongoDB, etc.]
- Migrations: `[migration command]`
- Schema location: [where schema defined]

### External Services
- [Service 1]: [purpose and configuration]
- [Service 2]: [purpose and configuration]

### API Patterns
- REST endpoints: [conventions]
- Authentication: [method]
- Error handling: [pattern]
```

### Deployment & Ops

```markdown
## Deployment & Ops

### Local Development
- Start: `[command]`
- Stop: `[command]`
- Reset: `[command]`

### CI/CD Pipeline
- Platform: [GitHub Actions, etc.]
- Triggers: [when pipeline runs]
- Required checks: [list checks]

### Deployment
- Staging: [process]
- Production: [process]
- Rollback: [procedure]
```

### Agent Workflow Tips

```markdown
## Agent Workflow Tips

- Maintain explicit TODO list - exactly one item "in-progress" at a time
- Use sequential reasoning for multi-step tasks
- Document key assumptions in final summary
- Run smallest relevant test subset, but don't skip required quality gates
- When adding new commands, document them here
- Update this file when discovering new patterns
```

### Common Pitfalls & Edge Cases

```markdown
## Common Pitfalls & Edge Cases

### [Technology] Gotchas
- [Specific issue]: [solution]
- [Common error]: [how to avoid]

### Integration Challenges
- [Challenge]: [workaround]

### Performance Bottlenecks
- [Bottleneck]: [optimization approach]
```

### Need Help Section

```markdown
## Need Help?

### Documentation
- Architecture: [link to design docs]
- API Docs: [link to API documentation]
- Contributing: [link to contributing guide]

### Updating This File
Found a new pattern, command, or gotcha? Update this AGENTS.md immediately - it's the canonical playbook for all agents working on this project.

### Additional Resources
- Official agents.md standard: https://agents.md/
- Examples: https://github.com/search?q=path%3AAGENTS.md&type=code
```

## Critical Requirements

### Accuracy Over Assumptions

**Never Guess**:
- Package manager names
- Testing framework names
- Build tool names
- Command syntax

**Always Verify**:
- Commands actually work
- Tool versions are correct
- File paths exist
- Dependencies are accurate

**Cross-Check**:
- Lock files for package managers
- Config files for build tools
- Test files for testing frameworks
- Package files for dependencies

### Technology-Agnostic Principles

**Focus On**:
- Methodology rather than specific tech details
- Universal concepts (build, test, deploy)
- Logical project boundaries
- Workflow patterns

**Organize By**:
- Project structure (frontend/backend, services)
- Development phase (setup, development, testing)
- Quality assurance stages

### Agent-Specific Concerns

**Include**:
- Commands agents can run programmatically
- Quality gates agents must pass
- Automation workflows (CI/CD)
- Error handling expectations
- Failure recovery procedures

### Living Documentation

**Design For**:
- Evolution as project grows
- Easy updates by future agents
- Pattern discovery and documentation
- Continuous improvement

**Emphasize**:
- File should be updated with new patterns
- Agents should maintain accuracy
- Documentation evolves with codebase

## Validation Checklist

Before finalizing AGENTS.md:

- [ ] All commands are accurate and runnable
- [ ] Package managers match actual usage
- [ ] Testing frameworks correctly named
- [ ] File paths and directories accurate
- [ ] Quality gate commands pass
- [ ] Technology stack matches reality
- [ ] No contradictions between sections
- [ ] Build commands verified
- [ ] Test commands verified
- [ ] Lint commands verified
- [ ] Version numbers correct
- [ ] Directory structure accurate

## Example Sections by Technology

### Node.js/TypeScript Projects

```markdown
### Frontend (React/TypeScript)
- Package manager: npm (verified via package-lock.json)
- Build: `npm run build`
- Dev server: `npm run dev`
- Tests: `npm test` (Jest + React Testing Library)
- Lint: `npm run lint` (ESLint)
- Type check: `npm run type-check` (TypeScript)
```

### Python Projects

```markdown
### Backend (Python/Django)
- Package manager: pip (verified via requirements.txt)
- Virtual env: `python -m venv venv`
- Install: `pip install -r requirements.txt`
- Tests: `pytest` (pytest framework)
- Lint: `ruff check .` (Ruff linter)
- Type check: `mypy .` (MyPy)
```

### Multi-Service Projects

```markdown
### Services Architecture
├── frontend/ (Astro + TypeScript)
│   └── Quality gates: build, lint, type-check
├── backend/ (Strapi CMS)
│   └── Quality gates: build, lint
└── tests/ (Playwright E2E)
    └── Quality gates: e2e tests
```

## Integration with References

The skill includes reference files for additional context:

### Reference Files
Place example AGENTS.md files in `references/` subdirectory:
- `references/node-example.md` - Node.js project example
- `references/python-example.md` - Python project example
- `references/monorepo-example.md` - Monorepo example

These serve as templates and inspiration.

## Output Location

Create file at repository root: `./AGENTS.md`

## Quality Standards

The created AGENTS.md must be:
- **Accurate**: All information verified against codebase
- **Complete**: Covers all essential agent workflows
- **Actionable**: Provides executable commands
- **Clear**: Well-organized and easy to follow
- **Maintained**: Designed for ongoing updates
- **Agent-Focused**: Optimized for autonomous agents

## Anti-Patterns to Avoid

- Guessing tool or framework names
- Including unverified commands
- Copying from templates without validation
- Omitting quality gates
- Vague or ambiguous instructions
- Including outdated information
- Ignoring project-specific patterns
- Missing critical setup steps
- Forgetting to test commands
- Assuming without verifying
