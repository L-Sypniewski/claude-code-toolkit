# Agent Configuration Examples

Example configurations for different agent types.

## Proactive Agent

Activates automatically based on keywords:

```yaml
---
name: senior-engineer
description: Senior engineer for all development and implementation tasks.
Use PROACTIVELY for fix, implement, build, create, add, refactor, optimize
keywords. Delegates to technical-architecture-advisor for architectural concerns.
---
```

**Characteristics**:
- Activates on common action keywords
- Takes initiative
- Knows when to escalate (architectural concerns)

---

## Reactive Agent

Activates when explicitly requested:

```yaml
---
name: technical-architecture-advisor
description: Architecture evaluation and design guidance. Use when requested
for architectural decisions, system design, or when senior-engineer identifies
architectural concerns requiring expert analysis.
---
```

**Characteristics**:
- Waits for explicit invocation
- Provides specialized expertise
- Advisory role (doesn't implement)

---

## Coordinator Agent

Manages multi-agent workflows:

```yaml
---
name: workflow-orchestrator
description: Coordinates complex multi-step workflows involving multiple agents.
Use when tasks require coordination between specialized agents, parallel work
streams, or complex dependencies.
---
```

**Characteristics**:
- Breaks down complex tasks
- Delegates to specialized agents
- Monitors progress and integration

---

## Reviewer Agent

Quality assurance role:

```yaml
---
name: code-reviewer
description: Expert code review with comprehensive quality analysis. Use after
implementation to validate code quality, security, and best practices.
---
```

**Characteristics**:
- Post-implementation verification
- Provides actionable feedback
- Quality gate enforcement

---

## Configuration Best Practices

### Clear Activation Triggers
```yaml
# ✅ Good - specific keywords
description: Use PROACTIVELY for fix, implement, build...

# ❌ Bad - vague
description: Helps with coding
```

### Defined Boundaries
```yaml
# ✅ Good - clear scope
description: ...Delegates to technical-architecture-advisor for architectural concerns.

# ❌ Bad - no escalation path
description: Does everything
```

### Appropriate Tool Access
```yaml
# ✅ Good - minimal necessary tools
tools: Read, Write, Edit, Bash, Grep, Glob

# ❌ Bad - unnecessary tools for reviewer
tools: Read, Write, Edit, Bash, Grep, Glob, AskUserQuestion, Task, ...
```
