# Deployment Patterns

Container publishing and deployment patterns for .NET applications.

## Container Publishing (csproj-based)

Publish containers directly from project files without Dockerfiles.

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

For most .NET apps, csproj-based publishing is simpler.

## Deployment Patterns

### Local Development

Use .NET Aspire AppHost for full-stack local development. All services, databases, caches start together.

### Configuration Management

- **Development**: AppHost manages configuration
- **Production**: Azure App Configuration, Kubernetes ConfigMaps, environment variables
- Use `IConfiguration` consistently across environments

## References

- [Container Publishing](https://learn.microsoft.com/en-us/dotnet/core/docker/publish-as-container)
- [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/)
- [Docker](https://docs.docker.com/)
