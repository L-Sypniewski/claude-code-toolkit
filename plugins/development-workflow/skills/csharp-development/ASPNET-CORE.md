# ASP.NET Core Patterns

Production patterns for ASP.NET Core applications.

## Service Registration

**Extension methods** for feature organization: `AddFeatureServices(IServiceCollection, IConfiguration)`

- Scope: `AddScoped` for repositories/services
- Configuration: `services.Configure<TOptions>(config.GetSection(...))`
- Return `IServiceCollection` for chaining

## Background Services

**Inherit `BackgroundService`** for long-running tasks

- Create scopes for scoped dependencies
- Handle exceptions (except `OperationCanceledException`)
- Respect `CancellationToken` from `stoppingToken`
- Retry with delay on failures

## Message Queues

**Background consumers** for async processing

- Event-driven failure handling
- Transactional message processing
- Dead letter queues for failures

## Middleware

**Pipeline order matters**: Authentication → Authorization → Endpoints

- Use `app.UseMiddleware<T>()` for custom middleware
- Short-circuit with `context.Response.WriteAsync()` when needed
- Avoid blocking operations in middleware

## Configuration

**Options pattern** with `IOptions<T>`, `IOptionsSnapshot<T>`, `IOptionsMonitor<T>`

- Validate with `ValidateDataAnnotations()` or custom validation
- Bind sections with `configuration.GetSection(SectionName)`
- Use `const string SectionName` in options classes
