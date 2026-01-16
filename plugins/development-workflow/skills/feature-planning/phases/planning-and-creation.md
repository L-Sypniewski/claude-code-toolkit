# Phase 3-4: Planning and Plan File Creation

## Phase 3: Implementation Planning

### Success Criteria
- [ ] Implementation strategy defined
- [ ] Files to modify/create identified
- [ ] Steps defined with tests for each (if testable)
- [ ] Architecture guidance received (if complexity ≥ 5)
- [ ] User approved to proceed

### Steps

1. **Delegate to Planning Agents**

   **Always invoke senior-engineer** with prompt:
   ```
   Create an implementation plan for this feature.

   Requirements:
   [Include full requirements]

   Complexity Score: X/8

   IMPORTANT PLANNING RULES:
   - Do NOT include any time estimates
   - Each step that produces testable code MUST include its test(s)
   - Tests are NOT batched at the end - they go with each step
   - Favor integration tests with real infrastructure; test infra must be created during tests and removed afterwards
   - Plan must be trackable so another agent can resume from any step

   Provide:
   1. High-level implementation strategy
   2. Specific files to modify/create with paths
   3. Implementation steps - each step includes:
      - Implementation task
      - Test(s) for that task (if applicable)
      - Success criteria for the step
   4. Validation criteria (specific, measurable)
   ```

   **If complexity ≥ 5, also invoke technical-architecture-advisor** with prompt:
   ```
   Review this feature and provide architectural guidance.

   Requirements:
   [Include full requirements]

   Complexity Score: X/8

   Evaluate:
   1. Architectural approach and alternatives
   2. Integration with existing systems
   3. Potential risks and mitigations
   4. Testing strategy (favor integration tests)
   5. What could go wrong and how to prevent it
   ```

2. **Update TodoWrite and ask for approval**:
   - Mark Phase 3 as complete
   
   ```
   Phase 3 (Implementation Planning) complete.
   
   Summary: 
   - Strategy defined: [brief description]
   - Files affected: [count]
   - Implementation steps: [count]
   - Architecture guidance: [Yes/No]
   
   Proceed to Phase 4 (Plan File Creation)?
   ```

**WAIT for user approval before proceeding.**

---

## Phase 4: Plan File Creation

### Success Criteria
- [ ] Plan file created at `plans/feature-[name]-[date].md`
- [ ] All sections populated from planning output
- [ ] Steps include tests alongside implementation
- [ ] No time estimates in plan
- [ ] User approved to proceed

### Steps

1. **Generate Plan File**

   Create file: `plans/feature-[sanitized-title]-[timestamp].md`

   Where:
   - `[sanitized-title]` = Feature title, lowercase, spaces to hyphens, special chars removed
   - `[timestamp]` = YYYYMMDD format

   Use template from [templates/plan-file.md](../templates/plan-file.md).

2. **Verify Plan Structure**
   - [ ] No time estimates present
   - [ ] Each implementation step has associated test (if applicable)
   - [ ] Success criteria defined for each step
   - [ ] Plan is trackable (clear checkboxes, status markers)

3. **Update TodoWrite and ask for approval**:
   - Mark Phase 4 as complete
   
   ```
   Phase 4 (Plan File Creation) complete.
   
   Summary:
   - Plan file: plans/feature-[name]-[date].md
   - Implementation steps: [count]
   - Tests included: [count]
   
   Proceed to Phase 5 (Plan Validation)?
   ```

**WAIT for user approval before proceeding.**
