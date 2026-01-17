# GitHub Copilot Custom Agents

This directory contains GitHub Copilot custom agent equivalents of the Claude Code agents from the `plugins/` directory. These agents are designed to be copied to your organization's `.github-private` repository for use with GitHub Copilot coding agent.

## 📋 Overview

These custom agents are conversions of the Claude Code toolkit agents, adapted to work with GitHub Copilot's agent system. They provide specialized expertise for various development workflows.

## 🔄 Key Differences: Claude Code vs GitHub Copilot Agents

| Aspect | Claude Code Agents | GitHub Copilot Agents |
|--------|-------------------|----------------------|
| **File Location** | `plugins/*/agents/*.md` | `.github/agents/*.agent.md` |
| **File Extension** | `.md` | `.agent.md` |
| **Tools Format** | MCP tool names (e.g., `mcp__github__get_issue`) | Tool aliases (e.g., `read`, `edit`, `github/*`) |
| **Model Property** | `model: sonnet` (supported) | `model:` (VS Code only, ignored on GitHub.com) |
| **Color Property** | `color: blue` (supported) | Not supported |
| **Target Property** | Not supported | `target: vscode` or `github-copilot` (optional) |
| **MCP Servers** | Configured via MCP tools | Org/Enterprise level only via `mcp-servers` property |

### Tool Aliases Reference

Copilot agents use these tool aliases instead of specific MCP tool names:

| Alias | Description | Example Tools |
|-------|-------------|---------------|
| `read` | Read file contents | `Read`, `NotebookRead` |
| `edit` | Edit files | `Edit`, `Write`, `MultiEdit` |
| `search` | Search for files/text | `Grep`, `Glob` |
| `execute` | Execute shell commands | `Bash`, `shell` |
| `web` | Web search and fetch | `WebSearch`, `WebFetch` |
| `agent` | Invoke other custom agents | `Task`, `custom-agent` |
| `github/*` | All GitHub MCP tools | `github/get_issue`, `github/create_pull_request` |
| `playwright/*` | All Playwright MCP tools | `playwright/browser_navigate`, `playwright/browser_screenshot` |

## 📁 Available Agents

### Development Workflow Agents

| Agent | Description | Source Plugin |
|-------|-------------|---------------|
| `senior-engineer` | Senior engineer for implementation tasks | development-workflow |
| `code-reviewer` | Expert code review specialist | development-workflow |
| `technical-architecture-advisor` | Evaluates architectural decisions | development-workflow |
| `pull-request-creator` | Creates comprehensive PRs | development-workflow |
| `feature-requirements-clarifier` | Resolves gaps in requirements | development-workflow |
| `feature-issue-analyzer` | Normalizes feature requests | development-workflow |
| `feature-plan-validator` | Validates implementation plans | development-workflow |
| `screenshot-comparator` | Creates before/after screenshot comments | development-workflow |

### Context Engineering Agents

| Agent | Description | Source Plugin |
|-------|-------------|---------------|
| `context-engineering-orchestrator` | Coordinates context engineering pipelines | context-engineering |
| `context-engineering-prp-generator` | Generates Product Requirements Prompts | context-engineering |
| `context-engineering-executor` | Executes PRPs with validation | context-engineering |
| `context-engineering-github-issue-analyzer` | Analyzes GitHub issues | context-engineering |

### UI/UX Audit Agents

| Agent | Description | Source Plugin |
|-------|-------------|---------------|
| `ui-ux-audit-orchestrator` | Orchestrates comprehensive UI/UX audits | ui-ux-audit |
| `ui-ux-page-auditor` | Audits individual pages for UI/UX issues | ui-ux-audit |

### Plugin Creation Agents

| Agent | Description | Source Plugin |
|-------|-------------|---------------|
| `plugin-creator` | Creates production-ready Claude Code plugins | plugin-creator |
| `plugin-validator` | Validates plugin structure and security | plugin-creator |

### Documentation Agents

| Agent | Description | Source Plugin |
|-------|-------------|---------------|
| `agents-md-organizer` | Reorganizes large AGENTS.md files | documentation-templates |

## 🚀 Installation

### For Organization-Wide Use

1. Copy the contents of this `.github/agents/` directory to your organization's `.github-private` repository:

```bash
# In your .github-private repository
mkdir -p agents
cp -r /path/to/claude-code-toolkit/.github/agents/* agents/
```

2. Commit and push the changes:

```bash
git add agents/
git commit -m "Add Copilot custom agents from claude-code-toolkit"
git push
```

3. The agents will now be available to all repositories in your organization.

### For Repository-Specific Use

1. Copy the agents to your repository's `.github/agents/` directory:

```bash
mkdir -p .github/agents
cp -r /path/to/claude-code-toolkit/.github/agents/* .github/agents/
```

2. Commit and push:

```bash
git add .github/agents/
git commit -m "Add Copilot custom agents"
git push
```

## 📖 Usage

### On GitHub.com

1. Navigate to the [agents tab](https://github.com/copilot/agents)
2. Select your repository from the dropdown
3. Use the agents dropdown in the prompt box to select your custom agent
4. Provide your task description

### In VS Code

1. Open GitHub Copilot Chat
2. From the agents dropdown at the bottom of the chat view, select your custom agent
3. Ask your question or provide your task

### Assigning to Issues

1. Open an issue in your repository
2. Click the "Assign to Copilot" button
3. Select your custom agent from the dropdown
4. Copilot will process the issue using your specialized agent

## 🔧 Customization

### Adding Your Own Tools

You can customize the `tools` property in each agent to enable or disable specific capabilities:

```yaml
---
name: my-custom-agent
description: My specialized agent
tools: ["read", "edit", "search", "github/*"]  # Customize this list
---
```

### Tool Configuration Options

- `["*"]` or omit property - Enable all available tools
- `[]` - Disable all tools (read-only agent)
- `["read", "search"]` - Enable only specific tools
- `["github/*"]` - Enable all tools from GitHub MCP server
- `["github/get_issue", "github/create_pull_request"]` - Enable specific GitHub tools

### Adding MCP Servers (Organization/Enterprise Level Only)

For organization-level agents, you can configure MCP servers:

```yaml
---
name: my-custom-agent
description: My specialized agent with MCP
tools: ["read", "edit", "custom-mcp/tool-1"]
mcp-servers:
  custom-mcp:
    type: "local"
    command: "some-command"
    args: ["--arg1", "--arg2"]
    tools: ["*"]
    env:
      API_KEY: ${{ secrets.MY_API_KEY }}
---
```

## ⚠️ Limitations

### Properties Ignored on GitHub.com

The following properties from VS Code custom agents are **not supported** on GitHub.com:

- `model` - AI model selection
- `argument-hint` - Argument hints
- `handoffs` - Agent handoff configuration

### MCP Server Restrictions

- Repository-level agents **cannot** configure MCP servers directly
- Repository-level agents can use tools from MCP servers configured in repository settings
- Organization/Enterprise-level agents can configure MCP servers in the agent profile

## 📚 Related Resources

- [GitHub Copilot Custom Agents Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [Custom Agents Configuration Reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Claude Code Toolkit (Source Repository)](https://github.com/L-Sypniewski/claude-code-toolkit)
- [Awesome Copilot Agents Collection](https://github.com/github/awesome-copilot/tree/main/agents)

## 📄 License

These agents are derived from the Claude Code Toolkit and are licensed under the MIT License.
