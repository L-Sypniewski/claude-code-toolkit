# Phase 7-8: Implementation and Completion

## Phase 7: Implementation

### Success Criteria
- [ ] All implementation steps completed
- [ ] All tests pass for each step
- [ ] Plan file updated after each step
- [ ] User approved completion

### Critical Rules

1. **Test with each step** - Do not proceed to next step until tests pass and/or acceptance criteria is met
2. **Update plan immediately** - Mark step complete in plan file before moving on
3. **Real infrastructure** - Use test containers, local instances over mocks
4. **Ephemeral test infra** - Test infrastructure must be created during tests and removed afterwards
5. **Stop on failure** - If tests fail, fix before proceeding

### Steps

1. **Update Plan File Status**

   Update plan file:
   - Status: "Planning" → "Implementation"
   - Current Phase: "Phase 7: Implementation"
   - Last Updated: [timestamp]

2. **Execute Each Implementation Step**

   For each step in the plan:
   
   a) **Implement the step**
   b) **Run tests for that step** (if applicable)
      - Use integration tests with real infrastructure when possible
      - Test infrastructure must be created during tests and removed afterwards
   c) **Verify success criteria met**
   d) **Update plan file immediately**:
      - Mark step checkbox as complete: `[x]`
      - Add implementation notes
      - Update "Last Updated" timestamp
   e) **Do NOT proceed if tests fail or acceptance criteria not met**

3. **After Each Major Section**

   Report progress to user:
   ```
   Implementation Progress:
   - Steps completed: X/Y
   - Tests passing: [Yes/No]
   - Current section: [name]
   
   Continue with next section?
   ```

   **WAIT for user approval before continuing.**

4. **On Implementation Complete**

   ```
   Phase 7 (Implementation) complete.
   
   Summary:
   - All steps completed: [X/X]
   - All tests passing: Yes
   - Plan file updated: Yes
   
   Proceed to Phase 8 (Completion)?
   ```

**WAIT for user approval before proceeding.**

---

## Phase 8: Completion

### Success Criteria
- [ ] All implementation verified complete
- [ ] Feature working as specified
- [ ] User chose post-implementation actions
- [ ] Plan file finalized

### Steps

1. **Verify Implementation Complete**

   Read plan file and verify:
   - All implementation step checkboxes marked `[x]`
   - All tests passing
   - Validation criteria addressed

2. **Final Verification**

   If testable:
   - Run full test suite
   - Verify no regressions
   - Test feature end-to-end

3. **Present Completion Summary**

   ```
   Feature Implementation Complete!

   - Feature: [Title]
   - Plan: plans/feature-[name]-[timestamp].md
   - Source: [GitHub Issue #X | Prompt | File: path]
   - Steps completed: X/X
   - Tests: All passing
   ```

4. **Offer Post-Implementation Options**

   Ask user:
   ```
   What would you like to do next?
   
   Options (select multiple):
   - Run code review (invoke code-reviewer agent)
   - Create pull request (invoke pull-request-creator agent)
   - Update GitHub issue (post completion comment) [if applicable]
   - Nothing, I'll handle it manually
   ```

5. **Execute User Choices**

   Based on selection:
   - Code review: Invoke `code-reviewer` with plan file and changed files
   - Create PR: Invoke `pull-request-creator` with plan file context
   - Update issue: Post completion comment to GitHub issue (if source was github-issue)
   - Manual: Provide plan file location

6. **Finalize Plan File**

   Update plan file:
   - Status: "Completed"
   - Add completion timestamp
   - Add PR link if created
   - Add code review notes if performed

7. **Final Summary**

   ```
   Phase 8 (Completion) complete.
   
   Feature workflow finished.
   - Plan file: plans/feature-[name]-[timestamp].md
   - Status: Completed
   [- PR: #X if created]
   [- Code review: Completed if performed]
   ```
