---
name: feature-planning
description: End-to-end feature implementation workflow from requirements to completion. Auto-invoke for feature-from-issue, feature-from-prompt, feature-from-file, and resume-feature commands. Handles complexity assessment, planning, validation, approval, implementation, and completion phases.
---

# Feature Planning Workflow

Centralized workflow for implementing features from any input source. This skill defines the complete planning and implementation process used by all feature commands.

## Prerequisites

Before invoking this workflow, the caller must:
1. Obtain requirements from input source (GitHub issue, prompt, or file)
2. Delegate to `feature-issue-analyzer` agent for normalization
3. Provide source metadata (type: "github-issue" | "prompt" | "file", reference: issue number/file path/none)

### Handling Incomplete Requirements

If `feature-issue-analyzer` returns `COMPLETENESS: INCOMPLETE`:
1. Invoke `feature-requirements-clarifier` agent with the gaps
2. The clarifier will ask targeted questions to resolve ambiguities
3. Get enriched requirements with user clarifications
4. Continue workflow with complete requirements

See `requirements-clarification` skill for question patterns.

## Workflow Overview

The workflow consists of 8 phases:

| Phase | Name | Description |
|-------|------|-------------|
| 1 | Setup | Verify requirements, initialize tracking |
| 2 | Complexity Assessment | Score 0-8, determine arch advisor need |
| 3 | Implementation Planning | Delegate to senior-engineer (+ arch advisor if needed) |
| 4 | Plan File Creation | Generate `plans/feature-[name]-[date].md` |
| 5 | Plan Validation | Run feature-plan-validator, handle revisions |
| 6 | User Approval | Present summary, get go/no-go decision |
| 7 | Implementation | Delegate to agent, monitor progress |
| 8 | Completion | Verify done, offer code review/PR options |

## Phase Documentation

**For detailed phase instructions**, see:
- [phases/setup-and-assessment.md](phases/setup-and-assessment.md) - Phases 1-2
- [phases/planning-and-creation.md](phases/planning-and-creation.md) - Phases 3-4
- [phases/validation-and-approval.md](phases/validation-and-approval.md) - Phases 5-6
- [phases/implementation-and-completion.md](phases/implementation-and-completion.md) - Phases 7-8

## Templates

**For plan file structure**, see [templates/plan-file.md](templates/plan-file.md).

## Quick Reference

### Complexity Threshold

| Total Score | Action |
|-------------|--------|
| 0-4 | Proceed with `senior-engineer` only |
| 5-8 | Invoke `technical-architecture-advisor` first |

### Key User Interactions

1. **Phase 5**: If NEEDS REVISION → Ask: revise/retry/override
2. **Phase 6**: Ask: proceed/different agent/review/change plan
3. **Phase 8**: Ask: code review/create PR/update issue/manual

### Error Recovery

- **Planning fails**: Retry or manual planning
- **Validation fails critically**: Stop, require user intervention
- **Implementation interrupted**: Resume with `/resume-feature [plan-file]`
- **Any point**: Plan file preserves all state

## Integration with Other Skills

This workflow uses:
- **complexity-scoring** - For automated complexity assessment (Phase 2)
- **requirements-normalization** - Output format reference for requirements analysis
- **plan-validation-checklist** - Validation criteria for Phase 5
- **workflow-orchestration** - General workflow patterns

## Key Principles

1. **User Visibility**: User sees every phase, can review at each gate
2. **Interactive Decision-Making**: User approves plan, chooses post-implementation actions
3. **Context Savings**: Implementation runs in separate agent, main thread tracks progress
4. **Resumability**: Plan file as single source of truth enables resuming interrupted workflows
5. **Quality Gates**: Validation before implementation prevents wasted effort
6. **Intelligent Complexity Detection**: Automatically involves architecture advisor when needed
7. **Source Agnostic**: Same workflow regardless of input source (issue/prompt/file)
