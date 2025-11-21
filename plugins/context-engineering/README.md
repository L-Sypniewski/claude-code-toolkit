# Context Engineering Plugin

Advanced context engineering workflow with PRP (Prompt-Response-Plan) generation, execution orchestration, GitHub issue analysis, and reusable skills for systematic problem-solving and issue analysis.

## Features

### Agents

- **context-engineering-orchestrator** - Coordinates complex workflows and manages multi-step processes
- **context-engineering-prp-generator** - Generates structured PRPs for systematic problem-solving
- **context-engineering-executor** - Executes PRPs with precision and tracks progress
- **context-engineering-github-issue-analyzer** - Analyzes GitHub issues and extracts actionable insights

### Commands

- **/generate-prp** - Generate a Prompt-Response-Plan for structured problem-solving
- **/execute-prp** - Execute an existing PRP with tracking and validation
- **/initial-github-issue** - Process and analyze GitHub issues for workflow initiation

### Skills

**Skills are automatically activated by agents when relevant:**

- **prp-templates** - Comprehensive PRP templates and patterns for systematic problem-solving, including feature implementation, bug fixes, refactoring, and migration PRPs
- **issue-analysis-frameworks** - Systematic frameworks for analyzing GitHub issues, bug reports, and feature requests to extract actionable insights and create effective implementation plans

## Installation

This plugin is part of the Claude Code Toolkit marketplace. Install via:

```bash
/plugin marketplace add <marketplace-url>
/plugin install context-engineering
```

## Usage

The context engineering workflow typically follows these steps:

1. Use **/initial-github-issue** to analyze a GitHub issue
2. Use **/generate-prp** to create a structured plan
3. Use **context-engineering-orchestrator** agent to coordinate execution
4. Use **/execute-prp** to implement the plan with tracking

## Best Practices

- Start with issue analysis before generating PRPs
- Use the orchestrator for complex, multi-agent workflows
- Track PRP execution progress systematically
- Leverage GitHub issue insights for context-aware development

## License

MIT
