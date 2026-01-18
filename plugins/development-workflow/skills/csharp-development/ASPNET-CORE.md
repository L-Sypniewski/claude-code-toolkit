# ASP.NET Core Patterns

Production patterns for ASP.NET Core applications.

## Service Registration Extensions

**Organize DI registration per feature** using extension methods.

### Pattern

Create `AddFeatureNameServicesExtension` class with `AddFeatureNameServices(IServiceCollection, IConfiguration)` method:
- File naming: `AddFeatureNameServices.cs` in feature folder
- Class naming: `AddFeatureNameServicesExtension`
- Method naming: `AddFeatureNameServices`
- Register all feature services and configuration
- Return `IServiceCollection` for chaining
- In `Program.cs`, call `builder.Services.AddFeatureNameServices(builder.Configuration);`

### Example for "InvoicePrinting" feature

File: `Features/InvoicePrinting/AddInvoicePrintingServices.cs`
Class: `AddInvoicePrintingServicesExtension`
Method: `AddInvoicePrintingServices(this IServiceCollection services, IConfiguration configuration)`

Register in `Program.cs`: `builder.Services.AddInvoicePrintingServices(builder.Configuration);`

## Minimal APIs

**Use Minimal APIs by default.** Lightweight HTTP APIs without controllers.

### Principles

- **IEndpointRouteBuilder extensions** - Group endpoints in extension methods
- **Feature folders** - Organize endpoints with related code
- **Single file for simple endpoints** - DTOs and handler in same file when small
- **Extract to handlers for complex logic** - Don't put business logic in endpoints

### Basic Endpoint Structure

Define endpoints as extension methods on `IEndpointRouteBuilder`:

```csharp
public static class OrderEndpoints
{
    public static IEndpointRouteBuilder MapOrderEndpoints(this IEndpointRouteBuilder app)
    {
        app.MapGet("/api/orders/{id}", GetOrder);
        app.MapPost("/api/orders", CreateOrder);
        return app;
    }

    private static async Task<Results<Ok<Order>, NotFound>> GetOrder(string id, AppDbContext db)
        => await db.Orders.FindAsync(id) is Order order
            ? TypedResults.Ok(order)
            : TypedResults.NotFound();
}
```

Register in `Program.cs`: `app.MapOrderEndpoints();`

### TypedResults for Type-Safe Responses

Use `Results<TOk, TNotFound, TBadRequest>` and `TypedResults` instead of `IResult`.

### Inline DTOs

For simple endpoints, define request/response DTOs inline with record types:

### Complex Endpoints

Extract complex logic to handlers or services.

### Endpoint Filters

Add cross-cutting concerns (validation, logging, caching) with endpoint filters. Implement `IEndpointFilter` or use delegate filters. Register with `.AddEndpointFilter<T>()`.

### Feature Folder Organization

```
Features/Orders/
  ├── OrderEndpoints.cs       // Endpoint mappings
  └── AddOrderServices.cs     // DI registration
```

[Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)

## Background Services

Use `BackgroundService` base class for long-running tasks. Register as `services.AddHostedService<TBackgroundService>();`.

[Background Services](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services)

## Configuration & Options

Use **Options pattern** for type-safe configuration.

### Implementation

- Define options class with `const string SectionName = "ConfigSection"`
- Use `required` properties and data annotations
- Validate on startup

[Options Pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options)

## Message Queues & Event-Driven

Use `BackgroundService` for async message processing.

- Implement `BackgroundService` for queue consumer
- Handle idempotency for at-least-once delivery
- Use dead letter queues for failed messages

## References

- [ASP.NET Core Fundamentals](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/)
- [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)
- [Dependency Injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)
- [Configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/)
