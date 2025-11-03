Architecture advisor and senior-engineer should write plan for code refactoring - analyze the issues and write down a markdown file with a problem analysis and a plan (but without actual code snippets) for another AI Agent, so that it knows what needs to be done and can track progress without context of this conversation. The refactoring should improve code quality, maintainability, and performance without changing external behavior. Adhere to SOLID and YAGNI principles - avoid over-engineering or unnecessary abstractions.

MANDATORY WORKFLOW:

1. Create a markdown file named `refactoring-plan-[description]-[timestamp].md` in `.plans/` directory
2. Document analysis including:
   - Current code structure and problems
   - Refactoring goals and benefits
   - Step-by-step refactoring strategy
   - Files and components affected
   - Testing approach
3. **CRITICAL: Update the plan file IMMEDIATELY after completing each analysis step** - do not wait until the end
4. Mark progress status for each step AS YOU GO (pending/in-progress/completed)
5. **IMPORTANT: Plan must be kept current in real-time in case work is interrupted**

Use sequential thinking, context7 and microsoft-docs to solve the problem using latest documentation and best practices.
Files to be analyzed and problems identified (but not limited to):
$ARGUMENTS
