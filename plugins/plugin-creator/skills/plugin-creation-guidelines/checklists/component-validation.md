# Component Validation Checklist

Comprehensive validation checklist for all plugin components.

## File Structure

- [ ] `.claude-plugin/plugin.json` exists
- [ ] `README.md` exists
- [ ] At least one of: agents/, commands/, skills/ exists
- [ ] All agent files have `.md` extension
- [ ] All skill directories contain `SKILL.md`
- [ ] All command files have `.md` extension

## Metadata Validation

- [ ] plugin.json has all required fields (name, version, description, author)
- [ ] Plugin name is kebab-case
- [ ] Version follows semantic versioning (X.Y.Z)
- [ ] Description is comprehensive (50-200 chars)
- [ ] Keywords array has 4-8 relevant keywords
- [ ] Repository and homepage URLs are valid

## Agent Validation

- [ ] Agent files have YAML frontmatter
- [ ] Frontmatter includes: name, description, tools, color, model
- [ ] Description follows WHEN + WHEN NOT pattern
- [ ] Agent name matches filename (without .md)
- [ ] Line count: 100-400 lines (target: 300)
- [ ] Tools list is appropriate (no unnecessary tools)
- [ ] Explicit skill references if applicable
- [ ] Clear workflow sections
- [ ] Error handling documented
- [ ] Integration points documented
- [ ] No security vulnerabilities in prompts

## Skill Validation

- [ ] Skill directory name is kebab-case
- [ ] Contains `SKILL.md` file
- [ ] SKILL.md has YAML frontmatter
- [ ] Frontmatter includes: name, description
- [ ] Description follows WHEN + WHEN NOT pattern
- [ ] Skill name matches directory name
- [ ] Line count: 300-500 lines (comprehensive reference)
- [ ] Organized into clear sections
- [ ] Contains examples (good and bad)
- [ ] Integration points documented
- [ ] No security vulnerabilities in example code

### Advanced Skill Validation (Claude Code 2.1+)

- [ ] If `context: fork` is used, skill genuinely benefits from isolation
- [ ] If `allowed-tools` specified, tools are appropriate for skill purpose
- [ ] If `metadata` present, includes useful organizational info (author, version)
- [ ] Skill description enables proper progressive disclosure activation
- [ ] Description under 200 chars for efficient initial loading
- [ ] Forked context skills document isolation rationale

## Command Validation

- [ ] Command file name is kebab-case
- [ ] Contains clear title (# heading)
- [ ] Documents arguments ($ARGUMENTS or $1, $2, etc.)
- [ ] Describes default behavior if no args
- [ ] Includes workflow steps
- [ ] Delegates to specific agent(s)
- [ ] Includes usage examples
- [ ] Line count: 50-150 lines

## README Validation

- [ ] Has clear title matching plugin name
- [ ] Brief one-line description at top
- [ ] Overview section explaining purpose
- [ ] Features list (bullets or numbered)
- [ ] Components tables (agents, commands, skills)
- [ ] Installation instructions
- [ ] Usage examples with actual commands
- [ ] Best practices section
- [ ] Integration section (if applicable)
- [ ] Requirements section (if applicable)
- [ ] License section

## Naming Conventions

- [ ] All component names use kebab-case
- [ ] Multi-agent plugins use consistent prefix
- [ ] Agent names are descriptive of role
- [ ] Skill names indicate domain/methodology
- [ ] Command names are verb + object
- [ ] No spaces in any names

## Integration Patterns

- [ ] Commands explicitly delegate to agents
- [ ] Agents explicitly reference skills (if applicable)
- [ ] Agent-to-agent spawning uses Task tool
- [ ] All references use exact component names
- [ ] Integration points documented in all components

## Security Validation

- [ ] Bash scripts: Input validation present
- [ ] Bash scripts: Proper quoting for paths
- [ ] Bash scripts: No shell injection vulnerabilities
- [ ] Python scripts: No eval/exec on user input
- [ ] Python scripts: Safe subprocess usage
- [ ] Python scripts: Path validation present
- [ ] Agent prompts: Confirmation gates for destructive ops
- [ ] Agent prompts: GET-only for web navigation
- [ ] Skills: Example code has no vulnerabilities
- [ ] Commands: Argument validation before delegation

## Token Optimization

- [ ] No content duplication between components
- [ ] Skills used as single source of truth
- [ ] Agent descriptions are concise
- [ ] No unnecessary verbosity
- [ ] Templates extracted to skills, not inline
- [ ] DRY principles applied throughout

## Quality Metrics

### Agent Quality
- **Line Count**: 100-400 lines (optimal: 300)
- **Description**: WHEN + WHEN NOT pattern
- **Tools**: Only necessary tools listed
- **DRY**: References skills vs duplicating content

### Skill Quality
- **Line Count**: 300-500 lines
- **Organization**: Clear sections and subsections
- **Examples**: Both good and bad patterns shown
- **Reusability**: Multiple agents can reference

### Advanced Skill Quality (Claude Code 2.1+)
- **Context Isolation**: Forked context used appropriately (not overused)
- **Progressive Disclosure**: Description triggers correct activation
- **Metadata**: Optional fields used meaningfully when present
- **Tool Access**: `allowed-tools` list is minimal and appropriate

### Command Quality
- **Line Count**: 50-150 lines
- **Clarity**: Clear delegation and workflow
- **Examples**: Concrete usage examples
- **Documentation**: Arguments and defaults clear

### README Quality
- **Completeness**: All required sections present
- **Examples**: Working, concrete examples
- **Integration**: Dependencies documented
- **Clarity**: Easy to understand for new users
