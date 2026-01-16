# Development Workflow Plugin

Comprehensive development toolkit with intelligent feature workflows, senior engineering expertise, code review, architecture advisory, visual testing, and PR management capabilities for end-to-end software development workflows.

## Features

### 🆕 Intelligent Feature Workflow

**NEW in v1.4.0**: Automated end-to-end feature implementation workflow with intelligent planning, validation, and execution.

#### Commands

- **/feature-from-issue** `<issue-number>` - Implement feature from GitHub issue with full workflow
- **/feature-from-prompt** `<description>` - Implement feature from text description
- **/feature-from-file** `<file-path>` - Implement feature from local specification file
- **/resume-feature** `<plan-file>` - Resume interrupted feature workflow

#### Agents

- **feature-issue-analyzer** - Normalizes requirements from any input source (GitHub/prompt/file) (haiku - fast)
- **feature-requirements-clarifier** - Asks clarifying questions to resolve gaps in incomplete requirements (sonnet - reasoning)
- **feature-plan-validator** - Validates plans for completeness, feasibility, and clarity (sonnet - analytical)

#### Workflow Phases

1. **Requirements Analysis** - Two-agent pattern for optimal performance:
   - feature-issue-analyzer normalizes input (haiku - fast)
   - feature-requirements-clarifier resolves gaps if needed (sonnet - reasoning)
2. **Complexity Assessment** - Automated 0-8 point scoring system
3. **Intelligent Planning** - senior-engineer + optional architecture advisor (auto-invoked for complex features)
4. **Plan Validation** - Automated quality gates before implementation
5. **User Approval** - Interactive review and approval
6. **Delegated Implementation** - Context-saving agent delegation
7. **Progress Tracking** - Real-time plan file updates

#### Key Features

- **Composable Inputs**: Works with GitHub issues, text prompts, or local files
- **Intelligent Complexity Detection**: Automatically involves architecture advisor when needed (complexity ≥5/8)
- **Quality Gates**: Validation before implementation prevents wasted effort
- **Resumability**: Interrupt and resume workflows at any point
- **User Visibility**: See every phase, review plans before implementation
- **Plan Files**: All state persisted in `plans/` directory for traceability

#### Example Usage

```bash
# From GitHub issue
/feature-from-issue 123

# From text description
/feature-from-prompt Add dark mode toggle with persistent user preferences

# From specification file
/feature-from-file features/csv-export.md

# Resume interrupted workflow
/resume-feature plans/feature-dark-mode-20260105.md
```

See individual command files for detailed documentation and examples.

### Agents

- **senior-engineer** - Primary development agent for implementation and problem-solving
- **code-reviewer** - Expert code review with comprehensive quality analysis
- **pull-request-creator** - Professional PR documentation and creation
- **technical-architecture-advisor** - Architecture evaluation and design guidance
- **screenshot-comparator** - Visual regression testing and UI comparison
- **frontend-ui-designer** - UI design direction, layout, and interaction guidance

### Commands

- **/create-pr** - Create well-documented pull requests
- **/implement-plan** - Execute implementation plans systematically
- **/bug-fix-implement** - Structured bug fixing workflow
- **/bug-investigation-plan** - Systematic bug investigation and root cause analysis
- **/refactoring-plan** - Plan and execute refactoring efforts
- **/technical-translator-prompt** - Translate technical concepts across contexts
- **/plan-markdown-writer** - Generate structured project plans in markdown format

### Skills

- **feature-planning** - End-to-end feature implementation workflow from requirements to completion (auto-invoked by feature commands)
- **code-review-checklist** - Comprehensive checklist covering correctness, performance, security, and maintainability
- **refactoring-patterns** - Proven refactoring techniques for improving code quality and reducing complexity
- **workflow-orchestration** - Multi-step workflow coordination patterns for complex development tasks
- **ui-design-guidelines** - UI design methodology, visual systems, and spec templates for frontend work

## Installation

This plugin is part of the Claude Code Toolkit marketplace. Install via:

```bash
/plugin marketplace add <marketplace-url>
/plugin install development-workflow
```

## Usage

### Development Lifecycle

1. **Planning**: Use **/plan-markdown-writer** to create structured project plans
2. **Architecture Planning**: Use **technical-architecture-advisor** for design decisions
3. **Implementation**: Use **senior-engineer** for feature development
4. **Code Review**: Use **code-reviewer** for quality assurance
5. **Visual Verification**: Use **screenshot-comparator** for UI testing
6. **PR Creation**: Use **/create-pr** or **pull-request-creator** for documentation

### Bug Fixing Workflow

1. Use **/bug-investigation-plan** to analyze and understand the issue
2. Use **/bug-fix-implement** to systematically fix the bug
3. Use **code-reviewer** to validate the fix
4. Use **/create-pr** to document and submit changes

### Refactoring Workflow

1. Consult **technical-architecture-advisor** for refactoring strategy
2. Use **/refactoring-plan** to structure the refactoring effort
3. Use **senior-engineer** to implement changes
4. Use **code-reviewer** for quality validation

## Agent Cooperation

The **senior-engineer** and **technical-architecture-advisor** agents are designed to work together:
- Architecture advisor provides high-level design guidance
- Senior engineer implements the architectural decisions
- Both agents ensure technical excellence and maintainability

## Best Practices

- Start complex features with architecture review
- Use code review before creating PRs
- Leverage visual testing for UI changes
- Document decisions in PR descriptions
- Follow systematic workflows for bugs and refactoring
- Skills provide procedural knowledge that agents automatically access when relevant
- Leverage code-review-checklist for thorough quality assessment

## Documentation References

For understanding how agents, skills, and commands work in Claude Code:

- **Official Claude Code Sub-Agents**: https://code.claude.com/docs/en/sub-agents
- **Official Claude Code Skills**: https://code.claude.com/docs/en/skills
- **Agent Skills Platform Overview**: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- **Agent Skills Open Standard**: https://agentskills.io/home
- **Claude Code Components Guide**: https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins

### Key Concepts

**Skills** are auto-invoked context providers. Claude loads them based on description matching - you don't explicitly assign skills to agents. Skills use progressive disclosure: metadata loaded at startup, full SKILL.md loaded when triggered.

**Subagents** are explicit workflow orchestrators invoked via Task tool. They run in separate context windows with configurable tool access.

**Commands** are user-initiated shortcuts (`/command`) that invoke subagents or execute workflows.

## License

MIT
