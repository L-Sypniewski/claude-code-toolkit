# Claude Code Toolkit

A comprehensive plugin marketplace for [Claude Code CLI](https://claude.ai/code) with modular plugins for enhanced development workflows, context engineering, git management, and documentation.

## 🎯 What is This?

This repository serves as a **Claude Code Plugin Marketplace** containing curated, production-ready plugins that extend Claude Code's capabilities. Each plugin includes **agents** (specialized AI workers), **commands** (slash commands), and **skills** (reusable domain knowledge) that work together to enhance your development workflow. Plugins are self-contained and can be installed independently based on your needs.

## 📦 Available Plugins

### 🔧 Context Engineering

**Advanced workflow automation with PRP generation and GitHub issue analysis**

- 4 specialized agents for workflow orchestration
- GitHub issue analysis and processing
- PRP (Prompt-Response-Plan) generation and execution
- Multi-step workflow coordination
- **Skills**: PRP templates, issue analysis frameworks

[View Details →](plugins/context-engineering/README.md)

### 💻 Development Workflow

**Complete development lifecycle support from architecture to PR creation**

- Senior engineering and implementation support
- Expert code review capabilities
- Architecture advisory and design guidance
- Visual regression testing
- Professional PR documentation
- Bug investigation and fixing workflows
- Refactoring planning and execution
- **Skills**: Code quality standards, security best practices, testing patterns

[View Details →](plugins/development-workflow/README.md)

### 🌿 Git & Project Management

**Git worktree utilities and project planning tools**

- Parallel development with git worktrees
- Streamlined worktree merging and cleanup
- Structured project plan generation
- **Skills**: Git workflow best practices, commit conventions

[View Details →](plugins/git-project-management/README.md)

### 📚 Documentation Templates

**Templates and examples for project documentation**

- AGENTS.md creation templates
- Claude Code delegation rules examples
- Real-world documentation patterns
- Best practices guides
- **Skills**: Documentation patterns, README guidelines

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
│   │   ├── agents/               # Specialized workflow agents
│   │   ├── commands/             # Slash commands
│   │   └── skills/               # Reusable domain knowledge
│   ├── development-workflow/     # Development lifecycle tools
│   │   ├── agents/               # Development agents
│   │   ├── commands/             # Development commands
│   │   └── skills/               # Code quality, security, testing skills
│   ├── git-project-management/   # Git and planning utilities
│   │   ├── commands/             # Git workflow commands
│   │   └── skills/               # Git best practices skills
│   └── documentation-templates/  # Documentation templates
│       ├── prompts/              # Documentation prompts
│       ├── examples/             # Real-world examples
│       └── skills/               # Documentation pattern skills
├── README.md                      # This file
└── .claude/                       # Local settings
```

## 🧩 Understanding Components

### Agents
Specialized AI workers with their own context windows that can:
- Handle complex, multi-step tasks
- Collaborate with other agents
- Make architectural decisions
- Perform deep analysis and review

### Commands
Slash commands that provide:
- Quick access to specific workflows
- Structured task execution
- One-time operations
- Interactive prompts

### Skills
Reusable domain knowledge that:
- **Automatically activate** when agents need them
- Provide guidelines and best practices
- Ensure consistency across tasks
- Complement agents with expert knowledge
- Can be used by multiple agents

**Example:** The `code-quality-standards` skill is automatically referenced by the `senior-engineer` agent during code implementation and by the `code-reviewer` agent during code reviews, ensuring consistent quality standards.

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

4. **Start using agents, commands, and skills:**
   - Agents activate automatically based on your tasks
   - Commands are available via slash commands (e.g., `/create-pr`)
   - Skills automatically activate when agents need domain knowledge

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

## 🛠️ Plugin Development

Each plugin follows Claude Code standards:

- `.claude-plugin/plugin.json` with metadata
- Standard directory structure (`agents/`, `commands/`)
- Individual README with usage instructions
- Semantic versioning

See the [Claude Code Plugin Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference) for plugin development guidelines.

## 📖 Documentation

### Plugin Documentation

- [Context Engineering Plugin](plugins/context-engineering/README.md)
- [Development Workflow Plugin](plugins/development-workflow/README.md)
- [Git & Project Management Plugin](plugins/git-project-management/README.md)
- [Documentation Templates Plugin](plugins/documentation-templates/README.md)

### External Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Plugin Marketplace Guide](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)
- [Plugin Development Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)

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
