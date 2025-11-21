# Development Workflow Plugin

Comprehensive development toolkit with senior engineering expertise, code review, architecture advisory, visual testing, PR management capabilities, and reusable skills for code quality, security best practices, and testing patterns.

## Features

### Agents

- **senior-engineer** - Primary development agent for implementation and problem-solving
- **code-reviewer** - Expert code review with comprehensive quality analysis
- **pull-request-creator** - Professional PR documentation and creation
- **technical-architecture-advisor** - Architecture evaluation and design guidance
- **screenshot-comparator** - Visual regression testing and UI comparison

### Commands

- **/create-pr** - Create well-documented pull requests
- **/implement-plan** - Execute implementation plans systematically
- **/bug-fix-implement** - Structured bug fixing workflow
- **/bug-investigation-plan** - Systematic bug investigation and root cause analysis
- **/refactoring-plan** - Plan and execute refactoring efforts
- **/technical-translator-prompt** - Translate technical concepts across contexts
- **/plan-markdown-writer** - Generate structured project plans in markdown format

### Skills

**Skills are automatically activated by agents when relevant:**

- **code-quality-standards** - Comprehensive code quality standards and best practices for writing maintainable, readable, and performant code across multiple programming languages
- **security-best-practices** - Security best practices and vulnerability prevention guidelines covering OWASP Top 10, secure coding patterns, and security architecture
- **testing-patterns** - Testing patterns and strategies for writing effective unit, integration, and end-to-end tests across different testing frameworks

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

## License

MIT
