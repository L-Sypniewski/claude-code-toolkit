# Infrastructure Patterns

Modern infrastructure patterns for .NET 10 applications using .NET Aspire and container publishing.

## .NET Aspire

**Code-first orchestration for cloud-native .NET applications.** Simplifies local development, deployment, and observability for distributed apps.

### What is .NET Aspire

Opinionated stack for building observable, production-ready cloud-native applications. Provides:
- **Service orchestration** - Run and connect multiple projects/services locally
- **Service discovery** - Automatic connection string resolution
- **Telemetry** - Built-in logging, metrics, and distributed tracing
- **Resource management** - Databases, caches, message queues as code

Use when building microservices, distributed apps, or apps with external dependencies (databases, Redis, message queues).

[.NET Aspire Documentation](https://learn.microsoft.com/en-us/dotnet/aspire/)

### AppHost Project

**Orchestration entry point.** Defines all services, resources, and their relationships.

#### Structure

Create `AppHost` project (type: `Aspire Application Host`):
- Reference all service projects
- Define resources (databases, caches, storage)
- Configure service connections
- Manage environment variables

#### Program.cs Pattern

```csharp
var builder = DistributedApplication.CreateBuilder(args);

// Add resources
var postgres = builder.AddPostgres("postgres").AddDatabase("appdb");
var redis = builder.AddRedis("cache");

// Add projects with resource references
builder.AddProject<Projects.Api>("api")
    .WithReference(postgres)
    .WithReference(redis);

builder.Build().Run();
```

Resources auto-configure connection strings for referenced services.

### ServiceDefaults Project

**Shared configuration across services.** Class library with OpenTelemetry, health checks, and service discovery configuration.

#### What it provides

- OpenTelemetry instrumentation (logging, metrics, tracing)
- Health check endpoints
- Service discovery client configuration
- Resilience patterns (retry, circuit breaker)

Register in each service: `builder.AddServiceDefaults();`

### Service Discovery

**Automatic endpoint resolution** - services reference each other by name, not hardcoded URLs.

#### How it works

AppHost injects service endpoints as configuration. HttpClient automatically resolves named services:

```csharp
builder.Services.AddHttpClient<IOrderService, OrderServiceClient>(
    client => client.BaseAddress = new("https+http://api"));
```

`https+http://api` resolves to actual service URL at runtime - HTTPS in production, HTTP locally.

### Telemetry & Monitoring

**Built-in observability dashboard** shows:
- Distributed traces (OpenTelemetry)
- Logs aggregated from all services
- Metrics (request rates, durations, errors)
- Resource health (databases, caches)

Access at `http://localhost:PORT` when running AppHost.

### Integration Testing with Aspire

Use `DistributedApplicationTestingBuilder` to create test AppHost. Start entire application stack for integration tests. All service discovery and resources work in test environment.

[Aspire Testing](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/testing)

## Container Publishing (csproj-based)

**No Dockerfiles needed** - publish containers directly from project files.

### Enable Container Support

Add to `.csproj`:

```xml
<PropertyGroup>
  <PublishProfile>DefaultContainer</PublishProfile>
  <ContainerImageName>myapp</ContainerImageName>
  <ContainerImageTag>latest</ContainerImageTag>
</PropertyGroup>
```

### Publishing Commands

```bash
# Publish to local Docker daemon
dotnet publish -t:PublishContainer

# Publish to registry
dotnet publish -t:PublishContainer -p:ContainerRegistry=myregistry.azurecr.io

# Custom tag
dotnet publish -t:PublishContainer -p:ContainerImageTag=v1.2.3
```

### Configuration Properties

Common properties: `ContainerImageName`, `ContainerImageTag`, `ContainerRegistry`, `ContainerBaseImage`, `ContainerPort`

[Container Publishing](https://learn.microsoft.com/en-us/dotnet/core/docker/publish-as-container)

### When to Use Dockerfiles

Use traditional Dockerfiles when:
- Need multi-stage builds with custom build steps
- Require OS-level dependencies (apt-get, apk)
- Custom base image not in Microsoft registry
- Complex file copying/manipulation
- Integration with existing Docker Compose workflows

For most .NET apps, csproj-based publishing is simpler and sufficient.

## Deployment Patterns

### Local Development

Use .NET Aspire AppHost for full-stack local development with one F5. All services, databases, caches start together.

### Production

Options:
1. **Azure Container Apps** - Native Aspire deployment with `azd up`
2. **Kubernetes** - Generate manifests from Aspire with `aspirate`
3. **Docker Compose** - Generate compose file from Aspire
4. **Direct container publish** - Individual services with csproj publishing

### Configuration Management

- **Development**: AppHost manages configuration
- **Production**: Azure App Configuration, Kubernetes ConfigMaps, environment variables
- Use `IConfiguration` consistently across environments

## References

- [.NET Aspire](https://learn.microsoft.com/en-us/dotnet/aspire/)
- [Container Publishing](https://learn.microsoft.com/en-us/dotnet/core/docker/publish-as-container)
- [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/)
- [Docker](https://docs.docker.com/)
