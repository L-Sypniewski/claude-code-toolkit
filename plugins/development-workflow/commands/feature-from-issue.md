---
description: Implement a feature from a GitHub issue with intelligent planning and validation
argument-hint: <issue-number>
---

# Feature From GitHub Issue

Comprehensive workflow for implementing features from GitHub issues. Coordinates requirement analysis, intelligent planning, validation, and implementation with full user visibility and control.

## Usage

```bash
/feature-from-issue 123
```

Where `123` is the GitHub issue number in the current repository.

## Workflow Steps

### PHASE 1: Setup and Requirements Analysis

1. **Extract Repository Information**
   ```bash
   git remote get-url origin
   ```
   Parse owner and repository name from the remote URL.

2. **Delegate to feature-issue-analyzer Agent**
   Use the Task tool to invoke `feature-issue-analyzer` with:
   - Issue number: $ARGUMENTS
   - Repository owner and name from step 1
   - Source type: "github-issue"

   The analyzer will:
   - Fetch the GitHub issue details
   - Create structured requirements (FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS)
   - Post analysis comment to the GitHub issue
   - Return normalized requirements

3. **Create TodoWrite for Progress Tracking**
   Initialize todo list with workflow phases:
   - [ ] Requirements analysis
   - [ ] Complexity assessment
   - [ ] Implementation planning
   - [ ] Plan validation
   - [ ] User approval
   - [ ] Implementation
   - [ ] Completion

### PHASE 2: Complexity Assessment

4. **Calculate Complexity Score (0-8 points)**

   Analyze the requirements from Phase 1 and score across 4 dimensions:

   **File Scope (0-2 points)**:
   - 0: Single file modification
   - 1: 2-4 files mentioned
   - 2: 5+ files or new directory structure needed

   **Pattern Introduction (0-2 points)**:
   - 0: Using existing patterns (analyzer mentions "existing pattern", "similar to")
   - 1: Minor pattern variation (analyzer mentions "adapt", "modify")
   - 2: New architectural pattern (analyzer mentions "new pattern", "introduce")

   **Integration Complexity (0-2 points)**:
   - 0: Isolated feature (no external systems mentioned)
   - 1: Integration with 1-2 systems/APIs
   - 2: Integration with 3+ systems or external APIs

   **Breaking Changes (0-2 points)**:
   - 0: Backward compatible (no mention of breaking changes)
   - 1: Minor breaking changes or internal API changes
   - 2: Major breaking changes, public API modifications, or migration required

   **Display to User**:
   ```
   Complexity Assessment:
   - File Scope: X/2
   - Pattern Introduction: X/2
   - Integration Complexity: X/2
   - Breaking Changes: X/2
   - TOTAL: X/8

   Architecture Advisor: [Will be involved | Not needed]
   ```

5. **Update TodoWrite**
   - Mark "Requirements analysis" as completed
   - Mark "Complexity assessment" as completed
   - Mark "Implementation planning" as in_progress

### PHASE 3: Implementation Planning

6. **Delegate to Planning Agents**

   **Always invoke senior-engineer**:
   Use Task tool to invoke `senior-engineer` with prompt:
   ```
   Create an implementation plan for this feature based on the following requirements:

   [Include full requirements from Phase 1]

   Complexity Score: X/8

   Please provide:
   1. High-level implementation strategy
   2. Specific files to modify/create with paths
   3. Implementation steps broken into logical phases
   4. Recommended implementation agent
   5. Validation criteria (specific, measurable)

   Focus on architectural approach and strategy, not detailed code.
   ```

   **Conditionally invoke technical-architecture-advisor** (if complexity ≥ 5):
   Use Task tool to invoke `technical-architecture-advisor` with prompt:
   ```
   Review this feature and provide architectural guidance:

   [Include full requirements from Phase 1]

   Complexity Score: X/8

   Please evaluate:
   1. Architectural approach and alternatives
   2. Integration with existing systems
   3. Potential risks and mitigations
   4. Best practices and patterns to follow
   5. What could go wrong and how to prevent it

   Provide complete architectural guidance for the implementation.
   ```

   The architecture advisor provides guidance BEFORE implementation begins (consultation pattern, no callbacks during implementation).

7. **Update TodoWrite**
   - Mark "Implementation planning" as completed
   - Mark "Plan validation" as in_progress

### PHASE 4: Plan File Creation

8. **Generate Plan File**

   Create file: `plans/feature-[sanitized-title]-[timestamp].md`

   Where:
   - `[sanitized-title]` = Issue title, lowercase, spaces to hyphens, special chars removed
   - `[timestamp]` = YYYYMMDD format

   **Plan Structure**:
   ```markdown
   # Feature: [Issue Title]

   **Status**: Planning
   **Source**: GitHub Issue #$ARGUMENTS
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
   **Plan File**: plans/feature-[name]-[timestamp].md
   **Assigned Agent**: [To be confirmed after validation]
   **Related Issue**: #$ARGUMENTS
   **Related PR**: [Will be added when created]
   ```

### PHASE 5: Plan Validation

9. **Delegate to feature-plan-validator Agent**

   Use Task tool to invoke `feature-plan-validator` with:
   - Plan file path from step 8
   - Request comprehensive validation (completeness, feasibility, clarity)

   The validator will return a validation report with:
   - Approval decision (APPROVED / APPROVED WITH NOTES / NEEDS REVISION)
   - Specific feedback on completeness, feasibility, clarity
   - Recommendations for improvements

10. **Update Plan File with Validation Results**

    Append validation report to plan file in "Validation Results" section.

    If validation status is NEEDS REVISION:
    - Show validation feedback to user
    - Ask if they want to:
      a) Revise plan manually
      b) Re-run planning with additional context
      c) Proceed anyway (override)
    - If revising, return to Phase 3

11. **Update TodoWrite**
    - Mark "Plan validation" as completed
    - Mark "User approval" as in_progress

### PHASE 6: User Approval

12. **Present Plan Summary to User**

    ```
    Plan Summary:
    - Feature: [Title]
    - Complexity: X/8 [with/without] architecture advisor input
    - Files to modify: Y files
    - Implementation phases: Z phases
    - Recommended agent: [agent-name]
    - Validation status: [APPROVED/APPROVED WITH NOTES]

    Plan file: plans/feature-[name]-[timestamp].md
    GitHub issue: #$ARGUMENTS

    [If APPROVED WITH NOTES, show key recommendations]
    ```

13. **Get User Approval**

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

14. **Update TodoWrite**
    - Mark "User approval" as completed
    - Mark "Implementation" as in_progress

### PHASE 7: Implementation

15. **Update Plan File Status**

    Update plan file:
    - Status: "Planning" → "Implementation"
    - Current Phase: "Planning" → "Implementation"
    - Assigned Agent: [confirmed agent from user approval]
    - Last Updated: [new timestamp]

16. **Delegate to Implementation Agent**

    Use Task tool to invoke the approved agent (typically `senior-engineer`) with:
    ```
    Implement the feature according to this plan:

    Plan file: plans/feature-[name]-[timestamp].md
    GitHub issue: #$ARGUMENTS

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

17. **Monitor Progress** (if running in background)

    Periodically:
    - Read plan file to check progress
    - Update TodoWrite based on completed steps
    - Show progress updates to user

    If not running in background:
    - Wait for agent completion
    - Agent updates plan file directly

### PHASE 8: Completion

18. **Verify Implementation Complete**

    Read plan file and verify:
    - All implementation step checkboxes are marked
    - Status is updated to "Completed" or "Ready for Review"
    - Validation criteria are addressed

19. **Post-Implementation Options** (Ask User)

    Use AskUserQuestion:
    ```
    Question: "Implementation complete! What would you like to do next?"
    MultiSelect: true
    Options:
    - "Run code review" (invoke code-reviewer agent)
    - "Create pull request" (invoke pull-request-creator agent)
    - "Update GitHub issue" (post completion comment)
    - "Nothing, I'll handle it manually"
    ```

20. **Execute User Choices**

    Based on user selection:
    - Code review: Invoke `code-reviewer` with plan file and changed files
    - Create PR: Invoke `pull-request-creator` with plan file context
    - Update issue: Post completion comment to GitHub issue #$ARGUMENTS with plan summary
    - Manual: Provide user with plan file location and next steps

21. **Final TodoWrite Update**
    - Mark "Implementation" as completed
    - Mark "Completion" as completed
    - Show final summary

22. **Final Summary to User**

    ```
    Feature Implementation Complete!

    - Feature: [Title]
    - Plan: plans/feature-[name]-[timestamp].md
    - GitHub Issue: #$ARGUMENTS
    - Implementation Agent: [agent-name]
    - Status: [Completed/Ready for Review]

    [If PR created: Pull Request: #XYZ]
    [If code review done: Code review feedback in plan file]

    Next steps: [Based on user choices]
    ```

## Integration with workflow-orchestration Skill

This command follows the workflow-orchestration skill patterns:

- **Sequential Workflow**: Analysis → Planning → Validation → Implementation
- **Delegation Pattern**: Main thread delegates to specialized agents, monitors progress
- **Handoff Pattern**: Clear transitions with validation gates between phases
- **Progress Tracking**: TodoWrite + plan file for visibility
- **Error Handling**: Validation gates catch issues before implementation

## Error Handling

**GitHub API Failures**:
- If issue fetch fails: Show error, suggest manual feature-from-prompt as fallback
- If comment post fails: Continue (analysis is more important than posting)

**Planning Failures**:
- If senior-engineer or arch advisor fails: Show error, offer to retry or manual planning
- If validation fails critically: Stop, show feedback, require user intervention

**Implementation Failures**:
- If implementation agent fails: Plan file shows last completed step
- User can use `/resume-feature [plan-file]` to continue
- All progress preserved in plan file

**User Interruption**:
- At any point, workflow can be stopped
- Plan file preserves all state
- Use `/resume-feature [plan-file]` to continue

## Key Principles

1. **User Visibility**: User sees every phase, can review at each gate
2. **Interactive Decision-Making**: User approves plan, chooses post-implementation actions
3. **Context Savings**: Implementation runs in separate agent, main thread tracks progress
4. **Resumability**: Plan file as single source of truth enables resuming interrupted workflows
5. **Quality Gates**: Validation before implementation prevents wasted effort
6. **Intelligent Complexity Detection**: Automatically involves architecture advisor when needed

## Example Invocation

```bash
/feature-from-issue 42
```

This will:
1. Fetch GitHub issue #42 from current repo
2. Analyze and structure requirements
3. Calculate complexity score
4. Create implementation plan (with arch advisor if needed)
5. Validate plan for completeness, feasibility, clarity
6. Get your approval
7. Implement the feature
8. Offer code review / PR creation

All tracked in `plans/feature-[name]-[date].md` with real-time progress updates.
