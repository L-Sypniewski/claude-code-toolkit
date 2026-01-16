---
description: Resume an interrupted feature workflow from its plan file
argument-hint: <plan-file-path>
---

# Resume Feature Workflow

Resume a feature implementation workflow that was interrupted or paused. Reads the plan file to determine current state and continues from the appropriate checkpoint.

## Usage

```bash
/resume-feature plans/feature-dark-mode-20260105.md
```

The command reads the plan file, analyzes the current state, and continues the workflow from where it left off.

## When to Use

**Use resume-feature when**:
- Implementation was interrupted (system crash, user stopped work)
- You paused at approval gate to review plan
- Implementation agent failed mid-execution
- You want to continue after manual changes to plan
- Switching between features (resume later)

## How It Works

The command analyzes the plan file to determine:
1. **Current phase**: Analysis / Planning / Validation / Implementation / Completed
2. **Completion status**: What's done, what's pending
3. **Next action**: What should happen next

Then continues the workflow from the appropriate checkpoint.

## Workflow States and Resumption

### State 1: Analysis Complete, Planning Not Started

**Plan file shows**:
- Requirements analysis section filled
- Implementation plan section empty
- Status: "Analysis"

**Resumption**:
1. Read requirements from plan file
2. Calculate complexity score (skip if already in plan)
3. Continue to planning phase (senior-engineer + optional arch advisor)
4. Proceed with normal workflow from there

### State 2: Planning Complete, Validation Not Started

**Plan file shows**:
- Requirements and implementation plan filled
- Validation results section empty
- Status: "Planning"

**Resumption**:
1. Delegate to feature-plan-validator
2. Update plan with validation results
3. Get user approval
4. Continue to implementation

### State 3: Validation Complete, Implementation Not Started

**Plan file shows**:
- Requirements, plan, and validation results filled
- Implementation steps unchecked
- Status: "Planning" or "Validation"

**Resumption**:
1. Show plan summary to user
2. Get user approval (if not already given)
3. Delegate to implementation agent
4. Continue monitoring implementation

### State 4: Implementation In Progress

**Plan file shows**:
- Some implementation step checkboxes marked
- Others still unchecked
- Status: "Implementation"
- Progress notes showing last completed step

**Resumption**:
1. Show current progress summary
2. Identify last completed step
3. Ask user: "Continue implementation from step X?"
4. If yes: Delegate to implementation agent with context about resumption
5. Agent reads plan, sees completed steps, continues from next step

### State 5: Implementation Complete

**Plan file shows**:
- All implementation steps checked
- Status: "Completed" or "Ready for Review"

**Resumption**:
1. Show completion summary
2. Offer post-implementation options:
   - Code review (if not done)
   - Create PR (if not done)
   - Update related issue (if applicable)
3. Execute user choices

### State 6: Fully Complete

**Plan file shows**:
- All steps completed
- PR created
- Code review done
- Status: "Completed"

**Resumption**:
1. Show summary: "This feature is complete!"
2. Display links to PR, issue, etc.
3. No further action needed
4. Optional: Archive or move plan file

## Detailed Workflow

### 1. Read and Parse Plan File

```bash
# Verify file exists
if ! [ -f "$ARGUMENTS" ]; then
    echo "Error: Plan file not found: $ARGUMENTS"
    exit 1
fi
```

Use Read tool to access plan file. Parse:
- **Status** field
- **Current Phase** field
- Checkbox states in Implementation Steps
- Validation Results section presence
- Completion markers

### 2. Determine Current State

Create state assessment:
```markdown
## Workflow State Assessment

**File**: $ARGUMENTS
**Status**: [from plan file]
**Current Phase**: [from plan file]

**Completed**:
- [x] Requirements analysis
- [x] Complexity assessment
- [x] Implementation planning
- [?] Plan validation
- [?] User approval
- [?] Implementation
- [ ] Completion

**Next Action**: [Determined action]
```

Show this to user for transparency.

### 3. Ask User Confirmation

Use AskUserQuestion:
```
Question: "Resume feature workflow from [next-action]?"
Options:
- "Yes, continue workflow" (Recommended)
- "No, let me review the plan first"
- "No, I've made manual changes - re-validate plan"
- "No, start implementation from scratch"
```

If user chooses to review:
- Show plan file location
- Wait for user to say they're ready
- Re-ask confirmation

If user says they made changes:
- Re-run validation on modified plan
- Update validation results
- Continue with normal workflow

If user wants fresh start:
- Ask which phase to restart from
- Clear appropriate sections
- Continue from that phase

### 4. Resume Workflow

Based on determined state and user confirmation:

**Resume Planning**:
```
Continuing implementation planning...
[Delegates to senior-engineer and optional arch advisor]
[Updates plan file with planning results]
[Continues to validation phase]
```

**Resume Validation**:
```
Validating implementation plan...
[Delegates to feature-plan-validator]
[Updates plan with validation results]
[Asks for user approval]
```

**Resume Implementation**:
```
Resuming implementation from step X...
[Shows current progress]
[Delegates to implementation agent with resume context]

Context provided to agent:
- Plan file path
- Last completed step
- Instruction to continue from next unchecked step
- Note: This is a resumption, check completed items before proceeding
```

**Complete Workflow**:
```
Implementation already complete!
Offering post-implementation options...
[Code review / PR creation / Issue update]
```

### 5. Continue Normal Workflow

From the resumption point, follow the standard workflow:
- If resuming implementation: Monitor progress, update todos
- If resuming validation: Validate, get approval, implement
- If completing: Offer post-impl options

### 6. Update TodoWrite

Create or update TodoWrite based on current state:
```
- [x] Requirements analysis (from plan file)
- [x] Complexity assessment (from plan file)
- [x] Implementation planning (from plan file)
- [x] Plan validation (if done)
- [ ] User approval (if pending)
- [ ] Implementation (mark in_progress)
- [ ] Completion
```

## Edge Cases

### Modified Plan File

If user manually edited plan file:
- Re-validate plan before continuing
- Ensure modifications don't break workflow
- Update validation results section

### Corrupted Plan File

If plan file is malformed or missing critical sections:
```
Error: Plan file appears corrupted or incomplete.
Missing required sections: [list]

Options:
1. Restore from backup (if available)
2. Start new workflow with same requirements
3. Manual recovery (specify what to fix)
```

### Conflicting State

If plan says "Completed" but implementation steps aren't all checked:
```
Warning: Plan status is "Completed" but some steps appear incomplete.

Completed: X/Y implementation steps

Options:
1. Mark remaining steps as complete (if done outside plan)
2. Resume implementation for incomplete steps
3. Review plan file to fix inconsistency
```

### Multiple Interruptions

If workflow was resumed multiple times:
- Plan file tracks "Last Updated" timestamp
- Implementation notes show resumption points
- All valid - just continue from current state

## Best Practices

### Before Resuming

1. **Review plan file** - Check what was done, what's pending
2. **Check codebase** - Verify no conflicts with other changes
3. **Understand context** - Read implementation notes for any issues encountered

### During Resumption

1. **Trust the plan** - Checkboxes indicate what's done
2. **Let agent continue** - Don't re-implement completed steps
3. **Monitor progress** - Watch for issues from the interruption

### After Resumption

1. **Verify completeness** - Ensure nothing was skipped
2. **Test thoroughly** - Interrupted work may have edge cases
3. **Update plan** - Document the resumption and any challenges

## Examples

### Example 1: Interrupted During Implementation

```bash
$ /resume-feature plans/feature-dark-mode-20260105.md

Reading plan file: plans/feature-dark-mode-20260105.md

Workflow State Assessment:
- Status: Implementation
- Current Phase: Implementation
- Progress: 5/12 implementation steps completed
- Last update: 2026-01-05 14:32:00

Next Action: Resume implementation from Step 6

Resume feature workflow from Step 6?
> Yes, continue workflow

Resuming implementation...
[Senior engineer agent invoked]

Implementation agent: Reading plan file...
Implementation agent: Steps 1-5 already complete
Implementation agent: Continuing from Step 6...
[Progress continues]
```

### Example 2: Paused at Approval Gate

```bash
$ /resume-feature plans/feature-auth-improvements-20260105.md

Reading plan file: plans/feature-auth-improvements-20260105.md

Workflow State Assessment:
- Status: Planning
- Current Phase: Validation
- Progress: Plan validated (✅ APPROVED)
- Last update: 2026-01-05 10:15:00

Next Action: Get user approval to proceed with implementation

Resume feature workflow from user approval?
> Yes, continue workflow

Plan Summary:
- Feature: JWT Authentication Improvements
- Complexity: 6/8 (architecture advisor involved)
- Files to modify: 8 files
- Implementation phases: 3 phases
- Recommended agent: senior-engineer
- Validation: ✅ APPROVED

Ready to proceed with implementation?
> Yes, proceed with senior-engineer

[Implementation begins]
```

### Example 3: After Manual Changes

```bash
$ /resume-feature plans/feature-pagination-20260105.md

Reading plan file: plans/feature-pagination-20260105.md

Workflow State Assessment:
- Status: Planning
- Current Phase: Validation
- Last update: 2026-01-05 09:45:00

Next Action: Re-validate plan (manual changes detected)

Resume feature workflow from re-validation?
> Yes, I made changes - re-validate plan

Re-validating modified plan...
[feature-plan-validator invoked]

Validation Results:
- Completeness: PASS
- Feasibility: FEASIBLE
- Clarity: CLEAR

Overall: ✅ APPROVED WITH NOTES
Note: Modified approach for pagination state looks good

Ready to proceed with implementation?
> Yes, proceed with senior-engineer

[Implementation begins]
```

## Integration with Other Commands

**Initial creation**:
```bash
/feature-from-issue 42        # Creates plan, starts workflow
[... user interrupts ...]
/resume-feature plans/feature-[name]-[date].md   # Continues
```

**Multiple resumptions**:
```bash
/resume-feature plans/feature-x.md    # Resume once
[... work on something else ...]
/resume-feature plans/feature-x.md    # Resume again later
```

**After implementation**:
```bash
/resume-feature plans/feature-x.md    # Resume completed feature
> Offer code review / PR creation
```

## Error Messages

### File Not Found
```
Error: Plan file not found: plans/missing.md

Available plan files in plans/:
- feature-dark-mode-20260105.md
- feature-auth-20260104.md

Check the file path and try again.
```

### Invalid Plan File
```
Error: File is not a valid feature plan: plans/other-doc.md

Required sections missing:
- Feature title (# Feature: ...)
- Status field
- Requirements Analysis section

This doesn't appear to be a feature plan file.
```

### Cannot Determine State
```
Warning: Unable to determine workflow state from plan file.

The plan file exists but current state is unclear.

Manual inspection needed:
- File: plans/feature-x.md
- Review Status and Current Phase fields
- Check Implementation Steps checkboxes
- Verify Validation Results section

Would you like to start fresh or manually specify resumption point?
```

## Tips for Successful Resumption

1. **Don't modify plan structure** - Agents expect specific format
2. **Update checkboxes accurately** - Checked = actually complete
3. **Add notes for context** - Helps agents understand state
4. **Keep Status field current** - Indicates overall progress
5. **Don't skip validation** - If plan changed, re-validate
6. **Review before resuming** - Understand what was done

## Resumability Design

The entire feature workflow system is designed for resumability:
- **Plan file is single source of truth** - All state persists there
- **Checkboxes track progress** - Granular completion indicators
- **Notes document decisions** - Context for resumption
- **Status fields indicate phase** - Easy to determine next action
- **Validation is rerunnable** - Can re-validate modified plans
- **Agents read state** - Implementation agent checks completed items

This means workflows can be:
- Interrupted at any point
- Resumed hours or days later
- Resumed by different users (shared plan file)
- Resumed after manual changes
- Resumed multiple times

The workflow is robust, stateful, and designed for real-world interruptions.

## See Also

- `feature-planning` skill - Complete workflow documentation
- `feature-issue-analyzer` agent - Requirements normalization
- `feature-plan-validator` agent - Plan validation
- `senior-engineer` agent - Implementation agent
