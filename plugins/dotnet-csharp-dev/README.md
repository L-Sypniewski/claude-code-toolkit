# .NET C# Development Plugin

Expert guidance for .NET C# development with modern best practices, design patterns, and comprehensive testing guidelines.

## Overview

Comprehensive C# development skill covering modern language features, enterprise patterns, and testing strategies. Uses **progressive disclosure** to keep context efficient.

**What's included:**

- Modern C# (12+) features and conventions
- Async/await, DI, error handling, null safety
- Enterprise patterns (Repository, Unit of Work, Factory, Strategy)
- ASP.NET Core & Blazor patterns
- Comprehensive testing (xUnit, FluentAssertions, FakeItEasy, Testcontainers)
- Performance optimization and common pitfalls

## Structure

```
dotnet-csharp-dev/
├── skills/csharp-development/
│   ├── SKILL.md              # Core patterns
│   ├── TESTING.md            # Testing guidelines
│   ├── PATTERNS.md           # Enterprise patterns
│   ├── ASPNET-CORE.md        # ASP.NET Core patterns
│   └── BLAZOR.md             # Blazor patterns
└── README.md
```

**Progressive disclosure:** Main SKILL.md links to detailed references loaded only when needed.

## Installation

### Claude Code

```bash
# Personal skills
cp -r plugins/dotnet-csharp-dev/skills/csharp-development ~/.claude/skills/

# Project-specific
cp -r plugins/dotnet-csharp-dev/skills/csharp-development ./.claude/skills/
```

## Usage

Activates automatically when working with C# code. Examples:

- "Create a UserService with async patterns and DI"
- "Review this C# code for best practices"
- "Implement repository pattern with Unit of Work"
- "Write xUnit tests for this service"
- "Optimize this LINQ query"

## References

- [Microsoft C# Conventions](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [.NET Design Guidelines](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/)
- [xUnit](https://xunit.net/) | [FluentAssertions](https://fluentassertions.com/) | [EF Core](https://docs.microsoft.com/en-us/ef/core/)
