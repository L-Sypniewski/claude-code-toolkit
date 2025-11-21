---
name: pr-creator
description: Create comprehensive pull requests with detailed descriptions, issue references, and modern GitHub best practices. Use when asked to create PRs with well-documented changes. Focuses on small, focused PRs, clear problem-solution narratives, comprehensive testing documentation, and AI-assisted review integration. Analyzes commits and diffs to create informative PR descriptions with proper issue linking.
---

# PR Creator

Expert in creating comprehensive, well-documented pull requests that clearly communicate changes and enable effective collaboration.

## When to Use

- Creating pull requests for completed features
- Documenting changes for team review
- Linking work to GitHub issues
- Preparing PRs with testing and validation info
- Creating professional PR documentation

## Core Capabilities

1. **Change Analysis**: Systematic analysis of branch differences
2. **Context Research**: Understanding related documentation and best practices
3. **Issue Integration**: Proper linking to GitHub issues
4. **Problem-Solution Documentation**: Clear narrative of changes
5. **Testing Documentation**: Comprehensive validation information
6. **Small PR Focus**: Following modern best practices for PR size

## Small, Focused PRs (Modern Best Practice)

### Why Small PRs Matter

- **Faster reviews**: Easier and quicker to understand and approve
- **Reduced risk**: Less surface area for bugs or breaking changes
- **Better history**: Clearer project history with atomic changes
- **Easier rollbacks**: Individual features can be reverted independently

### Guidelines for PR Scope

- **Single purpose**: One specific feature, bug fix, or improvement per PR
- **Incremental development**: Break large features into sequential PRs
- **File guidance**: Provide reviewers with suggested review order
- **Dependency awareness**: Consider concurrent development impact

### When to Split PRs

Split when changes:
- Span multiple components or services
- Involve both frontend and backend
- Require refactoring across many files
- Include both code and configuration updates

## PR Creation Process

### 1. Scope Assessment & Planning

**Evaluate Changes**:
- Should changes be split into smaller PRs?
- Are there dependencies or sequencing needs?
- How does this impact concurrent work?
- Is incremental delivery possible?

### 2. Branch & Change Analysis

**Understand Modifications**:
- Run `git status` and `git diff` to see changes
- Compare branch with base branch
- Analyze commit history
- Identify scope and nature (feature, bugfix, refactor)

**Example Commands**:
```bash
# Check current status
git status

# See diff against base
git diff main

# Review commit history
git log main..HEAD --oneline

# See changed files
git diff --name-only main
```

### 3. Self-Review & Pre-Submission Validation

**Quality Checks**:
- [ ] Run comprehensive local testing
- [ ] Perform security review
- [ ] Validate code quality standards
- [ ] Check performance implications
- [ ] Use AI tools for initial review feedback

**Security Review**:
- Dependency diff analysis
- Code scanning results
- Secrets audit
- Vulnerability assessment

### 4. Issue Research & Context Gathering

**Research Activities**:
- Retrieve and analyze referenced GitHub issue
- Research relevant documentation
- Understand problem domain thoroughly
- Gather context about related components

### 5. Problem-Solution Narrative Development

Structure the story of changes:

**What the problem was**:
- Clear description of original issue
- Why it needed to be addressed
- Impact on users or system

**The initial implementation**:
- Document starting point
- Any previous approaches tried
- Why changes were needed

**The fixed implementation**:
- Explain final solution
- Key technical decisions
- Why this approach was chosen

**Remarks for enhancements**:
- Future improvement opportunities
- Known limitations
- Follow-up work needed

### 6. PR Description Structuring & Submission

**PR Title**:
- Clear, concise description of changes
- Follow project conventions (e.g., "feat:", "fix:", "refactor:")
- Reference issue number if applicable

**PR Description Structure**:

```markdown
## Summary
Brief overview of changes and motivation

## Problem
Clear description of the issue being solved

## Solution
Explanation of the approach and implementation

## Changes
- List of key modifications
- File-by-file summary if helpful
- Review order suggestions for complex PRs

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests verified
- [ ] Manual testing performed
- [ ] Security review completed

## Performance Impact
Expected performance implications (if any)

## Security Considerations
Security review results and considerations

## Breaking Changes
Any breaking changes and migration guide (if applicable)

## Related Issues
Fixes #123
Closes #456
Related to #789

## Screenshots/Demos
Visual evidence of changes (if UI-related)

## Reviewer Notes
- Guidance on review approach
- Areas requiring special attention
- Complexity notes
```

**Issue Referencing**:
- `Fixes #123` - Closes issue on merge
- `Closes #456` - Alternative syntax
- `Related to #789` - Links without closing
- `Part of #101` - For multi-PR features

**Labels & Assignees**:
- Add appropriate labels (feature, bugfix, etc.)
- Assign relevant reviewers
- Set priority if needed
- Link to projects or milestones

## PR Description Best Practices

### Clear Communication

- Use simple, direct language
- Explain "why" not just "what"
- Provide context for decisions
- Include examples where helpful

### Formatting

- Use markdown for readability
- Include code blocks with syntax highlighting
- Use checklists for testing/validation
- Add screenshots for visual changes

### Completeness

- Cover all modified areas
- Explain non-obvious changes
- Document any workarounds
- Note future work or tech debt

### Reviewer-Friendly

- Suggest review order for complex changes
- Highlight areas needing careful review
- Provide testing instructions
- Include relevant documentation links

## AI-Assisted Review Integration

### GitHub Copilot Integration

- Request Copilot review before submission
- Address AI-identified issues
- Document AI review findings
- Include in PR description

### AI Review Checklist

- [ ] AI initial review completed
- [ ] Critical issues addressed
- [ ] Suggestions evaluated
- [ ] Review findings documented

## Quality Checklist

Before creating PR:

- [ ] All commits have meaningful messages
- [ ] Code follows project conventions
- [ ] Tests added/updated as needed
- [ ] Documentation updated
- [ ] No debug code or console logs
- [ ] Dependencies properly declared
- [ ] Performance implications considered
- [ ] Security review completed
- [ ] Breaking changes documented
- [ ] Issue references included

## Common PR Types

### Feature PR

```markdown
## Summary
Add user authentication with OAuth2

## Problem
Users need secure login without managing passwords

## Solution
Implement OAuth2 with Google and GitHub providers

## Changes
- Add OAuth2 middleware
- Create auth routes
- Update user model
- Add security tests

Fixes #123
```

### Bug Fix PR

```markdown
## Summary
Fix memory leak in data processing pipeline

## Problem
Application crashes after processing large datasets

## Solution
Properly cleanup resources and add memory monitoring

## Changes
- Fix resource disposal in DataProcessor
- Add memory usage monitoring
- Update tests to catch leaks

Fixes #456
```

### Refactoring PR

```markdown
## Summary
Refactor authentication module for better testability

## Problem
Auth module tightly coupled, hard to test

## Solution
Extract interfaces, use dependency injection

## Changes
- Extract IAuthProvider interface
- Implement dependency injection
- Update tests to use mocks
- Improve documentation

Related to #789
```

## Integration with Other Skills

- **code-reviewer**: Review before PR creation
- **senior-engineer**: Implement changes before PR
- **architecture-advisor**: Ensure architectural soundness

## Anti-Patterns to Avoid

- Creating PRs without testing
- Vague or missing descriptions
- Including unrelated changes
- Ignoring code review feedback
- Forgetting to reference issues
- Overly large, unfocused PRs
- Missing testing documentation
- Unclear commit messages
