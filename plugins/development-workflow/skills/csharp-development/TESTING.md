# .NET Testing Guidelines

Modern testing patterns for .NET 10 applications using TUnit, AwesomeAssertions, and TestContainers.

## Core Principles

1. **Add tests for every behavioral change**
2. **Sociable tests** - Use real objects, avoid over-mocking
3. **Test behavior** not implementation
4. **High-level integration tests preferred** - Test through HTTP endpoints when possible
5. **Real dependencies** - Use TestContainers for databases, WebApplicationFactory for APIs
6. **AAA Pattern** - Arrange, Act, Assert
7. **Async testing** - Use async/await consistently

## Test Framework: TUnit

Modern, high-performance testing framework for .NET.

### Basic Structure

- `[Test]` attribute for test methods
- Async by default - all test methods should be `async Task`
- Naming: `MethodName_Scenario_ExpectedResult`

### Parameterized Tests

- `[Arguments]` - Single parameter values per test case
- `[Matrix]` - Cartesian product of parameter combinations
- `[MethodDataSource]` - Complex data from method

### Lifecycle Hooks

- `[Before(Test)]` / `[After(Test)]` - Per-test setup/cleanup
- `[Before(Class)]` / `[After(Class)]` - Once per class
- `[Before(Assembly)]` / `[After(Assembly)]` - Once per assembly

### Running Tests

```bash
dotnet test
dotnet test -- TUnit.MaxParallelTests=4
dotnet test --filter "FullyQualifiedName~TestName"
```

[TUnit Documentation](https://github.com/thomhurst/TUnit)

## Assertions: AwesomeAssertions

Fluent assertion syntax with better performance than FluentAssertions.

### Syntax

All assertions use `await Assert.That(value).{Assertion}()`:

- **Equality**: `IsEqualTo()`, `IsNotEqualTo()`
- **Null**: `IsNull()`, `IsNotNull()`
- **Numeric**: `IsGreaterThan()`, `IsLessThan()`, `IsInRange()`, `IsPositive()`, `IsNegative()`
- **Strings**: `Contains()`, `StartsWith()`, `EndsWith()`, `Matches()`, `IsNullOrEmpty()`
- **Collections**: `HasCount()`, `IsEmpty()`, `Contains()`, `ContainsInOrder()`, `AllSatisfy()`, `IsInAscendingOrder()`
- **Boolean**: `IsTrue()`, `IsFalse()`
- **Exceptions**: `ThrowsAsync<T>()`, `WithMessage()`
- **Types**: `IsOfType<T>()`, `IsAssignableTo<T>()`

### AssertionScope

Use `new AssertionScope()` to report all failures together instead of stopping at first failure.

[AwesomeAssertions Documentation](https://github.com/AwesomeAssertions/AwesomeAssertions)

## Mocking: FakeItEasy

**Prefer real implementations over mocks.** Use mocks only for external dependencies (HTTP APIs, email services, payment gateways).

### Basic Usage

- **Create**: `A.Fake<IInterface>()`
- **Configure returns**: `A.CallTo(() => fake.Method()).Returns(value)`
- **Throw exceptions**: `A.CallTo(() => fake.Method()).Throws<TException>()`
- **Verify calls**: `A.CallTo(() => fake.Method()).MustHaveHappenedOnceExactly()`
- **Argument matchers**: `A<T>._` (any), `A<T>.That.Matches(predicate)`

[FakeItEasy Documentation](https://fakeiteasy.github.io/)

## Integration Testing

### WebApplicationFactory

Test ASP.NET Core apps end-to-end. Implement `IAsyncLifetime`, create factory with custom configuration, inject test services. Test through HTTP client for full request/response cycle.

### TestContainers

Use real databases in tests with Docker containers. Supports PostgreSQL, MySQL, SQL Server, MongoDB, Redis, etc. Start containers in `InitializeAsync()`, dispose in `DisposeAsync()`.

```csharp
_container = new PostgreSqlBuilder()
    .WithImage("postgres:16")
    .WithDatabase("testdb")
    .Build();
await _container.StartAsync();
```

[Testcontainers for .NET](https://dotnet.testcontainers.org/)

### TimeProvider Testing

Use `TimeProvider` injection for testable time-dependent code. Test with `FakeTimeProvider` from `Microsoft.Extensions.Time.Testing`.

```csharp
var timeProvider = new FakeTimeProvider(fixedDateTime);
```

## Best Practices

**DO:**
- Write tests alongside code (TDD when appropriate)
- Test behavior, not implementation details
- Use descriptive names: `MethodName_Scenario_ExpectedResult`
- Keep tests isolated (no shared state)
- Prefer real objects over mocks (sociable tests)
- Use AssertionScope for multiple assertions
- Test edge cases (null, empty, boundaries, exceptions)
- Clean up resources (`IAsyncLifetime`, `IDisposable`)
- Use high-level integration tests (test through HTTP)
- Use TestContainers for real databases
- Use `TimeProvider` for time-dependent code

**DON'T:**
- Test framework internals or third-party libraries
- Over-mock (prefer real implementations)
- Write brittle tests (avoid coupling to implementation)
- Share state between tests
- Ignore flaky tests (fix or remove)
- Test private methods directly (test through public API)
- Use `Thread.Sleep` (use `Task.Delay` or `FakeTimeProvider`)
- Catch exceptions in tests (use exception assertions)
- Use production databases
- Mock DbContext (use in-memory database or TestContainers)

## Test Organization

**File naming**: `ClassNameTests.cs`
**Directory structure**: Mirror `src` structure

```
src/Features/Orders/
  OrderService.cs

tests/Features/Orders/
  OrderServiceTests.cs
```

**Quality gates**: `dotnet build && dotnet test && dotnet format --verify-no-changes`

## Migration Guides

### xUnit to TUnit

| xUnit | TUnit |
|-------|-------|
| `[Fact]` | `[Test]` |
| `[Theory]` + `[InlineData]` | `[Test]` + `[Arguments]` |
| `[Theory]` + `[MemberData]` | `[Test]` + `[Matrix]` or `[MethodDataSource]` |
| `IClassFixture<T>` | `[Before(Class)]` / `[After(Class)]` |
| `ICollectionFixture<T>` | `[Before(Assembly)]` / `[After(Assembly)]` |
| `Assert.Equal(expected, actual)` | `await Assert.That(actual).IsEqualTo(expected)` |
| `Assert.True(condition)` | `await Assert.That(condition).IsTrue()` |
| `Assert.Throws<T>()` | `await Assert.That(act).ThrowsAsync<T>()` |

### FluentAssertions to AwesomeAssertions

**API is identical** - only namespace and syntax change:

- Change `using FluentAssertions` to `using AwesomeAssertions`
- Change `value.Should().Be(expected)` to `await Assert.That(value).IsEqualTo(expected)`
- All assertions are async
- Better performance and memory usage

## Troubleshooting

**Flaky tests**: Check shared state, use `FakeTimeProvider`, use TestContainers instead of in-memory databases, ensure proper cleanup

**Slow tests**: Profile execution, reduce DB/network calls, use in-memory for unit tests, parallelize (TUnit default), optimize setup/teardown

**CI failures**: Check timezone differences (use `TimeProvider.GetUtcNow()`), verify environment variables, check file path differences, use TestContainers for consistency

## References

- [TUnit](https://github.com/thomhurst/TUnit)
- [AwesomeAssertions](https://github.com/AwesomeAssertions/AwesomeAssertions)
- [FakeItEasy](https://fakeiteasy.github.io/)
- [Testcontainers](https://dotnet.testcontainers.org/)
- [TimeProvider Testing](https://www.nuget.org/packages/Microsoft.Extensions.Time.Testing)
