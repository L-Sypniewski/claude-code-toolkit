---
description: Write a detailed refactoring plan with problem analysis and step-by-step strategy for another AI Agent
argument-hint: ""
---

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

PLAN STRUCTURE REQUIREMENTS FOR AI AGENTS:

- **NO TIME ESTIMATES**: Do not include time estimates (hours/days) - AI agents execute steps based on complexity, not time
- **Dependencies**: Clearly mark which steps depend on completion of previous steps
- **Complexity Indicators**: Label each step with complexity (Simple/Moderate/Complex) based on:
  - Number of files affected
  - Risk of breaking changes
  - Amount of analysis required
  - Interdependencies with other components
- **Completion Criteria**: Define clear, verifiable criteria for when each step is complete
- **Rollback Points**: Identify safe checkpoints where work can be paused and resumed

Use sequential thinking, context7 and microsoft-docs to solve the problem using latest documentation and best practices.
Files to be analyzed and problems identified (but not limited to):
$ARGUMENTS
