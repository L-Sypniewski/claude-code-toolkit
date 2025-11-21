# Claude Code Toolkit

A comprehensive plugin marketplace for [Claude Code CLI](https://claude.ai/code) with modular plugins following the **skills approach** for enhanced development workflows, context engineering, git management, and documentation.

## 🎯 What is This?

This repository serves as a **Claude Code Plugin Marketplace** containing curated, production-ready plugins that extend Claude Code's capabilities. Each plugin follows the **skills approach** from [Anthropic's skills repository](https://github.com/anthropics/skills), bundling skills that are automatically available when the plugin is installed. Skills are model-invoked based on their descriptions, making them seamlessly integrate into your Claude Code workflows.

### Skills Approach

Our plugins follow the modern skills approach where:
- **Skills are model-invoked**: Claude automatically uses the right skill based on its description
- **SKILL.md format**: Each skill has a YAML frontmatter + Markdown body structure
- **Self-contained**: Skills include all necessary context and instructions
- **Progressive disclosure**: Skills can include optional `scripts/`, `references/`, and `assets/` directories

Learn more about skills: [Anthropic Skills Documentation](https://support.claude.com/en/articles/12512176-what-are-skills)

## 📦 Available Plugins

### 🔧 Context Engineering

**Advanced workflow automation with PRP generation and GitHub issue analysis**

**Skills included:**
- `github-issue-analyzer` - Analyze GitHub issues and create structured analysis comments
- `prp-generator` - Generate Product Requirements Prompts from GitHub issue analysis
- `prp-executor` - Execute PRPs using pragmatic development methodology
- `workflow-orchestrator` - Coordinate context engineering pipeline workflows

GitHub issue analysis, PRP generation/execution, and multi-step workflow coordination.

[View Details →](plugins/context-engineering/README.md)

### 💻 Development Workflow

**Complete development lifecycle support from architecture to PR creation**

**Skills included:**
- `senior-engineer` - Senior software engineer for implementation tasks
- `code-reviewer` - Expert code review specialist
- `architecture-advisor` - Technical architecture advisor
- `pr-creator` - Create comprehensive pull requests
- `screenshot-comparator` - Visual regression testing with before/after comparisons

Senior engineering, code review, architecture advisory, visual testing, and PR management.

[View Details →](plugins/development-workflow/README.md)

### 🌿 Git & Project Management

**Git worktree utilities and project planning tools**

**Skills included:**
- `git-worktree-manager` - Manage Git worktrees for parallel development

Parallel development with git worktrees, streamlined merging and cleanup.

[View Details →](plugins/git-project-management/README.md)

### 📚 Documentation Templates

**Templates and examples for project documentation**

**Skills included:**
- `agents-md-creator` - Create comprehensive AGENTS.md files following agents.md standard

AGENTS.md creation with templates, examples, and best practices.

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
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin metadata
│   │   └── skills/               # Bundled skills
│   │       ├── github-issue-analyzer/
│   │       ├── prp-generator/
│   │       ├── prp-executor/
│   │       └── workflow-orchestrator/
│   ├── development-workflow/     # Development lifecycle tools
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin metadata
│   │   └── skills/               # Bundled skills
│   │       ├── senior-engineer/
│   │       ├── code-reviewer/
│   │       ├── architecture-advisor/
│   │       ├── pr-creator/
│   │       └── screenshot-comparator/
│   ├── git-project-management/   # Git and planning utilities
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin metadata
│   │   └── skills/               # Bundled skills
│   │       └── git-worktree-manager/
│   └── documentation-templates/  # Documentation templates
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin metadata
│       └── skills/               # Bundled skills
│           └── agents-md-creator/
│               ├── SKILL.md      # Skill definition
│               └── references/   # Example templates
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

4. **Start using skills:**
   - Skills activate automatically based on Claude's assessment of your needs
   - Skills are model-invoked - Claude decides when to use them based on their descriptions

### For Teams

1. **Configure team marketplace** in `.claude/settings.json`
2. **Document recommended plugins** for your project
3. **Share configuration** via version control
4. **Onboard new members** - plugins install automatically

## 💡 Usage Examples

### Context Engineering Workflow

```bash
# Skills are invoked automatically by Claude based on your requests:

# "Analyze this GitHub issue: https://github.com/owner/repo/issues/123"
# → github-issue-analyzer skill activates

# "Generate a PRP from that issue"
# → prp-generator skill activates

# "Execute the PRP"
# → prp-executor skill activates

# Or use the workflow orchestrator for end-to-end:
# "Run the complete context engineering workflow for issue #123"
# → workflow-orchestrator coordinates all skills
```

### Development Workflow

```bash
# Skills activate based on what you're doing:

# "I need architectural advice on using Redis vs PostgreSQL for caching"
# → architecture-advisor skill provides guidance

# "Implement OAuth authentication with Google and GitHub"
# → senior-engineer skill handles implementation

# "Review my changes before I create a PR"
# → code-reviewer skill performs comprehensive review

# "Create a pull request for my changes"
# → pr-creator skill generates professional PR

# "Create before/after screenshots for the homepage"
# → screenshot-comparator skill captures and compares
```

### Git Worktree Management

```bash
# Skills activate when you need worktree operations:

# "Create a worktree for feature/new-ui"
# → git-worktree-manager creates and sets up worktree

# "Merge my worktree back to main"
# → git-worktree-manager handles merge and cleanup
```

### Documentation Creation

```bash
# "Create an AGENTS.md file for this repository"
# → agents-md-creator skill generates comprehensive documentation
```

## 🛠️ Plugin Development

Each plugin follows the **skills approach**:

- `.claude-plugin/plugin.json` with metadata and skills array
- `skills/` directory containing skill folders
- Each skill has a `SKILL.md` file with YAML frontmatter + Markdown body
- Optional `scripts/`, `references/`, and `assets/` directories per skill
- Individual README with usage instructions
- Semantic versioning

### Creating a Skill

Each skill must have a `SKILL.md` file with:

```markdown
---
name: skill-name
description: Clear description of what the skill does and when Claude should use it
---

# Skill Name

[Skill instructions and guidance]
```

See the [Agent Skills Spec](https://github.com/anthropics/skills/blob/main/agent_skills_spec.md) and [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills) for detailed guidelines.

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
