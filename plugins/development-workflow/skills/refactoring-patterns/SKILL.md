---
name: refactoring-patterns
description: Common refactoring patterns and techniques for improving code quality, reducing complexity, and enhancing maintainability. Use when planning or executing code refactoring.
---

# Refactoring Patterns

This skill provides proven patterns for safe, effective code refactoring.

## Core Refactoring Principles

### Design Principles
1. **SOLID**: Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion
2. **KISS** (Keep It Simple, Stupid): Favor simplicity over complexity
3. **YAGNI** (You Aren't Gonna Need It): Don't add functionality until necessary
4. **DRY** (Don't Repeat Yourself): Avoid code duplication

### Refactoring Guidelines
1. **Red-Green-Refactor**: Ensure tests pass before and after refactoring
2. **Small Steps**: Make incremental changes, commit frequently
3. **One Thing at a Time**: Refactor OR add features, not both
4. **Maintain Behavior**: External behavior stays the same
5. **Avoid Premature Optimization**: Focus on clarity first, optimize when needed based on metrics

## Refactoring Approaches

### Architectural Level
- Restructure system components and module boundaries
- Refactor service boundaries in microservices/modular monoliths
- Redesign database schema and data access patterns
- Improve system scalability and performance architecture

### Module/Package Level
- Reorganize package structure for better cohesion
- Extract shared libraries or utilities
- Improve dependency management and reduce coupling
- Refactor cross-cutting concerns

### Class/Component Level
- Apply SOLID principles to class design
- Extract interfaces and abstractions
- Reduce class complexity and responsibilities
- Improve encapsulation and information hiding

### Method/Function Level
- Simplify complex logic
- Extract reusable functions
- Improve naming and readability
- Reduce parameter lists

## Refactoring Strategy

### 1. Understand the Code

Before refactoring:
- [ ] Read and understand the existing code
- [ ] Identify all test coverage
- [ ] Document current behavior
- [ ] Note any dependencies

### 2. Ensure Test Coverage

- [ ] Add tests if missing
- [ ] Verify all tests pass
- [ ] Consider adding characterization tests

### 3. Plan Refactoring

- [ ] Identify specific smells to address
- [ ] Choose appropriate refactoring patterns
- [ ] Plan sequence of small steps
- [ ] Consider creating feature flag if risky

### 4. Execute Incrementally

- [ ] Make one change at a time
- [ ] Run tests after each change
- [ ] Commit working code frequently
- [ ] Roll back if tests fail

### 5. Verify and Clean Up

- [ ] All tests pass
- [ ] Code is clearer and simpler
- [ ] No performance regression
- [ ] Update documentation

## Safe Refactoring Checklist

- [ ] Tests exist and pass before starting
- [ ] Each refactoring step is small and focused
- [ ] Tests pass after each step
- [ ] Behavior remains unchanged
- [ ] Performance is not degraded
- [ ] Code is more maintainable
- [ ] Team has reviewed changes

## Integration Points

Works with:
- `senior-engineer` agent for refactoring execution
- `technical-architecture-advisor` for large-scale refactoring
- `/refactoring-plan` command for structured refactoring
- `code-reviewer` agent for validating improvements
