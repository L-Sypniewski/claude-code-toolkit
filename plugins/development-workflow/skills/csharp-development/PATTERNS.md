# Enterprise Architecture Patterns

Design pattern guidance for .NET 10 C# applications. Emphasizes simplicity, SOLID principles, and avoiding over-engineering.

## Feature Slices Architecture

**Vertical slices over horizontal layers** - organize code by feature, not by technical role (Controllers/Services/Repositories).

### Principles

1. **Self-contained features** - Each feature folder contains everything: models, handlers, data access, DI registration
2. **High cohesion** - Related code stays together
3. **Accept duplication** - Don't extract shared code until patterns stabilize (Rule of Three)
4. **Clear boundaries** - Features evolve independently without rippling changes

### Structure

```
src/Features/{FeatureName}/
  ├── {Action}.cs           // Endpoint/command handler
  ├── {Model}.cs            // Domain model
  ├── Add{Feature}Services.cs  // DI registration
```

### When to Extract Shared Code
- Same logic in 3+ features (Rule of Three)
- Bug fix requires updating multiple features
- Abstraction is stable and unlikely to change

## Repository Pattern with EF Core

**Usually unnecessary when using EF Core.** DbContext already implements Repository and Unit of Work patterns.

### When to use DbContext directly

Use DbContext directly in services with constructor injection and readonly fields. Provides full EF Core capabilities (Include, projections, query filters).

### When Repository Pattern is appropriate

Use Repository Pattern when:
- Abstracting non-EF data sources (Dapper, HTTP APIs, file system, external services)
- Multiple ORMs in same application (rare)
- Domain-Driven Design with aggregate roots and complex domain logic
- Actually need to switch data sources (usually YAGNI)

[EF Core Documentation](https://learn.microsoft.com/en-us/ef/core/)

### Over-abstraction

**Skip interfaces for single implementations.** Create concrete classes until multiple implementations exist or polymorphism is needed.

For testing, use integration tests with real implementations or TestContainers.

## Specification Pattern

**Use when queries are complex AND reusable.** Don't use for simple queries - inline them instead.

### When to use

- Complex query logic used in multiple places
- Business rules that need composition (AND/OR logic)
- Queries that benefit from isolated testing

### When NOT to use

- Simple single-use queries (just use LINQ inline)
- Queries that are only used once
- Over-engineering simple data access

### Implementation

Define `ISpecification<T>` with `Apply(IQueryable<T>)` method. Create composable specifications for business rules. Add extension method to DbSet for fluent usage.

## Unit of Work Pattern

**DbContext already implements Unit of Work.** Use `SaveChangesAsync()` to commit all changes in a transaction. You rarely need custom implementation.

### When you need custom Unit of Work

**Only for multi-DbContext scenarios** (rare) - coordinating transactions across multiple database contexts with distributed transactions.

## Factory Pattern

**Create objects dynamically based on runtime conditions.** Use with `IServiceProvider` for DI-managed instances.

### When to use

- Need different implementations based on runtime data (payment method, notification type)
- Creating complex objects with varied initialization logic
- Strategy pattern implementation

### Registration

Register all implementations as services, inject `IServiceProvider` into factory, use switch expression to select implementation based on type parameter.

[Dependency Injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection)

## Strategy Pattern

**Encapsulate algorithms/behaviors, select at runtime.** Common for payment processing, notification delivery, validation rules, pricing calculations.

### Implementation approaches

1. **Enumeration of implementations** - Inject `IEnumerable<IStrategy>`, select based on criteria
2. **Factory + Strategy** - Use factory to create appropriate strategy
3. **Keyed services** (NET 8+) - Use `IServiceProvider.GetKeyedService<T>(key)`

[Strategy Pattern](https://refactoring.guru/design-patterns/strategy)

## Options Pattern

**Type-safe configuration with `IOptions<T>`.** Bind configuration sections to strongly-typed classes.

### Implementation

- Define options class with `const string SectionName`
- Use `required` properties or data annotations for validation
- Implement `IValidateOptions<T>` for custom validation
- Register with `services.Configure<TOptions>(configuration.GetSection(...))`

### Options Lifetime

- **`IOptions<T>`** - Singleton, read once at startup
- **`IOptionsSnapshot<T>`** - Scoped, reloads per request (multi-tenant scenarios)
- **`IOptionsMonitor<T>`** - Singleton, reloads when config changes (hot reload)

[Options Pattern](https://learn.microsoft.com/en-us/dotnet/core/extensions/options)

## Service Registration Extensions

**Organize DI registration with extension methods** per feature.

### Pattern

Create `AddFeatureNameServicesExtension` class with `AddFeatureNameServices(IServiceCollection, IConfiguration)` method. Register all feature services and configuration. Return `IServiceCollection` for chaining.

File naming: `AddFeatureNameServices.cs` in feature folder.

## Performance Patterns

### Memory Efficiency

- **`Span<T>` / `ReadOnlySpan<T>`** - Stack-allocated memory slices, no heap allocation, great for string/array manipulation
- **`Memory<T>` / `ReadOnlyMemory<T>`** - Similar to Span but async-safe
- **Avoid boxing value types** - Use generics with struct constraint
- **`StringBuilder`** - Use for string concatenation in loops
- **`ValueTask<T>`** - Use for frequently synchronous hot paths (reduces Task allocation)

[Performance Best Practices](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/performance/)

## Key Takeaways

1. **DbContext is already Repository + Unit of Work** - Don't wrap it unless abstracting non-EF sources
2. **Feature slices over layers** - Organize by feature, accept duplication until patterns emerge
3. **YAGNI** - Don't create abstractions until needed (Rule of Three)
4. **Specification Pattern** - Only for complex, reusable queries
5. **Factory/Strategy** - Use for runtime polymorphism
6. **Options Pattern** - Type-safe configuration binding
7. **Performance** - Use `Span<T>`, `Memory<T>`, `ValueTask<T>` where appropriate

**Prefer simplicity over clever abstractions. Build what you need now, refactor when patterns emerge.**
