---
name: git-workflow-best-practices
description: Comprehensive Git workflow best practices, branching strategies, and version control patterns for efficient collaborative development
author: Claude Code Toolkit
---

# Git Workflow Best Practices

This skill provides comprehensive Git workflow guidance and best practices that are automatically activated during version control operations.

## Purpose

Automatically activated when:
- Creating branches
- Managing worktrees
- Merging changes
- Resolving conflicts
- Planning git workflows
- Reviewing version control strategies

## Branching Strategies

### Git Flow

**Overview:**
- Main branches: `main` (production) and `develop` (integration)
- Supporting branches: `feature/*`, `release/*`, `hotfix/*`
- Best for: Projects with scheduled releases

**Branch Types:**

**Main Branches:**
- `main` - Production-ready code, always deployable
- `develop` - Integration branch for next release

**Supporting Branches:**
- `feature/*` - New features from `develop`
- `release/*` - Release preparation from `develop`
- `hotfix/*` - Emergency fixes from `main`

**Workflow:**
```
1. Create feature branch from develop
   git checkout -b feature/user-authentication develop

2. Work on feature, commit regularly
   git add .
   git commit -m "feat: add login form"

3. Merge back to develop when complete
   git checkout develop
   git merge --no-ff feature/user-authentication
   git branch -d feature/user-authentication

4. Create release branch when ready
   git checkout -b release/1.0.0 develop

5. Merge release to main and develop
   git checkout main
   git merge --no-ff release/1.0.0
   git tag -a v1.0.0
   git checkout develop
   git merge --no-ff release/1.0.0
```

### GitHub Flow

**Overview:**
- Single main branch: `main`
- Feature branches deployed directly via pull requests
- Best for: Continuous deployment, web applications

**Workflow:**
```
1. Create feature branch from main
   git checkout -b add-user-profile main

2. Make commits
   git commit -m "Add user profile page"

3. Push and create pull request
   git push -u origin add-user-profile

4. Review, test, and merge to main
   Deploy automatically after merge

5. Delete feature branch
   git branch -d add-user-profile
```

**Characteristics:**
- Simple and streamlined
- Everything in main is deployable
- Feature branches live short term
- Rapid iteration and deployment

### Trunk-Based Development

**Overview:**
- All developers work on `main` (trunk)
- Very short-lived feature branches (< 1 day)
- Best for: Experienced teams, continuous integration

**Workflow:**
```
1. Create short-lived feature branch
   git checkout -b quick-fix main

2. Commit and push frequently
   git commit -m "Fix validation bug"
   git push origin quick-fix

3. Create PR and merge immediately
   (After CI passes)

4. Delete branch immediately
   git branch -d quick-fix
```

**Key Practices:**
- Feature flags for incomplete features
- Rigorous automated testing
- Continuous integration
- Frequent merges to main

### GitLab Flow

**Overview:**
- Combines Git Flow and GitHub Flow
- Environment branches: `main`, `staging`, `production`
- Best for: Multi-environment deployments

**Branch Structure:**
- `main` - Development branch
- `staging` - Pre-production testing
- `production` - Production code
- `feature/*` - Feature branches

**Workflow:**
```
1. Feature development
   git checkout -b feature/new-api main

2. Merge feature to main
   (After review)

3. Deploy main to staging
   git checkout staging
   git merge main

4. Deploy staging to production
   git checkout production
   git merge staging
```

## Branch Naming Conventions

### Standard Prefixes

**Feature Branches:**
- `feature/` or `feat/` - New features
- Examples: `feature/user-authentication`, `feat/payment-integration`

**Bug Fix Branches:**
- `bugfix/` or `fix/` - Bug fixes
- Examples: `bugfix/login-error`, `fix/validation-bug`

**Hotfix Branches:**
- `hotfix/` - Emergency production fixes
- Examples: `hotfix/security-patch`, `hotfix/critical-bug`

**Release Branches:**
- `release/` - Release preparation
- Examples: `release/v1.2.0`, `release/2024-Q1`

**Refactoring Branches:**
- `refactor/` - Code refactoring
- Examples: `refactor/user-service`, `refactor/api-layer`

**Documentation Branches:**
- `docs/` - Documentation updates
- Examples: `docs/api-guide`, `docs/readme-update`

**Experimental Branches:**
- `experiment/` or `spike/` - Experiments or spikes
- Examples: `experiment/new-architecture`, `spike/graphql-api`

### Naming Best Practices

**Do:**
- Use lowercase and hyphens: `feature/user-profile`
- Be descriptive: `fix/payment-gateway-timeout`
- Include ticket number: `feature/JIRA-123-user-auth`
- Use consistent prefixes across team

**Don't:**
- Use spaces: `feature/user profile` ❌
- Be vague: `fix/bug` ❌
- Use special characters: `feature/user@profile` ❌
- Mix naming conventions: `Feature/UserProfile` ❌

## Commit Best Practices

### Atomic Commits

**Principles:**
- One logical change per commit
- Each commit should be buildable
- Commits should tell a story
- Easy to revert if needed

**Good Example:**
```
feat: add email validation to signup form
test: add unit tests for email validator
docs: update API documentation for signup endpoint
```

**Bad Example:**
```
Update files (contains validation, tests, docs, unrelated fixes)
```

### Commit Frequency

**Guidelines:**
- Commit frequently (multiple times per day)
- Commit at logical breakpoints
- Commit before context switching
- Don't commit broken code to shared branches
- Commit before risky operations

### Commit Message Structure

See the `commit-conventions` skill for detailed commit message guidelines.

## Merging Strategies

### Merge Types

**1. Merge Commit (--no-ff)**
```bash
git merge --no-ff feature/new-feature
```
**Pros:**
- Preserves branch history
- Clear feature boundaries
- Easy to revert entire feature

**Cons:**
- Creates merge commits
- Can clutter history

**Use When:**
- Want to preserve feature branch history
- Need clear feature boundaries
- Working with Git Flow

**2. Fast-Forward Merge**
```bash
git merge --ff-only feature/new-feature
```
**Pros:**
- Linear history
- No merge commits
- Clean history

**Cons:**
- Loses branch context
- Harder to revert features

**Use When:**
- Branch is up-to-date with target
- Want linear history
- Using trunk-based development

**3. Squash and Merge**
```bash
git merge --squash feature/new-feature
git commit -m "feat: complete feature description"
```
**Pros:**
- Clean, linear history
- One commit per feature
- Easy to review history

**Cons:**
- Loses detailed commit history
- Harder to debug
- Can't revert individual commits

**Use When:**
- Feature has messy commit history
- Want one commit per feature
- Using GitHub Flow

**4. Rebase and Merge**
```bash
git checkout feature/new-feature
git rebase main
git checkout main
git merge --ff-only feature/new-feature
```
**Pros:**
- Linear history
- Preserves commits
- No merge commits

**Cons:**
- Rewrites history
- Can be complex with conflicts
- Dangerous on shared branches

**Use When:**
- Want linear history with preserved commits
- Working on personal branches
- Team is comfortable with rebasing

## Conflict Resolution

### Prevention

**Best Practices:**
- Pull/fetch frequently
- Communicate with team about overlapping work
- Use feature flags for large changes
- Keep feature branches short-lived
- Rebase frequently on long-lived branches

### Resolution Process

**Step 1: Understand the Conflict**
```bash
git status  # See conflicting files
git diff    # See conflict markers
```

**Step 2: Choose Resolution Strategy**
- Manual resolution (most common)
- Use "ours" version: `git checkout --ours file.txt`
- Use "theirs" version: `git checkout --theirs file.txt`
- Use merge tool: `git mergetool`

**Step 3: Resolve Conflicts**
```
<<<<<<< HEAD (your changes)
current code
=======
incoming code
>>>>>>> branch-name (their changes)
```

**Step 4: Test and Commit**
```bash
# After resolving
git add resolved-file.txt
git commit  # Complete the merge

# Or for rebase
git rebase --continue
```

### Conflict Resolution Tips

**Do:**
- Understand both sides of conflict
- Test after resolution
- Review entire file, not just conflict markers
- Communicate with other developer if unclear
- Preserve intent of both changes when possible

**Don't:**
- Blindly accept one side
- Resolve without understanding
- Skip testing
- Leave conflict markers
- Commit without reviewing

## Git Worktree Best Practices

### When to Use Worktrees

**Good Use Cases:**
- Working on multiple features simultaneously
- Comparing implementations side-by-side
- Hot-fixing while working on feature
- Running tests on different branches
- Reviewing pull requests while coding

### Worktree Management

**Creating Worktrees:**
```bash
# Create worktree for feature
git worktree add ../myproject-feature feature/new-ui

# Create worktree for hotfix
git worktree add ../myproject-hotfix -b hotfix/security-fix main
```

**Listing Worktrees:**
```bash
git worktree list
```

**Removing Worktrees:**
```bash
# Remove worktree directory
rm -rf ../myproject-feature

# Prune worktree metadata
git worktree prune
```

### Worktree Best Practices

**Do:**
- Use descriptive directory names
- Clean up after merging
- Keep worktrees separate from main repository
- Use for short-term parallel work

**Don't:**
- Share worktree directories
- Nest worktrees
- Keep old worktrees around indefinitely
- Use for long-term branches

## Git History Management

### Interactive Rebase

**Use Cases:**
- Clean up commit history before PR
- Combine related commits
- Reorder commits logically
- Edit commit messages
- Split large commits

**Interactive Rebase Commands:**
```bash
git rebase -i HEAD~3  # Last 3 commits

# Commands in editor:
# pick = keep commit
# reword = change commit message
# edit = amend commit
# squash = combine with previous
# fixup = like squash, discard message
# drop = remove commit
```

### Git History Best Practices

**Do:**
- Rebase personal branches before PR
- Clean up work-in-progress commits
- Keep history readable and logical
- Write clear commit messages

**Don't:**
- Rebase shared branches
- Force push to protected branches
- Rewrite public history
- Rebase without understanding implications

## Tagging

### Version Tags

**Semantic Versioning:**
```bash
# Create annotated tag
git tag -a v1.2.3 -m "Release version 1.2.3"

# Push tags
git push origin v1.2.3
git push origin --tags  # All tags
```

**Tag Naming:**
- Use semantic versioning: `v1.2.3`
- Use date-based: `release-2024-01-15`
- Be consistent across project

### Lightweight vs Annotated Tags

**Annotated Tags (Recommended):**
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
```
- Contains metadata (tagger, date, message)
- Can be verified (GPG signed)
- Shows in `git show`

**Lightweight Tags:**
```bash
git tag v1.0.0
```
- Just a pointer to commit
- No additional metadata
- Use for temporary markers

## Remote Repository Management

### Remote Best Practices

**Fetching:**
```bash
git fetch origin  # Update remote tracking branches
git fetch --all   # Update all remotes
git fetch --prune # Remove deleted remote branches
```

**Pulling:**
```bash
git pull origin main  # Fetch and merge
git pull --rebase origin main  # Fetch and rebase
```

**Pushing:**
```bash
git push origin feature/new-feature
git push -u origin feature/new-feature  # Set upstream
git push --force-with-lease  # Safer force push
```

### Force Push Guidelines

**Never Force Push:**
- Protected branches (main, develop)
- Shared feature branches
- Public branches others depend on

**Safe to Force Push:**
- Personal feature branches after rebase
- Branches only you work on
- With `--force-with-lease` to prevent data loss

## Git Workflow Checklist

### Starting New Work

- [ ] Pull latest changes: `git pull origin main`
- [ ] Create feature branch: `git checkout -b feature/name`
- [ ] Verify branch: `git status`

### During Development

- [ ] Commit frequently with clear messages
- [ ] Pull/rebase regularly: `git pull --rebase origin main`
- [ ] Push to remote regularly
- [ ] Keep commits atomic and logical

### Before Creating PR

- [ ] Rebase on latest main: `git rebase main`
- [ ] Clean up commit history if needed
- [ ] Run tests locally
- [ ] Review all changes: `git diff main`
- [ ] Push to remote: `git push origin feature/name`

### After PR Approval

- [ ] Merge to main (via PR)
- [ ] Pull latest main: `git pull origin main`
- [ ] Delete feature branch: `git branch -d feature/name`
- [ ] Delete remote branch: `git push origin --delete feature/name`

## Common Git Pitfalls

**Avoid:**
- Committing large binary files
- Committing secrets or credentials
- Force pushing to shared branches
- Long-lived feature branches (> 2 weeks)
- Working directly on main/develop
- Skipping commit messages
- Mixing unrelated changes in one commit
- Not pulling before starting work
- Committing broken code to shared branches
- Complex merge commits without proper resolution

## Emergency Procedures

### Undo Last Commit (Not Pushed)
```bash
git reset --soft HEAD~1  # Keep changes staged
git reset HEAD~1         # Keep changes unstaged
git reset --hard HEAD~1  # Discard changes
```

### Recover Deleted Branch
```bash
git reflog  # Find commit SHA
git checkout -b recovered-branch <SHA>
```

### Undo Pushed Commit
```bash
git revert <commit-SHA>  # Create new commit that undoes changes
git push origin main
```

### Fix Wrong Branch
```bash
# Committed to main instead of feature branch
git branch feature/my-feature  # Create branch at current commit
git reset --hard origin/main   # Reset main to remote
git checkout feature/my-feature  # Switch to feature branch
```

## Usage by Agents

This skill is automatically available to:
- All agents when performing git operations
- Specifically useful during worktree management
- Referenced during branch creation and merging
- Applied during code review for git workflow compliance

The skill ensures consistent and effective git workflows across all development activities.
