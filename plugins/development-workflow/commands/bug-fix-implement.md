---
description: Implement bug fix following the investigation plan and track progress while implementing
argument-hint: <bug-fix-plan-file>
---

Architecture advisor and senior-engineer must implement bug fix following the investigation plan and track progress while implementing.

MANDATORY WORKFLOW:
1. Read the bug fix plan markdown file: $ARGUMENTS
2. Update the plan file status to "in-progress" before starting implementation
3. Follow the fix strategy step-by-step from the plan
4. **CRITICAL: Update the plan file IMMEDIATELY AFTER EACH STEP with:**
   - Step completion status (do not batch updates)
   - Any deviations from original plan
   - Unexpected findings or complications
   - Additional steps needed
5. Run tests to verify the fix works
6. Update the plan file with final status and test results

Use sequential thinking, context7 and microsoft-docs to solve the problem using latest documentation and best practices.
**IMPORTANT: The plan file MUST be kept up-to-date in real-time throughout the implementation process. Update after EACH action, not at the end, in case work is interrupted.**