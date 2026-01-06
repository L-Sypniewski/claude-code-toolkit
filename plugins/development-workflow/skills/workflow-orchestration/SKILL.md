---
name: workflow-orchestration
description: Execute and manage multi-step workflows with progress tracking, error handling, and validation. Use when running complex development workflows, coordinating multi-phase tasks, or managing workflow state and recovery.
---

# Workflow Orchestration

Execute and manage complex workflows with multiple phases and validation points.

## Core Execution Principles

### 1. Phase-Based Execution

Break workflows into distinct phases with clear boundaries:

```markdown
Phase 1: Analysis → Phase 2: Implementation → Phase 3: Validation
```

Each phase should have:
- Clear entry criteria (what must be true to start)
- Defined deliverables (what it produces)
- Exit criteria (when it's complete)

### 2. Visible Progress

Track progress explicitly so status is always clear:

```markdown
### Phase 2: Implementation 🔄
- [x] Core functionality
- [ ] Edge cases
- [ ] Tests
```

Symbols: ✅ Complete | 🔄 In Progress | ⏸️ Blocked | ❌ Failed

### 3. Graceful Recovery

Every workflow should handle failures:
- Define contingency plans before starting
- Know when to rollback vs. retry vs. escalate
- Document failures for future learning

## Workflow Patterns

### Sequential
```
Step 1 → Step 2 → Step 3 → Done
```
**Use when**: Each step depends on the previous step's output

### Parallel
```
     ┌→ Task A ┐
Start├→ Task B ├→ Merge → Continue
     └→ Task C ┘
```
**Use when**: Tasks are independent and can run concurrently

### Iterative
```
Plan → Execute → Review → [Refine] → Loop until done
```
**Use when**: Requirements evolve or refinement cycles needed

## Progress Tracking

**For detailed tracking patterns**, see [guides/progress-tracking.md](guides/progress-tracking.md).

**Quick reference** - Status template:
```markdown
## Workflow Status

### Phase 1: [Name] ✅
- [x] Task completed

### Phase 2: [Name] 🔄
- [x] Task done
- [ ] Task pending
```

## Error Handling

**For error handling strategies**, see [guides/error-handling.md](guides/error-handling.md).

**Quick reference** - When failures occur:
1. **Rollback**: If implementation broke existing functionality
2. **Retry**: If failure was due to correctable issue
3. **Escalate**: If issue is beyond current scope

## Workflow Templates

**For ready-to-use templates**, see [guides/workflow-templates.md](guides/workflow-templates.md).

Available templates:
- Bug Fix Workflow
- Feature Development Workflow
- Refactoring Workflow
- Investigation Workflow

## Best Practices Checklist

- [ ] Workflow broken into clear phases
- [ ] Each phase has entry/exit criteria
- [ ] Progress tracked with status symbols
- [ ] Contingency plans defined
- [ ] Deliverables specified for each phase
- [ ] Recovery strategy known before starting
