---
name: refactoring-patterns
description: Refactoring patterns for code quality and maintainability. Use when planning or executing refactoring.
---

# Refactoring Patterns

## Guidelines

1. **Red-Green-Refactor**: Tests pass before and after
2. **Small Steps**: Incremental changes, commit frequently
3. **One Thing at a Time**: Refactor OR add features, not both
4. **Maintain Behavior**: External behavior unchanged

## Refactoring Levels

- **Architectural**: System components, service boundaries
- **Module**: Package structure, shared libraries, dependencies
- **Class**: Design patterns, interfaces, encapsulation
- **Function**: Logic simplification, naming, parameters

## Strategy

1. **Understand**: Read code, identify tests, document behavior, note dependencies
2. **Test Coverage**: Add missing tests, verify all pass
3. **Plan**: Create markdown checklist with incremental steps, risks
4. **Execute**: One change at a time, test after each, commit frequently
5. **Verify**: Tests pass, code clearer, docs updated

## Checklist

- [ ] Tests pass before/after each step
- [ ] Behavior unchanged
- [ ] Never remove existing tests
