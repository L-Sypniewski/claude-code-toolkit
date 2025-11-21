---
name: testing-patterns
description: Common testing patterns, best practices, and strategies for unit, integration, and end-to-end testing. Use when writing tests or designing testing strategies.
---

# Testing Patterns

This skill provides proven testing patterns and strategies for comprehensive test coverage.

## Test Pyramid

Aim for this distribution:

```
        /\
       /E2E\      10% - End-to-End (slow, brittle)
      /------\
     /  INT   \   20% - Integration (medium speed)
    /----------\
   /   UNIT     \ 70% - Unit Tests (fast, focused)
  /--------------\
```

## Unit Testing Patterns

### AAA Pattern (Arrange-Act-Assert)

```javascript
test('calculateTotal adds tax correctly', () => {
  // Arrange
  const cart = { subtotal: 100 };
  const taxRate = 0.1;
  
  // Act
  const total = calculateTotal(cart, taxRate);
  
  // Assert
  expect(total).toBe(110);
});
```

### Test Data Builders

Create reusable test data factories:

```javascript
class UserBuilder {
  constructor() {
    this.user = {
      id: 1,
      name: 'Test User',
      email: 'test@example.com'
    };
  }
  
  withId(id) {
    this.user.id = id;
    return this;
  }
  
  withEmail(email) {
    this.user.email = email;
    return this;
  }
  
  build() {
    return this.user;
  }
}

// Usage
const user = new UserBuilder()
  .withId(42)
  .withEmail('john@example.com')
  .build();
```

### Parameterized Tests

Test multiple inputs efficiently:

```python
@pytest.mark.parametrize("input,expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
])
def test_is_prime(input, expected):
    assert is_prime(input) == expected
```

## Integration Testing

### Database Tests

```javascript
describe('UserRepository', () => {
  beforeEach(async () => {
    await database.migrate();
    await database.seed();
  });
  
  afterEach(async () => {
    await database.rollback();
  });
  
  it('creates user with valid data', async () => {
    const userData = { name: 'John', email: 'john@example.com' };
    const user = await userRepo.create(userData);
    
    expect(user.id).toBeDefined();
    expect(user.name).toBe('John');
  });
});
```

### API Tests

```javascript
describe('POST /api/users', () => {
  it('creates user and returns 201', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'John', email: 'john@example.com' })
      .expect(201);
    
    expect(response.body.user.name).toBe('John');
  });
  
  it('returns 400 for invalid email', async () => {
    await request(app)
      .post('/api/users')
      .send({ name: 'John', email: 'invalid-email' })
      .expect(400);
  });
});
```

## Mocking Strategies

### Dependency Injection

Make code testable by injecting dependencies:

```javascript
class OrderService {
  constructor(paymentGateway, emailService) {
    this.paymentGateway = paymentGateway;
    this.emailService = emailService;
  }
  
  async placeOrder(order) {
    await this.paymentGateway.charge(order.total);
    await this.emailService.sendConfirmation(order);
  }
}

// In tests
test('placeOrder charges payment gateway', async () => {
  const mockGateway = { charge: jest.fn() };
  const mockEmail = { sendConfirmation: jest.fn() };
  
  const service = new OrderService(mockGateway, mockEmail);
  await service.placeOrder({ total: 100 });
  
  expect(mockGateway.charge).toHaveBeenCalledWith(100);
});
```

### Time Mocking

Control time in tests:

```javascript
test('token expires after 1 hour', () => {
  const now = new Date('2025-01-01T10:00:00Z');
  jest.setSystemTime(now);
  
  const token = createToken();
  
  jest.setSystemTime(new Date('2025-01-01T11:01:00Z'));
  expect(isTokenValid(token)).toBe(false);
});
```

## Test Organization

### File Structure

```
src/
  users/
    user.service.js
    user.service.test.js
    user.repository.js
    user.repository.test.js
tests/
  integration/
    user-api.test.js
  e2e/
    user-flow.test.js
```

### Test Naming

Be descriptive and specific:

```javascript
// ❌ Bad
test('user test', () => { ... });

// ✅ Good
test('createUser throws ValidationError when email is invalid', () => { ... });
```

## Edge Cases to Test

Always test:

- Empty inputs (`''`, `[]`, `{}`, `null`, `undefined`)
- Boundary values (min, max, just below/above limits)
- Invalid types (string where number expected)
- Concurrent operations (race conditions)
- Network failures (timeouts, disconnects)
- Large datasets (performance, memory)

## Test Smells to Avoid

- **Flaky tests**: Non-deterministic results
- **Slow tests**: Unit tests taking seconds
- **Testing implementation**: Test behavior, not internals
- **Giant setup**: Tests with 50+ lines of setup
- **Assertion roulette**: Multiple unrelated assertions
- **Test interdependence**: Tests depending on execution order

## Integration Points

Works with:
- `senior-engineer` agent for test strategy
- `code-reviewer` agent for test coverage validation
- CI/CD pipelines for automated testing
