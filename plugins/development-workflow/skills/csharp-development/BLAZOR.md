# Blazor Patterns

Patterns for Blazor Server, WebAssembly, and Static SSR applications.

## Component Design

**Keep components simple and reusable** (dumb components)

- `[Parameter, EditorRequired]` for required props
- `EventCallback<T>` for events
- Avoid business logic in components
- One responsibility per component

## Component Lifecycle

**Override lifecycle methods** when needed:

- `OnInitialized(Async)`: Component initialization
- `OnParametersSet(Async)`: After parameters set
- `OnAfterRender(Async)`: After component rendered
- `Dispose`: Cleanup (implement `IDisposable`)

## State Management

**Cascading parameters** for passing data down component tree

- Use `[CascadingParameter]` to receive
- Use `<CascadingValue>` to provide
- Prefer explicit parameters for direct parent-child

## Localization

**IStringLocalizer<T>** for multi-language support

- Resource files: `App.resx`, `App.{culture}.resx`
- Inject: `@inject IStringLocalizer<App> Localizer`
- Use: `@Localizer["Key"]`

## Forms & Validation

**EditForm** with model binding

- `DataAnnotationsValidator` for attribute validation
- `ValidationSummary` or `ValidationMessage<T>` for errors
- `OnValidSubmit` / `OnInvalidSubmit` for handling

## Rendering Modes

**Static SSR**: Fast, no interactivity (default)  
**Interactive Server**: SignalR, server-side state  
**Interactive WebAssembly**: Client-side, offline capable  
**Interactive Auto**: Server then WebAssembly
