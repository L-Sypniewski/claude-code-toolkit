---
name: feature-planning
description: End-to-end feature implementation workflow from requirements to completion. Auto-invoke for feature-from-issue, feature-from-prompt, feature-from-file, and resume-feature commands. Handles complexity assessment, planning, validation, approval, implementation, and completion phases.
---

# Feature Planning Workflow

Centralized workflow for implementing features from any input source. Execute phases sequentially with mandatory user approval between each phase.

## Critical Rules

1. **Testing is NOT deferred** - Each phase includes its own tests; phase is not complete until tests pass
2. **Mandatory approval** - MUST wait for user approval after each phase before proceeding
3. **Success criteria required** - Phase is NOT complete until success criteria are met
4. **No time estimates** - Plans must NOT contain any time estimates
5. **Update before proceed** - MUST update plan file marking tasks complete before next phase
6. **Trackable state** - Plan must be structured so another agent can resume from any point
7. **Favor integration testing** - Use test containers, local instances (docker, CLI tools) over mocks when possible

Use sequential thinking, Context7, and microsoft-docs for latest documentation and best practices.

## Workflow Overview

| Phase | Name | Success Criteria |
|-------|------|------------------|
| 1 | Setup | Requirements verified, tracking initialized |
| 2 | Complexity Assessment | Score calculated, arch advisor decision made |
| 3 | Implementation Planning | Strategy defined, files identified, steps with tests defined |
| 4 | Plan File Creation | Plan file created at `plans/feature-[name]-[date].md` |
| 5 | Plan Validation | Validator approved or revisions completed |
| 6 | User Approval | User explicitly approved implementation |
| 7 | Implementation | All steps completed with passing tests |
| 8 | Completion | Feature verified working, user chose next steps |

## Phase Documentation

**For detailed phase instructions**, see:
- [phases/setup-and-assessment.md](phases/setup-and-assessment.md) - Phases 1-2
- [phases/planning-and-creation.md](phases/planning-and-creation.md) - Phases 3-4
- [phases/validation-and-approval.md](phases/validation-and-approval.md) - Phases 5-6
- [phases/implementation-and-completion.md](phases/implementation-and-completion.md) - Phases 7-8

## Templates

**For plan file structure**, see [templates/plan-file.md](templates/plan-file.md).

## Phase Execution Protocol

After completing each phase:

1. **Update plan file** - Mark completed tasks with `[x]`
2. **Report phase summary** to user
3. **Ask for approval**:
   ```
   Phase [N] complete. 
   
   Summary: [what was accomplished]
   Success criteria met: [list criteria and status]
   
   Proceed to Phase [N+1]?
   ```
4. **Wait for explicit user approval** before proceeding
5. If user says no: Stop and await further instructions

## Testing Strategy

**For testable features**, each implementation step should include:

1. **Test scaffolding** - Create test files alongside implementation
2. **Integration tests preferred** - Use real infrastructure:
   - Test containers (Docker)
   - Local database instances
   - CLI tools to spawn/teardown services
3. **Step not complete** until tests pass
4. **Test before moving on** - Don't batch tests at the end

**Infrastructure patterns**:
```bash
# Example: Start test database
docker run -d --name test-db -p 5432:5432 postgres:15

# Run tests against real database
npm test

# Cleanup
docker stop test-db && docker rm test-db
```

## Quick Reference

### Complexity Threshold

| Total Score | Action |
|-------------|--------|
| 0-4 | Proceed with `senior-engineer` only |
| 5-8 | Invoke `technical-architecture-advisor` first |

### Error Recovery

- **Planning fails**: Retry or manual planning
- **Validation fails critically**: Stop, require user intervention
- **Implementation interrupted**: Resume with `/resume-feature [plan-file]`
- **Tests fail**: Fix before proceeding, do not skip

## Integration with Other Skills

This workflow uses:
- **requirements-extraction** - For input normalization from any source
- **complexity-scoring** - For automated complexity assessment (Phase 2)
- **requirements-normalization** - Output format reference
- **plan-validation-checklist** - Validation criteria for Phase 5
- **workflow-orchestration** - General workflow patterns

## Key Principles

1. **User Visibility**: User sees every phase, approves each transition
2. **Test-Driven Phases**: Tests are part of each phase, not deferred
3. **Resumability**: Plan file tracks state for any agent to continue
4. **Quality Gates**: Phase incomplete until criteria met
5. **No Rushing**: No time estimates, focus on correctness
6. **Real Testing**: Favor integration tests with actual infrastructure
