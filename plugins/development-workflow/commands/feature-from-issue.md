---
description: Implement a feature from a GitHub issue with intelligent planning and validation
argument-hint: <issue-number>
---

# Feature From GitHub Issue

Implement a feature from GitHub issue #$ARGUMENTS.

## Instructions

1. **Extract repository info**:
   ```bash
   git remote get-url origin
   ```
   Parse owner and repository name from the URL.

2. **Extract requirements** using `requirements-extraction` skill:
   - Source type: "github-issue"
   - Issue number: $ARGUMENTS
   - Follow [sources/github-issue.md](../skills/requirements-extraction/sources/github-issue.md)

3. **If requirements INCOMPLETE**: Invoke `feature-requirements-clarifier` agent to resolve gaps.

4. **Execute feature planning** using `feature-planning` skill:
   - Pass normalized requirements
   - Source metadata: `github-issue`, Issue #$ARGUMENTS
   - Follow all phases with mandatory user approval

5. **On completion**: Offer to post completion comment to the GitHub issue.

## Source Metadata

- **Type**: github-issue
- **Reference**: Issue #$ARGUMENTS
- **Plan file**: `plans/feature-[title]-[date].md`
- **Related**: Link PR back to issue when created
