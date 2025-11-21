---
name: code-review-checklist
description: Comprehensive code review checklist covering correctness, performance, security, and maintainability. Use when performing code reviews or preparing code for review.
---

# Code Review Checklist

This skill provides a systematic approach to code review, ensuring comprehensive quality assessment.

## Core Review Areas

### 1. Correctness

- [ ] **Logic**: Code implements requirements correctly
- [ ] **Edge Cases**: Handles boundary conditions and error cases
- [ ] **Data Validation**: Input validation is thorough
- [ ] **Error Handling**: Errors are caught and handled appropriately
- [ ] **Type Safety**: Types are used correctly (for typed languages)

### 2. Performance

- [ ] **Algorithmic Complexity**: Appropriate algorithms chosen (time/space)
- [ ] **Resource Usage**: No unnecessary memory allocations
- [ ] **Database Queries**: Efficient queries, proper indexing
- [ ] **Caching**: Appropriate use of caching strategies
- [ ] **Async Operations**: Non-blocking where appropriate

### 3. Security

- [ ] **Input Sanitization**: User input is sanitized
- [ ] **SQL Injection**: Parameterized queries used
- [ ] **XSS Protection**: Output is escaped properly
- [ ] **Authentication**: Auth checks are present and correct
- [ ] **Authorization**: Permission checks are enforced
- [ ] **Secrets**: No hardcoded credentials or API keys
- [ ] **HTTPS**: Secure communication enforced

### 4. Maintainability

- [ ] **Naming**: Clear, descriptive variable/function names
- [ ] **Function Length**: Functions are focused and concise
- [ ] **Duplication**: No unnecessary code duplication (DRY)
- [ ] **Comments**: Complex logic is documented
- [ ] **SOLID Principles**: Code follows good design principles
- [ ] **Testability**: Code structure supports testing

### 5. Testing

- [ ] **Unit Tests**: Core logic has unit test coverage
- [ ] **Integration Tests**: Component interactions are tested
- [ ] **Test Quality**: Tests are meaningful, not just for coverage
- [ ] **Edge Cases**: Tests cover boundary conditions
- [ ] **Mocking**: Appropriate use of mocks/stubs

### 6. Documentation

- [ ] **API Docs**: Public APIs are documented
- [ ] **README Updates**: Documentation reflects changes
- [ ] **Migration Guides**: Breaking changes documented
- [ ] **Inline Comments**: Complex logic explained
- [ ] **Changelog**: Changes noted in changelog

## Language-Specific Checks

### JavaScript/TypeScript

- [ ] No use of `var`, prefer `const`/`let`
- [ ] Proper async/await usage, no promise chains
- [ ] TypeScript types defined (no `any` without justification)
- [ ] Dependencies up to date, no security vulnerabilities

### Python

- [ ] PEP 8 compliance (or project style guide)
- [ ] Type hints used for function signatures
- [ ] Proper use of context managers (`with` statements)
- [ ] Virtual environment dependencies specified

### Java

- [ ] Proper exception handling (no empty catch blocks)
- [ ] Resources closed properly (try-with-resources)
- [ ] Thread safety considered for concurrent code
- [ ] Null safety (Optional, annotations)

## Review Comments Template

Use this format for actionable feedback:

```markdown
**[Category]**: [Issue]

**Location**: file.js:123

**Current**: 
```code snippet```

**Suggestion**:
```improved code```

**Rationale**: Why this change improves the code

**Priority**: [Critical|High|Medium|Low]
```

## Quick Wins

Fast improvements with high impact:

1. Remove unused imports/variables
2. Fix inconsistent formatting
3. Add missing error handling
4. Improve variable names
5. Extract magic numbers to constants
6. Add basic input validation

## Integration with Plugin

Works with:
- `code-reviewer` agent for automated review
- `senior-engineer` agent for implementation guidance
- Pre-PR review workflow
