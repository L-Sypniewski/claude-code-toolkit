# Blazor Patterns

Patterns for Blazor applications in .NET 10 - Server, WebAssembly, and Static SSR.

## Component Design

**Keep components simple and reusable** (favor dumb/presentational components over smart components).

### Component Principles

- **One responsibility** - Component does one thing well
- **Required parameters** - Use `[Parameter, EditorRequired]` for required props
- **Events over state mutation** - Use `EventCallback<T>` for parent communication
- **Avoid business logic** - Delegate to services
- **Small, focused** - Single clear responsibility

### Parameters & Events

- `[Parameter]` for input
- `[Parameter, EditorRequired]` for required input
- `EventCallback<T>` for raising events to parent
- Avoid `[Parameter] { get; set; }` with logic in setter - prefer immutable parameters

[Blazor Components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/)

## Component Lifecycle

Override lifecycle methods when needed:

- **OnInitialized(Async)** - Component initialization, load initial data
- **OnParametersSet(Async)** - After parameters set (every render if parameters change)
- **OnAfterRender(Async)** - After component rendered, use for JS interop
- **Dispose** - Cleanup (implement `IDisposable` or `IAsyncDisposable`)

**Common patterns:**
- Load data in `OnInitializedAsync`
- React to parameter changes in `OnParametersSetAsync`
- JavaScript interop in `OnAfterRenderAsync` (check `firstRender`)
- Unsubscribe from events in `Dispose`

[Lifecycle](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle)

## State Management

### Cascading Parameters

**Pass data down component tree** without prop drilling.

- Use `<CascadingValue Value="@value">` to provide
- Use `[CascadingParameter]` to receive
- Prefer explicit parameters for direct parent-child communication
- Use for app-wide state (user, theme, culture)

### State Containers

For shared state across components, create state container service:
- Singleton for app-wide state (WebAssembly)
- Scoped for per-circuit state (Server)
- Raise `StateChanged` event for reactivity
- Components subscribe to state changes

[State Management](https://learn.microsoft.com/en-us/aspnet/core/blazor/state-management)

## Localization

**IStringLocalizer<T>** for multi-language support.

### Setup

- Create resource files: `Resources/App.resx`, `Resources/App.{culture}.resx`
- Inject: `@inject IStringLocalizer<App> Localizer`
- Use: `@Localizer["Key"]`
- Configure supported cultures in `Program.cs`

[Localization](https://learn.microsoft.com/en-us/aspnet/core/blazor/globalization-localization)

## Forms & Validation

**EditForm** with model binding for data entry.

### Components

- `<EditForm Model="@model" OnValidSubmit="HandleSubmit">`
- `<DataAnnotationsValidator />` for attribute-based validation
- `<ValidationSummary />` for all errors or `<ValidationMessage For="@(() => model.Property)" />` for specific field
- `OnValidSubmit` when valid, `OnInvalidSubmit` when invalid

### Form Controls

Use built-in input components (`InputText`, `InputNumber`, `InputDate`, `InputCheckbox`, `InputSelect`) for data binding and validation.

[Forms & Validation](https://learn.microsoft.com/en-us/aspnet/core/blazor/forms/)

## Rendering Modes (.NET 8+)

Choose rendering mode based on interactivity needs:

### Static SSR (Server-Side Rendering)

**Default mode.** Fast initial load, no interactivity, SEO-friendly. Use for content-heavy pages.

### Interactive Server

**SignalR connection** to server. Server-side state, low latency, requires persistent connection. Use for low-latency interactive applications with server proximity.

Apply with `@rendermode InteractiveServer` on component or page.

### Interactive WebAssembly

**Client-side execution** in browser. Offline-capable, no server round-trips, larger download. Use for offline scenarios or compute-intensive client-side operations.

Apply with `@rendermode InteractiveWebAssembly` on component or page.

### Interactive Auto

**Server initially, then WebAssembly** after download. Fast first load, then client-side. Most flexible rendering strategy.

Apply with `@rendermode InteractiveAuto` on component or page.

[Render Modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes)

## JavaScript Interop

Use **IJSRuntime** for calling JavaScript from .NET. Inject and call with `await JSRuntime.InvokeAsync<T>("functionName", args)`.

**Best practices:**
- Minimize JS interop (use Blazor components when possible)
- Use `OnAfterRenderAsync` for JS interop
- Check `firstRender` to avoid repeated JS calls
- Dispose JS object references

[JS Interop](https://learn.microsoft.com/en-us/aspnet/core/blazor/javascript-interoperability/)

## Performance

- **Virtualization** - `<Virtualize Items="@items">` for large lists
- **Streaming rendering** - `@attribute [StreamRendering]` for faster perceived load
- **Component disposal** - Clean up subscriptions and timers
- **Avoid re-renders** - Override `ShouldRender()` or use `@key` attribute
- **Lazy loading** - Load assemblies on demand (WebAssembly)

[Performance Best Practices](https://learn.microsoft.com/en-us/aspnet/core/blazor/performance)

## Best Practices

**DO:**
- Keep components small and focused
- Use services for business logic
- Prefer EventCallback over direct state mutation
- Use required parameters for mandatory inputs
- Implement IDisposable for cleanup
- Use appropriate render mode for use case
- Minimize JavaScript interop

**DON'T:**
- Put business logic in components
- Share state through cascading parameters excessively
- Use Server rendering mode for high-scale public internet applications
- Ignore component disposal
- Overuse StateHasChanged()

## References

- [Blazor Documentation](https://learn.microsoft.com/en-us/aspnet/core/blazor/)
- [Components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/)
- [Forms & Validation](https://learn.microsoft.com/en-us/aspnet/core/blazor/forms/)
- [State Management](https://learn.microsoft.com/en-us/aspnet/core/blazor/state-management)
- [Render Modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes)
