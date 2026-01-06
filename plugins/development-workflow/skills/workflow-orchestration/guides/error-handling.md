# Error Handling Guide

Strategies for handling failures during workflow execution.

## Contingency Plan Template

```markdown
## Contingency Plans

### If [phase] fails:
1. [Immediate action]
2. [Root cause analysis]
3. [Recovery strategy]
4. [Retry or escalate]
```

## Common Failure Scenarios

### Implementation Failure

```markdown
### If implementation fails:
1. Rollback to previous stable state
2. Analyze failure root cause
3. Adjust plan based on learnings
4. Retry with updated approach
```

**Root causes to check**:
- Missing dependencies
- Incorrect assumptions about existing code
- Scope creep during implementation

### Validation Failure

```markdown
### If validation fails:
1. Document specific failures
2. Create targeted fixes
3. Re-run validation subset
4. Escalate if pattern of failures
```

**Common validation failures**:
- Test failures (unit, integration)
- Linting/formatting issues
- Build errors
- Performance regressions

### External Dependency Failure

```markdown
### If external dependency unavailable:
1. Document the dependency and its purpose
2. Check for alternatives or fallbacks
3. Implement mock/stub if possible
4. Pause workflow and notify stakeholders
```

## Recovery Strategies

### Rollback
When to use: Implementation broke existing functionality
```markdown
1. git stash or git reset to known good state
2. Document what was attempted
3. Analyze why it failed
4. Plan smaller incremental approach
```

### Retry with Adjustment
When to use: Failure was due to correctable issue
```markdown
1. Identify specific failure point
2. Make targeted fix
3. Re-run from failed step (not from beginning)
4. Verify fix resolved issue
```

### Escalation
When to use: Issue beyond current scope or expertise
```markdown
1. Document everything attempted
2. Clearly state the blocker
3. Propose potential solutions if any
4. Hand off to appropriate agent or human
```

## Error Documentation

Always document failures for future reference:

```markdown
## Error Log

### [Date/Time] - [Phase] - [Error Type]
**What happened**: [Description]
**Root cause**: [Analysis]
**Resolution**: [What fixed it]
**Prevention**: [How to avoid in future]
```
