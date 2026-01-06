---
description: Implement a feature from a text description with intelligent planning and validation
argument-hint: <feature-description>
---

# Feature From Prompt

Comprehensive workflow for implementing features from text descriptions. Same intelligent planning and validation as feature-from-issue, but takes direct text input instead of GitHub issue.

## Usage

```bash
/feature-from-prompt Add dark mode toggle to settings with persistent user preference
```

The entire prompt after the command becomes the feature description.

## Workflow

This command follows the **same workflow as feature-from-issue** with one key difference: the input source.

### Input Phase Difference

**Instead of**:
- Fetching GitHub issue via API
- Posting analysis comment to issue

**This command**:
- Takes feature description from $ARGUMENTS
- Delegates to feature-issue-analyzer with source type "prompt"
- Analyzer structures the prompt text into FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS format
- No GitHub comment posting (no issue to comment on)

### Identical Phases

All other phases are **exactly the same**:

1. **Requirements Analysis**: feature-issue-analyzer normalizes the prompt
2. **Complexity Assessment**: Same 0-8 point scoring system
3. **Implementation Planning**: senior-engineer + optional arch advisor
4. **Plan File Creation**: `plans/feature-[title]-[date].md`
5. **Plan Validation**: feature-plan-validator checks completeness/feasibility/clarity
6. **User Approval**: Review plan and approve implementation
7. **Implementation**: Delegate to approved agent
8. **Completion**: Optional code review / PR creation

## Detailed Workflow

### PHASE 1: Requirements Analysis

1. **Delegate to feature-issue-analyzer Agent**
   Use Task tool to invoke `feature-issue-analyzer` with:
   - Feature description: $ARGUMENTS
   - Source type: "prompt"

   The analyzer will:
   - Analyze the text description
   - Structure into FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS format
   - Ask clarifying questions if description is vague
   - Return normalized requirements

2. **Create TodoWrite for Progress Tracking**
   (Same as feature-from-issue)

### PHASE 2-8: Identical to feature-from-issue

Follow the exact same workflow as `/feature-from-issue` from Phase 2 onwards:

- Calculate complexity score (0-8 points)
- Delegate to planning agents (senior-engineer + optional arch advisor based on complexity)
- Create plan file with all sections
- Validate plan (completeness, feasibility, clarity)
- Get user approval
- Delegate to implementation agent
- Monitor progress via plan file
- Offer post-implementation options (code review, PR creation)

**Plan file structure** is identical except:
- **Source** field shows: "Prompt" instead of "GitHub Issue #X"
- No "Related Issue" in metadata section
- No GitHub comment posting in completion phase

## Comparison with feature-from-issue

| Aspect | feature-from-issue | feature-from-prompt |
|--------|-------------------|---------------------|
| **Input** | GitHub issue number | Text description |
| **Requirements** | Fetched from GitHub API | Provided directly |
| **Analysis Comment** | Posted to issue | Not applicable |
| **Complexity Scoring** | ✓ Same algorithm | ✓ Same algorithm |
| **Planning** | ✓ Same agents | ✓ Same agents |
| **Validation** | ✓ Same validator | ✓ Same validator |
| **Plan File** | Source: GitHub Issue #X | Source: Prompt |
| **Implementation** | ✓ Same process | ✓ Same process |
| **Completion** | Can update issue | No issue to update |

## Example Invocations

### Simple Feature
```bash
/feature-from-prompt Add pagination to the user list page with 25 items per page
```

### Complex Feature
```bash
/feature-from-prompt Implement real-time notifications using WebSockets. Users should see toast notifications for new messages, mentions, and system alerts. Notifications should persist in a notification center with read/unread status. Include browser notification permission handling and fallback to polling for unsupported browsers.
```

### Feature with Technical Context
```bash
/feature-from-prompt Add Redis caching layer for product catalog API endpoints. Cache product details for 5 minutes, category listings for 15 minutes. Implement cache invalidation on product updates. Use Redis cluster-aware client with connection pooling.
```

## Tips for Writing Good Prompts

### Be Specific
**Bad**: "Add search"
**Good**: "Add search functionality to product catalog with filters for category, price range, and brand. Show results as user types with 300ms debounce."

### Include Context
**Bad**: "Optimize performance"
**Good**: "Optimize product list API performance. Current response time is 2s, target is <200ms. Consider adding database indexes on category_id and price columns, and implement pagination."

### Mention Technical Constraints
**Bad**: "Add authentication"
**Good**: "Add JWT-based authentication to Express.js API. Use bcrypt for password hashing, store refresh tokens in Redis with 7-day expiration. Integrate with existing PostgreSQL user table."

### Specify Examples or Edge Cases
**Bad**: "Handle errors better"
**Good**: "Improve error handling in payment flow. Handle: network timeouts (retry 3 times), invalid card (show user-friendly message), insufficient funds (suggest adding payment method), API errors (log and alert team)."

## When to Use This vs feature-from-issue

**Use feature-from-issue when**:
- Feature is tracked in GitHub issues
- You want analysis posted to issue for team visibility
- Issue has discussion/comments with additional context
- Want to link PR back to issue automatically

**Use feature-from-prompt when**:
- Quick feature implementation without creating an issue
- Feature is defined in another system (Jira, Linear, etc.)
- Ad-hoc feature request in conversation
- Prototyping or exploratory work
- Feature details are clearer in direct description than scattered across issue comments

## Integration with Other Commands

**After feature-from-prompt completes**:
- Can create PR with `/create-pr` (won't auto-link to issue since there isn't one)
- Can manually create GitHub issue to track if needed
- Can convert to feature-from-file workflow by saving plan file

**Resumability**:
- If interrupted, use `/resume-feature plans/feature-[name]-[date].md`
- Plan file preserves all state regardless of input source

## Error Handling

**Vague Descriptions**:
- Analyzer will ask clarifying questions
- User provides additional context
- Can iterate until requirements are clear

**Missing Technical Details**:
- Analyzer makes reasonable assumptions where safe
- Flags critical gaps for user validation
- Planning agents may request more detail

**Otherwise**: Same error handling as feature-from-issue (planning failures, validation issues, implementation errors all handled identically)

## Key Benefits

1. **No GitHub Issue Required**: Implement features quickly without issue overhead
2. **Same Quality Process**: Full planning, validation, and implementation workflow
3. **Flexibility**: Accepts any level of detail, refines through clarification
4. **Composability**: Output (plan file) is identical format, enables consistent processes

## Example Workflow

```bash
$ /feature-from-prompt Add export to CSV functionality for user reports

[Analyzer structures requirements]
Requirements Analysis Complete!
- Feature: CSV export for user reports
- Complexity Score: 3/8
- Architecture advisor: Not needed

Creating implementation plan...
[Senior engineer creates plan]

Plan created: plans/feature-csv-export-20260105.md

[Validator checks plan]
Validation: ✅ APPROVED

Ready to proceed with implementation?
> Yes, proceed with senior-engineer

[Implementation begins]
Implementing feature according to plan...
[Progress updates in real-time]

Implementation complete!
- Plan: plans/feature-csv-export-20260105.md
- Status: Completed

What would you like to do next?
> Create pull request

[PR created: #42]
Done! Pull request created: #42
```
