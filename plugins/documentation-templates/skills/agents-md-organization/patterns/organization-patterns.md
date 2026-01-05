# AGENTS.md Organization Patterns

Four patterns for organizing large AGENTS.md files to save context window space.

## Pattern 1: Root + Referenced Details

**Best for**: Single projects with detailed documentation that's becoming unwieldy

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

---

## Pattern 2: Nested AGENTS.md for Subprojects

**Best for**: Monorepos or projects with distinct components

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

---

## Pattern 3: Category-Based Organization

**Best for**: Complex projects with multiple technology domains

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

---

## Pattern 4: Tests Subdirectory Pattern

**Best for**: Projects where testing guidelines are substantial relative to other content

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

---

## Pattern Selection Guide

| Scenario | Recommended Pattern |
|----------|---------------------|
| Single project, detailed docs | Pattern 1: Root + Referenced |
| Monorepo with distinct components | Pattern 2: Nested AGENTS.md |
| Multiple technology domains | Pattern 3: Category-Based |
| Heavy testing documentation | Pattern 4: Tests Subdirectory |
| Combination of above | Mix patterns as needed |
