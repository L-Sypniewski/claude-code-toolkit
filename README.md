# Claude Code Toolkit

A comprehensive plugin marketplace for [Claude Code CLI](https://claude.ai/code) with modular plugins for enhanced development workflows, context engineering, git management, and documentation.

## 🎯 What is This?

This repository serves as a **Claude Code Plugin Marketplace** containing curated, production-ready plugins that extend Claude Code's capabilities. Each plugin is self-contained and can be installed independently based on your needs.

## 📦 Available Plugins

### 🔧 Context Engineering

**Advanced workflow automation with PRP generation and GitHub issue analysis**

- 4 specialized agents for workflow orchestration
- 3 Claude Code skills for procedural knowledge
- GitHub issue analysis and processing
- PRP (Prompt-Response-Plan) generation and execution
- Multi-step workflow coordination

[View Details →](plugins/context-engineering/README.md)

### 💻 Development Workflow

**Complete development lifecycle support from architecture to PR creation**

- 5 specialized agents for development excellence
- 2 Claude Code skills for coding standards and patterns
- Senior engineering and implementation support
- Expert code review capabilities
- Architecture advisory and design guidance
- Visual regression testing
- Professional PR documentation
- Bug investigation and fixing workflows
- Refactoring planning and execution

[View Details →](plugins/development-workflow/README.md)

### 🌿 Git & Project Management

**Git worktree utilities and project planning tools**

- 2 Claude Code skills for git workflows and project planning
- Parallel development with git worktrees
- Streamlined worktree merging and cleanup
- Structured project plan generation
- Git workflow patterns and best practices

[View Details →](plugins/git-project-management/README.md)

### 📚 Documentation Templates

**Templates and examples for project documentation**

- 2 Claude Code skills for agent documentation and delegation
- AGENTS.md creation templates
- Claude Code delegation rules examples
- Real-world documentation patterns
- Best practices guides

[View Details →](plugins/documentation-templates/README.md)

## 🚀 Installation

### Install the Entire Marketplace

```bash
# Add this marketplace to Claude Code
/plugin marketplace add https://github.com/L-Sypniewski/claude-code-toolkit.git

# Or for local development
/plugin marketplace add /path/to/claude-code-toolkit
```

### Install Individual Plugins

Once the marketplace is added, install specific plugins:

```bash
/plugin install context-engineering
/plugin install development-workflow
/plugin install git-project-management
/plugin install documentation-templates
```

### Team Installation (Automatic)

For teams, add to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": [
    "https://github.com/L-Sypniewski/claude-code-toolkit.git"
  ]
}
```

## 📋 Repository Structure

```
claude-code-toolkit/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace configuration
├── plugins/
│   ├── context-engineering/      # Context engineering workflows
│   ├── development-workflow/     # Development lifecycle tools
│   ├── git-project-management/   # Git and planning utilities
│   └── documentation-templates/  # Documentation templates
├── README.md                      # This file
└── .claude/                       # Local settings
```

## 🎓 Getting Started

### For Individual Developers

1. **Install the marketplace:**

   ```bash
   /plugin marketplace add https://github.com/L-Sypniewski/claude-code-toolkit.git
   ```

2. **Browse available plugins:**

   ```bash
   /plugin list
   ```

3. **Install plugins you need:**

   ```bash
   /plugin install development-workflow
   ```

4. **Start using agents and commands:**
   - Agents activate automatically based on your tasks
   - Commands are available via slash commands (e.g., `/create-pr`)

### For Teams

1. **Configure team marketplace** in `.claude/settings.json`
2. **Document recommended plugins** for your project
3. **Share configuration** via version control
4. **Onboard new members** - plugins install automatically

## 💡 Usage Examples

### Context Engineering Workflow

```bash
# Analyze a GitHub issue
/initial-github-issue https://github.com/owner/repo/issues/123

# Generate a structured PRP
/generate-prp

# Execute the PRP with tracking
/execute-prp
```

### Development Workflow

```bash
# Get architecture guidance
# (technical-architecture-advisor agent activates automatically)

# Implement with senior engineer agent
# (senior-engineer agent provides implementation support)

# Review code before commit
# (code-reviewer agent performs comprehensive review)

# Create professional PR
/create-pr
```

### Git Worktree Management

```bash
# Start parallel feature development
/create_worktree feature/new-ui

# After completion, merge and cleanup
/merge_worktree feature/new-ui
```

## 🎓 Understanding Skills vs Agents vs Commands

This marketplace includes three types of components that work together:

### 🤖 Agents
**Specialized AI entities** with dedicated context for complex tasks
- Have their own context windows and tool access
- Actively perform work (implement features, review code, etc.)
- Explicitly invoked or automatically activated based on context
- Example: `senior-engineer`, `code-reviewer`

### ⚡ Commands
**User-invoked actions** via slash commands
- Direct user control with `/command-name`
- Execute specific workflows or tasks
- Example: `/create-pr`, `/generate-prp`

### 📚 Skills
**Modular knowledge packages** that Claude auto-loads
- Provide procedural knowledge and templates
- Automatically loaded when context matches
- No explicit invocation needed
- Complement agents by providing domain expertise
- Example: `code-review-checklist`, `git-workflow-patterns`

**Key Difference**: Agents *do work*, commands *trigger workflows*, skills *provide knowledge*.

## 🛠️ Plugin Development

Each plugin follows Claude Code standards:

- `.claude-plugin/plugin.json` with metadata
- Standard directory structure (`agents/`, `commands/`, `skills/`)
- Individual README with usage instructions
- Semantic versioning

Plugin structure:
```
plugin-name/
├── .claude-plugin/
│   └── plugin.json
├── agents/           # AI workers with context
├── commands/         # User-invoked actions
├── skills/          # Auto-loaded knowledge
│   └── skill-name/
│       └── SKILL.md  # Required skill file
└── README.md
```

See the [Claude Code Plugin Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference) for plugin development guidelines and the [Anthropic Skills Repository](https://github.com/anthropics/skills) for skill creation guidance.

## 📖 Documentation

### Plugin Documentation

- [Context Engineering Plugin](plugins/context-engineering/README.md)
- [Development Workflow Plugin](plugins/development-workflow/README.md)
- [Git & Project Management Plugin](plugins/git-project-management/README.md)
- [Documentation Templates Plugin](plugins/documentation-templates/README.md)

### External Resources

#### Official Claude Code Documentation
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code) - Main documentation hub
- [Plugin Development Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference) - How to build plugins
- [Plugin Marketplace Guide](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces) - Publishing to marketplaces
- [Agent Skills Documentation](https://docs.claude.com/en/docs/claude-code/agent-skills) - Creating and using skills

#### Skills Resources
- [Anthropic Skills Repository](https://github.com/anthropics/skills) - Official skills examples
- [Agent Skills Overview](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Technical deep dive
- [Skills Specification](https://github.com/anthropics/skills/blob/main/agent_skills_spec.md) - SKILL.md format

## 🤝 Contributing

We welcome contributions! You can:

- **Add new plugins** to the marketplace
- **Improve existing plugins** with new agents/commands
- **Enhance documentation** and examples
- **Report issues** or suggest features

Please ensure:

- Plugins follow Claude Code standards
- Include comprehensive README files
- Use semantic versioning
- Test thoroughly before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Resources

- [Claude Code CLI](https://claude.ai/code)
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Official Claude Code Examples](https://github.com/anthropics/claude-code-examples)
- [Copilot Agent Equivalents](https://github.com/TwentyFiveDev-L-Sypniewski/.github-private) - GitHub Copilot agent equivalents for these Claude Code plugins

## 📞 Support

- Create an [issue](https://github.com/L-Sypniewski/claude-code-toolkit/issues) for bugs or feature requests
- Check existing [discussions](https://github.com/L-Sypniewski/claude-code-toolkit/discussions) for community help
- Review plugin-specific README files for detailed usage guides

---

⭐ If you find this marketplace helpful, please consider giving it a star!
