# GitHub Copilot Custom Agents

This directory contains GitHub Copilot custom agent definitions converted from Claude Code agents. These agents provide specialized capabilities for context engineering and development workflows.

## Installation

1. Copy the desired agent files to your repository's `.github/agents/` directory
2. GitHub Copilot will automatically detect and load the agents
3. Invoke agents using `@agent-name` in your Copilot chat

## Agent Catalog

### Context Engineering Agents

#### 1. github-issue-analyzer
**Purpose**: Analyzes GitHub issues and posts structured analysis comments

**Tools**: `github/*`, `web`, `read`, `search`

**Usage**:
```
@github-issue-analyzer Analyze issue #123 and create structured comment
```

**Capabilities**:
- Comprehensive GitHub issue analysis
- Structured comment creation (FEATURE, EXAMPLES, DOCUMENTATION, OTHER CONSIDERATIONS)
- Technical research and best practices integration
- Automated comment posting to GitHub issues

---

#### 2. prp-generator
**Purpose**: Generates Product Requirements Prompts from GitHub issue analysis

**Tools**: `github/*`, `custom-agent`, `read`, `search`, `web`, `todo`

**Usage**:
```
@prp-generator Generate PRP from issue #123
```

**Capabilities**:
- Transforms structured issue analysis into implementation blueprints
- Delegates to technical-architecture-advisor for architectural optimization
- Creates context-dense PRPs with validation loops
- Progressive implementation planning with checkpoints
- Feature categorization and testing strategy

---

#### 3. executor
**Purpose**: Executes Product Requirements Prompts with pragmatic development

**Tools**: `*` (all tools)

**Usage**:
```
@executor Execute PRP file: path/to/prp.md
```

**Capabilities**:
- Pragmatic implementation approach (build validation + optional testing)
- Progressive phase-based implementation
- Comprehensive validation gates
- Artifact cleanup and documentation updates
- Real-time progress tracking

---

#### 4. orchestrator
**Purpose**: Coordinates context engineering pipeline workflows

**Tools**: `github/*`, `custom-agent`, `todo`, `read`, `search`

**Usage**:
```
@orchestrator Execute complete pipeline for issue #123
```

**Capabilities**:
- Multi-agent workflow coordination
- State management and progress tracking
- Flexible invocation (full pipeline or individual steps)
- Error recovery and branching logic
- Comprehensive reporting

---

### Development Workflow Agents

#### 5. code-reviewer
**Purpose**: Expert code review analyzing quality, security, performance, architecture

**Tools**: `github/*`, `custom-agent`, `read`, `search`, `web`

**Usage**:
```
@code-reviewer Review PR #456
```

**Capabilities**:
- Multi-level analysis (line → method → class → architecture)
- Delegates to technical-architecture-advisor for architectural concerns
- Structured feedback by severity (Critical, Major, Minor)
- Security and best practices validation
- Comprehensive quality assessment

---

#### 6. pull-request-creator
**Purpose**: Creates comprehensive pull requests with detailed descriptions

**Tools**: `github/*`, `read`, `search`, `web`

**Usage**:
```
@pull-request-creator Create PR for current branch fixing issue #789
```

**Capabilities**:
- Small, focused PR advocacy (GitHub best practices)
- Problem-solution narrative structure
- Security review checklist integration
- Self-review requirements
- Comprehensive change documentation

---

#### 7. technical-architecture-advisor
**Purpose**: Evaluates technical approaches and challenges assumptions

**Tools**: `read`, `search`, `web`

**Usage**:
```
@technical-architecture-advisor Is there a better way to implement X?
```

**Capabilities**:
- Critical technical evaluation (questions every approach)
- Architecture-first analysis method
- Pushes back on suboptimal solutions
- Educational focus on principles
- One-way handoff (no callbacks during implementation)

---

#### 8. screenshot-comparator
**Purpose**: Creates before/after screenshot comments for PRs and issues

**Tools**: `playwright/*`, `github/*`, `shell`, `read`

**Usage**:
```
@screenshot-comparator Create before/after screenshots for PR #123
Pages: /, /about
Viewports: desktop, mobile
Server: localhost:3000
```

**Capabilities**:
- Git state management (safe stashing)
- Playwright integration for screenshots
- Before/after comparison workflow
- Formatted GitHub comments with visual comparisons

---

#### 9. senior-engineer
**Purpose**: Primary implementation agent for all development tasks

**Tools**: `*` (all tools)

**Usage**:
```
@senior-engineer Implement feature X with proper architecture
```

**Capabilities**:
- Mandatory planning workflow for complex tasks
- Real-time plan updates
- Delegates to technical-architecture-advisor for architectural decisions
- Comprehensive engineering methodology
- One-way handoff protocol with advisor

---

## Agent Collaboration Patterns

### Context Engineering Pipeline

```
@orchestrator → @github-issue-analyzer → @prp-generator → @executor
```

Complete workflow from GitHub issue to implementation.

### Code Review with Architecture

```
@code-reviewer → @technical-architecture-advisor (if needed)
```

Code review with optional architectural consultation.

### Implementation with Architecture

```
@senior-engineer → @technical-architecture-advisor (for complex decisions)
```

Implementation with architectural guidance.

### PR Creation

```
@senior-engineer → @pull-request-creator
```

Implementation followed by comprehensive PR creation.

## Tool Mapping Reference

### GitHub MCP Tools

Copilot provides out-of-box GitHub MCP server with read-only tools scoped to source repository:

- `github/get_issue` - Retrieve issue details
- `github/list_issues` - List repository issues
- `github/get_pull_request` - Get PR details
- `github/list_pull_requests` - List PRs
- `github/get_file_contents` - Read file contents
- `github/list_commits` - List commit history
- `github/get_commit` - Get commit details
- `github/search_code` - Search code across repository
- `github/search_issues` - Search issues and PRs

**Note**: Write operations (create/update) may require additional permissions or configuration.

### Playwright MCP Tools

Copilot provides out-of-box Playwright MCP server for browser automation:

- `playwright/navigate` - Navigate to URL
- `playwright/screenshot` - Capture screenshots
- `playwright/*` - All Playwright tools for browser automation

**Note**: Configured to access localhost only by default.

### Generic Tool Aliases

- `read` - Read file contents
- `edit` - Edit files
- `search` - Search files/text (Grep/Glob)
- `web` - Web search and fetch
- `shell` - Execute shell commands
- `custom-agent` - Invoke other agents
- `todo` - Task list management

## Capability Matrix

| Agent | GitHub | Web | Files | Shell | Playwright | Custom Agents |
|-------|--------|-----|-------|-------|------------|---------------|
| github-issue-analyzer | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| prp-generator | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| executor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| orchestrator | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ |
| code-reviewer | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| pull-request-creator | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| technical-architecture-advisor | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ |
| screenshot-comparator | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| senior-engineer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Limitations vs Claude Code

### Features Not Available in Copilot

1. **Model Selection**: Copilot uses default model for all agents (no haiku/sonnet/opus choice)
2. **Color Coding**: No visual organization or UI customization
3. **Explicit MCP Tool Control**: Category-level tool access only (not granular tool-by-tool)
4. **Context7 MCP**: Not available out-of-box (use `web` tool as fallback)
5. **Microsoft Docs MCP**: Not available out-of-box (use `web` tool as fallback)
6. **Sequential Thinking MCP**: Not available (methodology incorporated into instructions)

### What Works Well

1. **GitHub MCP Integration**: Out-of-box `github/*` namespace for repository operations
2. **Playwright Integration**: Out-of-box `playwright/*` namespace for browser automation
3. **Agent Collaboration**: `custom-agent` tool for multi-agent workflows
4. **Markdown Instructions**: Same format as Claude Code
5. **Tool Categories**: Broad tool access via aliases (read, edit, search, web, shell)

## Migration Notes

These agents have been converted from Claude Code format to GitHub Copilot format with the following adaptations:

1. **Tool Mapping**: MCP tool names converted to Copilot tool categories and namespaces
2. **Instruction Simplification**: Structured sections converted to narrative flow
3. **Model Removal**: Model selection removed (Copilot uses default)
4. **Color Removal**: Visual organization removed (not supported)
5. **Research Tools**: Context7 and Microsoft Docs replaced with generic `web` tool
6. **Sequential Thinking**: Methodology incorporated into agent instructions directly

For detailed migration information, see `MIGRATION-NOTES.md`.

## Contributing

When creating new agents or modifying existing ones:

1. Follow the YAML frontmatter format with `name`, `description`, and `tools`
2. Use appropriate tool categories/namespaces for capabilities
3. Keep instructions clear, narrative, and actionable
4. Test agent behavior in actual Copilot environment
5. Document any GitHub-specific limitations or requirements

## Support

For issues or questions:
- GitHub Copilot Documentation: https://docs.github.com/en/copilot
- Custom Agents Reference: https://docs.github.com/en/copilot/reference/custom-agents-configuration
- Claude Code Agents (original): https://github.com/anthropics/claude-code

## License

These agent definitions are provided as-is for use with GitHub Copilot. Refer to your Claude Code and GitHub Copilot licenses for usage terms.
