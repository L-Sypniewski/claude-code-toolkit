# Infrastructure Patterns

Modern infrastructure patterns for .NET applications.

## .NET Aspire

Code-first orchestration for cloud-native .NET applications.

### Scaffolding

Install Aspire templates:

```bash
dotnet new install Aspire.ProjectTemplates
```

Create new Aspire application:

```bash
dotnet new aspire          # Full template
dotnet new aspire-starter  # Minimal template
```

[.NET Aspire Documentation](https://learn.microsoft.com/en-us/dotnet/aspire/)

### Telemetry & Monitoring

Built-in observability dashboard shows:
- Distributed traces (OpenTelemetry)
- Logs aggregated from all services
- Metrics (request rates, durations, errors)
- Resource health (databases, caches)

Access at `http://localhost:PORT` when running AppHost.

### Integration Testing with Aspire

Use `DistributedApplicationTestingBuilder` to create test AppHost. Start entire application stack for integration tests.

[Aspire Testing](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/testing)

## OpenTelemetry

Use OpenTelemetry for observability. Configure via ServiceDefaults or directly in each service.

[OpenTelemetry with .NET](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel)

## References

- [.NET Aspire](https://learn.microsoft.com/en-us/dotnet/aspire/)
- [OpenTelemetry](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel)
