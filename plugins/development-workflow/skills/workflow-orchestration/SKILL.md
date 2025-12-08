---
name: workflow-orchestration
description: Coordinate multi-step workflows involving multiple agents, commands, and validation points. Use when managing complex development workflows that require coordination between different specialized agents.
---

# Workflow Orchestration

This skill provides patterns for orchestrating complex workflows with multiple agents and validation points.

## Workflow Patterns

### Sequential Workflow

For workflows where each step depends on the previous one:

```markdown
1. Initial Analysis → 2. Planning → 3. Implementation → 4. Validation
```

**When to use**: Linear dependencies, each step builds on previous results

### Parallel Workflow

For independent tasks that can run concurrently:

```markdown
        ┌→ Task A ┐
Start → ├→ Task B ├→ Merge → Continue
        └→ Task C ┘
```

**When to use**: Independent components, can be developed/tested separately

### Iterative Workflow

For workflows requiring refinement:

```markdown
Plan → Implement → Review → [Refine Plan] → Loop until criteria met
```

**When to use**: Exploratory tasks, requirements evolve during execution

## Agent Coordination

### Handoff Pattern

Clear transitions between specialized agents:

```markdown
1. github-issue-analyzer: Extract requirements
2. prp-generator: Create structured plan
3. executor: Implement solution
4. Code review (external): Validate quality
```

**Handoff checklist**:
- [ ] Previous agent completed all deliverables
- [ ] Next agent has required context
- [ ] Success criteria clearly defined

### Delegation Pattern

Main orchestrator delegates to specialists:

```markdown
Orchestrator
    ├→ Technical research → Report findings
    ├→ Implementation → Deliver code
    └→ Documentation → Update docs
```

**Delegation checklist**:
- [ ] Clear scope and boundaries for each agent
- [ ] Expected outputs defined
- [ ] Time/resource constraints communicated

## Progress Tracking

Use structured tracking for visibility:

```markdown
## Workflow Status

### Phase 1: Analysis ✅
- [x] GitHub issue analyzed
- [x] Requirements extracted
- [x] PRP generated

### Phase 2: Implementation 🔄
- [x] Core functionality implemented
- [ ] Edge cases handled
- [ ] Tests written

### Phase 3: Validation ⏸️
- [ ] Code review
- [ ] Integration tests
- [ ] Documentation updated
```

Symbols: ✅ Complete | 🔄 In Progress | ⏸️ Blocked | ❌ Failed

## Error Handling

Define fallback strategies:

```markdown
## Contingency Plans

### If implementation fails:
1. Rollback to previous stable state
2. Analyze failure root cause
3. Adjust plan based on learnings
4. Retry with updated approach

### If validation fails:
1. Document specific failures
2. Create targeted fixes
3. Re-run validation subset
4. Escalate if pattern of failures
```

## Workflow Templates

### Bug Fix Workflow

```markdown
1. Issue Analysis → Reproduce bug
2. Root Cause → Identify problem
3. Fix Design → Plan solution
4. Implementation → Apply fix
5. Testing → Verify resolution
6. Regression Check → Ensure no side effects
```

### Feature Development Workflow

```markdown
1. Requirements → Define scope
2. Design Review → Architecture validation
3. Prototype → Quick proof of concept
4. Implementation → Full feature build
5. Testing → Comprehensive validation
6. Documentation → User-facing docs
7. Deployment → Staged rollout
```


