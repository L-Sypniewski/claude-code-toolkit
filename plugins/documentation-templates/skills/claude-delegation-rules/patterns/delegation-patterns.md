# Delegation Patterns

Four patterns for effective agent delegation in Claude Code.

## Pattern 1: One-Way Handoff

Agent completes work and hands off to next agent:

```markdown
Senior Engineer
  1. Completes implementation
  2. Documents approach
  3. Hands off to Code Reviewer
     ↓
Code Reviewer
  1. Receives implementation
  2. Performs review
  3. Provides feedback
```

**When to use**: Sequential workflow, clear completion criteria

**Example**:
```markdown
## Delegation Protocol in senior-engineer.md

After implementation:
1. Document changes made
2. Run tests and verify success
3. Create summary for code-reviewer
4. Delegate to code-reviewer with context
5. DO NOT return to implementation unless requested
```

---

## Pattern 2: Consultation Pattern

Agent delegates for advice, then continues work:

```markdown
Senior Engineer
  1. Encounters architectural decision
  2. Delegates to technical-architecture-advisor
  3. Receives architectural guidance
  4. Continues implementation with guidance
```

**When to use**: Specialized knowledge needed, agent continues after consultation

**Example**:
```markdown
## Delegation Protocol in senior-engineer.md

When architectural guidance needed:
1. Identify architectural question
2. Prepare context and specific questions
3. Delegate to technical-architecture-advisor
4. Receive recommendations
5. Incorporate into implementation plan
6. Continue implementation
```

---

## Pattern 3: Parallel Execution

Multiple agents work simultaneously:

```markdown
Orchestrator
  ├─→ Backend Developer (API implementation)
  ├─→ Frontend Developer (UI implementation)
  └─→ Documentation Writer (docs update)
     ↓
  Integration Phase
```

**When to use**: Independent tasks, can run concurrently

**Example**:
```markdown
## Orchestrator Delegation

For feature development:
1. Break down into independent components
2. Delegate backend to senior-engineer-backend
3. Delegate frontend to senior-engineer-frontend
4. Delegate docs to documentation-writer
5. Monitor progress from all agents
6. Coordinate integration when complete
```

---

## Pattern 4: Iterative Refinement

Agent delegates, receives feedback, iterates:

```markdown
Developer
  ↓
Code Reviewer → Feedback
  ↓
Developer (iteration)
  ↓
Code Reviewer → Approval
```

**When to use**: Quality refinement, iterative improvement

---

## Pattern Selection Guide

| Scenario | Pattern |
|----------|---------|
| Sequential workflow | One-Way Handoff |
| Need expert opinion | Consultation |
| Independent parallel tasks | Parallel Execution |
| Quality iteration cycles | Iterative Refinement |
