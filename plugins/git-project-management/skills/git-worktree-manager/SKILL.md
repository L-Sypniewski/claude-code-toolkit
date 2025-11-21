---
name: git-worktree-manager
description: Manage Git worktrees for parallel development workflows. Use when creating, merging, or managing Git worktrees for working on multiple branches simultaneously. Provides streamlined worktree creation with automatic dependency installation, worktree merging with cleanup, and safe parallel development workflows. Use for /create_worktree and /merge_worktree commands or when users need to work on multiple features concurrently.
---

# Git Worktree Manager

Specialized Git worktree management for parallel development workflows, enabling efficient multi-branch work.

## When to Use

- Creating worktrees for parallel feature development
- Merging completed worktrees back to main branch
- Managing multiple concurrent development streams
- Isolating experimental changes
- Working on hotfixes while feature development continues

## Core Capabilities

1. **Worktree Creation**: Create new worktrees with branch setup
2. **Dependency Installation**: Automatic dependency setup in new worktrees
3. **Worktree Merging**: Safe merge and cleanup workflows
4. **Conflict Resolution**: Guidance for handling merge conflicts
5. **Cleanup Management**: Proper worktree removal and branch cleanup

## Git Worktrees Overview

### What are Worktrees?

Git worktrees allow multiple working directories for a single repository, enabling:
- Parallel development on different branches
- Quick context switching without stashing
- Independent dependency installations per branch
- Isolated build artifacts and configurations

### Benefits

- **No Stashing**: Switch contexts without saving/restoring changes
- **Parallel Builds**: Run tests on one branch while developing another
- **Clean Separation**: Each worktree has its own working directory
- **Faster Switching**: No need to rebuild dependencies

## Worktree Creation

### Natural Language Triggers

Users typically request worktree creation with phrases like:
- "Create a worktree for feature/new-ui"
- "Set up a worktree for working on the authentication feature"
- "I need to work on a hotfix in parallel, create a worktree"

**Parameters to gather**:
- `branch-name` (required): Name for new branch
- `path` (optional): Custom worktree path (default: `../project-{branch-name}`)

### Creation Process

**1. Parse Arguments**:
```bash
branch_name=$1  # Required
worktree_path=${2:-"../project-$branch_name"}  # Optional with default
```

**2. Verify Git Repository**:
```bash
# Check if in git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not in a git repository"
    exit 1
fi
```

**3. Show Current Worktrees**:
```bash
# Display existing worktrees
git worktree list
```

**4. Create Worktree**:
```bash
# Create new worktree with new branch
git worktree add "$worktree_path" -b "$branch_name"

# Navigate to new worktree
cd "$worktree_path"
```

**5. Check Dependencies**:
```bash
# List directory contents
ls -la

# Check for dependency files
if [ -f "package.json" ]; then
    echo "Found Node.js project"
fi

if [ -f "requirements.txt" ]; then
    echo "Found Python project"
fi

# Similar checks for other project types
```

**6. Install Dependencies**:

**Node.js Projects**:
```bash
# Frontend dependencies
if [ -d "frontend" ] && [ -f "frontend/package.json" ]; then
    cd frontend && npm ci && cd ..
fi

# Backend dependencies
if [ -d "backend" ] && [ -f "backend/package.json" ]; then
    cd backend && npm ci && cd ..
fi

# Root dependencies
if [ -f "package.json" ]; then
    npm ci
fi
```

**Python Projects**:
```bash
# Create virtual environment if needed
if [ -f "requirements.txt" ]; then
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi
```

**Multi-Service Projects** (example pattern):
```bash
# Install dependencies for each service
services=("astro" "strapi" "tests")

for service in "${services[@]}"; do
    if [ -d "$service" ] && [ -f "$service/package.json" ]; then
        echo "Installing dependencies for $service..."
        cd "$service"
        npm ci
        cd ..
    fi
done
```

**7. Provide Usage Instructions**:
```
Worktree created successfully!

Location: $worktree_path
Branch: $branch_name

To start working:
1. cd $worktree_path
2. Start development servers
3. Make your changes
4. Commit and push when ready

To merge back:
Use /merge_worktree <target-branch> when complete
```

## Worktree Merging

### Natural Language Triggers

Users typically request worktree merging with phrases like:
- "Merge my worktree back to main"
- "I'm done with this feature, merge and clean up the worktree"
- "Merge this worktree into develop"

**Parameters to gather**:
- `target-branch` (required): Branch to merge into (e.g., 'master', 'main', 'develop')

### Merging Process

**1. Parse Arguments**:
```bash
target_branch=$1  # Required
```

**2. Verify Worktree Context**:
```bash
# Check if in a worktree (not main repo)
if git rev-parse --git-dir | grep -q "\.git/worktrees"; then
    echo "In worktree - proceeding"
else
    echo "Not in a worktree - aborting"
    exit 1
fi
```

**3. Get Current Branch**:
```bash
current_branch=$(git branch --show-current)
echo "Current branch: $current_branch"
```

**4. Check for Uncommitted Changes**:
```bash
if [ -n "$(git status --porcelain)" ]; then
    echo "Error: You have uncommitted changes"
    echo "Please commit or stash your changes first"
    git status
    exit 1
fi
```

**5. Push Current Branch**:
```bash
# Push to origin
git push origin "$current_branch"

# Or push with upstream tracking
git push -u origin "$current_branch"
```

**6. Navigate to Main Repository**:
```bash
# Get main repository path
main_repo=$(git rev-parse --git-dir | sed 's/\.git\/worktrees\/.*//')

# Navigate to main repo
cd "$main_repo"
```

**7. Switch to Target Branch**:
```bash
# Checkout target branch
git checkout "$target_branch"

# Pull latest changes
git pull origin "$target_branch"
```

**8. Merge Feature Branch**:
```bash
# Merge with no-fast-forward to preserve history
git merge --no-ff "$current_branch" -m "Merge $current_branch into $target_branch"

# Or use fast-forward if preferred
git merge "$current_branch"
```

**9. Push Merged Changes**:
```bash
git push origin "$target_branch"
```

**10. Remove Worktree**:
```bash
# Get worktree path
worktree_path=$(git worktree list | grep "$current_branch" | awk '{print $1}')

# Remove worktree
git worktree remove "$worktree_path"

# Or force remove if needed
git worktree remove --force "$worktree_path"
```

**11. Ask About Branch Deletion**:
```
Worktree merged and removed successfully!

Would you like to delete the feature branch '$current_branch'?
- Local branch: git branch -d $current_branch
- Remote branch: git push origin --delete $current_branch

Reply 'yes' to delete both, or handle manually.
```

## Conflict Resolution

### When Conflicts Occur

If merge conflicts arise:

**1. Identify Conflicts**:
```bash
# Git will show conflicted files
git status

# View conflict details
git diff
```

**2. Resolution Process**:
```
Merge conflict detected!

Conflicted files:
[list of files from git status]

To resolve:
1. Open each conflicted file
2. Look for conflict markers (<<<<<<<, =======, >>>>>>>)
3. Resolve conflicts by choosing or combining changes
4. Remove conflict markers
5. Stage resolved files: git add <file>
6. Continue merge: git merge --continue

Or abort merge: git merge --abort
```

**3. Manual Resolution Steps**:
```bash
# For each conflicted file
vim conflicted_file.txt  # or preferred editor

# After resolving
git add conflicted_file.txt

# After all conflicts resolved
git merge --continue

# Or commit if needed
git commit -m "Resolve merge conflicts from $current_branch"
```

## Best Practices

### Worktree Creation

- **Naming Convention**: Use descriptive branch names (e.g., `feature/oauth`, `bugfix/memory-leak`)
- **Location**: Keep worktrees in parallel directories for easy access
- **Dependencies**: Always install dependencies after creation
- **Initial Commit**: Make small initial commit to establish branch

### Worktree Usage

- **Regular Commits**: Commit frequently in worktree
- **Push Often**: Push changes to backup and enable collaboration
- **Stay Updated**: Regularly merge target branch into feature branch
- **Clean Working Tree**: Keep working directory clean

### Merging

- **Pre-Merge Checks**: Ensure all tests pass before merging
- **Update First**: Pull latest target branch before merging
- **Review Changes**: Review all changes before finalizing merge
- **Clean Up**: Remove worktrees and branches after merge

### Parallel Development

- **Independent Changes**: Use worktrees for independent features
- **Avoid Conflicts**: Coordinate with team on file changes
- **Test Isolation**: Each worktree can have different test runs
- **Build Isolation**: Separate build artifacts per worktree

## Common Workflows

### Feature Development

```bash
# 1. Create worktree for feature
/create_worktree feature/new-auth ../auth-work

# 2. Develop in worktree
cd ../auth-work
# ... make changes, commit, test ...

# 3. Merge when complete
/merge_worktree main
```

### Hotfix While Developing

```bash
# Already working on feature in worktree
cd ~/project-feature

# Need urgent hotfix - create hotfix worktree
/create_worktree hotfix/critical-bug ../hotfix-work

# Work on hotfix
cd ../hotfix-work
# ... fix bug, test, commit ...

# Merge hotfix
/merge_worktree main

# Return to feature work
cd ~/project-feature
# Continue feature development
```

### Parallel Feature Testing

```bash
# Feature 1 in worktree 1
cd ~/project-feature-1
npm test  # Run tests

# Feature 2 in worktree 2  (simultaneously)
cd ~/project-feature-2
npm test  # Run different tests

# Main branch also available
cd ~/project
npm start  # Run main app
```

## Error Handling

### Common Issues

**Worktree Already Exists**:
```
Error: worktree already exists

Solution:
1. List worktrees: git worktree list
2. Remove existing: git worktree remove <path>
3. Try creation again
```

**Uncommitted Changes**:
```
Error: uncommitted changes prevent merge

Solution:
1. Review changes: git status
2. Commit: git commit -am "message"
3. Or stash: git stash
4. Try merge again
```

**Merge Conflicts**:
```
Error: merge conflicts

Solution:
1. Resolve conflicts manually
2. Stage resolved files
3. Complete merge: git merge --continue
4. Or abort: git merge --abort
```

**Branch Already Exists**:
```
Error: branch already exists

Solution:
1. Use different branch name
2. Or checkout existing: git checkout <branch>
3. Or force create: git checkout -B <branch>
```

## Quality Checklist

Before merging worktree:

- [ ] All changes committed
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Branch pushed to origin
- [ ] Target branch updated
- [ ] Merge conflicts resolved (if any)
- [ ] Build successful

## Integration with Other Skills

- **senior-engineer**: Implement features in worktrees
- **code-reviewer**: Review before merging worktrees
- **pr-creator**: Create PRs from worktree branches

## Anti-Patterns to Avoid

- Creating worktrees for tiny changes (overkill)
- Forgetting to install dependencies in new worktrees
- Merging without testing
- Leaving stale worktrees around
- Not pushing worktree branches (loss risk)
- Merging with uncommitted changes
- Ignoring merge conflicts
- Not cleaning up after merge
