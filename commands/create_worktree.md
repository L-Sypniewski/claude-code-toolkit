Create a new Git worktree with branch name and optional path: $ARGUMENTS

First, parse the arguments to extract:
- Branch name (required, first argument)
- Worktree path (optional, second argument - if not provided, use ../project-{branch-name})

Then execute these steps:
1. Verify we're in a Git repository
2. Show current worktrees with `git worktree list`
3. Create the worktree using `git worktree add <path> -b <branch-name>`
4. Navigate to the new worktree directory
5. List directory contents and check for dependency files (package.json, requirements.txt, etc.)
6. Install dependencies for each service:
   - Run `npm ci` in astro/ directory (frontend dependencies)
   - Run `npm ci` in strapi/ directory (CMS dependencies)
   - Run `npm ci` in tests/ directory (test dependencies)
7. Provide instructions on how to start working in the new worktree
If any errors occur, explain them and suggest solutions.