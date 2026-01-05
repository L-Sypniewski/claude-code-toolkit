# Real-World Organization Examples

Examples of organized AGENTS.md structures for different project types.

## Example 1: .NET Monolith

```
/
├── AGENTS.md                         # Overview + quality gates
├── docs/
│   ├── architecture.md               # Architecture deep-dive
│   └── coding-standards.md           # .NET conventions
├── src/
│   └── Project/
└── tests/
    ├── AGENTS.md                     # Testing guidelines
    └── ...
```

**Benefit**: Agent loads root overview initially; detailed testing guidelines only when working in `tests/`

---

## Example 2: Microservices Monorepo

```
/
├── AGENTS.md                         # General standards
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

**Benefit**: Each service loads only its own AGENTS.md - agent working on `auth-service` doesn't load gateway or data service conventions

---

## Example 3: Full-Stack Web App

```
/
├── AGENTS.md                         # Overview
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

**Benefit**: Frontend work loads only frontend conventions; backend conventions stay out of context

---

## Why This Matters

### Before Organization

- Single large AGENTS.md file
- Agent loads entire file every time
- All conventions compete for context window space

### After Organization

- Root AGENTS.md contains overview + references
- Nested files loaded based on working directory
- Detailed docs loaded only when explicitly referenced
- Context window focused on relevant content

**Result**: Agent has relevant context for current task without being overwhelmed by unrelated conventions.
