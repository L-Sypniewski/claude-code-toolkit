# .NET Testing Guidelines

Production testing patterns based on ConvoClarity application.

## Core Principles

1. **Add tests for every behavioral change**
2. **Sociable tests** - Use real objects, avoid over-mocking
3. **Test behavior** not implementation
4. **AAA Pattern** - Arrange, Act, Assert
5. **Async testing** - Use async/await
6. **Real dependencies** - Testcontainers for databases

## Test Framework: xUnit

**Structure:** `[Fact]` for single test, `[Theory]` with `[InlineData]` for parameterized tests, `[MemberData]` for complex data

**Naming:** `MethodName_Scenario_ExpectedResult`

**Organization:** Mirror src structure in test project

## Assertions: AwesomeAssertions (FluentAssertions)

**Syntax:** `.Should()` methods - readable assertions  
**AssertionScope:** Use `using var _ = new AssertionScope()` to report all failures together  
**Collections:** `.Should().HaveCount()`, `.OnlyContain()`, `.BeInAscendingOrder()`  
**Exceptions:** `await act.Should().ThrowAsync<TException>().WithMessage()`

## Mocking: FakeItEasy

**Create fakes:** `A.Fake<IInterface>()`  
**Return values:** `A.CallTo(() => fake.Method()).Returns(value)`  
**Throw exceptions:** `A.CallTo(() => fake.Method()).Throws<TException>()`  
**Verify calls:** `A.CallTo(() => fake.Method()).MustHaveHappenedOnceExactly()`  
**Argument matchers:** `A<T>._` (any), `A<T>.That.Matches(predicate)`

## Test Fixtures

**IClassFixture<T>:** Shared setup for tests in a class  
**ICollectionFixture<T>:** Share across multiple test classes  
**Dispose pattern:** Clean up after tests

## Time-Dependent Testing

**TimeProvider** (preferred): Inject for testable time  
**FakeTimeProvider:** Set fixed time for tests  
**Avoid `DateTime.Now`:** Use `TimeProvider.GetUtcNow()`

## Integration Testing

**WebApplicationFactory<TProgram>:** Test ASP.NET Core apps end-to-end  
**Testcontainers:** Docker containers for real databases  
**Test organization:** Mirror src structure

## Background Job Testing

**Test message consumers:** Verify processing logic  
**Mock dependencies:** Use FakeItEasy for external services  
**Event-driven failures:** Assert failure events raised

## Best Practices

**DO:**

- Write tests alongside code
- Test behavior not implementation
- Descriptive names: `Method_Scenario_Result`
- Keep tests isolated
- Prefer real objects over mocks
- AssertionScope for multiple assertions
- Test edge cases (null, empty, boundaries)
- Clean up resources (IDisposable)

**DON'T:**

- Test framework internals
- Over-mock (prefer real implementations)
- Write brittle tests (avoid implementation coupling)
- Share state between tests
- Ignore flaky tests
- Test private methods directly
- Use `Thread.Sleep`
- Catch exceptions in tests
- Use production databases

## Test Organization

**File naming:** `ClassNameTests.cs`  
**Directory:** Mirror src structure  
**Quality gates:** `dotnet build && dotnet test && dotnet format`

## Troubleshooting

**Flaky tests:** Add explicit waits, use TimeProvider, check shared state  
**Slow tests:** Profile, reduce DB/network calls, use in-memory databases, parallelize  
**CI failures:** Check timezones, environment variables, file paths

## References

- [xUnit](https://xunit.net/)
- [FluentAssertions](https://fluentassertions.com/)
- [FakeItEasy](https://fakeiteasy.github.io/)
- [Testcontainers](https://dotnet.testcontainers.org/)
