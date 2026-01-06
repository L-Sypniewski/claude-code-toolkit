# Workflow Templates

Ready-to-use templates for common development workflows.

## Bug Fix Workflow

```markdown
## Bug Fix: [Issue Title]

### 1. Issue Analysis
- [ ] Reproduce the bug
- [ ] Document reproduction steps
- [ ] Identify affected components

### 2. Root Cause
- [ ] Trace code path
- [ ] Identify problematic code
- [ ] Understand why it fails

### 3. Fix Design
- [ ] Plan the solution
- [ ] Consider edge cases
- [ ] Identify potential regressions

### 4. Implementation
- [ ] Apply the fix
- [ ] Keep changes minimal and focused

### 5. Testing
- [ ] Verify bug is fixed
- [ ] Add test for the bug
- [ ] Run existing tests

### 6. Regression Check
- [ ] Run full test suite
- [ ] Manual smoke test if applicable
- [ ] Check related functionality
```

## Feature Development Workflow

```markdown
## Feature: [Feature Name]

### 1. Requirements
- [ ] Define scope clearly
- [ ] Identify acceptance criteria
- [ ] List out-of-scope items

### 2. Design Review
- [ ] Architectural approach
- [ ] Integration points
- [ ] Data model changes

### 3. Prototype (Optional)
- [ ] Quick proof of concept
- [ ] Validate approach works
- [ ] Identify unknowns early

### 4. Implementation
- [ ] Core functionality
- [ ] Edge cases
- [ ] Error handling

### 5. Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

### 6. Documentation
- [ ] Code comments where needed
- [ ] API documentation
- [ ] User-facing docs

### 7. Review & Deploy
- [ ] Code review
- [ ] Address feedback
- [ ] Merge and deploy
```

## Refactoring Workflow

```markdown
## Refactoring: [Target Area]

### 1. Assessment
- [ ] Identify code to refactor
- [ ] Document current behavior
- [ ] Write tests for current behavior (if missing)

### 2. Planning
- [ ] Define target state
- [ ] Break into incremental steps
- [ ] Identify risks

### 3. Incremental Changes
- [ ] Make one change at a time
- [ ] Run tests after each change
- [ ] Commit frequently

### 4. Validation
- [ ] All tests pass
- [ ] No behavior changes (unless intended)
- [ ] Performance not degraded

### 5. Cleanup
- [ ] Remove dead code
- [ ] Update documentation
- [ ] Final review
```

## Investigation Workflow

```markdown
## Investigation: [Topic]

### 1. Define Question
- [ ] What specifically are we trying to learn?
- [ ] What decisions depend on this?

### 2. Research
- [ ] Review existing code
- [ ] Check documentation
- [ ] Search for prior art

### 3. Experiment (If Needed)
- [ ] Create isolated test
- [ ] Try different approaches
- [ ] Document findings

### 4. Synthesize
- [ ] Summarize findings
- [ ] Make recommendation
- [ ] Document for future reference
```
