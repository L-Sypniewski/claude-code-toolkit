# Context Handoff Guide

Best practices for passing context between agents during delegation.

## What to Pass

**Always include**:
- Purpose of delegation
- Current state/progress
- Specific questions or tasks
- Success criteria
- Relevant files or code
- Constraints or requirements

## Example Handoff Message

```markdown
@technical-architecture-advisor

I need architectural guidance for implementing a caching layer.

**Context**:
- Current system: REST API with PostgreSQL
- Performance issue: N+1 queries on user dashboard
- Load: 10k requests/hour, growing 20% monthly

**Specific Questions**:
1. Should we use Redis or in-memory caching?
2. What caching strategy (write-through, write-back)?
3. How to handle cache invalidation?

**Constraints**:
- Must support horizontal scaling
- Budget: Can add $200/month infrastructure
- Timeline: 2 weeks

**Files**:
- src/api/users.js (current implementation)
- src/database/queries.js (problematic queries)

**Success Criteria**:
- Dashboard load time < 500ms
- Cache hit rate > 80%
- Zero data inconsistencies
```

## What NOT to Pass

- Unnecessary history
- Unrelated code
- Implementation details (unless relevant)
- Personal opinions without context
- Ambiguous requirements

## Shared Context Files

Use shared files for multi-agent workflows:

```markdown
# .plans/feature-implementation.md

## Status: In Progress

## Architecture Review
**Owner**: technical-architecture-advisor
**Status**: ✅ Complete
**Outcome**: Use microservices pattern, see details below

## Implementation
**Owner**: senior-engineer
**Status**: 🔄 In Progress (60%)
**Next Steps**: Complete API endpoints

## Testing
**Owner**: QA agent
**Status**: ⏸️ Waiting for implementation
```

## Communication Protocol

**Starting Delegation**:
```markdown
@agent-name

**Task**: [Clear, specific task]
**Context**: [Essential background]
**Deliverables**: [What you need back]
**Timeline**: [If applicable]
```

**Completing Delegation**:
```markdown
@delegating-agent

**Status**: Complete
**Summary**: [What was done]
**Deliverables**: [Links to files, decisions]
**Next Steps**: [What should happen next]
**Blockers**: [Any issues encountered]
```
