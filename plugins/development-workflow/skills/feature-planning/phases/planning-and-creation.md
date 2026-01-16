# Phase 3-4: Planning and Plan File Creation

## Phase 3: Implementation Planning

### 1. Delegate to Planning Agents

**Always invoke senior-engineer**:
Use Task tool to invoke `senior-engineer` with prompt:
```
Create an implementation plan for this feature based on the following requirements:

[Include full requirements from caller]

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

[Include full requirements from caller]

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

### 2. Update TodoWrite

- Mark "Implementation planning" as completed
- Mark "Plan validation" as in_progress

## Phase 4: Plan File Creation

### 1. Generate Plan File

Create file: `plans/feature-[sanitized-title]-[timestamp].md`

Use the template from [templates/plan-file.md](../templates/plan-file.md).

Fill in:
- Feature title and metadata
- Requirements analysis output
- Architecture recommendations (if applicable)
- Implementation strategy from senior-engineer
- Files to modify/create with checkboxes
- Implementation steps with checkboxes
- Validation criteria
