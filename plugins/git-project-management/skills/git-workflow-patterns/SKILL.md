---
name: git-workflow-patterns
description: Standard git workflows, branching strategies, and best practices for version control. Use when working with git branches, commits, or collaborative development workflows.
---

# Git Workflow Patterns

This skill provides proven patterns for effective version control with Git.

## Branching Strategies

### Git Flow

Classic branching model for release-based workflows:

```
main (production)
  └─ develop (integration)
       ├─ feature/user-auth
       ├─ feature/payment
       └─ release/1.2.0
```

**Branches**:
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features
- `release/*`: Release preparation
- `hotfix/*`: Urgent production fixes

**When to use**: Traditional release cycles, multiple versions in production

### GitHub Flow

Simplified workflow for continuous deployment:

```
main (production)
  ├─ feature/user-auth
  ├─ feature/payment
  └─ bugfix/login-error
```

**Workflow**:
1. Create branch from `main`
2. Make changes and commit
3. Open pull request
4. Review and discuss
5. Deploy for testing
6. Merge to `main`

**When to use**: Continuous deployment, single production version

### Trunk-Based Development

Minimal branching, frequent integration:

```
main (trunk)
  ├─ short-lived-branch-1 (< 1 day)
  └─ short-lived-branch-2 (< 1 day)
```

**Rules**:
- Branches live < 24 hours
- Commit to main frequently
- Use feature flags for incomplete features
- Strong CI/CD pipeline required

**When to use**: High-velocity teams, mature CI/CD

## Commit Best Practices

### Commit Message Format

Follow conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples**:
```
feat(auth): add OAuth2 login support

Implemented OAuth2 authentication flow with Google and GitHub providers.
Added callback handlers and token refresh logic.

Closes #123
```

```
fix(api): resolve race condition in user creation

The user creation endpoint had a race condition when multiple requests
arrived simultaneously. Added proper locking mechanism.

Fixes #456
```

### Atomic Commits

Each commit should:
- Represent one logical change
- Pass all tests
- Be deployable (in trunk-based development)
- Have a clear, descriptive message

```bash
# ❌ Bad - multiple unrelated changes
git commit -m "Fixed bug and added feature"

# ✅ Good - separate logical changes
git commit -m "fix(auth): resolve login timeout issue"
git commit -m "feat(profile): add avatar upload"
```

## Pull Request Workflow

### PR Creation

1. **Keep PRs small**: < 400 lines of changes ideal
2. **Self-review first**: Review your own changes before requesting review
3. **Write clear description**: What, why, and how
4. **Link issues**: Reference related issues/tickets
5. **Add tests**: Include test coverage
6. **Update docs**: Keep documentation in sync

### PR Template

```markdown
## Description
[What changes does this PR introduce?]

## Motivation
[Why are these changes needed?]

## Changes
- Change 1
- Change 2
- Change 3

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-reviewed the changes
- [ ] Documentation updated
- [ ] No breaking changes (or migration guide provided)

Closes #issue_number
```

## Git Worktree Workflows

### Parallel Development

Work on multiple features simultaneously:

```bash
# Main working directory
/project (main branch)

# Additional worktrees
/project-worktrees/feature-a (feature/a branch)
/project-worktrees/feature-b (feature/b branch)
/project-worktrees/hotfix (hotfix/critical branch)
```

**Use cases**:
- Urgent hotfix while working on feature
- Review PR without stashing changes
- Run tests on one branch while developing on another
- Compare implementations side by side

### Worktree Commands

```bash
# Create new worktree
git worktree add ../project-feature-a feature/a

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../project-feature-a

# Prune stale worktrees
git worktree prune
```

## Conflict Resolution

### Merge vs Rebase

**Merge**:
```bash
git checkout feature
git merge main
```
- Preserves history
- Shows when features were integrated
- Can create complex history graph

**Rebase**:
```bash
git checkout feature
git rebase main
```
- Linear history
- Cleaner git log
- Rewrites history (don't rebase public branches)

### Conflict Resolution Steps

1. **Identify conflicts**:
```bash
git status  # Shows conflicted files
```

2. **Understand both sides**:
```bash
git diff --conflict=diff3  # Shows base, ours, theirs
```

3. **Resolve conflicts**:
- Open conflicted files
- Look for conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
- Choose correct version or merge manually
- Remove conflict markers

4. **Test resolution**:
```bash
# Run tests to verify resolution
npm test

# Continue merge/rebase
git add .
git commit  # or git rebase --continue
```

## Git Hygiene

### Before Committing

- [ ] Run linter
- [ ] Run tests
- [ ] Review changes with `git diff`
- [ ] Stage only relevant changes
- [ ] Write clear commit message

### Regular Maintenance

```bash
# Keep branches up to date
git fetch --prune

# Clean merged branches
git branch --merged | grep -v "main\|develop" | xargs git branch -d

# Clean untracked files (be careful!)
git clean -fd --dry-run  # Preview
git clean -fd             # Execute
```

## Advanced Patterns

### Feature Flags

Deploy incomplete features safely:

```javascript
if (featureFlags.isEnabled('new-ui')) {
  return <NewUI />;
}
return <OldUI />;
```

Benefits:
- Deploy to production without exposing feature
- Gradual rollout
- Easy rollback
- A/B testing

### Branch Protection Rules

Protect important branches:

- Require pull request reviews
- Require status checks to pass
- Require branches to be up to date
- Restrict force pushes
- Restrict deletions

## Integration with Plugin

Works with:
- `/create_worktree` command for parallel development
- `/merge_worktree` command for worktree cleanup
- Project planning and task management
