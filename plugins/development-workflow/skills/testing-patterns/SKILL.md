---
name: testing-patterns
description: Comprehensive testing patterns, strategies, and best practices for writing effective unit, integration, and end-to-end tests across different testing frameworks
author: Claude Code Toolkit
---

# Testing Patterns and Best Practices

This skill provides comprehensive testing guidelines and patterns that are automatically activated during test creation, code review, and quality assurance tasks.

## Purpose

Automatically activated when:
- Writing unit tests
- Creating integration tests
- Implementing end-to-end tests
- Reviewing test code
- Evaluating test coverage
- Designing testing strategies

## Testing Pyramid

### Unit Tests (70% of tests)

**Characteristics:**
- Fast execution (milliseconds)
- Test individual functions/methods in isolation
- No external dependencies (databases, APIs, file systems)
- High code coverage
- Run frequently during development

**Best Practices:**
- Test one thing per test
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)
- Keep tests independent
- Avoid test interdependencies
- Mock external dependencies

### Integration Tests (20% of tests)

**Characteristics:**
- Test interactions between components
- Include some external dependencies
- Slower than unit tests (seconds)
- Verify component integration
- Test API contracts and data flow

**Best Practices:**
- Test realistic scenarios
- Use test databases or containers
- Clean up test data after each test
- Test error conditions
- Verify integration points
- Use appropriate fixtures

### End-to-End Tests (10% of tests)

**Characteristics:**
- Test complete user workflows
- Include all system components
- Slowest tests (minutes)
- Test from user perspective
- Verify critical business paths

**Best Practices:**
- Focus on critical user journeys
- Keep tests maintainable
- Use page object pattern
- Implement proper waits and timeouts
- Test on multiple browsers/devices
- Run in CI/CD pipeline

## Test Structure Patterns

### AAA Pattern (Arrange, Act, Assert)

```
// Arrange - Set up test data and conditions
const user = createTestUser();
const service = new UserService();

// Act - Execute the behavior under test
const result = service.authenticate(user);

// Assert - Verify expected outcome
expect(result.isAuthenticated).toBe(true);
```

### Given-When-Then (BDD Style)

```
Given a user with valid credentials
When they attempt to log in
Then they should be successfully authenticated
```

### Test Fixture Setup

**Setup and Teardown:**
- Use `beforeEach`/`afterEach` for test isolation
- Use `beforeAll`/`afterAll` for expensive setup
- Clean up resources after tests
- Reset mocks between tests
- Ensure test independence

## Test Naming Conventions

### Descriptive Test Names

**Good naming patterns:**
- `should_returnError_when_inputIsInvalid`
- `test_authenticateUser_withValidCredentials_returnsSuccess`
- `getUserById_whenUserExists_shouldReturnUser`
- `it('throws error when password is too short')`

**Test name structure:**
- What is being tested
- Under what conditions
- Expected outcome

### BDD-Style Naming

```
describe('UserAuthentication', () => {
  describe('when credentials are valid', () => {
    it('should authenticate the user', () => {});
    it('should generate a session token', () => {});
  });
  
  describe('when credentials are invalid', () => {
    it('should return authentication error', () => {});
    it('should increment failed login counter', () => {});
  });
});
```

## Test Data Management

### Test Data Strategies

**Inline Test Data:**
- Use for simple, one-off test cases
- Keep data close to tests
- Make test data explicit

**Test Factories/Builders:**
- Create reusable test data builders
- Use builder pattern for complex objects
- Provide sensible defaults
- Allow customization for specific tests

**Fixtures:**
- Use for consistent test data
- Store in separate files when appropriate
- Version control test fixtures
- Document fixture purpose and structure

### Test Data Best Practices

- Use realistic but anonymized data
- Create minimal test data needed
- Make test data generation deterministic
- Avoid hardcoding IDs and timestamps
- Use factories for complex object creation
- Clean up test data after tests

## Mocking and Stubbing

### When to Mock

**Good candidates for mocking:**
- External APIs and services
- Database connections
- File system operations
- Time-dependent code
- Network requests
- Third-party services

### Mocking Strategies

**Types of Test Doubles:**
- **Dummy** - Objects passed but never used
- **Stub** - Returns predefined responses
- **Spy** - Records how it was called
- **Mock** - Verifies expected interactions
- **Fake** - Working implementation (simplified)

### Mocking Best Practices

- Mock external dependencies, not internal code
- Avoid over-mocking (makes tests brittle)
- Verify meaningful interactions
- Use fake implementations for complex dependencies
- Reset mocks between tests
- Test real integrations in integration tests

## Test Coverage

### Coverage Metrics

**Types of Coverage:**
- Line coverage (statements executed)
- Branch coverage (all paths tested)
- Function coverage (functions called)
- Condition coverage (boolean expressions)

**Coverage Goals:**
- Aim for 80%+ line coverage
- 100% coverage on critical paths
- Focus on meaningful coverage, not just numbers
- Cover edge cases and error paths
- Don't ignore trivial getters/setters unless truly simple

### Coverage Blind Spots

**Areas to ensure coverage:**
- Error handling and edge cases
- Boundary conditions
- Null/undefined handling
- Asynchronous operations
- State transitions
- Configuration variations

## Testing Asynchronous Code

### Promises and Async/Await

**Testing async code:**
```javascript
// Using async/await
test('fetches user data', async () => {
  const user = await fetchUser(123);
  expect(user.name).toBe('John');
});

// Using promises
test('fetches user data', () => {
  return fetchUser(123).then(user => {
    expect(user.name).toBe('John');
  });
});
```

### Callbacks

**Testing callbacks:**
```javascript
test('calls callback with data', (done) => {
  fetchUser(123, (error, user) => {
    expect(error).toBeNull();
    expect(user.name).toBe('John');
    done();
  });
});
```

### Event Emitters

**Testing events:**
```javascript
test('emits event when data changes', (done) => {
  const emitter = new DataEmitter();
  emitter.on('change', (data) => {
    expect(data.value).toBe('new');
    done();
  });
  emitter.update('new');
});
```

## Testing Best Practices

### General Principles

**FIRST Principles:**
- **Fast** - Tests should run quickly
- **Independent** - Tests shouldn't depend on each other
- **Repeatable** - Same results every time
- **Self-validating** - Pass or fail, no manual verification
- **Timely** - Write tests early (TDD) or with code

### Test Quality

**Characteristics of good tests:**
- Clear and focused
- Easy to understand
- Test one concept
- Provide good error messages
- Are maintainable
- Run reliably
- Test behavior, not implementation

### Common Anti-Patterns to Avoid

**Testing anti-patterns:**
- Tests that depend on execution order
- Tests with hidden dependencies
- Overly complex test setup
- Testing implementation details
- Fragile tests (break with minor changes)
- Slow tests in unit test suite
- Tests that test the framework
- Assertion roulette (too many assertions)
- Mock everything syndrome

## Test-Driven Development (TDD)

### Red-Green-Refactor Cycle

1. **Red** - Write a failing test
2. **Green** - Write minimal code to pass
3. **Refactor** - Improve code while keeping tests green

### TDD Benefits

- Better design through testability
- Higher confidence in changes
- Living documentation
- Fewer bugs
- Easier refactoring
- Focus on requirements

### When to Use TDD

**Good for:**
- Complex business logic
- Algorithm implementation
- Bug fixing (write test first)
- New feature development
- Unfamiliar code areas

## Behavior-Driven Development (BDD)

### BDD Tools and Patterns

**Common BDD frameworks:**
- Cucumber (Gherkin syntax)
- Jest (describe/it syntax)
- RSpec (Ruby)
- Jasmine (JavaScript)

### BDD Best Practices

- Write scenarios from user perspective
- Use ubiquitous language
- Keep scenarios focused
- Avoid technical details in feature files
- Reuse step definitions appropriately

## Testing Patterns by Type

### API Testing

**REST API tests should verify:**
- HTTP status codes
- Response body structure
- Response headers
- Error responses
- Authentication/authorization
- Rate limiting
- Input validation

### Database Testing

**Database test patterns:**
- Use in-memory databases for speed
- Use transactions for test isolation
- Test data constraints
- Verify triggers and procedures
- Test migrations
- Use containers for integration tests

### UI Testing

**UI test best practices:**
- Use page object pattern
- Test user workflows, not UI structure
- Use data-test attributes
- Implement proper waits
- Test accessibility
- Verify error states

### Performance Testing

**Performance test types:**
- Load testing (expected load)
- Stress testing (beyond capacity)
- Spike testing (sudden increases)
- Endurance testing (sustained load)
- Scalability testing

## Test Frameworks by Language

### JavaScript/TypeScript

**Popular frameworks:**
- Jest - Full-featured, zero-config
- Mocha + Chai - Flexible, modular
- Vitest - Fast, Vite-powered
- Cypress - E2E testing
- Playwright - Cross-browser testing

### Python

**Popular frameworks:**
- pytest - Most popular, extensible
- unittest - Built-in standard library
- nose2 - Extension of unittest
- Robot Framework - Keyword-driven

### Java

**Popular frameworks:**
- JUnit 5 - Standard unit testing
- TestNG - Feature-rich testing
- Mockito - Mocking framework
- Selenium - Web automation
- Rest-Assured - API testing

### Go

**Popular frameworks:**
- testing package (built-in)
- Testify - Assertions and mocking
- Ginkgo - BDD framework
- GoMock - Mocking framework

## CI/CD Integration

### Test Automation

**CI/CD best practices:**
- Run unit tests on every commit
- Run integration tests on pull requests
- Run E2E tests before deployment
- Parallelize test execution
- Cache dependencies
- Report test coverage
- Fail fast on test failures

### Test Environment Management

- Use containerization (Docker)
- Implement environment parity
- Manage test data properly
- Use infrastructure as code
- Implement smoke tests for deployments

## Test Maintenance

### Keeping Tests Healthy

**Regular maintenance:**
- Remove obsolete tests
- Update tests with code changes
- Refactor duplicated test code
- Fix flaky tests immediately
- Update test data periodically
- Review and improve test coverage

### Dealing with Flaky Tests

**Strategies:**
- Identify root cause (timing, environment, data)
- Add proper waits/retries
- Improve test isolation
- Use deterministic test data
- Mock time-dependent code
- Quarantine flaky tests temporarily

## Testing Checklist

When writing or reviewing tests, verify:

- [ ] Tests follow AAA/Given-When-Then pattern
- [ ] Test names are descriptive
- [ ] Tests are independent and isolated
- [ ] External dependencies are mocked appropriately
- [ ] Edge cases and error paths are tested
- [ ] Async code is tested correctly
- [ ] Test data is managed properly
- [ ] Tests run fast (especially unit tests)
- [ ] Tests are deterministic (no randomness)
- [ ] Good coverage of critical paths
- [ ] Tests are maintainable and readable
- [ ] Setup and teardown are implemented
- [ ] Assertions are meaningful and specific

## Usage by Agents

This skill is automatically available to:
- **senior-engineer** - During implementation and test writing
- **code-reviewer** - When reviewing test code quality
- **technical-architecture-advisor** - When designing testing strategies

The skill ensures comprehensive testing practices across all development activities.
