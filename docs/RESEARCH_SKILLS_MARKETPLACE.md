# Research Summary: Claude Skills and Marketplaces

## Date: 2026-01-17

## Research Question
Can skills be exposed in custom plugin marketplaces, and what is the structure for creating skills for Claude Code?

## Research Findings

### 1. Skills CAN be Exposed in Marketplaces ✅

**Answer: YES** - Skills are part of plugins, and plugins are distributed via marketplace.json catalogs.

### How It Works

1. **Marketplace Structure**: A marketplace is defined by a `.claude-plugin/marketplace.json` file that catalogs available plugins
2. **Plugin Structure**: Each plugin contains a `.claude-plugin/plugin.json` and can include:
   - **Agents**: AI workers with dedicated context
   - **Commands**: User-invoked slash commands
   - **Skills**: Auto-loaded knowledge packages
3. **Distribution**: Users add marketplaces with `/plugin marketplace add <url>` and install plugins with `/plugin install <name>`

### 2. SKILL.md Format Specification

Skills follow the official Anthropic Agent Skills specification from [agentskills.io](https://agentskills.io/specification).

#### Required Structure

```markdown
---
name: skill-name              # MUST match directory name (lowercase, hyphen-separated)
description: What the skill does and when to use it
---

# Skill Content
[Markdown body with instructions, examples, best practices]
```

#### Optional Fields

```yaml
license: MIT                  # License identifier
allowed-tools:                # Pre-approved tools (Claude Code specific)
  - tool1
  - tool2
metadata:                     # Custom key-value pairs
  author: "Author Name"
  version: "1.0.0"
  category: "development"
```

#### Validation Rules

- **Name**: Must be lowercase, hyphen-separated, and match parent directory name exactly
- **Directory**: Must be named identically to the skill name
- **File**: Must be named `SKILL.md` at the root of the skill directory
- **Frontmatter**: Must start with `---` and end with `---`
- **Body**: Freeform Markdown content

### 3. How Skills Work

**Progressive Disclosure**:
1. Claude loads only YAML metadata initially for all skills
2. Metadata is used for discovery and matching based on description
3. Full skill content is loaded only when relevant to the current context
4. This minimizes context window usage

**Auto-Loading**:
- Skills are automatically loaded when their description matches the current context
- No explicit invocation needed
- Example: Asking to "review this code" auto-loads `code-review-checklist` skill

**Complementary to Agents**:
- **Agents**: Do work (implement features, review code)
- **Commands**: Trigger workflows (/create-pr, /generate-prp)
- **Skills**: Provide knowledge (best practices, templates, checklists)

### 4. Plugin Marketplace Structure

```
marketplace-repo/
├── .claude-plugin/
│   └── marketplace.json          # Catalog of plugins
├── plugins/
│   ├── plugin-name/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin metadata
│   │   ├── agents/               # Optional: AI workers
│   │   ├── commands/             # Optional: Slash commands
│   │   ├── skills/               # Optional: Knowledge packages
│   │   │   └── skill-name/
│   │   │       └── SKILL.md     # Required for each skill
│   │   └── README.md
└── README.md
```

### 5. marketplace.json Format

```json
{
  "name": "marketplace-name",
  "owner": {
    "name": "Owner Name",
    "url": "https://github.com/owner/repo"
  },
  "metadata": {
    "version": "1.0.0",
    "description": "Marketplace description",
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "source": "./plugins/plugin-name",
      "description": "Plugin description",
      "version": "1.0.0",
      "category": "development",
      "keywords": ["keyword1", "keyword2"]
    }
  ]
}
```

### 6. Official Resources

#### Documentation
- **Skills Specification**: https://agentskills.io/specification
- **Claude Code Skills**: https://code.claude.com/docs/en/skills
- **Plugin Marketplaces**: https://code.claude.com/docs/en/plugin-marketplaces
- **Plugin Reference**: https://code.claude.com/docs/en/plugins-reference
- **Agent Skills Overview**: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

#### Examples
- **Official Skills**: https://github.com/anthropics/skills
- **Official Plugins**: https://github.com/anthropics/claude-plugins-official
- **Claude Code Examples**: https://github.com/anthropics/claude-code-examples

### 7. Best Practices for Skills

#### Skill Creation
1. **Focused Content**: Each skill should cover a specific domain
2. **Clear Descriptions**: Write descriptions that clearly indicate when to use the skill
3. **Concise**: Keep content concise to minimize context window usage
4. **Examples**: Include practical examples where helpful
5. **Progressive Detail**: Start with core concepts, then provide details

#### Skill Naming
- Use lowercase with hyphens: `api-security-patterns`
- Be descriptive: `code-review-checklist` not just `review`
- Match directory name exactly

#### Integration
- Design skills to complement agents (provide knowledge agents can use)
- Skills should provide reference material, not perform work
- Include templates, checklists, and best practices

### 8. Implementation for .NET Development

Based on this research, I created a `.NET Development` plugin with a comprehensive C# skill:

**Plugin**: `dotnet-development`
- **Version**: 1.0.0
- **Category**: development
- **Keywords**: dotnet, csharp, c#, .net, development, best-practices

**Skill**: `csharp-dotnet-development`
- **Purpose**: Comprehensive C# and .NET development guidance
- **Coverage**: 
  - SOLID principles and clean code
  - C# naming conventions and modern features (C# 10+)
  - Async/await best practices
  - Dependency injection patterns
  - Entity Framework Core best practices
  - ASP.NET Core API development
  - Testing strategies
  - Security best practices
  - Performance optimization
  - Common pitfalls to avoid

**Size**: 17KB+ of comprehensive guidance

**Auto-loads when**: Developing, reviewing, or refactoring .NET applications

## Conclusion

✅ **Skills can be exposed in marketplaces** as part of plugins  
✅ **Marketplace distribution is simple** via Git repositories  
✅ **Skills follow an open standard** (Anthropic Agent Skills specification)  
✅ **Auto-loading works via description matching** for seamless integration  
✅ **Progressive disclosure** ensures efficient context window usage  

The .NET Development plugin demonstrates a complete implementation following all best practices and specifications.

## Next Steps for Further Development

The user mentioned they will iterate on the details of C# .NET development patterns themselves. Future enhancements could include:

1. **Additional Skills**:
   - `blazor-development` - Blazor-specific patterns
   - `minimal-apis` - Minimal API patterns
   - `grpc-services` - gRPC development
   - `microservices-patterns` - .NET microservices

2. **Commands**:
   - `/dotnet-new-api` - Scaffold new API project
   - `/dotnet-migration` - Create EF Core migration
   - `/dotnet-test` - Run .NET tests with coverage

3. **Agents**:
   - `dotnet-architect` - Architecture guidance
   - `dotnet-security-reviewer` - Security-focused reviews
   - `dotnet-performance-analyzer` - Performance optimization

4. **Company-Specific Customization**:
   - Internal library patterns
   - Company coding standards
   - Deployment practices
   - CI/CD workflows
