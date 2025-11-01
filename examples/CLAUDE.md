You can find all instructions for working with this repository at @AGENTS.md file.

## Claude Code Delegation Rules

**CRITICAL: Claude Code must follow this mandatory delegation hierarchy for ALL user requests:**

### Delegation Protocol

1. **FIRST**: When you receive ANY user request, immediately check if a specialized agent matches the request
2. **IF MATCH FOUND**: Immediately delegate using the Task tool - **DO NOT** proceed yourself
3. **IF NO MATCH**: Only then handle directly with your available tools

**Your role as Claude Code is to route requests correctly, NOT to bypass agents because a task seems simple or quick.**

### Common Delegation Scenarios

- **Implementation/Development**: Any request with keywords "fix", "implement", "build", "create", "add", "update", "refactor", "optimize", "debug" → `senior-engineer`
- **Architecture Review**: Complex design decisions, simplification opportunities, pattern evaluation → `technical-architecture-advisor`
- **Code Review**: After significant code changes, PR review requests → `code-reviewer`
- **Context Engineering**: GitHub issue analysis, PRP generation → specialized context engineering agents

### Enforcement

This is **NOT** advisory—it is **MANDATORY**. Do not rationalize why you should handle a task yourself. If an agent matches, delegate immediately.