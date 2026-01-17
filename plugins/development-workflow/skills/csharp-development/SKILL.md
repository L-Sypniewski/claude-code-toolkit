---
name: csharp-development
description: Expert guidance for .NET C# development covering best practices, design patterns, architecture, testing, and modern C# idioms. Includes production-tested patterns from enterprise applications. Use when writing, reviewing, or refactoring C# code, designing .NET applications, or implementing enterprise patterns. DO NOT use for non-.NET languages or frontend-only JavaScript/TypeScript work.
---

# .NET C# Development Expert

Expert .NET C# guidance with production-tested patterns from Blazor, ASP.NET Core, and Entity Framework Core applications.

## When to Use

**USE for:** C# code, .NET architecture, design patterns, testing, async/await, LINQ, ASP.NET Core, EF Core  
**DON'T use for:** Non-.NET languages, frontend-only work, F#/VB.NET

## Modern C# Features

- Nullable reference types (`?` annotations)
- Pattern matching over if-else
- Records for DTOs
- Primary constructors (C# 12+) for DI
- Collection expressions `[1, 2, 3]`
- `required` keyword (C# 11+)
- File-scoped namespaces `namespace MyApp;`
- Init-only properties (`init`)
- Target-typed new `new()`
- Raw string literals `"""`

## Naming Conventions

- **PascalCase**: Classes, methods, properties, public fields, constants
- **camelCase**: Local variables, parameters, primary constructor params
- **\_camelCase**: Private instance fields
- **s_camelCase**: Private static fields
- **IPascalCase**: Interfaces (prefix `I`)
- **Async suffix**: All async methods
- **Repository suffix**: Repository classes

## Code Organization

**Feature-based structure** (vertical slices): `Features/Users/`, `Features/Orders/`

- One type per file, filename matches type name
- Keep related code together (models, services, repos in same feature folder)

**Helper methods:** Static when no instance state needed, skip interfaces for single implementations

## Async/Await

- Use async/await consistently
- **NEVER** use `.Result` or `.Wait()` (deadlocks)
- `ConfigureAwait(false)` in libraries only
- Return `Task<T>` when just returning awaitable
- `ValueTask<T>` for hot paths
- Always `Async` suffix
- `CancellationToken` for long operations

## Dependency Injection

**Constructor injection** (prefer primary constructors C# 12+)

**Lifetimes:**

- **Singleton**: Stateless services, caches
- **Scoped**: DbContext, repositories (per-request)
- **Transient**: Lightweight, stateless

## Error Handling

- Exceptions for exceptional cases
- Result pattern for expected failures
- **Never** swallow exceptions - log and re-throw
- Use `ArgumentException.ThrowIfNullOrEmpty()`

## Null Safety

- Enable `<Nullable>enable</Nullable>`
- Pattern matching: `if (user is not null)`
- Null-conditional: `user?.Name ?? "Unknown"`
- Null-coalescing: `_cache ??= new()`
- Explicit nullability: `User?` vs `User`

## LINQ

- Multi-line for readability
- Understand deferred vs immediate execution
- **Avoid N+1**: Use `.Include()` in EF Core

## Additional Resources

**Detailed patterns:** See [PATTERNS.md](PATTERNS.md) for Repository, Unit of Work, Factory, Strategy, Options patterns

**ASP.NET Core:** See [ASPNET-CORE.md](ASPNET-CORE.md) for service registration, background services, message queues, middleware

**Blazor:** See [BLAZOR.md](BLAZOR.md) for component design, lifecycle, state management, forms, rendering modes

## Testing

**Comprehensive testing guidelines:** See [TESTING.md](TESTING.md)

## Common Pitfalls

**DON'T:**

- Use `.Result` / `.Wait()` (deadlocks)
- Swallow exceptions
- Use `async void` (except event handlers)
- Use `DateTime.Now` (use `UtcNow` or `DateTimeOffset`)
- Hardcode configs
- Ignore `CancellationToken`
- Compare strings without `StringComparison`
- Mutate collections while iterating

**DO:**

- Async/await consistently
- Enable nullable reference types
- Use dependency injection
- Write tests
- Pattern matching
- SOLID principles
- Records for DTOs
- Structured logging
- Handle disposal (`IDisposable`, `using`)

## References

- [Microsoft C# Coding Conventions](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [.NET Design Guidelines](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/)
- [xUnit](https://xunit.net/) | [FluentAssertions](https://fluentassertions.com/) | [EF Core](https://docs.microsoft.com/en-us/ef/core/)

## Skill Files

- **SKILL.md** - Core patterns (this file)
- **[ASPNET-CORE.md](ASPNET-CORE.md)** - ASP.NET Core patterns
- **[BLAZOR.md](BLAZOR.md)** - Blazor component patterns

**Write readable, maintainable, testable code. Correctness and clarity before performance optimization.**
