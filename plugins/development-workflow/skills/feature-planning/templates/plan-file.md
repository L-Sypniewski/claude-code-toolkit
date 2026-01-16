# Feature Plan File Template

Template for generating plan files at `plans/feature-[sanitized-title]-[timestamp].md`.

## Naming Convention

- `[sanitized-title]` = Feature title, lowercase, spaces to hyphens, special chars removed
- `[timestamp]` = YYYYMMDD format

## Template

```markdown
# Feature: [Title]

**Status**: Planning
**Source**: [GitHub Issue #X | Prompt | File: path]
**Complexity Score**: X/8 (Architecture Advisor: Yes/No)
**Recommended Agent**: [from senior-engineer response]
**Created**: [ISO timestamp]
**Last Updated**: [ISO timestamp]

## Requirements Analysis

[Full output from feature-issue-analyzer, including all sections:
FEATURE, EXAMPLES, DOCUMENTATION, OTHER CONSIDERATIONS]

## Implementation Plan

### Architecture Recommendations

[If architecture advisor was involved, include their full guidance]
[If not involved, note: "Not required (complexity < 5)"]

### Implementation Strategy

[High-level approach from senior-engineer]

### Files to Modify/Create

[List from senior-engineer with checkboxes:]
- [ ] `path/to/file1.ts` - Description of changes
- [ ] `path/to/file2.ts` - Description of changes

### Implementation Steps

[Phases from senior-engineer with checkboxes:]
- [ ] Phase 1: Foundation
  - [ ] Step 1.1: Description
  - [ ] Step 1.2: Description
- [ ] Phase 2: Enhancement
  - [ ] Step 2.1: Description
- [ ] Phase 3: Integration & Validation
  - [ ] Step 3.1: Description

### Validation Criteria

[Specific, testable criteria from senior-engineer:]
- [ ] Criterion 1: Measurable requirement
- [ ] Criterion 2: Measurable requirement

## Validation Results

[Will be filled by feature-plan-validator]

## Progress Tracking

**Current Phase**: Planning

### Completed Tasks
- [x] Requirements analysis completed by feature-issue-analyzer
- [x] Complexity assessment completed
- [x] Planning completed by senior-engineer
- [ ] Validation in progress...

### Implementation Notes
[Will be filled during implementation]

### Changes from Original Plan
[Will be documented as they occur]

## Metadata
**Plan File**: plans/feature-[sanitized-title]-[timestamp].md
**Assigned Agent**: [To be confirmed after validation]
**Related Issue**: [#X if GitHub issue source, otherwise N/A]
**Related PR**: [Will be added when created]
```

## Status Values

- **Planning**: Initial state, plan being created
- **Validation**: Plan under review by validator
- **Approved**: Ready for implementation
- **Implementation**: Feature being built
- **Completed**: Implementation finished
- **Ready for Review**: Implementation done, awaiting code review
