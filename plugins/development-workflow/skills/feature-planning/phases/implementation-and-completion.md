# Phase 7-8: Implementation and Completion

## Phase 7: Implementation

### 1. Update Plan File Status

Update plan file:
- Status: "Planning" → "Implementation"
- Current Phase: "Planning" → "Implementation"
- Assigned Agent: [confirmed agent from user approval]
- Last Updated: [new timestamp]

### 2. Delegate to Implementation Agent

Use Task Tool to invoke the approved agent (typically `senior-engineer`) with:
```
Implement the feature according to this plan:

Plan file: plans/feature-[name]-[timestamp].md
Source: [source metadata]

CRITICAL INSTRUCTIONS:
1. Read the complete plan file first
2. Follow the implementation strategy and steps
3. Update the plan file IMMEDIATELY after EACH step (not batched)
4. Mark checkboxes as you complete them
5. Document any deviations in "Changes from Original Plan"
6. Add implementation notes as you progress
7. Run validation tests after each phase
8. Update status when complete

The plan file is the single source of truth. Keep it updated in real-time.
```

Run this in the background if possible (saves context for main thread to track progress).

### 3. Monitor Progress (if running in background)

Periodically:
- Read plan file to check progress
- Update TodoWrite based on completed steps
- Show progress updates to user

If not running in background:
- Wait for agent completion
- Agent updates plan file directly

## Phase 8: Completion

### 1. Verify Implementation Complete

Read plan file and verify:
- All implementation step checkboxes are marked
- Status is updated to "Completed" or "Ready for Review"
- Validation criteria are addressed

### 2. Post-Implementation Options (Ask User)

Use AskUserQuestion:
```
Question: "Implementation complete! What would you like to do next?"
MultiSelect: true
Options:
- "Run code review" (invoke code-reviewer agent)
- "Create pull request" (invoke pull-request-creator agent)
- "Update GitHub issue" (post completion comment) [only if source is GitHub issue]
- "Nothing, I'll handle it manually"
```

### 3. Execute User Choices

Based on user selection:
- Code review: Invoke `code-reviewer` with plan file and changed files
- Create PR: Invoke `pull-request-creator` with plan file context
- Update issue: Post completion comment to GitHub issue with plan summary (if applicable)
- Manual: Provide user with plan file location and next steps

### 4. Final TodoWrite Update

- Mark "Implementation" as completed
- Mark "Completion" as completed
- Show final summary

### 5. Final Summary to User

```
Feature Implementation Complete!

- Feature: [Title]
- Plan: plans/feature-[name]-[timestamp].md
- Source: [GitHub Issue #X | Prompt | File: path]
- Implementation Agent: [agent-name]
- Status: [Completed/Ready for Review]

[If PR created: Pull Request: #XYZ]
[If code review done: Code review feedback in plan file]

Next steps: [Based on user choices]
```
