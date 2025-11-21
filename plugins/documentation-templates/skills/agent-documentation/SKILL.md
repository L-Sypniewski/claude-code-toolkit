---
name: agent-documentation
description: Standards and templates for documenting Claude Code agents including AGENTS.md files, agent specifications, and delegation patterns. Use when creating or documenting agents.
---

# Agent Documentation

This skill provides standards for documenting Claude Code agents effectively.

## AGENTS.md Structure

Every project with agents should have an AGENTS.md file:

```markdown
# Project Agents

This document describes the specialized agents available in this project.

## Overview

Brief description of the agent system and how agents collaborate.

## Available Agents

### [Agent Name]

**Purpose**: [What this agent does]

**Activation**: [When/how the agent is activated]

**Capabilities**:
- Capability 1
- Capability 2
- Capability 3

**Tools**: [List of tools available to this agent]

**Model**: [e.g., sonnet, opus]

**Delegation Pattern**: 
- Delegates to [other agent] for [specific tasks]
- Works with [other agent] on [scenarios]

**Example Usage**:
```
[Example of how to use this agent]
```

---

[Repeat for each agent]

## Agent Collaboration

### Workflow Patterns

Describe how agents work together:

```
Issue Analysis → github-issue-analyzer
       ↓
  PRP Generation → prp-generator
       ↓
  Implementation → senior-engineer
       ↓
  Code Review → code-reviewer
```

### Handoff Protocols

- **github-issue-analyzer → prp-generator**: Passes structured requirements
- **prp-generator → executor**: Provides execution plan
- **senior-engineer → code-reviewer**: Submits implemented code

## Best Practices

1. **Clear Boundaries**: Each agent has distinct responsibilities
2. **Explicit Handoffs**: Clear transition points between agents
3. **Context Preservation**: Agents receive necessary context
4. **Error Handling**: Agents handle their own error scenarios
```

## Agent Specification Format

Individual agent documentation (agent.md):

```markdown
---
name: agent-name
description: Clear description of what the agent does and when to use it
tools: [List of tool identifiers]
color: [blue|green|red|yellow|purple|...]
model: [sonnet|opus|haiku]
---

# Agent Name

[Detailed description of agent's role and capabilities]

## Core Responsibilities

1. **Responsibility 1**: [Description]
2. **Responsibility 2**: [Description]
3. **Responsibility 3**: [Description]

## When to Use

Use this agent when:
- Scenario 1
- Scenario 2
- Scenario 3

Do NOT use for:
- Counter-scenario 1
- Counter-scenario 2

## Methodology

Describe the agent's approach:

### Analysis Phase
[How agent analyzes problems]

### Planning Phase
[How agent creates plans]

### Execution Phase
[How agent executes solutions]

## Delegation Protocol

### When to Delegate

This agent delegates to other agents when:
- Condition 1: Delegate to [agent-name]
- Condition 2: Delegate to [agent-name]

### Delegation Process

1. **Identify Need**: [When to delegate]
2. **Prepare Context**: [What context to provide]
3. **Hand Off**: [How to transition]
4. **Integrate Results**: [How to use delegated work]

## Input Requirements

What this agent needs to function effectively:
- Input 1: [Description]
- Input 2: [Description]

## Output Deliverables

What this agent produces:
- Output 1: [Description and format]
- Output 2: [Description and format]

## Error Handling

How this agent handles common error scenarios:

### Scenario 1: [Error Type]
**Detection**: [How to detect]
**Response**: [What agent does]
**Recovery**: [How to recover]

### Scenario 2: [Error Type]
[Similar structure]

## Examples

### Example 1: [Scenario]
```
[Input]
→ [Agent processing]
→ [Output]
```

### Example 2: [Scenario]
```
[Input]
→ [Agent processing]
→ [Output]
```

## Configuration

### Tools Required
- Tool 1: [Purpose]
- Tool 2: [Purpose]

### Environment Variables
- `VAR_NAME`: [Description]

### Dependencies
- Dependency 1: [Why needed]

## Integration Points

How this agent integrates with:
- Other agents: [Description]
- Commands: [Description]
- External systems: [Description]

## Limitations

What this agent cannot do:
- Limitation 1: [Why and workaround]
- Limitation 2: [Why and workaround]

## Performance Considerations

- **Response Time**: [Typical timing]
- **Token Usage**: [Approximate usage]
- **Concurrency**: [Can run parallel with other agents?]
```

## Agent YAML Frontmatter Fields

Required fields:
```yaml
---
name: agent-identifier  # Lowercase, hyphen-separated
description: Clear, concise description for Claude's decision-making
---
```

Optional fields:
```yaml
tools: tool1, tool2, tool3  # Comma-separated tool identifiers
color: blue  # Visual identifier in UI
model: sonnet  # Claude model to use
```

## Tool Identifiers

Common tools to list in agent specifications:

**MCP Tools**:
- `mcp__context7__resolve_library_id`
- `mcp__github__get_issue`
- `mcp__github__get_file_contents`
- `mcp__sequentialthinking__sequentialthinking`

**Standard Tools**:
- `Glob` - File pattern matching
- `Grep` - Text search
- `Read` - File reading
- `Write` - File writing
- `Edit` - File editing
- `Bash` - Command execution
- `WebFetch` - HTTP requests
- `WebSearch` - Web searching

**Specialized Tools**:
- `TodoWrite` - Task tracking
- `Task` - Task management

## Agent Naming Conventions

- Use descriptive, hyphenated names: `senior-engineer`, `code-reviewer`
- Avoid generic names: use `github-issue-analyzer` not `analyzer`
- Be specific to role: `technical-architecture-advisor` not `architect`
- Match file name: `senior-engineer.md` → `name: senior-engineer`

## Documentation Checklist

Agent documentation is complete when:

- [ ] Name is clear and follows conventions
- [ ] Description explains when to use the agent
- [ ] Core responsibilities are listed
- [ ] Delegation patterns are documented
- [ ] Input/output formats are specified
- [ ] Error handling is described
- [ ] Examples are provided
- [ ] Tool requirements are listed
- [ ] Integration points are documented
- [ ] Limitations are noted

## Integration with Plugin Components

This skill works with:
- Agent creation workflows
- Plugin documentation
- Team onboarding materials
- Agent testing and validation
