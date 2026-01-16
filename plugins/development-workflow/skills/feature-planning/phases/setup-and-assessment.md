# Phase 1-2: Setup and Complexity Assessment

## Phase 1: Setup (Requirements Handling)

### 1. Verify Requirements Completeness

Check the `COMPLETENESS` status from analyzer output.
- If `COMPLETE`: Proceed to Phase 2
- If `INCOMPLETE`: Invoke `feature-requirements-clarifier` agent first

### 2. Create TodoWrite for Progress Tracking

Initialize todo list with workflow phases:
- [ ] Requirements analysis
- [ ] Complexity assessment
- [ ] Implementation planning
- [ ] Plan validation
- [ ] User approval
- [ ] Implementation
- [ ] Completion

## Phase 2: Complexity Assessment

### 1. Calculate Complexity Score (0-8 points)

Use the `complexity-scoring` skill to analyze requirements across four dimensions:
- File Scope (0-2 points)
- Pattern Introduction (0-2 points)
- Integration Complexity (0-2 points)
- Breaking Changes (0-2 points)

See `complexity-scoring` skill for detailed scoring criteria and examples.

**Threshold**: If total score ≥ 5, involve `technical-architecture-advisor` in planning phase.

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

### 2. Update TodoWrite

- Mark "Requirements analysis" as completed
- Mark "Complexity assessment" as completed
- Mark "Implementation planning" as in_progress
