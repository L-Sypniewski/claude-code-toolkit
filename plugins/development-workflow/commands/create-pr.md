---
description: Create a pull request for the current branch against master with informative description
argument-hint: ""
---

Create a pull request for the current branch against master. Use both commit messages and diff on changed files to create a concise yet informative PR description.

WORKFLOW:
1. Get current branch name
2. Check git status and ensure branch is pushed to remote
3. Get commit history since diverging from master
4. Analyze both commit messages AND file diffs to understand all changes
5. Create PR with:
   - Clear title summarizing the changes
   - Concise yet informative summary section with bullet points (synthesized from commits and diffs)
   - Test plan section
   - Claude Code attribution

BASE BRANCH: master
