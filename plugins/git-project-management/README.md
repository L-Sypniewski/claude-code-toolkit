# Git & Project Management Plugin

Git worktree management and project planning utilities with reusable skills for git workflow best practices and commit message conventions.

## Features

### Commands

- **/create_worktree** - Create new git worktrees for parallel development branches
- **/merge_worktree** - Merge and clean up git worktrees after feature completion

### Skills

**Skills are automatically activated by agents when relevant:**

- **git-workflow-best-practices** - Comprehensive Git workflow best practices covering branching strategies (Git Flow, GitHub Flow, Trunk-Based Development), merging strategies, conflict resolution, and worktree management
- **commit-conventions** - Commit message conventions following Conventional Commits specification, including proper commit types, scopes, descriptions, and best practices for clear version control history

## Installation

This plugin is part of the Claude Code Toolkit marketplace. Install via:

```bash
/plugin marketplace add <marketplace-url>
/plugin install git-project-management
```

## Usage

### Git Worktree Workflow

**Starting Parallel Work:**
1. Use **/create_worktree** to create a new worktree for a feature branch
2. Work independently in the new worktree without affecting your main branch
3. Multiple worktrees allow simultaneous work on different features

**Completing Work:**
1. Use **/merge_worktree** to merge changes back to the main branch
2. Automatically cleans up the worktree directory
3. Maintains clean git history

## Benefits

- **Parallel Development**: Work on multiple features simultaneously without branch switching
- **Clean Workflows**: Isolated worktrees prevent contamination between features
- **Efficient Merging**: Streamlined merge and cleanup process

## Best Practices

- Create worktrees for each significant feature or bug fix
- Use descriptive branch names for clarity
- Clean up worktrees promptly after merging

## Git Worktree Advantages

- No need to stash or commit WIP when switching contexts
- Fast branch switching (no checkout delays)
- Run tests simultaneously on different branches
- Avoid conflicts from incomplete work

## License

MIT
