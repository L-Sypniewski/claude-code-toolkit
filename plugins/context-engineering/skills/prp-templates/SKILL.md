---
name: prp-templates
description: Comprehensive PRP (Prompt-Response-Plan) templates and patterns for systematic problem-solving and structured workflow execution
author: Claude Code Toolkit
---

# PRP Templates and Patterns

This skill provides comprehensive PRP templates and structured patterns that are automatically activated during PRP generation and workflow orchestration.

## Purpose

Automatically activated when:
- Generating new PRPs
- Structuring problem-solving workflows
- Creating systematic execution plans
- Orchestrating multi-step processes
- Analyzing complex requirements

## What is a PRP?

A **PRP (Prompt-Response-Plan)** is a structured framework for:
- Breaking down complex problems into manageable steps
- Creating clear execution sequences
- Tracking progress systematically
- Ensuring comprehensive problem-solving
- Facilitating collaboration between agents

## PRP Structure Components

### 1. Problem Statement

**Purpose:** Clearly define what needs to be solved

**Template:**
```markdown
## Problem Statement

### Context
[Background information and current situation]

### Objective
[What success looks like - specific, measurable goals]

### Constraints
- [Technical constraints]
- [Time constraints]
- [Resource constraints]
- [Dependencies]

### Scope
**In Scope:**
- [What is included]

**Out of Scope:**
- [What is explicitly excluded]
```

### 2. Analysis Section

**Purpose:** Understand the problem deeply before planning

**Template:**
```markdown
## Analysis

### Current State
[Detailed description of current implementation/situation]

### Requirements
**Functional Requirements:**
1. [Requirement 1]
2. [Requirement 2]

**Non-Functional Requirements:**
1. [Performance requirements]
2. [Security requirements]
3. [Scalability requirements]

### Dependencies
**Technical Dependencies:**
- [Libraries, frameworks, services]

**Process Dependencies:**
- [Other tasks, teams, approvals]

### Risk Assessment
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| [Risk description] | High/Med/Low | High/Med/Low | [Strategy] |
```

### 3. Approach Section

**Purpose:** Define the strategy and methodology

**Template:**
```markdown
## Approach

### Strategy
[Overall approach and methodology - why this approach was chosen]

### Alternative Approaches Considered
1. **[Approach A]**
   - Pros: [...]
   - Cons: [...]
   - Why not chosen: [...]

2. **[Approach B]**
   - Pros: [...]
   - Cons: [...]
   - Why not chosen: [...]

### Architecture/Design Decisions
[Key architectural or design decisions and their rationale]

### Technology Stack
- [Technologies to be used and why]
```

### 4. Execution Plan

**Purpose:** Step-by-step implementation sequence

**Template:**
```markdown
## Execution Plan

### Phase 1: [Phase Name]
**Objective:** [What this phase accomplishes]
**Duration:** [Estimated time]

- [ ] Step 1.1: [Specific task]
  - Expected outcome: [...]
  - Verification: [How to verify completion]
  
- [ ] Step 1.2: [Specific task]
  - Expected outcome: [...]
  - Verification: [...]

### Phase 2: [Phase Name]
[Similar structure]

### Phase 3: [Phase Name]
[Similar structure]

### Critical Path
[Steps that cannot be delayed without delaying the entire project]

### Parallel Tasks
[Tasks that can be executed simultaneously]
```

### 5. Testing Strategy

**Purpose:** Ensure quality and correctness

**Template:**
```markdown
## Testing Strategy

### Unit Testing
- [ ] [Component 1 tests]
- [ ] [Component 2 tests]

### Integration Testing
- [ ] [Integration point 1]
- [ ] [Integration point 2]

### End-to-End Testing
- [ ] [User workflow 1]
- [ ] [User workflow 2]

### Test Data
[Required test data and how to generate it]

### Test Environment
[Environment setup requirements]

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

### 6. Monitoring and Success Metrics

**Purpose:** Track progress and measure success

**Template:**
```markdown
## Monitoring and Success Metrics

### Progress Tracking
- [Metric 1]: [Target]
- [Metric 2]: [Target]

### Success Criteria
**Must Have:**
- [ ] [Critical requirement 1]
- [ ] [Critical requirement 2]

**Should Have:**
- [ ] [Important requirement 1]
- [ ] [Important requirement 2]

**Nice to Have:**
- [ ] [Optional enhancement 1]

### KPIs
- [Performance metric]: [Target value]
- [Quality metric]: [Target value]
- [User satisfaction metric]: [Target value]
```

### 7. Rollback Plan

**Purpose:** Handle failures gracefully

**Template:**
```markdown
## Rollback Plan

### Rollback Triggers
- [Condition 1 that would trigger rollback]
- [Condition 2 that would trigger rollback]

### Rollback Steps
1. [Immediate action]
2. [Data restoration if needed]
3. [Service restoration]
4. [Verification steps]

### Data Backup Strategy
[How data will be backed up before changes]

### Communication Plan
[Who to notify and when]
```

## PRP Types and Templates

### 1. Feature Implementation PRP

**Use Case:** Implementing a new feature from scratch

**Key Sections:**
- Detailed feature requirements
- User stories and acceptance criteria
- Architecture and design
- Phase-by-phase implementation
- Testing and validation
- Documentation requirements

### 2. Bug Fix PRP

**Use Case:** Systematic bug investigation and resolution

**Key Sections:**
- Bug description and reproduction steps
- Root cause analysis
- Impact assessment
- Fix approach and alternatives
- Testing strategy to prevent regression
- Deployment and monitoring

### 3. Refactoring PRP

**Use Case:** Code refactoring or technical debt reduction

**Key Sections:**
- Current code analysis
- Technical debt assessment
- Refactoring goals and benefits
- Risk analysis
- Incremental refactoring steps
- Validation and performance testing

### 4. Investigation PRP

**Use Case:** Problem investigation and research

**Key Sections:**
- Investigation objectives
- Hypothesis to test
- Data collection methods
- Analysis framework
- Expected findings
- Action items based on findings

### 5. Migration PRP

**Use Case:** System or data migration projects

**Key Sections:**
- Current state assessment
- Target state definition
- Migration strategy (big bang vs. incremental)
- Data mapping and transformation
- Rollback and contingency plans
- Validation criteria

### 6. Integration PRP

**Use Case:** Integrating with external systems or APIs

**Key Sections:**
- Integration requirements
- API contract definition
- Authentication and security
- Error handling strategy
- Rate limiting and resilience
- Testing with mock services

## PRP Best Practices

### Planning Phase

**Do:**
- Start with clear problem definition
- Involve stakeholders early
- Consider multiple approaches
- Identify dependencies upfront
- Plan for failure scenarios
- Define measurable success criteria

**Don't:**
- Skip the analysis phase
- Make assumptions without validation
- Ignore non-functional requirements
- Underestimate complexity
- Forget about rollback plans

### Execution Phase

**Do:**
- Follow the plan but adapt as needed
- Update PRP with actual progress
- Document deviations and reasons
- Communicate blockers early
- Verify each step before proceeding
- Keep stakeholders informed

**Don't:**
- Silently deviate from the plan
- Skip verification steps
- Ignore test failures
- Rush through critical phases
- Forget to document learnings

### Review Phase

**Do:**
- Conduct retrospectives
- Document lessons learned
- Update templates based on experience
- Share knowledge with team
- Archive completed PRPs for reference

## PRP Checklist

Before starting execution, verify:

- [ ] Problem is clearly defined and understood
- [ ] Requirements are specific and measurable
- [ ] Approach is justified and optimal
- [ ] Risks are identified with mitigation plans
- [ ] Success criteria are defined
- [ ] Testing strategy is comprehensive
- [ ] Rollback plan exists
- [ ] Dependencies are documented
- [ ] Timeline is realistic
- [ ] Resources are available

During execution, track:

- [ ] Each step is completed and verified
- [ ] Progress is documented
- [ ] Blockers are communicated
- [ ] Tests are passing
- [ ] Documentation is updated
- [ ] Stakeholders are informed

After completion:

- [ ] Success criteria met
- [ ] All tests passed
- [ ] Documentation complete
- [ ] Retrospective conducted
- [ ] Lessons learned documented
- [ ] PRP archived

## Example: Complete PRP Template

```markdown
# PRP: [Project/Feature Name]

**Created:** [Date]
**Author:** [Name/Agent]
**Status:** [Planning/In Progress/Completed/On Hold]
**Priority:** [High/Medium/Low]

## Problem Statement

### Context
[Background]

### Objective
[Clear goal]

### Constraints
- [Constraint 1]
- [Constraint 2]

### Scope
**In Scope:** [...]
**Out of Scope:** [...]

## Analysis

### Current State
[Description]

### Requirements
**Functional:**
1. [Requirement]

**Non-Functional:**
1. [Requirement]

### Risk Assessment
[Risks and mitigation]

## Approach

### Strategy
[Chosen approach]

### Alternatives Considered
[Alternative approaches]

### Key Decisions
[Important decisions]

## Execution Plan

### Phase 1: Setup
- [ ] Task 1
- [ ] Task 2

### Phase 2: Implementation
- [ ] Task 1
- [ ] Task 2

### Phase 3: Testing
- [ ] Task 1
- [ ] Task 2

### Phase 4: Deployment
- [ ] Task 1
- [ ] Task 2

## Testing Strategy

### Unit Tests
[Tests]

### Integration Tests
[Tests]

### Acceptance Criteria
- [ ] [Criterion]

## Monitoring

### Success Metrics
- [Metric]: [Target]

### Progress Tracking
[How progress will be tracked]

## Rollback Plan

### Triggers
- [Trigger]

### Steps
1. [Step]

## Notes and Learnings

[Document insights, challenges, and solutions discovered during execution]
```

## Usage by Agents

This skill is automatically available to:
- **context-engineering-prp-generator** - During PRP creation and structuring
- **context-engineering-orchestrator** - When coordinating complex workflows
- **context-engineering-executor** - During PRP execution and tracking

The skill ensures consistent PRP structure and comprehensive problem-solving across all workflows.
