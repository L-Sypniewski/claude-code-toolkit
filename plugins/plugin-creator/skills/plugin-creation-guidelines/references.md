# Plugin Creation Guidelines - Research Sources

This document contains the source URLs and references for best practices distilled in the main SKILL.md.

## Primary Research Sources

### 1. Blog Post: Claude Skills, Commands, Subagents & Plugins
**URL**: https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins

**Key Topics**:
- WHEN/WHEN NOT description pattern for explicit boundaries
- Token optimization: Agent refactoring from 803 lines (62/100 score) to 281 lines (82-85/100 score)
- DRY principles: Extract templates to separate skill files
- Hybrid execution: Subagents analyze (Read/Grep/Glob), Main Claude executes (Write/Edit/Bash)
- Plugin distribution and marketplace integration

**Critical Insights**:
- Conciseness over comprehensiveness improves performance
- Generic descriptions fail; specificity prevents false positives
- Multi-skill coordination works—Claude loads complementary skills together

### 2. Blog Post: Understanding Claude Code Full Stack
**URL**: https://alexop.dev/posts/understanding-claude-code-full-stack/

**Key Topics**:
- Plugin architecture and organization
- Skills provide superior context efficiency vs MCP servers
- CLAUDE.md hierarchy for persistent project context
- Layered context strategy: CLAUDE.md + skills + subagents
- XML-tagged structures for reliable AI responses

**Critical Insights**:
- Skills activate contextually when descriptions match task context (automatic)
- Slash commands require explicit triggering (manual)
- Subagents enable parallel execution and context isolation
- Token efficiency through hierarchical context loading

### 3. Anthropic Official Examples
**URL**: https://github.com/anthropics/skills/tree/main/skills

**Key Topics**:
- Naming conventions: hyphenated lowercase
- Skill structure: SKILL.md with name/description frontmatter
- Technology specification in descriptions
- Self-contained organization per skill folder

**Examples Referenced**:
- `algorithmic-art`, `canvas-design`, `slack-gif-creator` (Creative & Design)
- `web-artifacts-builder`, `mcp-builder`, `webapp-testing` (Development & Technical)
- `brand-guidelines`, `internal-comms`, `theme-factory` (Enterprise & Communication)
- `skill-creator`, `template-skill` (Meta/Educational)

### 4. Official Claude Code Documentation
**URL**: https://code.claude.com/docs

**Key Topics** (referenced throughout SKILL.md):
- Plugin structure requirements
- Agent frontmatter schema
- Command argument patterns
- Skill auto-loading behavior
- Tool access specification

## Pattern Sources by Section

### Token Optimization (300-400 line recommendation)
- Source: youngleaders.tech blog post
- Evidence: 281-line agent scored 82-85/100 vs 803-line at 62/100
- Application: ui-ux-audit reference implementation

### WHEN/WHEN NOT Description Pattern
- Source: youngleaders.tech blog post
- Quote: "Description engineering is critical—use WHEN + WHEN NOT pattern"
- Impact: Reduces incorrect agent selection routing errors

### Orchestrator-Worker Pattern
- Source: ui-ux-audit validated implementation
- Evidence: 281-line orchestrator + 108-line worker + 322-line skill = 49% token reduction

### Naming Conventions (kebab-case)
- Source: Anthropic official examples repository
- Consistency: All 15 example skills use hyphenated lowercase
- Application: Plugin marketplace standard

### Skill-Augmented Architecture
- Source: alexop.dev blog post
- Principle: "Skills provide superior context efficiency"
- Pattern: Automatic contextual loading vs explicit invocation

## Usage Notes

**For Agents**: Reference this file when user asks about source materials or wants to verify best practices origin.

**For Users**: Use these URLs to explore original research and stay current with evolving patterns.

**Updates**: This file should be updated when new authoritative sources emerge or blog posts are revised.