---
name: csharp-development
description: Expert guidance for .NET 10/C# 14 development covering best practices, design patterns, architecture, testing, and modern C# idioms. Emphasizes SOLID principles, YAGNI, feature slices, and simplicity. Use when writing, reviewing, or refactoring C# code, designing .NET applications, or implementing enterprise patterns. DO NOT use for non-.NET languages or frontend-only JavaScript/TypeScript work.
---

# .NET C# Development Expert

Expert .NET C# guidance for .NET 10 and C# 14. Focused on production-tested patterns from Blazor, ASP.NET Core, and Entity Framework Core applications.

## When to Use

**USE for:** C# code, .NET architecture, design patterns, testing, async/await, LINQ, ASP.NET Core, EF Core
**DON'T use for:** Non-.NET languages, frontend-only work, F#/VB.NET

## Core Principles

**SOLID** - Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion

**YAGNI** - You Aren't Gonna Need It. Avoid over-engineering, build what's needed now, not what might be needed later.

**Simplicity** - Prefer straightforward solutions over clever abstractions. Three similar lines are better than premature abstraction.

## Modern C# Features

### C# 14 Features
- **`field` keyword** - Access backing field in property accessors for custom logic
- **Extension members** - Add members to existing types without inheritance
- **Null-conditional assignment** - `user?.Address ??= new Address()`

### C# 11-13 Features
- **Collection expressions** (C# 12) - `[1, 2, 3]` syntax with spread operators `[..first, ..second]`
- **`required` keyword** (C# 11+) - Enforce property initialization
- **File-scoped namespaces** - `namespace MyApp;`
- **Init-only properties** - `init` keyword for immutability
- **Records** - Immutable data structures for DTOs
- **Pattern matching** - Replace if-else chains
- **Nullable reference types** - `?` annotations

[C# Language Reference](https://learn.microsoft.com/en-us/dotnet/csharp/)

## Code Style Principles

### Comments: Write WHYs, Not WHATs
- Code should be self-documenting (use descriptive names)
- Comment business rules, non-obvious decisions, reasoning
- Avoid redundant comments that just describe what code does
- XML docs only for public APIs, complex algorithms, or cross-team interfaces

### Static Private Methods
Prefer static private methods when no instance state is needed - clearer intent, prevents accidental coupling to instance state.

### Immutability
Prefer immutable data structures using records and init-only properties.

### Prefer Microsoft Packages
Choose official Microsoft packages over third-party when available - better long-term support, integration, and performance. Use third-party only when Microsoft doesn't provide equivalent or when industry-standard (e.g., Serilog).

## Code Organization

### Feature Slices Architecture
**Vertical slices over horizontal layers** - organize by feature, not technical role. Each feature folder contains models, services, data access, and DI registration.

**Accept repetition between slices** - don't extract shared code until patterns stabilize (Rule of Three).

See [PATTERNS.md](PATTERNS.md) for detailed structure and examples.

## Naming Conventions
- **PascalCase**: Classes, methods, properties, public fields, constants
- **camelCase**: Local variables, parameters, constructor parameters
- **\_camelCase**: Private instance fields (use readonly for injected dependencies)
- **s\_camelCase**: Private static fields
- **IPascalCase**: Interfaces (prefix `I`)
- **Async suffix**: All async methods
- **Feature-based DI extensions**: `AddFeatureNameServices.cs`

## Async/Await
- Use async/await consistently
- **NEVER** use `.Result` or `.Wait()` (deadlocks)
- `ConfigureAwait(false)` in libraries only
- `ValueTask<T>` for hot paths (frequently synchronous completion)
- Always `Async` suffix on method names
- `CancellationToken` for long operations

## Dependency Injection
**Constructor injection with readonly fields** - inject dependencies via constructor, store in readonly fields for immutability and clarity.

**Lifetimes:**
- **Singleton**: Stateless services, caches
- **Scoped**: DbContext, per-request services (HTTP request lifetime)
- **Transient**: Lightweight, stateless services

## Error Handling
- Exceptions for exceptional cases only
- Result pattern for expected failures (return `Result<T>` or `Option<T>`)
- Never swallow exceptions - log and re-throw
- Use `ArgumentException.ThrowIfNullOrEmpty()` and `ArgumentNullException.ThrowIfNull()`

## Null Safety
- Enable `<Nullable>enable</Nullable>` in csproj
- Pattern matching: `if (user is not null)`
- Null-conditional: `user?.Name ?? "Unknown"`
- Null-coalescing assignment: `_cache ??= new()`
- Explicit nullability: `User?` vs `User`

## LINQ
- Multi-line for readability
- Understand deferred vs immediate execution
- **Avoid N+1**: Use `.Include()` in EF Core
- Query syntax for complex queries, method syntax for simple operations

[LINQ Documentation](https://learn.microsoft.com/en-us/dotnet/csharp/linq/)

## Additional Resources

**Detailed patterns:** See [PATTERNS.md](PATTERNS.md) for feature slices, Specification Pattern, Factory, Strategy, Options patterns, and **anti-patterns to avoid**

**ASP.NET Core:** See [ASPNET-CORE.md](ASPNET-CORE.md) for service registration, Minimal APIs, background services, middleware

**Blazor:** See [BLAZOR.md](BLAZOR.md) for component design, lifecycle, state management, forms, rendering modes

**Infrastructure:** See [INFRASTRUCTURE.md](INFRASTRUCTURE.md) for .NET Aspire orchestration and csproj-based dockerization

**Testing:** See [TESTING.md](TESTING.md) for TUnit, AwesomeAssertions, and TestContainers

## Common Pitfalls

**DON'T:**
- Use `.Result` / `.Wait()` (deadlocks)
- Swallow exceptions
- Use `async void` (except event handlers)
- Use `DateTime.Now` (use `TimeProvider.GetUtcNow()` or `DateTimeOffset.UtcNow`)
- Hardcode configs
- Ignore `CancellationToken`
- Compare strings without `StringComparison`
- Mutate collections while iterating
- Use Repository Pattern with EF Core (see [PATTERNS.md](PATTERNS.md) anti-patterns)
- Over-comment code (write WHYs, not WHATs)
- Create instance methods when static would work
- Create abstractions before they're needed (YAGNI)

**DO:**
- Async/await consistently
- Enable nullable reference types
- Use dependency injection with constructor injection and readonly fields
- Write tests (see [TESTING.md](TESTING.md))
- Pattern matching over if-else
- SOLID principles
- Records for DTOs and immutable data
- Structured logging
- Handle disposal (`IDisposable`, `using`)
- Use feature slices architecture
- Prefer static private methods for stateless logic
- Prefer Microsoft packages
- Write comments that explain WHY, not WHAT

## References

- [C# Coding Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [.NET Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/)
- [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/)

## Skill Files

- **SKILL.md** - Core patterns (this file)
- **[PATTERNS.md](PATTERNS.md)** - Design patterns and anti-patterns
- **[ASPNET-CORE.md](ASPNET-CORE.md)** - ASP.NET Core patterns
- **[BLAZOR.md](BLAZOR.md)** - Blazor component patterns
- **[INFRASTRUCTURE.md](INFRASTRUCTURE.md)** - .NET Aspire and dockerization
- **[TESTING.md](TESTING.md)** - Testing with TUnit and AwesomeAssertions

**Write simple, readable, maintainable code. Follow SOLID and YAGNI. Correctness and clarity before performance optimization.**
