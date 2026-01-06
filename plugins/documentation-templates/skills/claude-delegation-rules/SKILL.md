---
name: claude-delegation-rules
description: Design principles and patterns for creating multi-agent systems with clear delegation. Use when creating new agents, designing delegation hierarchies, establishing agent boundaries, or planning multi-agent coordination.
---

# Claude Delegation Rules

Design principles and patterns for creating effective multi-agent systems. This skill is for **designing agents** - how to structure them, define their boundaries, and plan their coordination.

## Core Delegation Principles

### 1. Single Responsibility

Each agent should have a clear, focused purpose:

```yaml
# ✅ Good - Clear, focused responsibility
name: code-reviewer
description: Expert code review with comprehensive quality analysis

# ❌ Bad - Too broad
name: developer
description: Does development tasks
```

### 2. Explicit Activation

Agents should know exactly when they should activate:

```yaml
# ✅ Good - Clear activation triggers
description: Senior engineer for implementation tasks. Use PROACTIVELY
for fix, implement, build, create, add, refactor, optimize keywords.

# ❌ Bad - Vague activation
description: Helps with coding
```

### 3. Clear Boundaries

Define what an agent does and doesn't do:

```markdown
## When to Use
- Implementing new features
- Fixing bugs
- Refactoring code

## When NOT to Use
- High-level architecture decisions (use technical-architecture-advisor)
- UI/UX design (use designer agent)
```

## Delegation Patterns

**For detailed patterns**, see [patterns/delegation-patterns.md](patterns/delegation-patterns.md):
- One-Way Handoff
- Consultation Pattern
- Parallel Execution
- Iterative Refinement

## Context Handoff

**For context handoff best practices**, see [guides/context-handoff.md](guides/context-handoff.md).

**Quick reference** - Always include:
- Purpose of delegation
- Current state/progress
- Specific questions or tasks
- Success criteria
- Relevant files or code
- Constraints or requirements

## Delegation Anti-Patterns

**For anti-patterns to avoid**, see [guides/anti-patterns.md](guides/anti-patterns.md).

**Quick reference**:
- ❌ Circular Delegation (infinite loops)
- ❌ Over-Delegation (too much overhead)
- ❌ Under-Context (not enough info)
- ❌ Ambiguous Boundaries (unclear ownership)

## Delegation Decision Tree

```
Does task require specialized expertise?
├─ No → Handle it yourself
└─ Yes → Is the expertise in your domain?
    ├─ Yes → Handle it yourself
    └─ No → Should you learn first or delegate?
        ├─ Learn → Research then handle
        └─ Delegate → Identify appropriate agent
            ↓
        Is agent clearly defined?
        ├─ Yes → Delegate with full context
        └─ No → Create spec for new agent
```

## Agent Configuration Examples

**For configuration examples**, see [examples/agent-configs.md](examples/agent-configs.md).

## Testing Delegation

Verify delegation works correctly:

1. **Clear Activation**: Agent activates for intended scenarios
2. **Proper Context**: Receives necessary information
3. **Appropriate Delegation**: Delegates to correct agents
4. **No Loops**: No circular delegation patterns
5. **Clean Handoffs**: Clear completion and transitions

## Best Practices Checklist

- [ ] Each agent has single, clear responsibility
- [ ] Activation criteria are explicit and testable
- [ ] Delegation triggers are well-defined
- [ ] Context handoff is comprehensive
- [ ] Boundaries between agents are clear
- [ ] Shared state is managed through files
- [ ] Error handling includes delegation paths
- [ ] No circular delegation patterns

## Integration Points

This skill informs:
- Agent specification creation
- AGENTS.md documentation
- Workflow design
- Plugin architecture
- Team collaboration patterns
