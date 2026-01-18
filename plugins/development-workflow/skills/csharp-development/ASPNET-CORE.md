# ASP.NET Core Patterns

Production patterns for ASP.NET Core applications in .NET 10.

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

**Lightweight HTTP APIs without controllers.** Use for simple CRUD endpoints, microservices, or when you want explicit control over routing.

### Principles

- **IEndpointRouteBuilder extensions** - Group endpoints in extension methods
- **Feature folders** - Organize endpoints with related code
- **Single file for simple endpoints** - DTOs and handler in same file when small
- **Extract to services for complex logic** - Don't put business logic in endpoints

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

    private static async Task<Results<Ok<Order>, NotFound>> GetOrder(string id, OrderService service)
        => // handler logic
}
```

Register in `Program.cs`: `app.MapOrderEndpoints();`

### TypedResults for Type-Safe Responses

Use `Results<TOk, TNotFound, TBadRequest>` and `TypedResults` instead of `IResult` for compile-time safety and OpenAPI inference.

### Inline DTOs

For simple endpoints, define request/response DTOs inline with record types:

### Complex Endpoints - Extract to Service

For business logic, validation, or multiple dependencies, inject service and delegate:

```csharp
private static async Task<Results<Ok<PaymentResult>, BadRequest>> ProcessPayment(
    PaymentRequest request,
    PaymentService service,
    ILogger<PaymentService> logger)
    => await service.ProcessPaymentAsync(request);
```

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

**Long-running tasks** using `BackgroundService` base class.

### Implementation

- Inherit from `BackgroundService`
- Override `ExecuteAsync(CancellationToken stoppingToken)`
- Handle exceptions (except `OperationCanceledException`)
- Respect `CancellationToken` for graceful shutdown

Register as `services.AddHostedService<TBackgroundService>();`

[Background Services](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services)

## Middleware

**Pipeline order matters**: Authentication → Authorization → Endpoints

## Configuration & Options

Use **Options pattern** for type-safe configuration.

### Implementation

- Define options class with `const string SectionName = "ConfigSection"`
- Use `required` properties and data annotations
- Validate on startup

[Options Pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options)

## Message Queues & Event-Driven

**Background consumers** for async message processing.

- Implement `BackgroundService` for queue consumer
- Handle idempotency for at-least-once delivery
- Use dead letter queues for failed messages

Common technologies: Azure Service Bus, RabbitMQ, AWS SQS, Kafka

## References

- [ASP.NET Core Fundamentals](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/)
- [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)
- [Dependency Injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)
- [Configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/)
