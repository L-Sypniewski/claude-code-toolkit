# Phase 1-2: Setup and Complexity Assessment

## Phase 1: Setup (Requirements Handling)

### Success Criteria
- [ ] Requirements received and verified
- [ ] Source metadata recorded
- [ ] TodoWrite initialized
- [ ] User approved to proceed

### Steps

1. **Verify Requirements Completeness**
   Check the `COMPLETENESS` status from requirements-extraction output.
   - If `COMPLETE`: Continue
   - If `INCOMPLETE`: Invoke `feature-requirements-clarifier` agent first

2. **Record Source Metadata**
   - Source type: github-issue | prompt | file
   - Reference: Issue #X | N/A | file path

3. **Create TodoWrite for Progress Tracking**
   Initialize todo list with workflow phases:
   - [ ] Phase 1: Setup
   - [ ] Phase 2: Complexity Assessment
   - [ ] Phase 3: Implementation Planning
   - [ ] Phase 4: Plan File Creation
   - [ ] Phase 5: Plan Validation
   - [ ] Phase 6: User Approval
   - [ ] Phase 7: Implementation
   - [ ] Phase 8: Completion

4. **Update plan and ask for approval**:
   ```
   Phase 1 (Setup) complete.
   
   Summary: Requirements extracted and verified
   - Source: [type] - [reference]
   - Completeness: [status]
   
   Proceed to Phase 2 (Complexity Assessment)?
   ```

**WAIT for user approval before proceeding.**

---

## Phase 2: Complexity Assessment

### Success Criteria
- [ ] Complexity score calculated (0-8)
- [ ] Architecture advisor decision made
- [ ] Score displayed to user
- [ ] User approved to proceed

### Steps

1. **Calculate Complexity Score (0-8 points)**

   Use the `complexity-scoring` skill to analyze requirements across four dimensions:
   - File Scope (0-2 points)
   - Pattern Introduction (0-2 points)
   - Integration Complexity (0-2 points)
   - Breaking Changes (0-2 points)

   See `complexity-scoring` skill for detailed scoring criteria and examples.

2. **Determine Architecture Advisor Involvement**
   - Score 0-4: Proceed with `senior-engineer` only
   - Score 5-8: Invoke `technical-architecture-advisor` in Phase 3

3. **Display to User**:
   ```
   Complexity Assessment:
   - File Scope: X/2
   - Pattern Introduction: X/2
   - Integration Complexity: X/2
   - Breaking Changes: X/2
   - TOTAL: X/8

   Architecture Advisor: [Will be involved | Not needed]
   ```

4. **Update TodoWrite and ask for approval**:
   - Mark Phase 1 as complete
   - Mark Phase 2 as complete
   
   ```
   Phase 2 (Complexity Assessment) complete.
   
   Summary: Complexity score calculated
   - Total: X/8
   - Architecture advisor: [Yes/No]
   
   Proceed to Phase 3 (Implementation Planning)?
   ```

**WAIT for user approval before proceeding.**
