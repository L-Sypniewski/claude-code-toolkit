---
name: plan-validation-checklist
description: Validation criteria, checklists, and report format for feature implementation plans. Auto-invoke when validating plans, checking completeness, or assessing implementation readiness. Do NOT load for requirements gathering or implementation tasks.
---

# Plan Validation Checklist

Criteria and report format for validating feature implementation plans.

## Three Validation Dimensions

### 1. Completeness Check

**Required Sections**:

```
✓ Requirements Analysis
  - [ ] Feature description (clear, specific)
  - [ ] Examples of feature in action
  - [ ] Technical context and constraints
  - [ ] Other considerations (performance, security)

✓ Implementation Plan
  - [ ] High-level implementation strategy
  - [ ] Files to modify/create (with specific paths)
  - [ ] Implementation steps (broken into phases)
  - [ ] Validation criteria (specific, testable)

✓ Architecture Recommendations (if complexity ≥5)
  - [ ] Architectural approach documented
  - [ ] Addresses architectural concerns
  - [ ] Provides clear guidance

✓ Metadata
  - [ ] Complexity score documented
  - [ ] Recommended implementation agent specified
  - [ ] Source (GitHub issue, prompt, file) noted
```

### 2. Feasibility Review

**Dependencies & Libraries**:
- Check libraries/frameworks exist and are available
- Verify version compatibility
- Validate API usage patterns against current docs
- Flag deprecated or problematic dependencies

**Codebase Integration**:
- Verify mentioned files exist (Glob/Grep to locate)
- Check proposed patterns align with existing code
- Identify conflicts with current architecture
- Assess impact on existing features

**Technical Constraints**:
- Evaluate approach respects project constraints
- Check security implications
- Assess performance impact
- Verify compatibility requirements are realistic

**Breaking Changes**:
- If breaking changes proposed, verify necessity
- Check migration path is defined
- Assess impact scope accurately

### 3. Clarity Assessment

**Specificity**:
- File paths specific (not "update auth files")
- Steps actionable (not "implement feature")
- Validation criteria measurable (not "make it work")

**Completeness**:
- Implementation agent can understand without questions
- Edge cases and errors addressed
- Expected behavior clear for all scenarios

**Sequencing**:
- Phases logically ordered
- Dependencies between steps clear
- Obvious where to start

**Ambiguity Detection**:
- Flag vague language ("probably", "maybe", "should work")
- Identify placeholders (TBD, TODO, [insert here])
- Note unvalidated assumptions

## Validation Report Format

```markdown
## Validation Report

### Overall Status
**Decision**: ✅ APPROVED | ⚠️ APPROVED WITH NOTES | ❌ NEEDS REVISION

### Completeness Check
**Status**: PASS | FAIL
**Score**: X/Y required sections present

Issues:
- [ ] Missing: [section]
- [ ] Incomplete: [section] - [what's missing]

### Feasibility Review
**Status**: FEASIBLE | QUESTIONABLE | NOT FEASIBLE

Technical Concerns:
- ⚠️ [Concern with details]
- ✅ [Validated approach]
- ❌ [Blocking issue]

Dependencies Validated:
- ✅ [lib] - [verification result]
- ⚠️ [lib] - [warning]
- ❌ [lib] - [not found/incompatible]

### Clarity Assessment
**Status**: CLEAR | NEEDS CLARIFICATION

Clarity Issues:
- ❌ Step X: "[vague step]" - [what's needed]
- ⚠️ [minor ambiguity]
- ✅ [validated aspect]

Ambiguities Found:
- Line X: "[quote]" - [issue]

### Recommendations

**Must Address** (blocking):
1. [Critical issue]
2. [Critical issue]

**Should Consider** (improvements):
1. [Suggestion]

**Nice to Have** (optional):
1. [Enhancement]

### Summary
[2-3 sentence outcome and key actions]
```

## Decision Criteria

### ✅ APPROVED
- All completeness checks pass
- No critical feasibility concerns
- Plan clear enough for implementation
- Minor issues noted but not blocking

### ⚠️ APPROVED WITH NOTES
- Completeness mostly passes (1-2 minor gaps)
- Feasibility sound with noted concerns
- Clarity sufficient with improvements recommended
- Implementation can proceed, should address notes

### ❌ NEEDS REVISION
- Missing critical sections
- Major feasibility concerns (dependencies missing, approach won't work)
- Too vague for implementation (many ambiguities)
- Requires iteration before implementation

## Common Issues to Check

**Vague Language**:
- "Probably", "maybe", "should work", "might need"
- "Update files", "add functionality", "fix issues"
- "Good performance", "fast enough", "secure"

**Missing Details**:
- TBD, TODO, [insert], ???
- Empty sections or placeholders
- "See above" without clear reference

**Unrealistic Expectations**:
- Dependencies not in package.json
- Files that don't exist
- APIs that changed in newer versions
- Incompatible library combinations

**Ambiguous Steps**:
- "Update authentication" (which files?)
- "Add tests" (what kind? coverage target?)
- "Deploy changes" (what environment? rollback plan?)
