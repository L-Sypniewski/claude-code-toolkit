# Database Patterns

Entity Framework Core patterns for feature-based organization.

## DbContext Partial Class Pattern

**Feature-based DbContext organization** using partial classes.

### Structure

- Base DbContext in `src/Database/{ProjectName}DbContext.cs`
- Each feature extends with partial class in `src/Features/{FeatureName}/Database/{ProjectName}DbContext.cs`
- Each feature defines entity configurations in `src/Features/{FeatureName}/Database/{EntityName}Configuration.cs`
- Configurations implement `IEntityTypeConfiguration<TEntity>`
- Register configurations in feature's partial DbContext using `OnModelCreating`

### Example Structure

```
src/
├── Database/
│   └── AppDbContext.cs           // Base partial class
└── Features/
    └── Orders/
        └── Database/
            ├── AppDbContext.cs   // Partial class for Orders
            ├── OrderConfiguration.cs
            └── OrderItemConfiguration.cs
```

### Base DbContext

```csharp
public partial class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        OnModelCreatingPartial(modelBuilder);
    }
}
```

### Feature Partial DbContext

```csharp
public partial class AppDbContext
{
    public DbSet<Order> Orders { get; set; }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfiguration(new OrderConfiguration());
    }
}
```

### Entity Configuration

```csharp
public class OrderConfiguration : IEntityTypeConfiguration<Order>
{
    public void Configure(EntityTypeBuilder<Order> builder)
    {
        builder.ToTable("Orders");
        builder.HasKey(o => o.Id);
        builder.Property(o => o.OrderNumber).IsRequired().HasMaxLength(50);
    }
}
```

## References

- [EF Core Documentation](https://learn.microsoft.com/en-us/ef/core/)
- [Entity Configuration](https://learn.microsoft.com/en-us/ef/core/modeling/)
