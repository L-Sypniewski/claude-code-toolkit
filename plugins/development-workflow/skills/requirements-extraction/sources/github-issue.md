# GitHub Issue Extraction

Extract and normalize feature requirements from a GitHub issue.

## Input

- **Issue number**: The GitHub issue ID
- **Repository**: Extracted from `git remote get-url origin`

## Extraction Steps

1. **Get repository info**:

   Extract the repository owner and name from the current git remote configuration.

   Parse owner and repository name.

2. **Fetch issue details** (prefer `gh` CLI, fallback to GitHub MCP if `gh` fails):

   **Primary method - gh CLI**:

   Use `gh issue view` to fetch the issue's title, body, labels, assignees, and comments in JSON format.
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
