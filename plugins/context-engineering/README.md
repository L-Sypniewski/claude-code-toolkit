# Context Engineering Plugin

Advanced context engineering workflow with PRP (Prompt-Response-Plan) generation, execution orchestration, and GitHub issue analysis for efficient software development processes.

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

- **prp-structure** - Standard structure and format for PRP documents with templates and best practices
- **github-issue-processing** - Patterns for extracting actionable information from GitHub issues
- **workflow-orchestration** - Multi-step workflow coordination patterns for complex development tasks

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
- Skills are automatically loaded by Claude when relevant context is detected
- Agents can leverage skills for procedural knowledge and templates

## License

MIT
