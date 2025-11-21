---
name: code-quality-standards
description: Comprehensive code quality standards and best practices for writing maintainable, readable, and performant code across multiple programming languages
author: Claude Code Toolkit
---

# Code Quality Standards

This skill provides comprehensive code quality standards and best practices that can be automatically referenced during code review, implementation, and refactoring tasks.

## Purpose

Automatically activated when:
- Reviewing code for quality issues
- Implementing new features
- Refactoring existing code
- Performing code analysis
- Creating or updating code style guidelines

## Universal Code Quality Principles

### 1. Naming Conventions

**Variables and Functions:**
- Use descriptive, self-documenting names
- Avoid abbreviations unless universally understood
- Use consistent naming patterns within the codebase
- Boolean variables should start with `is`, `has`, `should`, `can`
- Functions should use verb phrases (e.g., `getUserData`, `calculateTotal`)

**Constants:**
- Use uppercase with underscores (e.g., `MAX_RETRY_COUNT`)
- Group related constants together
- Document magic numbers with named constants

**Classes and Types:**
- Use PascalCase for class names
- Use nouns or noun phrases
- Make names specific and descriptive

### 2. Function Design

**Single Responsibility:**
- Each function should do one thing well
- If a function name contains "and", consider splitting it
- Keep functions under 50 lines when possible
- Extract complex logic into well-named helper functions

**Function Parameters:**
- Limit to 3-4 parameters when possible
- Use object parameters for functions with many arguments
- Make parameter intent clear through naming
- Avoid boolean parameters (use specific methods instead)

**Return Values:**
- Be consistent with return types
- Document unexpected return values
- Avoid returning null when possible (use Optional/Maybe patterns)
- Return early to avoid deep nesting

### 3. Code Organization

**File Structure:**
- One primary class/component per file
- Group related functionality together
- Keep files under 300-400 lines
- Use clear directory structures that reflect architecture

**Import Management:**
- Group imports by category (standard library, third-party, local)
- Remove unused imports
- Use absolute imports over relative when possible
- Avoid circular dependencies

**Comments and Documentation:**
- Write self-documenting code first
- Comment the "why", not the "what"
- Keep comments up-to-date with code changes
- Use JSDoc/Docstring conventions consistently
- Document complex algorithms and business logic

### 4. Error Handling

**Defensive Programming:**
- Validate input parameters
- Handle edge cases explicitly
- Fail fast with clear error messages
- Use custom error types for domain-specific errors

**Exception Management:**
- Catch specific exceptions, not generic ones
- Don't swallow exceptions silently
- Log errors with context
- Provide actionable error messages

### 5. Code Complexity

**Cyclomatic Complexity:**
- Keep functions under 10 complexity score
- Reduce nested conditionals
- Extract complex conditions into well-named functions
- Use guard clauses to reduce nesting

**DRY Principle (Don't Repeat Yourself):**
- Extract common patterns into reusable functions
- Avoid copy-paste coding
- Use inheritance or composition appropriately
- Create utility functions for repeated operations

### 6. Performance Considerations

**Optimization Guidelines:**
- Optimize for readability first, performance second
- Avoid premature optimization
- Use appropriate data structures
- Be mindful of time and space complexity
- Profile before optimizing

**Resource Management:**
- Close resources explicitly (files, connections, streams)
- Avoid memory leaks
- Use connection pooling when appropriate
- Implement proper cleanup in destructors/dispose methods

## Language-Specific Best Practices

### JavaScript/TypeScript

**Modern Syntax:**
- Use `const` by default, `let` when needed, never `var`
- Prefer arrow functions for callbacks
- Use template literals for string interpolation
- Use destructuring for cleaner code
- Leverage async/await over Promise chains

**Type Safety (TypeScript):**
- Enable strict mode
- Avoid `any` type
- Use interfaces for object shapes
- Define return types explicitly
- Use union types over enums when appropriate

### Python

**PEP 8 Compliance:**
- Use 4 spaces for indentation
- Maximum line length of 88-100 characters
- Use snake_case for functions and variables
- Use meaningful variable names
- Follow import ordering conventions

**Python Idioms:**
- Use list comprehensions appropriately
- Leverage context managers (`with` statements)
- Use type hints for function signatures
- Follow the Zen of Python principles
- Use dataclasses for data structures

### Java

**Java Conventions:**
- Follow standard naming conventions
- Use meaningful package names
- Prefer interfaces over abstract classes
- Use streams for collection operations
- Implement equals() and hashCode() consistently

**Object-Oriented Principles:**
- Favor composition over inheritance
- Program to interfaces
- Use dependency injection
- Apply SOLID principles
- Minimize mutability

### Go

**Go Idioms:**
- Use gofmt for consistent formatting
- Keep package names short and clear
- Use error values, not exceptions
- Prefer simplicity over cleverness
- Follow effective Go guidelines

**Concurrency:**
- Use channels for goroutine communication
- Avoid shared state when possible
- Use sync primitives appropriately
- Handle goroutine lifecycle properly

## Code Review Checklist

When reviewing code, verify:

- [ ] Names are clear and self-documenting
- [ ] Functions are small and focused
- [ ] No code duplication
- [ ] Error handling is comprehensive
- [ ] Edge cases are handled
- [ ] Comments explain "why", not "what"
- [ ] Code follows project conventions
- [ ] Tests are included and meaningful
- [ ] No security vulnerabilities
- [ ] Performance considerations addressed
- [ ] Documentation is updated
- [ ] Breaking changes are documented

## Anti-Patterns to Avoid

**Common Anti-Patterns:**
- God objects (classes that do too much)
- Spaghetti code (tangled dependencies)
- Magic numbers and strings
- Copy-paste programming
- Premature optimization
- Over-engineering
- Not invented here syndrome
- Golden hammer (one solution for everything)

## References and Resources

- Clean Code by Robert C. Martin
- Refactoring by Martin Fowler
- Design Patterns (Gang of Four)
- Language-specific style guides
- SOLID principles
- DRY, KISS, YAGNI principles

## Usage by Agents

This skill is automatically available to:
- **senior-engineer** - During implementation and code writing
- **code-reviewer** - During code review processes
- **technical-architecture-advisor** - When evaluating code quality concerns

The skill provides consistent standards that ensure code quality across all development activities.
