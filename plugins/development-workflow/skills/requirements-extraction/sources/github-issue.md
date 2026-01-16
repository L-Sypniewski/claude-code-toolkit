# GitHub Issue Extraction

Extract and normalize feature requirements from a GitHub issue.

## Input

- **Issue number**: The GitHub issue ID
- **Repository**: Extracted from `git remote get-url origin`

## Extraction Steps

1. **Get repository info**:
   Read the git remote origin URL and parse owner and repository name.

2. **Fetch issue details** (prefer `gh` CLI, fallback to GitHub MCP if `gh` fails):
   
   **Primary method - gh CLI**: Fetch issue title, body, labels, assignees, and comments.
   **Fallback - GitHub MCP tools** if `gh` CLI fails:
   - Issue title and body
   - Labels and assignees
   - Comments for additional context

3. **Extract structured content**:
   - Parse issue body for requirements
   - Identify examples from descriptions
   - Pull technical context from comments
   - Note any constraints mentioned

4. **Post analysis comment** to issue (optional):
   - Summarize extracted requirements
   - Note any gaps identified

## Output

```markdown
## FEATURE
[Extracted from issue title and body]

## EXAMPLES
[From issue description, acceptance criteria]

## DOCUMENTATION
[Technical references from comments, linked issues]

## OTHER CONSIDERATIONS
[Labels, constraints, mentioned edge cases]

---
**SOURCE**: github-issue
**REFERENCE**: Issue #[number]
**COMPLETENESS**: [COMPLETE | INCOMPLETE]
**CRITICAL GAPS**: [List if incomplete]
```

## Error Handling

- **Issue not found**: Return error with issue number
- **API failure**: Suggest `/feature-from-prompt` as fallback
- **Private repo**: Check authentication status
