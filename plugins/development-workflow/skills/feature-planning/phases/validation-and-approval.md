# Phase 5-6: Validation and User Approval

## Phase 5: Plan Validation

### Success Criteria
- [ ] Validator reviewed plan
- [ ] Validation results recorded in plan file
- [ ] If NEEDS REVISION: revisions completed
- [ ] User approved to proceed

### Steps

1. **Delegate to feature-plan-validator Agent**

   Invoke `feature-plan-validator` with:
   - Plan file path from Phase 4
   - Request comprehensive validation (completeness, feasibility, clarity)

   Validator checks:
   - No time estimates in plan
   - Each step has success criteria
   - Tests are included with steps (not batched)
   - Plan is trackable/resumable

   Returns:
   - Approval decision (APPROVED / APPROVED WITH NOTES / NEEDS REVISION)
   - Specific feedback on completeness, feasibility, clarity
   - Recommendations for improvements

2. **Update Plan File with Validation Results**

   Append validation report to plan file in "Validation Results" section.

   If validation status is NEEDS REVISION:
   - Show validation feedback to user
   - Ask if they want to:
     a) Revise plan manually
     b) Re-run planning with additional context
     c) Proceed anyway (override)
   - If revising, return to Phase 3

3. **Update TodoWrite and ask for approval**:
   - Mark Phase 5 as complete
   
   ```
   Phase 5 (Plan Validation) complete.
   
   Summary:
   - Validation status: [APPROVED/APPROVED WITH NOTES/NEEDS REVISION]
   - Issues found: [count or "None"]
   - Recommendations: [brief list]
   
   Proceed to Phase 6 (User Approval)?
   ```

**WAIT for user approval before proceeding.**

---

## Phase 6: User Approval

### Success Criteria
- [ ] Plan summary presented to user
- [ ] User explicitly approved implementation
- [ ] Agent assignment confirmed
- [ ] User approved to proceed to implementation

### Steps

1. **Present Plan Summary to User**

   ```
   Plan Summary:
   - Feature: [Title]
   - Complexity: X/8
   - Architecture advisor: [Yes/No]
   - Files to modify: Y files
   - Implementation steps: Z steps
   - Validation status: [APPROVED/APPROVED WITH NOTES]

   Plan file: plans/feature-[name]-[timestamp].md
   Source: [GitHub Issue #X | Prompt | File: path]

   [If APPROVED WITH NOTES, show key recommendations]
   ```

2. **Get Explicit User Approval**

   Ask user:
   ```
   Ready to proceed with implementation?
   
   Options:
   - "Yes, proceed with senior-engineer"
   - "Yes, but use different agent"
   - "No, let me review the plan first"
   - "No, the plan needs changes"
   ```

   If user wants to review or make changes:
   - Pause workflow
   - Show plan file location
   - Inform about `/resume-feature [plan-file]` command
   - **STOP** - Do not proceed

   If user chooses different agent:
   - Update plan file with new agent assignment

3. **Record Approval**

   Update plan file:
   - Status: "Approved for Implementation"
   - Assigned Agent: [confirmed agent]

4. **Ask for approval to begin implementation**:
   
   ```
   Phase 6 (User Approval) complete.
   
   Summary:
   - User approved: Yes
   - Assigned agent: [agent name]
   
   Begin Phase 7 (Implementation)?
   ```

**WAIT for user approval before proceeding.**
