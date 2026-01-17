# .NET Development Plugin

Comprehensive C# and .NET development skill providing best practices, patterns, conventions, and guidelines for building robust .NET applications.

## Overview

This plugin provides a comprehensive skill for .NET development, covering modern C# language features, ASP.NET Core, Entity Framework Core, testing, security, and performance optimization.

## Features

### 🎯 Included Skills

#### csharp-dotnet-development

**Purpose**: Comprehensive C# and .NET development guidance  
**Use When**: Developing, reviewing, or refactoring .NET applications  
**Provides**:
- SOLID principles and clean code practices
- C# naming conventions and coding standards
- Modern C# features (C# 10+)
- Async/await best practices
- Dependency injection patterns
- Entity Framework Core best practices
- ASP.NET Core API development
- Testing strategies (unit and integration)
- Security best practices (authentication, authorization, input validation)
- Performance optimization techniques
- Common pitfalls and anti-patterns

## Installation

### Add the Marketplace

```bash
/plugin marketplace add https://github.com/L-Sypniewski/claude-code-toolkit.git
```

### Install this Plugin

```bash
/plugin install dotnet-development
```

## Usage

The skill is automatically loaded by Claude when working with C# and .NET code. Simply work on your .NET projects, and Claude will reference this skill for:

- **Code implementation**: When writing new C# code
- **Code review**: When reviewing .NET pull requests
- **Refactoring**: When improving existing .NET code
- **Architecture**: When designing .NET application structure
- **Troubleshooting**: When debugging .NET issues

### Example Scenarios

#### Creating a New API Controller

```
"Create a new ASP.NET Core API controller for managing products with CRUD operations"
```

Claude will automatically reference the skill and follow best practices for:
- Controller structure and naming
- HTTP verb usage
- Status code handling
- Dependency injection
- Validation and error handling

#### Code Review

```
"Review this C# code for best practices and potential issues"
```

Claude will check against:
- SOLID principles
- Naming conventions
- Exception handling
- Async/await usage
- Security concerns
- Performance issues

#### Setting Up Entity Framework

```
"Configure Entity Framework Core with proper patterns"
```

Claude will apply:
- DbContext configuration
- FluentAPI usage
- Query optimization techniques
- Repository patterns (if applicable)

## What This Plugin Provides

### Coding Standards

- ✅ C# naming conventions (PascalCase, camelCase, etc.)
- ✅ File and project structure
- ✅ Modern C# language features

### Design Patterns

- ✅ SOLID principles
- ✅ Dependency injection
- ✅ Repository pattern
- ✅ CQRS with MediatR
- ✅ Clean architecture

### Framework Guidance

- ✅ ASP.NET Core API development
- ✅ Entity Framework Core
- ✅ Authentication & Authorization
- ✅ Validation (FluentValidation)

### Quality Assurance

- ✅ Unit testing with xUnit
- ✅ Integration testing
- ✅ Mocking with Moq
- ✅ Code quality tools

### Security

- ✅ Input validation and sanitization
- ✅ Authentication patterns
- ✅ Authorization policies
- ✅ Secrets management
- ✅ SQL injection prevention

### Performance

- ✅ Async/await optimization
- ✅ Memory management (Span<T>, ArrayPool)
- ✅ Caching strategies
- ✅ EF Core query optimization

## Skill Structure

```
plugins/dotnet-development/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── skills/
│   └── csharp-dotnet-development/
│       └── SKILL.md             # Main skill file
└── README.md                     # This file
```

## Extending This Plugin

You can extend this plugin by:

1. **Adding more skills**: Create additional skills for specific .NET domains
   - `blazor-development` - Blazor-specific patterns
   - `minimal-apis` - Minimal API patterns
   - `grpc-services` - gRPC development
   - `microservices-patterns` - .NET microservices

2. **Adding commands**: Create slash commands for common .NET tasks
   - `/dotnet-new-api` - Scaffold new API project
   - `/dotnet-migration` - Create EF Core migration

3. **Adding agents**: Create specialized agents
   - `dotnet-architect` - Architecture guidance
   - `dotnet-security-reviewer` - Security-focused reviews

## Best Practices Coverage

### ✅ Covered

- Modern C# language features (C# 10+)
- SOLID principles and clean code
- ASP.NET Core API development
- Entity Framework Core
- Async/await patterns
- Dependency injection
- Testing strategies
- Security best practices
- Performance optimization

### 📝 For You to Customize

The skill provides a solid foundation with framework and structure. You can customize by:

- Adding company-specific coding standards
- Including project-specific architectural patterns
- Adding custom validation rules
- Including internal library usage patterns
- Adding deployment and CI/CD practices

## Contributing

To contribute improvements to this skill:

1. Fork the repository
2. Create a feature branch
3. Update the skill content in `skills/csharp-dotnet-development/SKILL.md`
4. Update the version in `.claude-plugin/plugin.json`
5. Submit a pull request

## Version History

- **1.0.0** (2026-01-17)
  - Initial release
  - Comprehensive C# and .NET development skill
  - Coverage of modern C# features
  - ASP.NET Core and EF Core best practices
  - Security and performance guidelines

## Resources

### Official Documentation

- [.NET Documentation](https://docs.microsoft.com/en-us/dotnet/)
- [C# Language Reference](https://docs.microsoft.com/en-us/dotnet/csharp/)
- [ASP.NET Core Documentation](https://docs.microsoft.com/en-us/aspnet/core/)
- [Entity Framework Core](https://docs.microsoft.com/en-us/ef/core/)

### Community Resources

- [.NET Foundation](https://dotnetfoundation.org/)
- [C# Corner](https://www.c-sharpcorner.com/)
- [.NET Blog](https://devblogs.microsoft.com/dotnet/)

## License

MIT License - See [LICENSE](../../LICENSE) for details.

## Support

- Create an [issue](https://github.com/L-Sypniewski/claude-code-toolkit/issues) for bugs or feature requests
- Check the [discussions](https://github.com/L-Sypniewski/claude-code-toolkit/discussions) for community support
- Review the main [toolkit README](../../README.md) for general guidance

---

⭐ If you find this plugin helpful, please star the repository!
