---
description: Refactor existing Claude Code plugin to improve architecture, apply best practices, optimize tokens, or add new components
argument-hint: <plugin-path> [goals]
---

# Refactor Plugin

Refactor an existing Claude Code plugin to improve architecture, apply best practices, optimize tokens, or add new components.

## Arguments: $ARGUMENTS

**Format**: `/refactor-plugin [path] [goals]`

**Examples**:
- `/refactor-plugin plugins/my-plugin`
- `/refactor-plugin plugins/my-plugin "add security validation"`
- `/refactor-plugin plugins/my-plugin "optimize token usage"`
- `/refactor-plugin . "convert to orchestrator pattern"`

**Requirements**:
- path: Required, path to plugin directory
- goals: Optional, specific refactoring objectives

**Default**: If no goals provided, interactive workflow will collect requirements

## Workflow

1. **Analysis**: Validate current plugin and identify issues
2. **Goals**: Determine refactoring objectives (interactive if not provided)
3. **Backup**: Create backup of current plugin state
4. **Planning**: Use sequential thinking to plan safe refactoring approach
5. **Implementation**: Apply changes to plugin components
6. **Validation**: Validate refactored plugin against best practices
7. **Summary**: Present before/after comparison and improvements

## Refactoring Types

### Architecture Refactoring
**Goal**: Improve plugin structure and component organization

**Transformations**:
- Split monolithic agent into orchestrator-worker pattern
- Merge redundant agents doing similar work
- Extract skills from inline documentation in agents
- Reorganize component relationships for clarity

**Example**: `/refactor-plugin plugins/my-plugin "convert to orchestrator pattern"`

### Token Optimization
**Goal**: Reduce token usage while maintaining functionality

**Optimizations**:
- Apply DRY principles (extract duplicated content)
- Move repeated content to skills
- Shorten verbose prompts without losing clarity
- Remove unnecessary tool access from agents

**Example**: `/refactor-plugin plugins/my-plugin "optimize token usage"`

### Security Hardening
**Goal**: Add security validation and safe patterns

**Additions**:
- Add input validation to bash/python scripts
- Add confirmation gates for destructive operations
- Apply safe subprocess patterns (no shell=True)
- Remove hardcoded secrets or credentials
- Add GET-only navigation specifications

**Example**: `/refactor-plugin plugins/my-plugin "add security validation"`

### Best Practices Update
**Goal**: Align with latest Claude Code best practices

**Updates**:
- Apply WHEN/WHEN NOT description pattern
- Add explicit skill references to agents
- Update naming conventions to kebab-case
- Improve README documentation structure
- Add integration points documentation

**Example**: `/refactor-plugin plugins/my-plugin "update best practices"`

### Feature Addition
**Goal**: Add new capabilities to existing plugin

**Additions**:
- Add new agents for specialized tasks
- Create new skills for domain knowledge
- Add new commands for workflows
- Integrate new MCP tools (Playwright, GitHub, etc.)

**Example**: `/refactor-plugin plugins/my-plugin "add validator agent"`

## Delegation

Use the `plugin-creator` agent to execute this workflow. The agent will:
- Validate current plugin state using plugin-validator
- Collect refactoring goals interactively (if not provided)
- Plan safe refactoring approach using sequential thinking
- Create backup of current state
- Apply changes while preserving existing functionality
- Validate refactored plugin
- Provide detailed before/after comparison
- Show diff summary of changes made

## Additional Instructions

- **Always validate** plugin before refactoring (baseline assessment)
- **Preserve functionality** unless explicitly changing behavior
- **Create backup** before making destructive changes
- **Apply best practices** from `plugin-creation-guidelines` skill
- **Re-validate** after refactoring (verify improvements)
- **Use sequential thinking** to plan safe, incremental refactoring
- **Document changes** clearly in summary

## Output

Refactored plugin with:
- Updated components reflecting improvements
- Validation report comparing before/after metrics
- Diff summary showing specific changes
- Improved token efficiency metrics
- Enhanced security posture
- Better documentation quality
- Backup of original state for rollback

## Safety Features

- **Non-destructive**: Creates backup at `plugins/{plugin-name}.backup/` before changes
- **Validation Gates**: Validates before and after refactoring
- **Incremental**: Can refactor one aspect at a time
- **Reversible**: Keeps backup for rollback if needed
- **Safe Defaults**: Preserves working code unless explicitly changing

## Examples

### Example 1: Token Optimization
```
/refactor-plugin plugins/my-plugin "optimize token usage"
```

**Before**:
- Agent: 520 lines (too long)
- Duplication: Repeated validation logic in 3 agents
- Inline templates: Large code templates in agent prompts

**After**:
- Agent: 310 lines (optimal range)
- Duplication: Extracted to skill (single source of truth)
- Inline templates: Moved to skill, agents reference it
- **Improvement**: 40% token reduction, easier maintenance

### Example 2: Architecture Improvement
```
/refactor-plugin plugins/my-plugin "convert to orchestrator pattern"
```

**Before**:
- Single monolithic agent doing everything
- No parallelization
- 480 lines (too complex)

**After**:
- Orchestrator agent: 280 lines (coordinates workflow)
- 3 worker agents: 150-180 lines each (specialized tasks)
- Can process multiple items in parallel
- **Improvement**: Better separation of concerns, parallel execution

### Example 3: Security Hardening
```
/refactor-plugin plugins/my-plugin "add security validation"
```

**Before**:
- Bash script with no input validation
- Python script using `os.system()` with user input
- Agent with destructive ops, no confirmation gates

**After**:
- Bash: Added input validation, proper quoting, `set -euo pipefail`
- Python: Using `subprocess.run()` with list args, path validation
- Agent: Added AskUserQuestion confirmation before destructive ops
- **Improvement**: 3 critical vulnerabilities fixed

### Example 4: Add Components
```
/refactor-plugin plugins/my-plugin "add validator agent and skill"
```

**Before**:
- Plugin had no validation capabilities
- Manual quality checking required

**After**:
- New agent: `plugin-validator` (validates plugin quality)
- New skill: `validation-checklist` (quality criteria)
- New command: `/validate` (entry point)
- Updated README with validation usage
- **Improvement**: Built-in quality assurance

### Example 5: Interactive Refactoring
```
/refactor-plugin plugins/my-plugin
```

**Interactive Questions**:
1. "What aspect would you like to improve?"
   - Architecture, Security, Token Optimization, Documentation
2. "Specific goals?" (if multiple selected)
3. "Preserve all existing functionality?" (Yes/No)

**Result**: Customized refactoring based on user priorities

## Comparison Report Format

```markdown
# 🔄 Plugin Refactoring Report: {plugin-name}

## Refactoring Goals
- {goal 1}
- {goal 2}

## Before → After Comparison

### Token Metrics
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total Agent Lines | 520 | 310 | ↓ 40% ✅ |
| Average per Agent | 520 | 310 | ↓ 40% ✅ |
| Skill Lines | 0 | 280 | +280 (new) |

### Validation Scores
| Category | Before | After | Improvement |
|----------|--------|-------|-------------|
| Overall | WARN | PASS | ✅ |
| Security | FAIL (3 critical) | PASS | ✅ Fixed all |
| Best Practices | WARN (5 issues) | PASS | ✅ |
| Token Optimization | NEEDS WORK | OPTIMAL | ✅ |

### Components Changed
- ✏️ Modified: agent-1.md (520→310 lines)
- ➕ Added: skill-1/SKILL.md (280 lines)
- ✏️ Modified: README.md (updated with new skill)
- 🔒 Security: Fixed 3 critical vulnerabilities

## Detailed Changes

### agent-1.md
- Extracted validation logic to skill
- Applied WHEN/WHEN NOT pattern
- Added skill reference section
- Reduced from 520 to 310 lines

### skill-1/SKILL.md (NEW)
- Created validation-checklist skill
- Centralized validation criteria
- Added examples and templates

### Security Fixes
1. ✅ agent-1.md:45 - Added input validation
2. ✅ agent-1.md:78 - Added confirmation gate
3. ✅ skill-1/SKILL.md:120 - Fixed bash script quoting

## Backup Location
Original plugin backed up at: `plugins/{plugin-name}.backup/`

## Next Steps
1. Test refactored plugin with: /command-name
2. Review changes in detail
3. Remove backup once satisfied: `rm -rf plugins/{plugin-name}.backup/`

---
Refactored using plugin-creation-guidelines skill
```
