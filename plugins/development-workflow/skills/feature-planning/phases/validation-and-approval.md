# Phase 5-6: Validation and User Approval

## Phase 5: Plan Validation

### 1. Delegate to feature-plan-validator Agent

Use Task tool to invoke `feature-plan-validator` with:
- Plan file path from Phase 4
- Request comprehensive validation (completeness, feasibility, clarity)

The validator will return a validation report with:
- Approval decision (APPROVED / APPROVED WITH NOTES / NEEDS REVISION)
- Specific feedback on completeness, feasibility, clarity
- Recommendations for improvements

### 2. Update Plan File with Validation Results

Append validation report to plan file in "Validation Results" section.

If validation status is NEEDS REVISION:
- Show validation feedback to user
- Ask if they want to:
  a) Revise plan manually
  b) Re-run planning with additional context
  c) Proceed anyway (override)
- If revising, return to Phase 3

### 3. Update TodoWrite

- Mark "Plan validation" as completed
- Mark "User approval" as in_progress

## Phase 6: User Approval

### 1. Present Plan Summary to User

```
Plan Summary:
- Feature: [Title]
- Complexity: X/8 [with/without] architecture advisor input
- Files to modify: Y files
- Implementation phases: Z phases
- Recommended agent: [agent-name]
- Validation status: [APPROVED/APPROVED WITH NOTES]

Plan file: plans/feature-[name]-[timestamp].md
Source: [GitHub Issue #X | Prompt | File: path]

[If APPROVED WITH NOTES, show key recommendations]
```

### 2. Get User Approval

Use AskUserQuestion tool:
```
Question: "Ready to proceed with implementation?"
Options:
- "Yes, proceed with [recommended-agent]" (Recommended)
- "Yes, but use different agent" (specify which)
- "No, let me review the plan first"
- "No, the plan needs changes"
```

If user wants to review or make changes:
- Pause workflow
- Show plan file location
- Inform about `/resume-feature [plan-file]` command
- Exit workflow

If user chooses different agent:
- Update plan file with new agent assignment
- Continue to Phase 7

### 3. Update TodoWrite

- Mark "User approval" as completed
- Mark "Implementation" as in_progress
