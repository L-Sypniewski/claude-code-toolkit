# Claude Code Skills Guide

This guide explains the Skills included in the Claude Code Toolkit and how to use them effectively.

## What Are Skills?

Skills are modular knowledge packages that Claude automatically loads when relevant context is detected. Unlike agents (which actively perform work) or commands (which are explicitly invoked), skills provide procedural knowledge, templates, and best practices that Claude can reference as needed.

### Skills vs Agents vs Commands

| Component | Purpose | Activation | Example |
|-----------|---------|------------|---------|
| **Skills** | Provide knowledge & templates | Auto-loaded by Claude | `code-review-checklist` |
| **Agents** | Perform specialized work | Context-triggered or explicit | `senior-engineer` |
| **Commands** | Execute workflows | User invokes with `/` | `/create-pr` |

## Available Skills by Plugin

### 🔧 Context Engineering (3 skills)

#### prp-structure
**Purpose**: Standard structure for Prompt-Response-Plan documents  
**Use When**: Creating or formatting PRP documents  
**Provides**: Templates, naming conventions, integration patterns

#### github-issue-processing
**Purpose**: Extract actionable info from GitHub issues  
**Use When**: Analyzing GitHub issues for workflow execution  
**Provides**: Information extraction patterns, label interpretation, issue linking

### 💻 Development Workflow (3 skills)

#### code-review-checklist
**Purpose**: Comprehensive code review framework  
**Use When**: Performing code reviews or preparing code for review  
**Provides**: Review areas (correctness, performance, security), comment templates

#### refactoring-patterns
**Purpose**: Code refactoring techniques  
**Use When**: Planning or executing refactoring  
**Provides**: SOLID/KISS/YAGNI principles, multi-level refactoring (architectural to method-level), safe refactoring checklist

#### workflow-orchestration
**Purpose**: Coordinate multi-step workflows  
**Use When**: Managing complex workflows with multiple agents  
**Provides**: Workflow patterns (sequential, parallel, iterative), agent coordination, progress tracking

### 🌿 Git & Project Management (1 skill)

#### git-worktree-patterns
**Purpose**: Git worktree patterns for parallel development  
**Use When**: Working on multiple branches simultaneously, need separate working directories  
**Provides**: Worktree creation/management, parallel development patterns, worktree organization strategies

### 📚 Documentation Templates (2 skills)

#### agent-documentation
**Purpose**: Standards for creating AGENTS.md files for AI agents  
**Use When**: Creating instructions for AI agents working with your codebase  
**Provides**: AGENTS.md structure, setup commands, coding conventions, testing guidelines

#### claude-delegation-rules
**Purpose**: Agent delegation patterns and coordination  
**Use When**: Designing agent systems or delegation workflows  
**Provides**: Delegation principles, coordination patterns, context handoff, anti-patterns

### 🎨 UI/UX Audit (1 skill)

#### ui-ux-audit-guidelines
**Purpose**: Professional UI/UX audit methodology and design vocabulary  
**Use When**: Conducting visual and interaction design audits of web applications  
**Provides**: Evaluation criteria, viewport configurations, professional design terminology, improvement recommendation formats

## How Skills Work

### Automatic Loading

Skills are automatically loaded by Claude when the description matches the current context:

```yaml
---
name: code-review-checklist
description: Comprehensive code review checklist covering correctness, 
performance, security, and maintainability. Use when performing code 
reviews or preparing code for review.
---
```

When you ask Claude to "review this code", the `code-review-checklist` skill is automatically loaded because the description mentions "code reviews".

### Complementary to Agents

Skills provide knowledge that agents can use:

- **Agent**: `senior-engineer` implements a feature
- **Skill**: `refactoring-patterns` provides refactoring strategies the agent can reference
- **Result**: Implementation follows clean code principles and refactoring best practices

### Progressive Disclosure

Only the YAML frontmatter is initially loaded. The full skill content is loaded only if Claude determines it's relevant, minimizing context window usage.

## Skill Structure

Each skill follows the Anthropic Skills specification:

```
skill-name/
└── SKILL.md         # Required file
    ├── YAML frontmatter (required)
    │   ├── name: (required, matches directory name)
    │   └── description: (required, triggers auto-loading)
    └── Markdown body (required, provides knowledge)
```

### Required Fields

```yaml
---
name: skill-name        # Lowercase, hyphen-separated
description: Clear description of what the skill provides and when to use it
---
```

### Optional Fields

```yaml
license: MIT            # License for the skill
allowed-tools:          # Pre-approved tools (Claude Code only)
  - tool1
  - tool2
metadata:               # Custom key-value pairs
  author: "Your Name"
  version: "1.0"
```

### Advanced Fields (Claude Code 2.1+)

```yaml
context: fork           # Run skill in isolated subagent context
```

## Advanced Skill Features (Claude Code 2.1+)

### Forked Context Execution

Skills can now run in isolated subagent contexts using `context: fork`:

```yaml
---
name: resource-intensive-skill
description: Heavy analysis skill. Use when: analyzing large codebases.
context: fork
---
```

**When to Use Forked Context**:
- Resource-intensive operations that shouldn't consume main context
- Operations that might pollute main session state
- Skills that need to run in parallel with others
- Experimental operations that might fail

**When NOT to Use**:
- Simple reference skills (knowledge, checklists, templates)
- Skills that need to share state with main session
- Most standard plugin skills (keep it simple)

### Hot Reloading

Skills in `.claude/skills` directories are instantly available without restart:

```
~/.claude/skills/           # User-level skills (global)
.claude/skills/             # Project-level skills (local)
plugins/plugin-name/skills/ # Plugin-bundled skills
```

Changes to skill files are immediately reflected without restarting your session.

### Skills as Commands (Convergence)

Skills can now be invoked as slash commands, unifying the extension model:

| Component | Activation | Context | Best For |
|-----------|------------|---------|----------|
| Skills | Auto (contextual) | Shared or Forked | Knowledge, patterns, references |
| Commands | Manual (slash) | Main | User-triggered workflows |
| Subagents | Spawned (Task) | Forked | Parallel work, delegation |

This convergence reduces cognitive overhead when choosing between extension types.

## Best Practices

### Using Skills

1. **Trust Auto-Loading**: Skills are loaded automatically when relevant - no need to explicitly reference them
2. **Specific Descriptions**: Write clear, specific descriptions to ensure proper auto-loading
3. **Complement Agents**: Design skills to provide knowledge that agents can leverage
4. **Keep Focused**: Each skill should cover a specific domain or workflow

### Creating Custom Skills

1. **Follow the Spec**: Use the required YAML frontmatter format
2. **Match Directory Name**: Skill name must match its directory name
3. **Clear Descriptions**: Description should explain what and when
4. **Concise Content**: Skills share the context window - be concise
5. **Provide Examples**: Include practical examples where helpful

### Example Custom Skill

```markdown
---
name: api-security-patterns
description: Security patterns and best practices for REST APIs. Use when implementing API endpoints or reviewing API security.
---

# API Security Patterns

## Authentication

- Use OAuth 2.0 or JWT for authentication
- Never transmit credentials in URL parameters
- Implement token rotation and expiration

## Authorization

- Validate permissions on every request
- Use role-based access control (RBAC)
- Implement least privilege principle

[... additional content ...]
```

## Integration with Toolkit

All skills in this toolkit are designed to work seamlessly with:

- **Agents**: Provide knowledge agents can reference during work
- **Commands**: Support command execution with best practices
- **Workflows**: Enable consistent patterns across development processes

## Further Reading

- [Anthropic Skills Repository](https://github.com/anthropics/skills) - Official skills and examples
- [Agent Skills Overview](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Technical deep dive
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code) - Official documentation
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills) - Official skills guide
- [Subagents, Commands and Skills Convergence](https://vivekhaldar.com/articles/claude-code-subagents-commands-skills-converging/) - Understanding the unified model
- [Claude Skills Context Window Guide](https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills) - Progressive disclosure and efficiency

## Contributing Skills

To contribute new skills to the toolkit:

1. Follow the Anthropic Skills specification
2. Ensure skill complements existing agents/commands
3. Provide clear, actionable content
4. Include practical examples
5. Test with relevant use cases
6. Submit PR with skill documentation

See [Contributing Guidelines](../CONTRIBUTING.md) for more details.
