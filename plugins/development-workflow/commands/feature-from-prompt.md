---
description: Implement a feature from a text description with intelligent planning and validation
argument-hint: <feature-description>
---

# Feature From Prompt

Implement features from text descriptions with intelligent planning, validation, and execution.

## Usage

```bash
/feature-from-prompt Add dark mode toggle to settings with persistent user preference
```

The entire prompt after the command becomes the feature description.

## How It Works

This command is a thin wrapper that:
1. Takes the feature description from $ARGUMENTS
2. Delegates requirements analysis to `feature-issue-analyzer` agent
3. Invokes the `feature-planning` skill for the complete workflow

## Input Phase

### 1. Delegate to feature-issue-analyzer Agent

Use Task tool to invoke `feature-issue-analyzer` with:
- Feature description: $ARGUMENTS
- Source type: "prompt"

The analyzer will:
- Analyze the text description
- Structure into FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS format
- Return normalized requirements with completeness status

### 2. Handle Incomplete Requirements

If `feature-issue-analyzer` returns `COMPLETENESS: INCOMPLETE`:
- Invoke `feature-requirements-clarifier` agent with the gaps
- Get enriched requirements via clarifying questions
- Continue with complete requirements

### 3. Continue with Feature Planning Workflow

Pass the normalized requirements and source metadata to the `feature-planning` skill workflow:
- Source type: "prompt"
- Source reference: None
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
- **Source field**: "Prompt"
- **Related Issue**: N/A (no GitHub issue)

## When to Use

**Use feature-from-prompt when**:
- Quick feature implementation without creating an issue
- Feature is defined in another system (Jira, Linear, etc.)
- Ad-hoc feature request in conversation
- Prototyping or exploratory work
- Feature details are clearer in direct description

**Use feature-from-issue when**:
- Feature is tracked in GitHub issues
- You want analysis posted to issue for team visibility

## Writing Good Prompts

### Be Specific

**Bad**: "Add search"

**Good**: "Add search functionality to product catalog with filters for category, price range, and brand. Show results as user types with 300ms debounce."

### Include Context

**Bad**: "Optimize performance"

**Good**: "Optimize product list API performance. Current response time is 2s, target is <200ms. Consider adding database indexes and pagination."

### Mention Technical Constraints

**Bad**: "Add authentication"

**Good**: "Add JWT-based authentication to Express.js API. Use bcrypt for password hashing, store refresh tokens in Redis with 7-day expiration."

## Example Workflow

```bash
$ /feature-from-prompt Add export to CSV functionality for user reports

[Analyzer structures requirements]
Requirements Analysis Complete!
- Feature: CSV export for user reports
- Source: Prompt

[Continues with feature-planning workflow...]
- Complexity Score: 3/8
- Architecture advisor: Not needed
- Plan created: plans/feature-csv-export-20260105.md
- Validation: ✅ APPROVED

Ready to proceed with implementation?
> Yes, proceed with senior-engineer

[Implementation...]

Implementation complete!
- Plan: plans/feature-csv-export-20260105.md
- Status: Completed

What would you like to do next?
> Create pull request

[PR created: #42]
Done! Pull request created: #42
```

## Related Commands

- `/feature-from-issue` - Same workflow, GitHub issue input
- `/feature-from-file` - Same workflow, file input
- `/resume-feature` - Resume interrupted workflow from plan file

## See Also

- `feature-planning` skill - Complete workflow documentation
- `feature-issue-analyzer` agent - Requirements normalization
- `complexity-scoring` skill - Complexity assessment details
