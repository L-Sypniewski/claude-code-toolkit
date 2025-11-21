---
name: project-planning-templates
description: Templates and structures for project planning, task breakdown, and milestone tracking. Use when planning projects, creating roadmaps, or organizing development work.
---

# Project Planning Templates

This skill provides structured templates for effective project planning and execution.

## Project Plan Structure

### High-Level Project Plan

```markdown
# Project: [Project Name]

## Overview
Brief description of the project and its goals.

## Objectives
- Primary objective 1
- Primary objective 2
- Primary objective 3

## Stakeholders
- **Product Owner**: [Name] - Final decisions, priorities
- **Tech Lead**: [Name] - Technical direction
- **Developers**: [Names] - Implementation
- **QA**: [Name] - Quality assurance

## Timeline
- **Start Date**: [Date]
- **Target Launch**: [Date]
- **Key Milestones**: See milestones section

## Success Metrics
- Metric 1: [How measured, target value]
- Metric 2: [How measured, target value]
- Metric 3: [How measured, target value]
```

### Milestone Planning

```markdown
## Milestones

### Milestone 1: [Name] - [Target Date]
**Goal**: [What this milestone achieves]

**Deliverables**:
- [ ] Deliverable 1
- [ ] Deliverable 2
- [ ] Deliverable 3

**Dependencies**: None / [List dependencies]

**Risks**:
- Risk 1 (Mitigation: ...)
- Risk 2 (Mitigation: ...)

### Milestone 2: [Name] - [Target Date]
**Goal**: [What this milestone achieves]

**Deliverables**:
- [ ] Deliverable 1
- [ ] Deliverable 2

**Dependencies**: Milestone 1

**Risks**:
- Risk 1 (Mitigation: ...)
```

## Task Breakdown (WBS)

### Work Breakdown Structure

```markdown
## Work Breakdown Structure

### 1. Backend Development
#### 1.1 Database Design
- [ ] 1.1.1 Design schema
- [ ] 1.1.2 Create migration scripts
- [ ] 1.1.3 Add seed data

#### 1.2 API Development
- [ ] 1.2.1 User authentication endpoints
- [ ] 1.2.2 CRUD operations for resources
- [ ] 1.2.3 Business logic implementation

#### 1.3 Testing
- [ ] 1.3.1 Unit tests
- [ ] 1.3.2 Integration tests
- [ ] 1.3.3 Load testing

### 2. Frontend Development
#### 2.1 UI Components
- [ ] 2.1.1 Design system setup
- [ ] 2.1.2 Reusable components
- [ ] 2.1.3 Page layouts

#### 2.2 State Management
- [ ] 2.2.1 Setup Redux/Context
- [ ] 2.2.2 API integration
- [ ] 2.2.3 Error handling

### 3. DevOps
#### 3.1 CI/CD Pipeline
- [ ] 3.1.1 Setup GitHub Actions
- [ ] 3.1.2 Automated testing
- [ ] 3.1.3 Deployment scripts
```

### Task Estimation Template

```markdown
## Task: [Task Name]

**Description**: [Detailed task description]

**Estimated Effort**: [Hours/Days]

**Complexity**: [Low/Medium/High]

**Dependencies**: 
- Task ID 1
- Task ID 2

**Subtasks**:
1. [ ] Subtask 1 (2h)
2. [ ] Subtask 2 (4h)
3. [ ] Subtask 3 (1h)

**Acceptance Criteria**:
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Technical Notes**:
[Any technical considerations, libraries needed, etc.]

**Risks**:
- Risk 1: [Description and mitigation]
```

## Sprint Planning

### Sprint Template (Agile/Scrum)

```markdown
# Sprint [Number]: [Date Range]

## Sprint Goal
[What the team aims to accomplish this sprint]

## Capacity
- Developer A: 30 hours
- Developer B: 35 hours
- Developer C: 20 hours (part-time)
**Total**: 85 hours

## Sprint Backlog

### High Priority
- [ ] [USER-123] As a user, I want to... (8h)
- [ ] [USER-124] As a user, I want to... (5h)

### Medium Priority
- [ ] [USER-125] As a user, I want to... (13h)
- [ ] [TECH-45] Refactor authentication module (8h)

### Low Priority (if time permits)
- [ ] [DOC-12] Update API documentation (5h)

## Definition of Done
- [ ] Code complete and reviewed
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] Product owner accepted

## Sprint Retrospective (End of Sprint)

### What went well
- Item 1
- Item 2

### What could be improved
- Item 1
- Item 2

### Action items
- [ ] Action 1 (Owner: [Name])
- [ ] Action 2 (Owner: [Name])
```

## Roadmap Template

### Quarterly Roadmap

```markdown
# Q[N] [Year] Roadmap

## Q[N] Themes
1. **[Theme 1]**: [Description]
2. **[Theme 2]**: [Description]
3. **[Theme 3]**: [Description]

## Month 1: [Month Name]
### Features
- **[Feature Name]** - [Brief description]
  - Effort: [Size]
  - Value: [Impact]
  - Status: 🟢 On Track / 🟡 At Risk / 🔴 Blocked

### Technical Debt
- [Item 1]
- [Item 2]

## Month 2: [Month Name]
[Similar structure]

## Month 3: [Month Name]
[Similar structure]

## Dependencies & Risks

### External Dependencies
- Dependency 1: [Description, owner, status]
- Dependency 2: [Description, owner, status]

### Key Risks
- **Risk 1**: [Description]
  - **Impact**: High/Medium/Low
  - **Likelihood**: High/Medium/Low
  - **Mitigation**: [Plan]
```

## Technical Specification Template

```markdown
# Technical Specification: [Feature Name]

## Background
[Why this feature is needed]

## Goals
- Goal 1
- Goal 2

## Non-Goals
- What this feature will NOT do
- Out of scope items

## Proposed Solution

### Architecture
[High-level architecture diagram or description]

### Data Model
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  ...
);
```

### API Design
```
POST /api/v1/users
Request:
{
  "email": "user@example.com",
  "name": "John Doe"
}

Response: 201 Created
{
  "id": 123,
  "email": "user@example.com",
  "name": "John Doe"
}
```

### Security Considerations
- Authentication: [Method]
- Authorization: [Method]
- Data encryption: [Approach]

### Performance Considerations
- Expected load: [Numbers]
- Caching strategy: [Description]
- Database indexes: [List]

## Alternatives Considered
1. **Alternative 1**: [Description, pros/cons, why not chosen]
2. **Alternative 2**: [Description, pros/cons, why not chosen]

## Implementation Plan

### Phase 1: [Name]
- Task 1
- Task 2

### Phase 2: [Name]
- Task 1
- Task 2

## Testing Strategy
- Unit tests: [Coverage target]
- Integration tests: [Scenarios]
- Load tests: [Performance targets]

## Rollout Plan
1. Internal testing
2. Beta users (10%)
3. Gradual rollout (25%, 50%, 100%)
4. Monitor metrics

## Monitoring & Alerting
- Metrics to track: [List]
- Alerts to set up: [List]
- Dashboard updates: [List]

## Documentation Updates
- [ ] API documentation
- [ ] User guide
- [ ] Internal wiki

## Open Questions
1. Question 1?
2. Question 2?
```

## Risk Management

```markdown
## Risk Register

| ID | Risk | Impact | Likelihood | Mitigation | Owner | Status |
|----|------|--------|------------|------------|-------|--------|
| R1 | Third-party API downtime | High | Medium | Implement retry logic and fallback | Tech Lead | Active |
| R2 | Key developer unavailable | Medium | Low | Knowledge sharing sessions | Manager | Mitigated |
| R3 | Scope creep | High | High | Strict change control process | PM | Active |
```

## Integration Points

Works with:
- Git workflow for branch and PR organization
- `/create_worktree` for parallel work streams
- Development workflow for execution
- Team collaboration and communication
