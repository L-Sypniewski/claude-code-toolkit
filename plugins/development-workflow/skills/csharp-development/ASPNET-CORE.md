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

    private static async Task<IResult> GetOrder(string id, OrderService service)
        => // handler logic
}
```

Register in `Program.cs`: `app.MapOrderEndpoints();`

### TypedResults for Type-Safe Responses

Use `Results<TOk, TNotFound, TBadRequest>` and `TypedResults` instead of `IResult` for compile-time safety and OpenAPI inference.

Example: `Results<Ok<Order>, NotFound>` with `TypedResults.Ok(order)` or `TypedResults.NotFound()`

### Inline DTOs

For simple endpoints, define request/response DTOs inline with record types:

```csharp
record CreateOrderRequest(string CustomerId, List<OrderItem> Items);
record CreateOrderResponse(string OrderId, string Status);
```

### Complex Endpoints - Extract to Service

For business logic, validation, or multiple dependencies, inject service and delegate:

```csharp
private static async Task<IResult> ProcessPayment(
    PaymentRequest request,
    PaymentService service,
    ILogger<PaymentService> logger)
{
    return await service.ProcessPaymentAsync(request);
}
```

### Endpoint Filters

Add cross-cutting concerns (validation, logging, caching) with endpoint filters. Implement `IEndpointFilter` or use delegate filters. Register with `.AddEndpointFilter<T>()`.

### Feature Folder Organization

```
Features/Orders/
  ├── OrderEndpoints.cs       // Endpoint mappings
  ├── Order.cs                // Model
  ├── OrderService.cs         // Business logic
  └── AddOrderServices.cs     // DI registration
```

[Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)

## Background Services

**Long-running tasks** using `BackgroundService` base class.

### Implementation

- Inherit from `BackgroundService`
- Override `ExecuteAsync(CancellationToken stoppingToken)`
- Create scopes for scoped dependencies (`IServiceScopeFactory`)
- Handle exceptions (except `OperationCanceledException`)
- Respect `CancellationToken` for graceful shutdown
- Retry with delay on failures

### Common Use Cases

- Periodic cleanup jobs
- Message queue consumers
- Health monitoring
- Cache refresh
- Data synchronization

Register as `services.AddHostedService<TBackgroundService>();`

[Background Services](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services)

## Middleware

**Pipeline order matters**: Authentication → Authorization → Endpoints

### Custom Middleware

- Create class with `InvokeAsync(HttpContext context, RequestDelegate next)`
- Inject services via constructor
- Call `await next(context)` to continue pipeline
- Short-circuit with `context.Response.WriteAsync()` when needed
- Avoid blocking operations

Register with `app.UseMiddleware<TMiddleware>()` or extension method.

[Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware)

## Configuration & Options

**Options pattern** for type-safe configuration.

### Implementation

- Define options class with `const string SectionName = "ConfigSection"`
- Use `required` properties or data annotations
- Implement `IValidateOptions<T>` for custom validation
- Register with `services.Configure<TOptions>(configuration.GetSection(TOptions.SectionName))`

### Options Lifetimes

- **`IOptions<T>`** - Singleton, read once at startup (most common)
- **`IOptionsSnapshot<T>`** - Scoped, reloads per request (multi-tenant)
- **`IOptionsMonitor<T>`** - Singleton, reloads on config change (hot reload)

[Options Pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options)

## Message Queues & Event-Driven

**Background consumers** for async message processing.

### Patterns

- Implement `BackgroundService` for queue consumer
- Event-driven failure handling (publish failure events)
- Transactional message processing (consume + business logic in transaction)
- Dead letter queues for failed messages
- Idempotency for at-least-once delivery

### Common Technologies

- Azure Service Bus
- RabbitMQ
- AWS SQS
- Kafka

## References

- [ASP.NET Core Fundamentals](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/)
- [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)
- [Dependency Injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)
- [Configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/)
