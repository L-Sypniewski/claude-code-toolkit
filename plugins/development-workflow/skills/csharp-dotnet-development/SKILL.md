---
name: csharp-dotnet-development
description: C# and .NET development best practices, patterns, conventions, and guidelines. Use when developing, reviewing, or refactoring .NET applications including ASP.NET Core, Entity Framework, and C# code.
license: MIT
metadata:
  author: Claude Code Toolkit
  version: "1.0.0"
  category: development
---

# C# .NET Development Skill

This skill provides comprehensive guidance for C# and .NET development, covering best practices, design patterns, coding conventions, and framework-specific guidelines.

## Core Principles

### SOLID Principles

- **Single Responsibility**: Each class should have one reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable for their base types
- **Interface Segregation**: Many client-specific interfaces are better than one general-purpose interface
- **Dependency Inversion**: Depend on abstractions, not concretions

### Clean Code Practices

- Use meaningful, descriptive names for classes, methods, and variables
- Keep methods short and focused (typically < 20 lines)
- Favor composition over inheritance
- Write self-documenting code; comments explain "why", not "what"
- Follow the principle of least surprise

## Naming Conventions

### C# Standard Conventions

```csharp
// PascalCase for: classes, interfaces, methods, properties, constants
public class UserService { }
public interface IRepository { }
public void ProcessOrder() { }
public string FirstName { get; set; }
public const int MaxRetries = 3;

// camelCase for: local variables, method parameters, private fields (with _prefix)
private readonly ILogger _logger;
public void ValidateUser(string userName) {
    int retryCount = 0;
}

// UPPER_CASE for: enum values (optional, PascalCase also acceptable)
public enum Status {
    Pending,
    Approved,
    Rejected
}

// Async methods should end with "Async"
public async Task<User> GetUserAsync(int userId) { }
```

### File and Project Structure

```
Solution.sln
├── src/
│   ├── ProjectName.Domain/         # Entities, value objects, domain logic
│   ├── ProjectName.Application/    # Use cases, DTOs, interfaces
│   ├── ProjectName.Infrastructure/ # Data access, external services
│   └── ProjectName.Api/            # Web API, controllers
├── tests/
│   ├── ProjectName.Domain.Tests/
│   ├── ProjectName.Application.Tests/
│   └── ProjectName.Api.Tests/
└── docs/
```

## Language Features & Best Practices

### Modern C# Features (C# 10+)

```csharp
// Null-coalescing and null-conditional operators
string name = user?.Name ?? "Unknown";

// Pattern matching
if (result is { Success: true, Data: var data }) {
    ProcessData(data);
}

// Records for immutable data
public record UserDto(int Id, string Name, string Email);

// Init-only properties
public class Configuration {
    public string ApiKey { get; init; }
}

// File-scoped namespaces (C# 10+)
namespace MyApp.Services;

// Global using directives (in separate file)
global using System;
global using System.Collections.Generic;
global using System.Linq;
```

### Async/Await Best Practices

```csharp
// ✅ Good: Use async/await properly
public async Task<User> GetUserAsync(int id) {
    return await _repository.GetByIdAsync(id);
}

// ❌ Bad: Async void (except event handlers)
public async void ProcessData() { } // DON'T DO THIS

// ✅ Good: ConfigureAwait(false) in libraries
public async Task<Data> GetDataAsync() {
    return await _httpClient.GetAsync(url).ConfigureAwait(false);
}

// ✅ Good: Parallel operations when possible
var tasks = ids.Select(id => GetUserAsync(id));
var users = await Task.WhenAll(tasks);
```

### Exception Handling

```csharp
// ✅ Good: Specific exceptions, meaningful messages
public class UserNotFoundException : Exception {
    public UserNotFoundException(int userId) 
        : base($"User with ID {userId} was not found.") { }
}

// ✅ Good: Use try-catch appropriately
try {
    await ProcessOrderAsync(order);
} catch (InvalidOperationException ex) {
    _logger.LogError(ex, "Failed to process order {OrderId}", order.Id);
    throw; // Re-throw to preserve stack trace
}

// ❌ Bad: Empty catch blocks or catching everything
try {
    await DoSomethingAsync();
} catch { } // DON'T DO THIS
```

## Dependency Injection

### ASP.NET Core DI Registration

```csharp
// Startup.cs or Program.cs
services.AddTransient<IEmailService, EmailService>();  // New instance each time
services.AddScoped<IOrderService, OrderService>();     // One per request
services.AddSingleton<IConfiguration, Configuration>(); // One for lifetime

// Use constructor injection
public class OrderController : ControllerBase {
    private readonly IOrderService _orderService;
    private readonly ILogger<OrderController> _logger;

    public OrderController(IOrderService orderService, ILogger<OrderController> logger) {
        _orderService = orderService;
        _logger = logger;
    }
}
```

## Entity Framework Core Best Practices

### DbContext Configuration

```csharp
public class ApplicationDbContext : DbContext {
    public DbSet<User> Users { get; set; }
    public DbSet<Order> Orders { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        // Use FluentAPI for complex configurations
        modelBuilder.Entity<User>(entity => {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.Email)
                .IsRequired()
                .HasMaxLength(256);
            entity.HasIndex(e => e.Email).IsUnique();
        });

        // Apply configurations from separate files
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(ApplicationDbContext).Assembly);
    }
}
```

### Query Best Practices

```csharp
// ✅ Good: Use AsNoTracking for read-only queries
var users = await _context.Users
    .AsNoTracking()
    .Where(u => u.IsActive)
    .ToListAsync();

// ✅ Good: Explicit loading with Include
var orders = await _context.Orders
    .Include(o => o.Customer)
    .Include(o => o.OrderItems)
        .ThenInclude(oi => oi.Product)
    .ToListAsync();

// ✅ Good: Use projections to reduce data transfer
var userDtos = await _context.Users
    .Select(u => new UserDto(u.Id, u.Name, u.Email))
    .ToListAsync();

// ❌ Bad: N+1 query problem
foreach (var order in orders) {
    var customer = await _context.Customers.FindAsync(order.CustomerId); // DON'T
}
```

## ASP.NET Core API Development

### Controller Best Practices

```csharp
[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase {
    private readonly IUserService _userService;

    public UsersController(IUserService userService) {
        _userService = userService;
    }

    // ✅ Good: Use proper HTTP verbs and status codes
    [HttpGet("{id}")]
    [ProducesResponseType(typeof(UserDto), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<ActionResult<UserDto>> GetUser(int id) {
        var user = await _userService.GetByIdAsync(id);
        return user != null ? Ok(user) : NotFound();
    }

    [HttpPost]
    [ProducesResponseType(typeof(UserDto), StatusCodes.Status201Created)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<UserDto>> CreateUser([FromBody] CreateUserRequest request) {
        if (!ModelState.IsValid)
            return BadRequest(ModelState);

        var user = await _userService.CreateAsync(request);
        return CreatedAtAction(nameof(GetUser), new { id = user.Id }, user);
    }
}
```

### Validation and Error Handling

```csharp
// Use FluentValidation for complex validation
public class CreateUserRequestValidator : AbstractValidator<CreateUserRequest> {
    public CreateUserRequestValidator() {
        RuleFor(x => x.Email)
            .NotEmpty()
            .EmailAddress()
            .MaximumLength(256);

        RuleFor(x => x.Password)
            .NotEmpty()
            .MinimumLength(8)
            .Matches(@"[A-Z]").WithMessage("Password must contain uppercase")
            .Matches(@"[0-9]").WithMessage("Password must contain digit");
    }
}

// Global exception handler middleware
public class ExceptionHandlingMiddleware {
    private readonly RequestDelegate _next;
    private readonly ILogger<ExceptionHandlingMiddleware> _logger;

    public async Task InvokeAsync(HttpContext context) {
        try {
            await _next(context);
        } catch (Exception ex) {
            _logger.LogError(ex, "Unhandled exception occurred");
            await HandleExceptionAsync(context, ex);
        }
    }

    private static Task HandleExceptionAsync(HttpContext context, Exception exception) {
        context.Response.ContentType = "application/json";
        context.Response.StatusCode = exception switch {
            NotFoundException => StatusCodes.Status404NotFound,
            ValidationException => StatusCodes.Status400BadRequest,
            UnauthorizedException => StatusCodes.Status401Unauthorized,
            _ => StatusCodes.Status500InternalServerError
        };

        return context.Response.WriteAsJsonAsync(new {
            error = exception.Message,
            statusCode = context.Response.StatusCode
        });
    }
}
```

## Testing Best Practices

### Unit Testing with xUnit

```csharp
public class UserServiceTests {
    private readonly Mock<IUserRepository> _mockRepository;
    private readonly UserService _sut; // System Under Test

    public UserServiceTests() {
        _mockRepository = new Mock<IUserRepository>();
        _sut = new UserService(_mockRepository.Object);
    }

    [Fact]
    public async Task GetByIdAsync_WhenUserExists_ReturnsUser() {
        // Arrange
        var expectedUser = new User { Id = 1, Name = "John" };
        _mockRepository.Setup(r => r.GetByIdAsync(1))
            .ReturnsAsync(expectedUser);

        // Act
        var result = await _sut.GetByIdAsync(1);

        // Assert
        Assert.NotNull(result);
        Assert.Equal(expectedUser.Id, result.Id);
        Assert.Equal(expectedUser.Name, result.Name);
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("   ")]
    public async Task CreateAsync_WhenNameIsInvalid_ThrowsValidationException(string invalidName) {
        // Arrange
        var request = new CreateUserRequest { Name = invalidName };

        // Act & Assert
        await Assert.ThrowsAsync<ValidationException>(() => _sut.CreateAsync(request));
    }
}
```

### Integration Testing

```csharp
public class UsersControllerIntegrationTests : IClassFixture<WebApplicationFactory<Program>> {
    private readonly HttpClient _client;
    private readonly WebApplicationFactory<Program> _factory;

    public UsersControllerIntegrationTests(WebApplicationFactory<Program> factory) {
        _factory = factory;
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task GetUser_ReturnsSuccessStatusCode() {
        // Act
        var response = await _client.GetAsync("/api/users/1");

        // Assert
        response.EnsureSuccessStatusCode();
        var content = await response.Content.ReadAsStringAsync();
        Assert.NotEmpty(content);
    }
}
```

## Security Best Practices

### Authentication & Authorization

```csharp
// Use built-in authentication
services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => {
        options.TokenValidationParameters = new TokenValidationParameters {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = configuration["Jwt:Issuer"],
            ValidAudience = configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(configuration["Jwt:Key"]))
        };
    });

// Use authorization policies
services.AddAuthorization(options => {
    options.AddPolicy("AdminOnly", policy => 
        policy.RequireRole("Admin"));
    options.AddPolicy("CanEditUser", policy => 
        policy.RequireClaim("Permission", "User.Edit"));
});

// Apply to controllers/actions
[Authorize(Policy = "AdminOnly")]
public class AdminController : ControllerBase { }
```

### Input Validation & Sanitization

```csharp
// ✅ Good: Validate and sanitize all inputs
public class CreateUserRequest {
    [Required]
    [StringLength(100, MinimumLength = 2)]
    [RegularExpression(@"^[a-zA-Z\s]+$")]
    public string Name { get; set; }

    [Required]
    [EmailAddress]
    public string Email { get; set; }
}

// ✅ Good: Use parameterized queries (EF Core does this automatically)
var users = await _context.Users
    .Where(u => u.Email == email) // Safe - parameterized
    .ToListAsync();

// ❌ Bad: String interpolation in raw SQL
var query = $"SELECT * FROM Users WHERE Email = '{email}'"; // SQL INJECTION RISK!
```

### Secrets Management

```csharp
// ✅ Good: Use User Secrets in development
// dotnet user-secrets init
// dotnet user-secrets set "ApiKey" "your-api-key"

// ✅ Good: Use environment variables or Azure Key Vault in production
var apiKey = configuration["ApiKey"];
var connectionString = configuration.GetConnectionString("DefaultConnection");

// ❌ Bad: Hardcoded secrets
private const string ApiKey = "hardcoded-key-12345"; // DON'T DO THIS
```

## Performance Optimization

### Memory Management

```csharp
// ✅ Good: Use Span<T> and Memory<T> for performance-critical code
public void ProcessData(ReadOnlySpan<byte> data) {
    // No heap allocations
}

// ✅ Good: Use ArrayPool for temporary arrays
var pool = ArrayPool<byte>.Shared;
byte[] buffer = pool.Rent(1024);
try {
    // Use buffer
} finally {
    pool.Return(buffer);
}

// ✅ Good: Use StringBuilder for string concatenation
var sb = new StringBuilder();
foreach (var item in items) {
    sb.Append(item).Append(",");
}
```

### Caching

```csharp
// Use IMemoryCache for in-memory caching
services.AddMemoryCache();

public class UserService {
    private readonly IMemoryCache _cache;

    public async Task<User> GetUserAsync(int id) {
        return await _cache.GetOrCreateAsync($"user:{id}", async entry => {
            entry.SetAbsoluteExpiration(TimeSpan.FromMinutes(10));
            return await _repository.GetByIdAsync(id);
        });
    }
}

// Use IDistributedCache for distributed caching (Redis)
services.AddStackExchangeRedisCache(options => {
    options.Configuration = configuration["Redis:ConnectionString"];
});
```

## Logging

### Structured Logging with Serilog

```csharp
// Configure Serilog
Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Information()
    .WriteTo.Console()
    .WriteTo.File("logs/app-.log", rollingInterval: RollingInterval.Day)
    .CreateLogger();

builder.Host.UseSerilog();

// Use structured logging
_logger.LogInformation("User {UserId} created order {OrderId}", userId, orderId);
_logger.LogWarning("Failed login attempt for user {Email}", email);
_logger.LogError(ex, "Failed to process payment for order {OrderId}", orderId);
```

## Common Pitfalls to Avoid

### ❌ Don'ts

1. **Don't use `var` excessively when type is not obvious**
   ```csharp
   var result = Calculate(); // What type is this?
   ```

2. **Don't ignore disposal of IDisposable objects**
   ```csharp
   // ❌ Bad
   var stream = File.OpenRead("file.txt");
   
   // ✅ Good
   using var stream = File.OpenRead("file.txt");
   ```

3. **Don't block async code**
   ```csharp
   // ❌ Bad - can cause deadlocks
   var result = SomeAsyncMethod().Result;
   
   // ✅ Good
   var result = await SomeAsyncMethod();
   ```

4. **Don't use exceptions for control flow**
   ```csharp
   // ❌ Bad
   try {
       var user = GetUser(id);
   } catch {
       // User not found
   }
   
   // ✅ Good
   var user = TryGetUser(id, out var result) ? result : null;
   ```

5. **Don't mix business logic in controllers**
   ```csharp
   // ❌ Bad - controller contains business logic
   [HttpPost]
   public async Task<IActionResult> CreateOrder(OrderDto dto) {
       if (dto.Total < 0) return BadRequest();
       var order = new Order { /* map fields */ };
       await _context.SaveChangesAsync();
       return Ok();
   }
   
   // ✅ Good - delegate to service layer
   [HttpPost]
   public async Task<IActionResult> CreateOrder(OrderDto dto) {
       var result = await _orderService.CreateOrderAsync(dto);
       return result.IsSuccess ? Ok(result.Data) : BadRequest(result.Error);
   }
   ```

## Resources & Tools

### Essential NuGet Packages

- **FluentValidation**: Complex validation rules
- **AutoMapper**: Object-to-object mapping
- **Polly**: Resilience and transient fault handling
- **MediatR**: CQRS and mediator pattern implementation
- **Serilog**: Structured logging
- **Moq / NSubstitute**: Mocking frameworks for testing
- **xUnit / NUnit**: Testing frameworks
- **Swagger/Swashbuckle**: API documentation

### Code Quality Tools

- **dotnet format**: Code formatting
- **SonarAnalyzer.CSharp**: Static code analysis
- **StyleCop.Analyzers**: Style and consistency checking
- **Roslynator**: Code analysis and refactoring

## Integration with Plugin

This skill works standalone and can be referenced when:
- Implementing new C# / .NET features
- Reviewing .NET code for best practices
- Refactoring .NET applications
- Setting up new .NET projects
- Troubleshooting .NET issues
