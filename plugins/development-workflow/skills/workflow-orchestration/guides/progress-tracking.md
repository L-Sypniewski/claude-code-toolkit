# Progress Tracking Guide

Structured tracking for workflow visibility and status management.

## Status Symbols

| Symbol | Meaning | Use When |
|--------|---------|----------|
| ✅ | Complete | Phase fully finished, all deliverables met |
| 🔄 | In Progress | Currently being worked on |
| ⏸️ | Blocked | Waiting on dependency or external input |
| ❌ | Failed | Encountered error, needs intervention |

## Workflow Status Template

```markdown
## Workflow Status

### Phase 1: Analysis ✅
- [x] Requirements gathered
- [x] Scope defined
- [x] Plan created

### Phase 2: Implementation 🔄
- [x] Core functionality implemented
- [ ] Edge cases handled
- [ ] Tests written

### Phase 3: Validation ⏸️
- [ ] Code review
- [ ] Integration tests
- [ ] Documentation updated
```

## Best Practices

### Update Frequently
- Mark tasks complete immediately when done
- Update status symbols as phases transition
- Add notes for blocked items explaining the blocker

### Be Specific
- Break phases into checkable items
- Each item should be verifiable
- Avoid vague items like "finish implementation"

### Track Blockers
When a phase is blocked:
```markdown
### Phase 3: Validation ⏸️
**Blocked by**: Waiting for API credentials from team lead
**Since**: 2024-01-15
**Action needed**: Follow up if not resolved by EOD

- [ ] Integration tests (blocked)
- [ ] Code review
```

## Multi-Agent Progress

When multiple agents work in parallel:

```markdown
## Parallel Execution Status

### Backend (senior-engineer) 🔄
- [x] API endpoints created
- [ ] Database migrations

### Frontend (frontend-dev) ✅
- [x] UI components built
- [x] State management

### Integration ⏸️
**Waiting for**: Backend API completion
- [ ] Connect frontend to backend
- [ ] End-to-end testing
```
