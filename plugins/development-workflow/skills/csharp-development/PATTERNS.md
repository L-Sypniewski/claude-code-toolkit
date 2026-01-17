# Enterprise Architecture Patterns

Detailed design pattern implementations for .NET C# applications.

## Repository Pattern

**Purpose:** Abstract data access, enable testability, centralize data logic

**Rules:**

1. Never bind UI to DbContext directly
2. One repository per aggregate root
3. Domain-specific methods (e.g., `GetActiveUsersAsync`)
4. Return domain models, not DTOs

## Unit of Work Pattern

Manages transactions across multiple repositories, ensures atomic operations.

## Factory Pattern

Create objects dynamically based on runtime conditions. Use with `IServiceProvider` for DI-managed instances.

## Strategy Pattern

Encapsulate algorithms/behaviors, select at runtime. Common for payment processing, notification delivery, validation rules.

## Options Pattern

Type-safe configuration with `IOptions<T>`. Use `const string SectionName` for section binding.

## Background Services

Use `BackgroundService` base class for long-running tasks. Create scopes for scoped dependencies. Handle exceptions, respect `CancellationToken`.

## Service Registration Extensions

Organize DI registration with extension methods: `AddFeatureServices(IServiceCollection, IConfiguration)`.

## Performance Patterns

- Use `Span<T>` / `ReadOnlySpan<T>` for memory efficiency
- Avoid boxing value types
- `StringBuilder` for string concatenation in loops
- `Memory<T>` / `ReadOnlyMemory<T>` for async scenarios
