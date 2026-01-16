---
description: Implement a feature from a GitHub issue with intelligent planning and validation
argument-hint: <issue-number>
---

# Feature From GitHub Issue

Implement features from GitHub issues with intelligent planning, validation, and execution.

## Usage

```bash
/feature-from-issue 123
```

Where `123` is the GitHub issue number in the current repository.

## How It Works

This command is a thin wrapper that:
1. Extracts repository information from git
2. Delegates requirements analysis to `feature-issue-analyzer` agent
3. Invokes the `feature-planning` skill for the complete workflow

## Input Phase

### 1. Extract Repository Information

```bash
git remote get-url origin
```

Parse owner and repository name from the remote URL.

### 2. Delegate to feature-issue-analyzer Agent

Use the Task tool to invoke `feature-issue-analyzer` with:
- Issue number: $ARGUMENTS
- Repository owner and name from step 1
- Source type: "github-issue"

The analyzer will:
- Fetch the GitHub issue details
- Create structured requirements (FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS)
- Post analysis comment to the GitHub issue
- Return normalized requirements with completeness status

### 3. Handle Incomplete Requirements

If `feature-issue-analyzer` returns `COMPLETENESS: INCOMPLETE`:
- Invoke `feature-requirements-clarifier` agent with the gaps
- Get enriched requirements
- Continue with complete requirements

### 4. Continue with Feature Planning Workflow

Pass the normalized requirements and source metadata to the `feature-planning` skill workflow:
- Source type: "github-issue"
- Source reference: Issue #$ARGUMENTS
- Requirements: [structured output from analyzer]

The `feature-planning` skill handles all subsequent phases:
- Complexity assessment (0-8 scoring)
- Implementation planning (senior-engineer + optional arch advisor)
- Plan file creation
- Plan validation
- User approval
- Implementation delegation
- Completion options

## Output

- **Plan file**: `plans/feature-[title]-[date].md`
- **Source field**: "GitHub Issue #[number]"
- **Related Issue**: Linked in plan metadata
- **GitHub Comments**: Analysis posted to issue

## When to Use

**Use feature-from-issue when**:
- Feature is tracked in GitHub issues
- You want analysis posted to issue for team visibility
- Issue has discussion/comments with additional context
- Want to link PR back to issue automatically

## Error Handling

**GitHub API Failures**:
- If issue fetch fails: Show error with issue number
- Suggest using `/feature-from-prompt` as fallback with issue content

**Issue Not Found**:
- Show error: "Issue #X not found in repository"
- Verify issue number and repository

## Example Workflow

```bash
$ /feature-from-issue 42

Fetching GitHub issue #42...
[Analyzer fetches and structures requirements]

Requirements Analysis Complete!
- Feature: Dark Mode Toggle in Settings
- Source: GitHub Issue #42
- Analysis posted to issue

[Continues with feature-planning workflow...]
- Complexity Score: 4/8
- Architecture advisor: Not needed
- Plan created: plans/feature-dark-mode-toggle-20260105.md
- Validation: ✅ APPROVED

Ready to proceed with implementation?
> Yes, proceed with senior-engineer

[Implementation...]

Implementation complete!
- Plan: plans/feature-dark-mode-toggle-20260105.md
- GitHub Issue: #42

What would you like to do next?
> Create pull request

[PR created: #43]
Done! Pull request #43 created and linked to issue #42
```

## Related Commands

- `/feature-from-prompt` - Same workflow, text input instead of GitHub issue
- `/feature-from-file` - Same workflow, file input instead of GitHub issue
- `/resume-feature` - Resume interrupted workflow from plan file

## See Also

- `feature-planning` skill - Complete workflow documentation
- `feature-issue-analyzer` agent - Requirements normalization
- `complexity-scoring` skill - Complexity assessment details
