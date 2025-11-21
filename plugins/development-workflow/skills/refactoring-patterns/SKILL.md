---
name: refactoring-patterns
description: Common refactoring patterns and techniques for improving code quality, reducing complexity, and enhancing maintainability. Use when planning or executing code refactoring.
---

# Refactoring Patterns

This skill provides proven patterns for safe, effective code refactoring.

## Core Refactoring Principles

1. **Red-Green-Refactor**: Ensure tests pass before and after refactoring
2. **Small Steps**: Make incremental changes, commit frequently
3. **One Thing at a Time**: Refactor OR add features, not both
4. **Maintain Behavior**: External behavior stays the same

## Common Code Smells

### Long Method
**Smell**: Method exceeds 20-30 lines or does too many things  
**Refactor**: Extract Method - Break down into smaller, focused functions

### Duplicated Code
**Smell**: Same code structure appears in multiple places  
**Refactor**: Extract common code into shared functions/methods

### Large Class
**Smell**: Class has too many responsibilities  
**Refactor**: Extract Class - Separate concerns into distinct classes

### Feature Envy
**Smell**: Method uses more data from another class than its own  
**Refactor**: Move Method to the class that owns the data

## Refactoring Techniques

### Replace Conditional with Polymorphism
Use inheritance and polymorphism instead of switch statements or complex conditionals

### Introduce Parameter Object
Group related parameters into a single object for cleaner function signatures

### Replace Magic Numbers with Named Constants
Extract hardcoded values into well-named constants for clarity and maintainability

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
