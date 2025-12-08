---
name: git-worktree-patterns
description: Git worktree patterns for parallel development. Use when working on multiple branches simultaneously.
---

# Git Worktree Patterns

Multiple working directories per repo, each on different branch. Use for: urgent hotfixes, PR reviews, parallel testing, side-by-side comparison.

## Commands

```bash
# Create
git worktree add ../project-feature-a feature/a
git worktree add -b feature/new ../project-new

# List
git worktree list

# Remove
git worktree remove ../project-feature-a
git worktree prune  # cleanup stale refs
```

## Organization

Sibling dirs, nested `.worktrees/`, or centralized `/worktrees/`. Name clearly: `project-feature-auth`, `project-review`, `project-hotfix-bug`.

## Best Practices

- Remove when done to avoid clutter
- Don't checkout same branch in multiple worktrees
- Don't manually delete (use `git worktree remove`)
- Use `git worktree prune` for stale refs
