# External Documentation References

Synthesized knowledge from official AGENTS.md and Claude Code documentation sources.

## Official AGENTS.md Specification

**Source**: [agents.md](https://agents.md/)

### Key Points

- **Purpose**: AGENTS.md is a dedicated guide for AI coding agents, complementing README.md
- **Format**: Standard Markdown with no required fields - complete flexibility in structure
- **Ecosystem**: Works across 60,000+ open-source projects and multiple AI platforms (Claude, Copilot, Cursor, etc.)

### Nested Files for Monorepos

Create nested AGENTS.md files in subdirectories. Agents automatically prioritize the closest file in the directory tree, allowing tailored instructions per subproject.

**Precedence Rules**:
1. Nearest AGENTS.md to edited file takes priority
2. Explicit user prompts override all documentation

### Governance

AGENTS.md is stewarded by the Agentic AI Foundation under the Linux Foundation, with contributions from OpenAI Codex, Amp, Jules, Cursor, and Factory.

---

## GitHub's Analysis of 2,500+ Repositories

**Source**: [How to write a great agents.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)

### What Actually Works

1. **Specificity Over Vagueness**
   - Define specialists, not generalists
   - Bad: "helpful coding assistant"
   - Good: "test engineer who writes tests for React components, follows these examples, and never modifies source code"

2. **Command-First Approach**
   - Put executable commands in early sections
   - Include flags and specific options, not just tool names
   - Example: `pytest -v --cov=src` not just "run pytest"

3. **Show, Don't Tell**
   - One real code snippet outperforms paragraphs of explanation
   - Include examples of both good and bad code patterns

4. **Three-Tier Boundaries**
   - Always do
   - Ask first
   - Never do
   - Most common helpful constraint: "never commit secrets"

### Six Essential Sections

Top-performing AGENTS.md files cover:
1. Executable commands
2. Testing practices
3. Project structure
4. Code style guidelines
5. Git workflow
6. Explicit boundaries

### Practical Foundation

Start minimal with three elements:
- **Agent name** (e.g., `test-agent`)
- **Description** (one sentence about function)
- **Persona** (specific expertise and role)

Then expand iteratively based on where your agent makes mistakes.

### Six Agent Archetypes Worth Building

1. **@docs-agent** – Generates API documentation from code
2. **@test-agent** – Writes unit and integration tests
3. **@lint-agent** – Fixes style issues automatically
4. **@api-agent** – Creates endpoints and resolvers
5. **@dev-deploy-agent** – Handles development builds
6. Custom agents matching your workflow needs

**Key Insight**: Effective agents grow through iteration, not elaborate upfront planning.

---

## Claude Code Documentation

### Skills (platform.claude.com)

**Source**: [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

Skills use **progressive disclosure** with three loading levels:
1. **Level 1: Metadata** (always loaded) - name + description only
2. **Level 2: Instructions** (when triggered) - SKILL.md body
3. **Level 3: Resources** (as needed) - supporting files

**Best Practice**: Keep SKILL.md concise, extract detailed content to supporting files.

### Subagents (code.claude.com)

**Source**: [Sub-agents](https://code.claude.com/docs/en/sub-agents)

- Subagents run in separate context windows
- Tool access should be minimal necessary
- Skills are auto-invoked based on description matching

### Skills vs Commands

**Source**: [Claude Code Components Guide](https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins)

| Component | Invocation | Use Case |
|-----------|------------|----------|
| Skills | Auto (Claude decides) | Domain expertise, workflows |
| Commands | Manual (`/command`) | Frequent prompt templates |
| Agents | Via Task tool | Specialized workflows |

---

## Key Takeaways

1. **Start minimal, iterate based on mistakes** - Don't over-engineer upfront
2. **Specificity wins** - Define narrow specialists, not broad generalists
3. **Commands first** - Provide exact, copy-paste ready commands
4. **Show examples** - Real code snippets beat abstract descriptions
5. **Clear boundaries** - Always/Ask/Never categories work well
6. **Progressive disclosure** - Load detailed content only when needed
7. **Nested structure** - Use subdirectory AGENTS.md for monorepos
