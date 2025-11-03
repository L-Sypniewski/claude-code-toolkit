# Migration Notes: Claude Code → GitHub Copilot Agents

This document details the conversion process, tool mappings, and considerations when migrating from Claude Code agents to GitHub Copilot custom agents.

## Overview

Date: 2025-11-03
Source: Claude Code Toolkit (9 agents across 2 plugin categories)
Target: GitHub Copilot Custom Agents
Approach: Direct conversion with tool mapping and instruction simplification

## Tool Mapping Reference

### GitHub MCP Tools (Out-of-Box)

GitHub Copilot provides `github/*` namespace for repository operations:

| Claude Code Tool | Copilot Tool | Notes |
|------------------|--------------|-------|
| `mcp__github__get_issue` | `github/get_issue` | Direct mapping |
| `mcp__github__list_issues` | `github/list_issues` | Direct mapping |
| `mcp__github__get_pull_request` | `github/get_pull_request` | Direct mapping |
| `mcp__github__list_pull_requests` | `github/list_pull_requests` | Direct mapping |
| `mcp__github__create_pull_request` | `github/create_pull_request` | May require permissions |
| `mcp__github__add_issue_comment` | `github/add_issue_comment` | May require permissions |
| `mcp__github__get_file_contents` | `github/get_file_contents` | Direct mapping |
| `mcp__github__list_commits` | `github/list_commits` | Direct mapping |
| `mcp__github__get_commit` | `github/get_commit` | Direct mapping |

**Important**: GitHub MCP tools in Copilot are read-only by default and scoped to source repository. Write operations may require additional configuration or permissions.

### Playwright MCP Tools (Out-of-Box)

GitHub Copilot provides `playwright/*` namespace for browser automation:

| Claude Code Tool | Copilot Tool | Notes |
|------------------|--------------|-------|
| Bash (for screenshots) | `playwright/screenshot` | Cleaner approach |
| N/A | `playwright/navigate` | Available for navigation |
| N/A | `playwright/*` | All Playwright tools |

**Important**: Playwright server configured to access localhost only by default.

### Generic Tool Categories

| Claude Code Tool | Copilot Tool | Notes |
|------------------|--------------|-------|
| `Read` | `read` | Direct alias |
| `Write`, `Edit`, `MultiEdit` | `edit` | Combined into edit category |
| `Glob`, `Grep` | `search` | Combined into search category |
| `WebFetch`, `WebSearch` | `web` | Combined into web category |
| `Bash` | `shell` | Direct alias |
| `Task` (agent delegation) | `custom-agent` | Direct mapping |
| `TodoWrite` | `todo` | Direct alias |

### Unavailable MCP Tools

These Claude Code MCP tools have no direct Copilot equivalent:

| Claude Code Tool | Copilot Fallback | Impact |
|------------------|------------------|--------|
| `mcp__context7__resolve_library_id` | `web` | Use web search for docs |
| `mcp__context7__get_library_docs` | `web` | Use web search for docs |
| `mcp__microsoft-docs__microsoft_docs_search` | `web` | Use web search |
| `mcp__microsoft-docs__microsoft_docs_fetch` | `web` | Use web fetch |
| `mcp__microsoft-docs__microsoft_code_sample_search` | `web` | Use web search |
| `mcp__sequentialthinking__sequentialthinking` | N/A | Methodology incorporated into instructions |

## Per-Agent Conversion Details

### Context Engineering Agents

#### 1. github-issue-analyzer

**Claude Tools**:
```yaml
tools: mcp__sequentialthinking__sequentialthinking, mcp__github__get_issue,
  mcp__github__add_issue_comment, mcp__github__get_issue_comments,
  mcp__context7__resolve_library_id, mcp__context7__get_library_docs,
  WebFetch, WebSearch, mcp__microsoft-docs__microsoft_docs_search,
  mcp__microsoft-docs__microsoft_docs_fetch,
  mcp__microsoft-docs__microsoft_code_sample_search
```

**Copilot Tools**:
```yaml
tools: ["github/*", "web", "read", "search"]
```

**Changes**:
- Removed sequential-thinking MCP (methodology incorporated into instructions)
- Mapped GitHub MCP to `github/*` namespace
- Mapped Context7 and Microsoft Docs to `web` tool
- Added `read` and `search` for file operations

---

#### 2. prp-generator

**Claude Tools**:
```yaml
tools: mcp__sequentialthinking__sequentialthinking, mcp__github__get_issue,
  mcp__github__get_issue_comments, mcp__context7__resolve_library_id,
  mcp__context7__get_library_docs, WebFetch, WebSearch, Write, Read,
  mcp__microsoft-docs__microsoft_docs_search,
  mcp__microsoft-docs__microsoft_docs_fetch,
  mcp__microsoft-docs__microsoft_code_sample_search
```

**Copilot Tools**:
```yaml
tools: ["github/*", "custom-agent", "read", "search", "web", "todo"]
```

**Changes**:
- Removed sequential-thinking MCP
- Mapped GitHub MCP to `github/*` namespace
- Added `custom-agent` for delegation to technical-architecture-advisor
- Mapped Context7/Microsoft Docs to `web`
- Added `todo` for progress tracking

---

#### 3. executor

**Claude Tools**:
```yaml
tools: mcp__sequentialthinking__sequentialthinking, TodoWrite, Write, Read,
  MultiEdit, Glob, Grep, LS, Bash, mcp__github__get_file_contents,
  mcp__github__create_or_update_file, mcp__github__push_files,
  WebFetch, WebSearch
```

**Copilot Tools**:
```yaml
tools: ["*"]
```

**Changes**:
- Used wildcard `["*"]` for all tools (implementation agent needs full access)
- Includes all GitHub, Playwright, file, search, web, and shell tools

---

#### 4. orchestrator

**Claude Tools**:
```yaml
tools: Task, mcp__sequentialthinking__sequentialthinking, TodoWrite,
  mcp__github__get_issue, mcp__github__get_issue_comments,
  mcp__github__add_issue_comment, Write, Read, Bash
```

**Copilot Tools**:
```yaml
tools: ["github/*", "custom-agent", "todo", "read", "search"]
```

**Changes**:
- Mapped `Task` to `custom-agent` for multi-agent coordination
- Removed sequential-thinking MCP
- Mapped GitHub MCP to `github/*` namespace
- Added `todo` for workflow progress tracking
- Added `search` for codebase analysis

---

### Development Workflow Agents

#### 5. code-reviewer

**Claude Tools**:
```yaml
tools: Task, mcp__sequentialthinking__sequentialthinking,
  mcp__github__get_pull_request, mcp__github__get_pull_request_diff,
  mcp__github__get_pull_request_files, mcp__github__get_pull_request_comments,
  mcp__github__get_pull_request_reviews, mcp__github__get_file_contents,
  mcp__github__create_and_submit_pull_request_review, mcp__github__get_commit,
  mcp__github__list_commits, mcp__github__get_issue, Glob, Grep, Read,
  WebFetch, WebSearch, mcp__microsoft-docs__microsoft_docs_search,
  mcp__microsoft-docs__microsoft_docs_fetch,
  mcp__microsoft-docs__microsoft_code_sample_search
```

**Copilot Tools**:
```yaml
tools: ["github/*", "custom-agent", "read", "search", "web"]
```

**Changes**:
- Mapped all GitHub MCP to `github/*` namespace
- Added `custom-agent` for delegation to technical-architecture-advisor
- Mapped Microsoft Docs to `web`
- Simplified to tool categories

---

#### 6. pull-request-creator

**Claude Tools**:
```yaml
tools: mcp__sequentialthinking__sequentialthinking,
  mcp__context7__resolve_library_id, mcp__context7__get_library_docs,
  mcp__github__get_issue, mcp__github__get_file_contents,
  mcp__github__list_commits, mcp__github__get_commit,
  mcp__github__create_pull_request, mcp__github__get_pull_request_diff,
  mcp__github__get_pull_request_files, Glob, Grep, Read, WebFetch, WebSearch,
  mcp__microsoft-docs__microsoft_docs_search,
  mcp__microsoft-docs__microsoft_docs_fetch,
  mcp__microsoft-docs__microsoft_code_sample_search
```

**Copilot Tools**:
```yaml
tools: ["github/*", "read", "search", "web"]
```

**Changes**:
- Removed sequential-thinking MCP
- Mapped GitHub MCP to `github/*` namespace
- Mapped Context7 and Microsoft Docs to `web`
- Simplified to tool categories

---

#### 7. technical-architecture-advisor

**Claude Tools**:
```yaml
tools: mcp__sequentialthinking__sequentialthinking,
  mcp__context7__resolve_library_id, mcp__context7__get_library_docs,
  Glob, Grep, Read, LS, WebFetch, WebSearch,
  mcp__microsoft-docs__microsoft_docs_search,
  mcp__microsoft-docs__microsoft_docs_fetch,
  mcp__microsoft-docs__microsoft_code_sample_search
```

**Copilot Tools**:
```yaml
tools: ["read", "search", "web"]
```

**Changes**:
- Removed sequential-thinking MCP (incorporated into analysis methodology)
- Removed Context7 and Microsoft Docs (use `web` instead)
- Simplified to essential read-only tools
- No GitHub access needed (advisory role only)

---

#### 8. screenshot-comparator

**Claude Tools**:
```yaml
tools: mcp__sequentialthinking__sequentialthinking,
  mcp__context7__resolve_library_id, mcp__context7__get_library_docs,
  mcp__github__get_issue, mcp__github__get_file_contents,
  mcp__github__list_commits, mcp__github__get_commit,
  mcp__github__create_pull_request, mcp__github__get_pull_request_diff,
  mcp__github__get_pull_request_files, Glob, Grep, Read, Bash,
  WebFetch, WebSearch
```

**Copilot Tools**:
```yaml
tools: ["playwright/*", "github/*", "shell", "read"]
```

**Changes**:
- **Added `playwright/*`** for browser automation and screenshots (improvement!)
- Kept `github/*` for PR/issue integration
- Kept `shell` for git state management
- Removed Context7 (not needed for screenshots)
- Removed web tools (not needed)

---

#### 9. senior-engineer

**Claude Tools**:
```yaml
tools: mcp__sequentialthinking__sequentialthinking,
  mcp__context7__resolve_library_id, mcp__context7__get_library_docs,
  mcp__github__get_issue, mcp__github__get_file_contents,
  mcp__github__list_commits, mcp__github__get_commit,
  mcp__github__get_pull_request_diff, mcp__github__get_pull_request_files,
  Glob, Grep, Read, Bash, WebFetch, WebSearch,
  mcp__microsoft-docs__microsoft_docs_search,
  mcp__microsoft-docs__microsoft_docs_fetch,
  mcp__microsoft-docs__microsoft_code_sample_search
```

**Copilot Tools**:
```yaml
tools: ["*"]
```

**Changes**:
- Used wildcard `["*"]` for all tools (senior engineer needs full access)
- Includes all available tools: GitHub, Playwright, files, search, web, shell, custom-agent

---

## Instruction Conversion Approach

### Claude Code Structure (Highly Structured)

```markdown
## Core Responsibility
[Detailed sections]

## Analysis Framework
[Structured subsections]

## Error Handling
[Specific failure scenarios]

## Output Format
[Structured output expectations]

## Statelessness Note
[Execution model clarification]
```

### Copilot Structure (Narrative Flow)

```markdown
You are [role description].

Your primary responsibility is to [core function].

## Your Approach

When [condition], do [action].

[Narrative explanation of workflow]

## Your Methodology

[Key principles and practices]

[Implementation guidance]
```

### Key Simplifications

1. **Removed Structured Headers**: Converted "Core Responsibility", "Analysis Framework", etc. to narrative flow
2. **Consolidated Error Handling**: Integrated error handling into main instructions rather than separate section
3. **Removed Meta-Sections**: Eliminated "Output Format", "Statelessness Note", "Handoff Protocol" sections
4. **Preserved Core Logic**: Kept essential workflows, decision points, and validation requirements
5. **Maintained Collaboration**: Preserved agent delegation patterns using `custom-agent` tool

---

## Features Lost in Migration

### 1. Model Selection

**Claude Code**:
```yaml
model: sonnet  # or haiku, opus
```

**Copilot**: No model selection (uses default model for all agents)

**Impact**: Can't optimize for cost (haiku) or power (sonnet) per agent

---

### 2. Color Coding

**Claude Code**:
```yaml
color: purple  # or blue, red, yellow, green, orange
```

**Copilot**: No visual organization

**Impact**: Purely cosmetic, no functional loss

---

### 3. Explicit MCP Tool Control

**Claude Code**:
```yaml
tools: mcp__github__get_issue, mcp__context7__resolve_library_id, WebSearch
```

**Copilot**:
```yaml
tools: ["github/*", "web"]
```

**Impact**: Less precise tool access control (category vs individual tool)

---

### 4. Context7 Documentation Access

**Claude Code**: Direct access to up-to-date library documentation via Context7 MCP

**Copilot**: Generic web search/fetch only

**Impact**: Less targeted documentation research, may require more manual refinement

---

### 5. Microsoft Docs Integration

**Claude Code**: Direct access to Microsoft Learn documentation with optimized search

**Copilot**: Generic web search/fetch only

**Impact**: Less precise for Microsoft/Azure-specific documentation lookups

---

### 6. Sequential Thinking MCP

**Claude Code**: Explicit tool for deep, structured reasoning with branching logic

**Copilot**: Methodology incorporated into agent instructions

**Impact**: Less structured reasoning process, but agents can still apply systematic thinking

---

## Features Gained in Migration

### 1. Playwright Integration

**Copilot Advantage**: Out-of-box `playwright/*` namespace for browser automation

**Use Case**: screenshot-comparator agent now has cleaner browser automation vs bash scripts

**Benefit**: More reliable, maintainable screenshot capture

---

### 2. GitHub Namespace

**Copilot Advantage**: Clean `github/*` namespace with consistent naming

**Benefit**: Easier to understand and use GitHub tools vs verbose `mcp__github__` prefixes

---

## Testing Recommendations

### Phase 1: Individual Agent Testing

Test each agent independently to verify:

1. **Tool Access**: Confirm agent can access specified tool categories
2. **GitHub Integration**: Test `github/*` tool calls work correctly
3. **Playwright Integration**: Verify `playwright/*` tools function (screenshot-comparator)
4. **Agent Delegation**: Test `custom-agent` tool works for multi-agent workflows
5. **Instruction Clarity**: Ensure Copilot interprets instructions correctly

### Phase 2: Agent Collaboration Testing

Test multi-agent workflows:

1. **Orchestrator Pipeline**: Test full context engineering pipeline
2. **Code Review with Architecture**: Test code-reviewer → technical-architecture-advisor delegation
3. **Implementation with Architecture**: Test senior-engineer → technical-architecture-advisor delegation
4. **PR Creation Flow**: Test senior-engineer → pull-request-creator flow

### Phase 3: Production Testing

Test in real-world scenarios:

1. **Real GitHub Issues**: Test with actual issues in your repositories
2. **Real PRs**: Test code review and PR creation with real changes
3. **Complex Features**: Test executor with real PRPs
4. **Error Scenarios**: Test error handling and recovery mechanisms

---

## Known Limitations

### GitHub MCP Permissions

**Issue**: GitHub MCP tools are read-only by default in Copilot

**Impact**: Agents like github-issue-analyzer may not be able to post comments

**Workaround**: Configure GitHub MCP with appropriate write permissions at org/enterprise level

### Playwright Localhost Restriction

**Issue**: Playwright MCP configured for localhost access only by default

**Impact**: screenshot-comparator can only capture screenshots from local dev server

**Workaround**: Acceptable for most use cases (comparing local branch changes)

### Web Search Quality

**Issue**: Generic `web` tool less targeted than Context7 or Microsoft Docs MCP

**Impact**: Documentation research may be less precise

**Workaround**: Agents can still search effectively, may need more query refinement

### Agent Coordination Complexity

**Issue**: Multi-agent workflows rely on `custom-agent` tool behavior

**Impact**: Uncertain if Copilot's custom-agent tool supports same coordination patterns as Claude's Task tool

**Workaround**: Test thoroughly, may need to simplify orchestration patterns

---

## Future Enhancements

### Organization/Enterprise MCP Servers

Consider adding these MCP servers at org/enterprise level:

1. **Context7 MCP**: For precise library documentation access
2. **Microsoft Docs MCP**: For Microsoft/Azure-specific documentation
3. **Sequential Thinking MCP**: For structured reasoning (if available for Copilot)

### Agent Refinements

Based on testing, consider:

1. **Simplifying Orchestrator**: If multi-agent coordination is limited, merge orchestrator logic
2. **Enhancing Instructions**: Adjust instructions based on Copilot's interpretation
3. **Tool Permissions**: Configure GitHub MCP write permissions for posting agents
4. **Custom MCP Servers**: Build custom MCP servers for specialized needs

---

## Conclusion

The migration from Claude Code to GitHub Copilot agents is largely successful:

**✅ What Works**:
- Core agent functionality preserved
- GitHub integration enhanced with `github/*` namespace
- Playwright integration improved for screenshot-comparator
- Agent collaboration maintained via `custom-agent` tool

**⚠️ What Changed**:
- No model selection (use default for all)
- Generic web search instead of specialized documentation access
- Category-level tool access instead of granular control
- Simplified instructions (narrative vs structured)

**❌ What's Lost**:
- Context7 and Microsoft Docs direct integration
- Sequential thinking MCP explicit tool
- Visual organization (color coding)
- Per-agent model optimization

Overall, the Copilot agents provide equivalent functionality for most use cases, with some improved integrations (Playwright) and some reduced precision (documentation research).
