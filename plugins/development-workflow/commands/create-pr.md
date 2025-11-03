Create a pull request for the current branch against master.

WORKFLOW:
1. Get current branch name
2. Check git status and ensure branch is pushed to remote
3. Get commit history since diverging from master
4. Analyze all changes in the branch
5. Create PR with:
   - Clear title summarizing the changes
   - Summary section with bullet points
   - Test plan section
   - Claude Code attribution

BASE BRANCH: master
