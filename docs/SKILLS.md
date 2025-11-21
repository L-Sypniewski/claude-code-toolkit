# Skills Documentation

This document provides comprehensive information about the skills included in the Claude Code Toolkit plugins.

## What are Skills?

Skills are modular, reusable containers for domain expertise, utilities, and procedures that Claude Code agents can automatically invoke when needed. Unlike agents (which handle complex workflows) or commands (which are explicitly invoked), skills provide contextual knowledge that enhances agent capabilities.

### Key Characteristics

- **Automatically Activated**: Skills are invoked by agents when their domain knowledge is relevant
- **Reusable**: Multiple agents can reference the same skill
- **Complementary**: Skills provide domain expertise that agents can leverage
- **Lightweight**: No separate processes or context windows needed
- **Standards-Based**: Follow industry best practices and specifications

### Skills vs Agents vs Commands

| Feature | Skills | Agents | Commands |
|---------|--------|--------|----------|
| Activation | Automatic | Automatic or delegated | Manual (slash command) |
| Context | Shared with agent | Separate context window | Single execution |
| Purpose | Domain knowledge | Complex workflows | Specific actions |
| Usage | Referenced as needed | Multi-step tasks | One-time operations |

## Skills by Plugin

### Development Workflow Plugin

#### 1. Code Quality Standards

**File**: `plugins/development-workflow/skills/code-quality-standards/SKILL.md`

**Purpose**: Provides comprehensive code quality standards and best practices for writing maintainable, readable, and performant code.

**Coverage**:
- Universal code quality principles (naming, functions, organization)
- Language-specific best practices (JavaScript/TypeScript, Python, Java, Go)
- Code review checklist
- Anti-patterns to avoid
- SOLID principles and design patterns

**Used By**:
- `senior-engineer` - During code implementation
- `code-reviewer` - During code review
- `technical-architecture-advisor` - For code quality concerns

**Size**: 235 lines, ~7,000 characters

#### 2. Security Best Practices

**File**: `plugins/development-workflow/skills/security-best-practices/SKILL.md`

**Purpose**: Comprehensive security guidelines covering OWASP Top 10, secure coding patterns, and security architecture.

**Coverage**:
- OWASP Top 10 prevention (Injection, XSS, CSRF, etc.)
- Authentication and authorization patterns
- Encryption and cryptography best practices
- API security (REST, GraphQL)
- Security checklist and tools
- Incident response procedures

**Used By**:
- `senior-engineer` - For security-sensitive implementations
- `code-reviewer` - During security-focused reviews
- `technical-architecture-advisor` - For security architecture

**Size**: 380 lines, ~11,000 characters

#### 3. Testing Patterns

**File**: `plugins/development-workflow/skills/testing-patterns/SKILL.md`

**Purpose**: Testing strategies and best practices for writing effective unit, integration, and end-to-end tests.

**Coverage**:
- Testing pyramid (unit, integration, E2E)
- Test structure patterns (AAA, Given-When-Then)
- Test naming conventions
- Mocking and stubbing strategies
- TDD and BDD approaches
- CI/CD integration

**Used By**:
- `senior-engineer` - During test creation
- `code-reviewer` - When reviewing test code
- `technical-architecture-advisor` - For testing strategy design

**Size**: 497 lines, ~12,000 characters

### Context Engineering Plugin

#### 4. PRP Templates

**File**: `plugins/context-engineering/skills/prp-templates/SKILL.md`

**Purpose**: Comprehensive PRP (Prompt-Response-Plan) templates for systematic problem-solving.

**Coverage**:
- PRP structure components (problem, analysis, approach, execution)
- PRP types (feature, bug fix, refactoring, investigation, migration)
- Best practices for planning and execution
- Complete PRP template examples
- Progress tracking and success metrics

**Used By**:
- `context-engineering-prp-generator` - During PRP creation
- `context-engineering-orchestrator` - For workflow coordination
- `context-engineering-executor` - During PRP execution

**Size**: 502 lines, ~10,000 characters

#### 5. Issue Analysis Frameworks

**File**: `plugins/context-engineering/skills/issue-analysis-frameworks/SKILL.md`

**Purpose**: Systematic frameworks for analyzing GitHub issues, bug reports, and feature requests.

**Coverage**:
- Issue analysis framework (assessment, deep analysis, context extraction)
- Bug report analysis templates
- Feature request analysis templates
- Issue classification and prioritization
- Stakeholder analysis
- Solution brainstorming frameworks

**Used By**:
- `context-engineering-github-issue-analyzer` - During issue analysis
- `context-engineering-orchestrator` - For issue-based workflows
- `context-engineering-prp-generator` - When creating PRPs from issues

**Size**: 519 lines, ~12,000 characters

### Git & Project Management Plugin

#### 6. Git Workflow Best Practices

**File**: `plugins/git-project-management/skills/git-workflow-best-practices/SKILL.md`

**Purpose**: Comprehensive Git workflow practices covering branching strategies and version control patterns.

**Coverage**:
- Branching strategies (Git Flow, GitHub Flow, Trunk-Based Development)
- Branch naming conventions
- Merging strategies (merge, squash, rebase)
- Conflict resolution
- Git worktree management
- Emergency procedures and troubleshooting

**Used By**:
- All agents performing git operations
- Particularly useful during worktree management
- Referenced during branch creation and merging

**Size**: 621 lines, ~14,000 characters

#### 7. Commit Conventions

**File**: `plugins/git-project-management/skills/commit-conventions/SKILL.md`

**Purpose**: Commit message conventions following Conventional Commits specification.

**Coverage**:
- Conventional Commits format (type, scope, description, body, footer)
- Commit types (feat, fix, docs, style, refactor, etc.)
- Scope guidelines
- Description best practices
- Breaking changes documentation
- Tools and automation (Commitizen, Commitlint)

**Used By**:
- All agents when creating commits
- `pull-request-creator` - For analyzing commits in PR descriptions
- `senior-engineer` - During code commits

**Size**: 655 lines, ~14,000 characters

### Documentation Templates Plugin

#### 8. Documentation Patterns

**File**: `plugins/documentation-templates/skills/documentation-patterns/SKILL.md`

**Purpose**: Documentation patterns and structures for creating clear, maintainable technical documentation.

**Coverage**:
- Four types of documentation (Tutorials, How-To, Reference, Explanation)
- Documentation structure (README, API, Architecture, Code)
- Writing style and best practices
- Visual elements (diagrams, screenshots)
- Documentation maintenance
- Special types (Runbooks, ADRs)

**Used By**:
- All agents when creating or updating documentation
- Documentation-focused tasks
- Technical specification generation

**Size**: 709 lines, ~15,000 characters

#### 9. README Guidelines

**File**: `plugins/documentation-templates/skills/readme-guidelines/SKILL.md`

**Purpose**: Complete README.md guidelines and best practices for effective project documentation.

**Coverage**:
- Complete README template
- Section-by-section guidelines
- Badges and visual elements
- README for different project types
- Internationalization
- Accessibility considerations
- Common mistakes to avoid

**Used By**:
- All agents when creating or updating README files
- Project initialization workflows
- Repository setup tasks

**Size**: 832 lines, ~16,000 characters

## How Skills Work

### Automatic Activation

Skills are automatically activated by Claude Code when:
1. An agent is working on a task related to the skill's domain
2. The agent needs domain expertise or best practices
3. The task context matches the skill's description

**Example Flow**:
```
User: "Implement user authentication"
  ↓
senior-engineer agent activated
  ↓
Needs security guidance → security-best-practices skill activated
Needs code quality guidance → code-quality-standards skill activated
  ↓
Implementation with security and quality standards applied
```

### Agent-Skill Mapping

| Agent | Primary Skills Used |
|-------|-------------------|
| senior-engineer | code-quality-standards, security-best-practices, testing-patterns |
| code-reviewer | code-quality-standards, security-best-practices, testing-patterns |
| technical-architecture-advisor | code-quality-standards, security-best-practices |
| context-engineering-prp-generator | prp-templates, issue-analysis-frameworks |
| context-engineering-github-issue-analyzer | issue-analysis-frameworks |
| context-engineering-orchestrator | prp-templates, issue-analysis-frameworks |
| context-engineering-executor | prp-templates |
| All agents (git operations) | git-workflow-best-practices, commit-conventions |
| All agents (documentation) | documentation-patterns, readme-guidelines |

## Skills Statistics

- **Total Skills**: 8
- **Total Lines of Content**: 4,550 lines
- **Total Characters**: ~92,000 characters
- **Plugins with Skills**: 4 out of 4 (100%)
- **Average Skill Size**: 570 lines

### Distribution by Plugin

| Plugin | Skills | Lines | Focus Area |
|--------|--------|-------|------------|
| Development Workflow | 3 | 1,112 | Code quality, security, testing |
| Context Engineering | 2 | 1,021 | Problem-solving, issue analysis |
| Git & Project Management | 2 | 1,276 | Version control, commits |
| Documentation Templates | 2 | 1,541 | Documentation patterns, README |

## Implementation Details

### Directory Structure

Each skill follows the standard Claude Code structure:

```
plugins/
└── plugin-name/
    └── skills/
        └── skill-name/
            └── SKILL.md
```

### SKILL.md Format

Every SKILL.md file includes:

1. **Frontmatter** (required):
   ```yaml
   ---
   name: skill-name
   description: Brief description of the skill
   author: Claude Code Toolkit
   ---
   ```

2. **Skill Title**: Main heading with skill name

3. **Purpose Section**: Explains when the skill is activated

4. **Content Sections**: Comprehensive guidelines, patterns, and best practices

5. **Usage Section**: Lists which agents use the skill

### Best Practices Followed

1. **Comprehensive Coverage**: Each skill thoroughly covers its domain
2. **Practical Examples**: Include code examples, templates, and checklists
3. **Industry Standards**: Based on OWASP, Conventional Commits, Keep a Changelog, etc.
4. **Clear Structure**: Organized with clear headings and sections
5. **Actionable Content**: Provides checklists, templates, and step-by-step guides

## Version History

- **v1.1.0** (Current): Initial skills implementation
  - Added 8 comprehensive skills across all plugins
  - Updated all plugin versions to 1.1.0
  - Updated marketplace.json and README files

- **v1.0.0**: Initial release with agents and commands only (no skills)

## Future Enhancements

Potential areas for future skill additions:

1. **Development Workflow**:
   - Performance optimization patterns
   - Accessibility guidelines (WCAG)
   - Code review checklist automation

2. **Context Engineering**:
   - Requirements gathering frameworks
   - System design templates

3. **Git & Project Management**:
   - Release management practices
   - Changelog generation patterns

4. **Documentation Templates**:
   - API documentation templates
   - Architecture decision records (ADR) templates
   - Troubleshooting guide patterns

## Contributing Skills

When adding new skills to the toolkit:

1. **Choose the Right Plugin**: Place skill in the most relevant plugin
2. **Follow Naming Conventions**: Use kebab-case for skill names
3. **Create SKILL.md**: Include proper frontmatter and comprehensive content
4. **Update plugin.json**: Increment version (minor bump for new skills)
5. **Update README**: Document the new skill in plugin README
6. **Update marketplace.json**: Update plugin version and description
7. **Size Guidelines**: Aim for 300-800 lines of comprehensive content
8. **Testing**: Verify skill is properly recognized by Claude Code

## References

- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)

---

For questions or contributions, please open an issue on the [GitHub repository](https://github.com/L-Sypniewski/claude-code-toolkit).
