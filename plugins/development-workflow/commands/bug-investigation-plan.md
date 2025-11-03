Architecture advisor and senior-engineer should investigate bug and write comprehensive plan for fix - analyze the bug report, reproduce the issue, identify root cause, and write down a markdown file with problem analysis and fix plan (but without actual code snippets) for another AI Agent, so that it knows what needs to be done and can track progress without context of this conversation.

MANDATORY WORKFLOW:
1. Create a markdown file named `bug-fix-plan-[short-description]-[timestamp].md` in `.plans/` directory
2. Document investigation findings including:
   - Bug symptoms and reproduction steps
   - Root cause analysis
   - Affected components and files
   - Proposed fix strategy with step-by-step plan
   - Testing approach to verify the fix
3. **CRITICAL: Update the plan file IMMEDIATELY after completing each step** - do not wait until the end
4. Mark progress status for each step AS YOU GO (pending/in-progress/completed)
5. Document any blockers or changes to the approach AS THEY OCCUR
6. **IMPORTANT: Plan must be kept current in real-time in case work is interrupted**

Use sequential thinking, context7 and microsoft-docs to solve the problem using latest documentation and best practices.
Bug report or symptoms to investigate:
$ARGUMENTS