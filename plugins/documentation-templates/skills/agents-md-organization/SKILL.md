---
name: agents-md-organization
description: Patterns and best practices for organizing large AGENTS.md files using nested structure, modular references, and separation of concerns. Use when AGENTS.md files become too large or need better organization for context window efficiency.
---

# AGENTS.md Organization Patterns

This skill provides patterns and best practices for organizing large AGENTS.md files to save context window space and improve maintainability.

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

## Organization Patterns

### Pattern 1: Root + Referenced Details

**Root AGENTS.md** contains:
- TL;DR with project overview
- High-level architecture
- General coding standards
- Quality gates
- References to detailed documentation

**Referenced detail files** contain:
- Detailed coding conventions (e.g., `docs/coding-standards.md`)
- Comprehensive testing guidelines (e.g., `docs/testing-guide.md`)
- Architecture deep-dives (e.g., `docs/architecture.md`)
- Technology-specific details (e.g., `docs/blazor-patterns.md`)

**Example Root AGENTS.md Structure:**

```markdown
# ProjectName - Development Guide

## TL;DR
- Stack: [Key technologies]
- Quality Gates: [Essential commands]
- Key Constraints: [Critical limitations]

## Architecture Overview
High-level architecture description.

**For detailed architecture**: See [docs/architecture.md](docs/architecture.md)

## Coding Standards
Core principles: SOLID, KISS, YAGNI

**For detailed conventions**: See [docs/coding-standards.md](docs/coding-standards.md)

## Quality Gates
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Testing
Test with xUnit and AwesomeAssertions.

**For detailed testing guidelines**: See [docs/testing-guide.md](docs/testing-guide.md)
```

### Pattern 2: Nested AGENTS.md for Subprojects

For monorepos or projects with distinct components, create nested AGENTS.md files:

**Repository Structure:**
```
/
├── AGENTS.md                    # Root - general architecture
├── docs/
│   ├── architecture.md
│   └── coding-standards.md
├── backend/
│   ├── AGENTS.md                # Backend-specific instructions
│   └── src/
├── frontend/
│   ├── AGENTS.md                # Frontend-specific instructions
│   └── src/
└── infra/
    ├── AGENTS.md                # Infrastructure-specific instructions
    └── terraform/
```

**Root AGENTS.md:**
```markdown
# ProjectName - Development Guide

## TL;DR
- Monorepo with backend (Node.js), frontend (React), infrastructure (Terraform)
- Each component has its own AGENTS.md with specific instructions

## Repository Structure
- `backend/` - Node.js API server. See [backend/AGENTS.md](backend/AGENTS.md)
- `frontend/` - React SPA. See [frontend/AGENTS.md](frontend/AGENTS.md)
- `infra/` - Terraform configs. See [infra/AGENTS.md](infra/AGENTS.md)

## General Coding Standards
[General standards that apply to all components]
```

**backend/AGENTS.md:**
```markdown
# Backend - Development Guide

Inherits from root AGENTS.md, adds backend-specific context.

## Stack
- Node.js 20, Express, PostgreSQL, Jest

## Key Commands
```bash
cd backend
npm install
npm run dev      # Start dev server
npm test         # Run tests
npm run lint     # Lint code
```

## Backend-Specific Conventions
[Detailed backend conventions]

## Testing
[Detailed backend testing guidelines]
```

### Pattern 3: Category-Based Organization

Split by concern type:

```
/
├── AGENTS.md                    # Overview + references
├── .github/
│   └── agents/                  # Agent instructions (isolated from root)
│       ├── architecture.md
│       ├── coding-standards.md
│       ├── testing-guide.md
│       └── deployment.md
```

**Benefits:**
- Clear separation of concerns
- Easy to find specific information
- Agents load only what they need

### Pattern 4: Tests Subdirectory Pattern

When test guidelines are extensive, create nested AGENTS.md in test directory:

```
/
├── AGENTS.md                    # Root
├── src/
└── tests/
    ├── AGENTS.md                # Comprehensive testing guidelines
    └── ...
```

**Root AGENTS.md references:**
```markdown
## Testing
**Refer to `tests/AGENTS.md` for all testing guidelines.**

- Stack: xUnit, AwesomeAssertions, Testcontainers
- Run: `dotnet test`
```

**tests/AGENTS.md contains:**
- Detailed testing philosophy
- Test categories and organization
- Assertion library usage
- Mock patterns
- Integration test setup
- E2E test patterns

## How AI Agents Use Nested AGENTS.md

AI agents (Claude Coder, GitHub Copilot, Cursor) automatically:
1. **Load root AGENTS.md** first for general context
2. **Discover nested AGENTS.md files** when working in subdirectories
3. **Merge settings** with more specific (nested) files taking precedence
4. **Follow referenced links** when deeper context is needed

This ensures agents have:
- Right amount of context (not too much, not too little)
- Relevant local knowledge for their current location
- Ability to deep-dive when needed

## Migration Strategy

To reorganize an existing large AGENTS.md:

### Step 1: Identify Sections
Categorize current content:
- [ ] General architecture (keep in root)
- [ ] Core standards (keep in root)
- [ ] Quality gates (keep in root)
- [ ] Detailed conventions (move to separate file)
- [ ] Testing details (move to separate file or tests/AGENTS.md)
- [ ] Technology-specific details (move to separate files)
- [ ] Subproject details (move to nested AGENTS.md)

### Step 2: Create Structure
```bash
# Create directories
mkdir -p docs
mkdir -p .github/agents  # Optional: isolate from root

# Create detail files
touch docs/architecture.md
touch docs/coding-standards.md
touch docs/testing-guide.md
```

### Step 3: Extract Content
Move detailed sections to appropriate files, keeping structure:

**Before (Large AGENTS.md):**
```markdown
# Project - Development Guide

## Coding Standards
[10 pages of detailed conventions]

## Testing
[15 pages of testing details]
```

**After (Organized):**

**AGENTS.md:**
```markdown
# Project - Development Guide

## Coding Standards
Core principles: SOLID, KISS, YAGNI

**Detailed conventions**: [docs/coding-standards.md](docs/coding-standards.md)

## Testing
Use xUnit with AwesomeAssertions.

**Detailed guidelines**: [docs/testing-guide.md](docs/testing-guide.md)
```

**docs/coding-standards.md:**
```markdown
# Coding Standards

[10 pages of detailed conventions]
```

**docs/testing-guide.md:**
```markdown
# Testing Guide

[15 pages of testing details]
```

### Step 4: Add Navigation
Include clear references in root AGENTS.md:

```markdown
## Quick Links
- [Architecture Details](docs/architecture.md)
- [Coding Standards](docs/coding-standards.md)
- [Testing Guide](docs/testing-guide.md)
- [Backend Instructions](backend/AGENTS.md)
- [Frontend Instructions](frontend/AGENTS.md)
```

## Best Practices

### DO
✅ Keep root AGENTS.md under 300-400 lines
✅ Use nested AGENTS.md for distinct subprojects
✅ Extract detailed information to referenced files
✅ Maintain clear navigation with links
✅ Keep quality gates and key commands in root
✅ Update nested files when local conventions change

### DON'T
❌ Duplicate information across files
❌ Create too many nested levels (2-3 max)
❌ Put all detail in root AGENTS.md
❌ Create nested AGENTS.md without clear purpose
❌ Forget to reference nested files from root
❌ Mix subproject details in root AGENTS.md

## Context Window Efficiency

### Before Organization
- Root AGENTS.md: 1200 lines
- Agent loads entire file every time
- Context window: ~1200 lines consumed

### After Organization
- Root AGENTS.md: 200 lines (overview + references)
- backend/AGENTS.md: 300 lines (loaded only when in backend)
- docs/testing-guide.md: 400 lines (loaded only when needed)
- Context window: 200-500 lines depending on location and need

**Savings: 60-75% context window reduction**

## Real-World Examples

### Example 1: .NET Monolith
```
/
├── AGENTS.md                         # 250 lines - overview
├── docs/
│   ├── architecture.md               # Architecture deep-dive
│   └── coding-standards.md           # .NET conventions
├── src/
│   └── Project/
└── tests/
    ├── AGENTS.md                     # 350 lines - testing guidelines
    └── ...
```

### Example 2: Microservices Monorepo
```
/
├── AGENTS.md                         # 200 lines - general standards
├── services/
│   ├── auth-service/
│   │   ├── AGENTS.md                 # Auth service specifics
│   │   └── src/
│   ├── api-gateway/
│   │   ├── AGENTS.md                 # Gateway specifics
│   │   └── src/
│   └── data-service/
│       ├── AGENTS.md                 # Data service specifics
│       └── src/
└── docs/
    ├── architecture.md
    └── deployment.md
```

### Example 3: Full-Stack Web App
```
/
├── AGENTS.md                         # 300 lines - overview
├── backend/
│   ├── AGENTS.md                     # Node.js + PostgreSQL
│   └── src/
├── frontend/
│   ├── AGENTS.md                     # React + TypeScript
│   └── src/
└── docs/
    ├── api-docs.md
    └── design-system.md
```

## Template: Organized Root AGENTS.md

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

## Further Reading

- [AGENTS.md Specification](https://agents.md/)
- [GitHub's AGENTS.md Nested Files Support](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)
- [How to Write Great AGENTS.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
