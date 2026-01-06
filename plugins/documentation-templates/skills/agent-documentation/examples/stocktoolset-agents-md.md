# Complete AGENTS.md Example: StockToolset

This is a real-world example of an AGENTS.md file for a .NET project.

```markdown
# StockToolset - Development Guide

**Stack**: .NET 10, ASP.NET Core Minimal APIs, .NET Aspire 13, PostgreSQL, PGMQ.
**Principles**: SOLID, KISS, YAGNI. Consistency over innovation.

## Project Overview

Cloud-native .NET 10 modular monolith using Vertical Slice Architecture,
Aspire 13, PostgreSQL, and PGMQ.

## Repository Structure

- `StockStorage/src/`: Main app (Features/, Database/, Infrastructure/)
- `StockStorage/tests/`: Unified test project (Unit, Integration, System). **See `StockStorage/tests/AGENTS.md`**.
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

## Testing

**Refer to `StockStorage/tests/AGENTS.md` for all testing guidelines.**

- Stack: TUnit, AwesomeAssertions, Testcontainers.
- Categories: Unit, Integration, System.

## Quality Gates

### Code Quality
- [ ] `dotnet build` succeeds with zero warnings
- [ ] `dotnet format` shows no formatting issues
- [ ] All tests pass (`dotnet test`)

### Testing Requirements
- [ ] Integration tests for key workflows (favor sociable tests)
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

## What Makes This Example Good

1. **TL;DR at the top**: Stack and Principles immediately visible
2. **Clear structure**: Logical hierarchy from overview to details
3. **Nested AGENTS.md reference**: Testing details in dedicated file
4. **Actionable commands**: Copy-paste ready
5. **Checkboxes for quality gates**: Clear, verifiable criteria
6. **Concise**: Main guide stays focused, detailed content referenced elsewhere
