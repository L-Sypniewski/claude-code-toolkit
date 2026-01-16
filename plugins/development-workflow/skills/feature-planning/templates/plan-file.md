# Feature Plan File Template

Template for generating plan files at `plans/feature-[sanitized-title]-[timestamp].md`.

## Naming Convention

- `[sanitized-title]` = Feature title, lowercase, spaces to hyphens, special chars removed
- `[timestamp]` = YYYYMMDD format

## Template

```markdown
# Feature: [Title]

**Status**: Planning | Approved | Implementation | Completed
**Current Phase**: Phase [N]: [Name]
**Source**: [GitHub Issue #X | Prompt | File: path]
**Complexity Score**: X/8 (Architecture Advisor: Yes/No)
**Created**: [ISO timestamp]
**Last Updated**: [ISO timestamp]

## Requirements Analysis

[Full output from requirements-extraction, including all sections:
FEATURE, EXAMPLES, DOCUMENTATION, OTHER CONSIDERATIONS]

## Implementation Plan

### Architecture Recommendations

[If architecture advisor was involved, include their full guidance]
[If not involved, note: "Not required (complexity < 5)"]

### Implementation Strategy

[High-level approach - NO time estimates]

### Files to Modify/Create

- [ ] `path/to/file1.ts` - Description of changes
- [ ] `path/to/file2.ts` - Description of changes

### Implementation Steps

**IMPORTANT**: Each step includes its test. Tests are NOT batched at the end.

#### Step 1: [Name]
- [ ] **Implementation**: [What to build]
- [ ] **Test**: [Test to write/run for this step]
- **Success Criteria**: [How to verify step is complete]

#### Step 2: [Name]
- [ ] **Implementation**: [What to build]
- [ ] **Test**: [Test to write/run for this step]
- **Success Criteria**: [How to verify step is complete]

#### Step 3: [Name]
- [ ] **Implementation**: [What to build]
- [ ] **Test**: [Test to write/run for this step - favor integration tests]
- **Success Criteria**: [How to verify step is complete]

### Testing Strategy

**Prefer integration tests** with real infrastructure:
- Test containers for databases (PostgreSQL, MongoDB, etc.)
- Local service instances via Docker/CLI
- Real API calls to local services
- Spawn/teardown pattern for clean tests

### Validation Criteria

[Specific, measurable criteria - must all pass before completion]
- [ ] Criterion 1: [Measurable requirement]
- [ ] Criterion 2: [Measurable requirement]

## Validation Results

[Filled by feature-plan-validator]
- Status: [APPROVED | APPROVED WITH NOTES | NEEDS REVISION]
- Issues: [List any issues found]
- Recommendations: [List recommendations]

## Progress Tracking

### Phase Progress
- [x] Phase 1: Setup
- [x] Phase 2: Complexity Assessment
- [x] Phase 3: Implementation Planning
- [x] Phase 4: Plan File Creation
- [ ] Phase 5: Plan Validation
- [ ] Phase 6: User Approval
- [ ] Phase 7: Implementation
- [ ] Phase 8: Completion

### Implementation Progress
[Updated as steps complete - another agent can resume from here]
- Last completed step: [Step N]
- Next step: [Step N+1]
- Blocking issues: [None | List issues]

### Implementation Notes
[Filled during implementation]

### Changes from Original Plan
[Document any deviations]

## Metadata
**Plan File**: plans/feature-[sanitized-title]-[timestamp].md
**Assigned Agent**: [senior-engineer | other]
**Related Issue**: [#X if GitHub issue source, otherwise N/A]
**Related PR**: [Will be added when created]
```

## Status Values

- **Planning**: Plan being created (Phases 1-4)
- **Approved**: User approved, ready for implementation (Phase 6 complete)
- **Implementation**: Feature being built (Phase 7)
- **Completed**: Implementation finished and verified (Phase 8)

## Key Rules

1. **No time estimates** anywhere in the plan
2. **Tests with steps** - not batched at the end
3. **Trackable state** - clear checkboxes, "Last completed step" field
4. **Success criteria** for each step
5. **Integration tests** preferred over mocks
