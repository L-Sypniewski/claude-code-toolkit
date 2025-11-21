---
name: issue-analysis-frameworks
description: Comprehensive frameworks and methodologies for analyzing GitHub issues, bug reports, and feature requests to extract actionable insights and create effective implementation plans
author: Claude Code Toolkit
---

# Issue Analysis Frameworks

This skill provides systematic frameworks for analyzing issues and extracting actionable insights, automatically activated during GitHub issue processing and requirement analysis.

## Purpose

Automatically activated when:
- Analyzing GitHub issues
- Processing bug reports
- Evaluating feature requests
- Extracting requirements from issues
- Creating implementation plans from issues
- Triaging and prioritizing issues

## Issue Analysis Framework

### 1. Initial Assessment

**Purpose:** Quick evaluation of issue type and priority

**Questions to Answer:**
- What type of issue is this? (Bug, Feature, Enhancement, Question, Documentation)
- What is the reported severity/priority?
- Is the issue clearly described?
- Is there enough information to proceed?
- Are there duplicates?

**Assessment Template:**
```markdown
## Initial Assessment

**Issue Type:** [Bug/Feature/Enhancement/Task/Question]
**Reporter:** [Username]
**Priority:** [Critical/High/Medium/Low]
**Complexity:** [High/Medium/Low]
**Estimated Effort:** [T-shirt size: XS/S/M/L/XL]

**Clarity Score:** [1-5]
- 5: Perfectly clear with all details
- 3: Understandable but needs clarification
- 1: Vague and missing critical information

**Action Required:**
- [ ] Request more information
- [ ] Assign to team member
- [ ] Label appropriately
- [ ] Link to related issues
- [ ] Add to milestone
```

### 2. Deep Issue Analysis

**Purpose:** Comprehensive understanding of the issue

#### For Bug Reports

**Bug Analysis Template:**
```markdown
## Bug Analysis

### Problem Description
**What is broken:** [Clear description]
**Expected behavior:** [What should happen]
**Actual behavior:** [What actually happens]
**Impact:** [Who/what is affected]

### Reproduction
**Steps to reproduce:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Reproduction rate:** [Always/Sometimes/Rarely]
**Environment:**
- OS: [Operating system]
- Browser: [If applicable]
- Version: [Software version]
- Configuration: [Relevant settings]

### Root Cause Hypothesis
**Suspected cause:** [Initial hypothesis]
**Affected components:** [List of components]
**Related code areas:** [File paths or modules]

### Impact Assessment
**Severity:** [How serious is this bug?]
- Critical: System down, data loss, security issue
- High: Major functionality broken
- Medium: Workaround exists
- Low: Minor inconvenience

**Scope:** [How many users affected?]
- All users
- Specific user segment
- Edge case
- Single user

**Business Impact:**
- Revenue impact: [Yes/No - describe]
- User experience impact: [Describe]
- Reputation risk: [High/Medium/Low]

### Investigation Notes
[Document investigation steps, findings, and insights]
```

#### For Feature Requests

**Feature Analysis Template:**
```markdown
## Feature Analysis

### Feature Description
**What:** [Clear description of the feature]
**Why:** [Problem this solves or value it provides]
**Who:** [Target users or use cases]

### User Story
```
As a [user type],
I want to [action],
So that [benefit].
```

### Requirements
**Functional Requirements:**
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

**Non-Functional Requirements:**
- Performance: [Requirements]
- Security: [Requirements]
- Usability: [Requirements]
- Accessibility: [Requirements]

### Use Cases
**Primary Use Case:**
1. User [action]
2. System [response]
3. User [action]
4. Result: [outcome]

**Alternative Flows:**
[Alternative scenarios]

**Error Cases:**
[What can go wrong]

### Value Assessment
**User Value:**
- Problem solved: [Description]
- Frequency of use: [High/Medium/Low]
- User segment size: [Large/Medium/Small]

**Business Value:**
- Strategic alignment: [High/Medium/Low]
- Revenue potential: [Describe]
- Competitive advantage: [Yes/No]
- Cost to build: [Estimate]
- Maintenance cost: [Estimate]

### Effort vs. Value
**Value Score:** [1-10]
**Effort Score:** [1-10]
**Priority Score:** Value / Effort = [Score]

### Dependencies
**Technical Dependencies:**
- [Dependency 1]
- [Dependency 2]

**Feature Dependencies:**
- [Other feature needed first]

**External Dependencies:**
- [Third-party services, APIs]
```

### 3. Context Extraction

**Purpose:** Gather all relevant context and background

**Context Checklist:**
- [ ] Read entire issue thread and comments
- [ ] Review linked/related issues
- [ ] Check pull requests referencing this issue
- [ ] Review relevant documentation
- [ ] Examine affected code areas
- [ ] Check git history for related changes
- [ ] Look at similar resolved issues
- [ ] Understand system architecture context

**Context Documentation:**
```markdown
## Context

### Related Issues
- #123 - [Description and relevance]
- #456 - [Description and relevance]

### Related PRs
- #789 - [Description and relevance]

### Code Areas
- `src/module/file.js` - [Relevance]
- `src/component/other.js` - [Relevance]

### Historical Context
[Previous changes, decisions, or attempts related to this issue]

### Dependencies and Constraints
[External factors affecting implementation]

### Documentation References
- [Link to relevant docs]
- [Link to API specs]
```

### 4. Stakeholder Analysis

**Purpose:** Identify and understand all stakeholders

**Stakeholder Template:**
```markdown
## Stakeholder Analysis

### Primary Stakeholders
**Reporter:**
- Username: [@username]
- Role: [User/Customer/Developer]
- Motivation: [Why they care]
- Influence: [High/Medium/Low]

**Affected Users:**
- User segment: [Description]
- Impact level: [High/Medium/Low]
- Number affected: [Estimate]

**Technical Stakeholders:**
- Component owners: [@username]
- Architecture reviewers: [@username]
- Security team: [@username]

### Communication Plan
- Who needs to be informed: [List]
- Who needs to approve: [List]
- Update frequency: [Regular/On milestone/On completion]
```

### 5. Solution Brainstorming

**Purpose:** Generate and evaluate potential solutions

**Solution Template:**
```markdown
## Potential Solutions

### Solution 1: [Name]
**Description:** [How it works]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

**Complexity:** [High/Medium/Low]
**Risk:** [High/Medium/Low]

### Solution 2: [Name]
[Same structure]

### Recommended Solution
**Choice:** [Solution name]
**Rationale:** [Why this solution is best]
**Trade-offs:** [What we're accepting]
```

### 6. Implementation Strategy

**Purpose:** Define how to implement the solution

**Strategy Template:**
```markdown
## Implementation Strategy

### Approach
**Strategy:** [Big bang/Incremental/Feature flag]
**Rationale:** [Why this approach]

### Architecture Changes
**Components Affected:**
- [Component 1]: [Changes needed]
- [Component 2]: [Changes needed]

**New Components:**
- [Component name]: [Purpose]

### Database Changes
- [Schema changes if needed]
- [Migration strategy]
- [Data backfill plan]

### API Changes
**New Endpoints:**
- [Endpoint description]

**Modified Endpoints:**
- [Endpoint]: [Changes]

**Breaking Changes:**
- [List any breaking changes]
- [Migration path for clients]

### Testing Strategy
**Unit Tests:**
- [Test areas]

**Integration Tests:**
- [Test scenarios]

**Manual Testing:**
- [Test cases]

### Rollout Plan
**Phase 1:** [Description]
**Phase 2:** [Description]
**Phase 3:** [Description]

**Feature Flags:** [If using]
**Rollback Plan:** [How to rollback if needed]
```

### 7. Acceptance Criteria

**Purpose:** Define what "done" means

**Criteria Template:**
```markdown
## Acceptance Criteria

### Functional Criteria
- [ ] [Specific behavior 1 works as expected]
- [ ] [Specific behavior 2 works as expected]
- [ ] [Edge case 1 is handled]
- [ ] [Error case 1 shows appropriate message]

### Non-Functional Criteria
- [ ] Performance meets SLA (< X ms response time)
- [ ] Passes security review
- [ ] Accessible (WCAG 2.1 AA)
- [ ] Works on all supported browsers
- [ ] Mobile responsive

### Testing Criteria
- [ ] Unit test coverage > 80%
- [ ] All integration tests pass
- [ ] Manual testing completed
- [ ] QA sign-off obtained

### Documentation Criteria
- [ ] API documentation updated
- [ ] User documentation updated
- [ ] Release notes prepared
- [ ] Internal docs updated

### Operational Criteria
- [ ] Monitoring/alerting configured
- [ ] Logging implemented
- [ ] Runbook created
- [ ] Performance benchmarks documented
```

## Issue Classification Framework

### Priority Matrix

**Priority = Severity × Urgency**

| Severity | Urgency | Priority | Response Time |
|----------|---------|----------|---------------|
| High | High | P0 Critical | Immediate |
| High | Medium | P1 High | < 24 hours |
| Medium | High | P2 Medium | < 3 days |
| Medium | Medium | P3 Medium | < 1 week |
| Low | High | P3 Medium | < 1 week |
| Low | Medium | P4 Low | < 2 weeks |
| Low | Low | P5 Low | Backlog |

### Issue Labels Framework

**Type Labels:**
- `bug` - Something isn't working
- `feature` - New feature request
- `enhancement` - Improvement to existing feature
- `documentation` - Documentation improvement
- `performance` - Performance issue
- `security` - Security vulnerability
- `refactoring` - Code improvement

**Priority Labels:**
- `priority:critical` - P0
- `priority:high` - P1
- `priority:medium` - P2-P3
- `priority:low` - P4-P5

**Status Labels:**
- `status:needs-info` - More information needed
- `status:in-progress` - Currently being worked on
- `status:blocked` - Blocked by dependency
- `status:review` - Ready for review
- `status:ready` - Ready to start

**Category Labels:**
- `frontend` - Frontend related
- `backend` - Backend related
- `api` - API related
- `database` - Database related
- `infrastructure` - Infrastructure related

## Analysis Checklist

When analyzing an issue, verify:

- [ ] Issue type is correctly identified
- [ ] Priority is appropriately assigned
- [ ] All context is gathered and documented
- [ ] Requirements are extracted and clear
- [ ] Stakeholders are identified
- [ ] Multiple solutions are considered
- [ ] Recommended solution is justified
- [ ] Implementation strategy is defined
- [ ] Acceptance criteria are specific and testable
- [ ] Risks are identified with mitigation plans
- [ ] Dependencies are documented
- [ ] Effort is estimated
- [ ] Timeline is realistic

## Common Analysis Pitfalls

**Avoid:**
- Accepting vague or incomplete issue descriptions
- Skipping root cause analysis
- Jumping to solutions without understanding the problem
- Ignoring similar resolved issues
- Underestimating complexity
- Missing hidden dependencies
- Forgetting about non-functional requirements
- Not considering rollback scenarios
- Ignoring maintenance implications
- Failing to validate assumptions with stakeholders

## Issue Templates Recommendation

### Bug Report Template
```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., iOS]
- Browser: [e.g., chrome, safari]
- Version: [e.g., 22]

**Additional context**
Any other context about the problem.
```

### Feature Request Template
```markdown
**Is your feature request related to a problem?**
A clear description of the problem. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
Other solutions or features you've considered.

**Use case**
Describe how you would use this feature.

**Additional context**
Any other context, mockups, or screenshots.
```

## Usage by Agents

This skill is automatically available to:
- **context-engineering-github-issue-analyzer** - During issue analysis and processing
- **context-engineering-orchestrator** - When coordinating issue-based workflows
- **context-engineering-prp-generator** - When creating PRPs from issues

The skill ensures systematic and thorough issue analysis across all context engineering workflows.
