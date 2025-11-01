Merge the current worktree back to the target branch and clean up: $ARGUMENTS

Parse arguments to extract:
- Target branch (required, first argument like 'master' or 'develop')

Execute these steps:
1. Check if we're currently in a worktree (not the main repo)
2. Get current branch name with `git branch --show-current`
3. Check for uncommitted changes with `git status`
4. If there are uncommitted changes stop process and ask user to commit changes.
5. Push the current branch to origin
6. Navigate back to the main repository directory
7. Switch to the target branch and pull latest changes
8. Merge the current branch into the target branch
9. Remove the worktree with `git worktree remove <worktree-path>`
10. Ask if I should delete the feature branch locally

Handle any merge conflicts by explaining the resolution process.