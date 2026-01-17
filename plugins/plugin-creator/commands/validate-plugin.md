---
description: Validate an existing Claude Code plugin against best practices, security guidelines, and architectural patterns
argument-hint: <plugin-path>
---

# Validate Plugin

Validate an existing Claude Code plugin against best practices, security guidelines, and architectural patterns.

## Arguments: $ARGUMENTS

**Format**: `/validate-plugin [path]`

**Examples**:
- `/validate-plugin plugins/my-plugin`
- `/validate-plugin plugins/ui-ux-audit`
- `/validate-plugin .` (validate current plugin)

**Default**: If no path provided, validates plugin in current directory

## Workflow

1. **Discovery**: Locate plugin directory and components
2. **Structure**: Validate file structure and required files
3. **Metadata**: Check plugin.json completeness and correctness
4. **Components**: Validate agents, skills, commands against templates
5. **Security**: Check for vulnerabilities in scripts and prompts
6. **Optimization**: Assess token usage and DRY compliance
7. **Integration**: Verify component relationships and references
8. **Report**: Generate comprehensive validation report with recommendations

## Delegation

Use the `plugin-validator` agent to execute this workflow. The agent will:
- Read all plugin files systematically using Read and Glob tools
- Check against comprehensive best practices checklist
- Validate security patterns in bash/python scripts and agent prompts
- Assess token optimization (300-400 line target per agent)
- Verify naming conventions (kebab-case) and integration patterns
- Generate detailed report with specific file:line references
- Categorize issues by severity (Critical/High/Medium/Low)
- Provide actionable recommendations for improvements

## Additional Instructions

- Use sequential thinking for systematic validation
- Reference the `plugin-creation-guidelines` skill for validation criteria
- Report issues with specific file locations and line numbers
- Categorize issues by severity:
  - ❌ Critical: Security vulnerabilities, broken references, missing required files
  - ⚠️ High: Best practice violations, token optimization issues
  - ⚠️ Medium: Incomplete documentation, minor pattern issues
  - ℹ️ Low: Polish opportunities, optional improvements
- Provide actionable, specific recommendations

## Output

Comprehensive validation report including:
- Summary with pass/fail counts by category
- File structure validation results
- Metadata completeness check
- Component-by-component analysis with tables
- Security vulnerabilities with severity ratings
- Token optimization assessment
- README quality evaluation
- Prioritized recommendations (High/Medium/Low priority)
- Next steps

## Use Cases

### Use Case 1: After Manual Edits
Validate plugin after making manual changes to ensure best practices maintained

**Example**:
```
/validate-plugin plugins/my-plugin
```

**Result**: Report shows if edits introduced any issues or broke patterns

### Use Case 2: Before Publishing
Final quality check before sharing plugin with team or community

**Example**:
```
/validate-plugin plugins/my-plugin
```

**Expected**: Clean validation with all checks passing, no security issues

### Use Case 3: Regular Audits
Periodic validation to ensure plugin stays up-to-date with best practices

**Example**:
```
/validate-plugin plugins/legacy-plugin
```

**Result**: Identifies areas where plugin can be improved to match current standards

### Use Case 4: Learning Best Practices
Validate example plugins to learn what good patterns look like

**Example**:
```
/validate-plugin plugins/ui-ux-audit
```

**Result**: See how well-architected plugins score on validation

## Examples

### Example 1: Validate Specific Plugin
```
/validate-plugin plugins/ui-ux-audit
```

**Expected Output**:
```markdown
# 🔍 Plugin Validation Report: ui-ux-audit

## Summary
- ✅ Passed: 78 checks
- ⚠️ Warnings: 2 issues
- ❌ Failed: 0 issues
- 🔒 Security: PASS - 0 vulnerabilities

**Overall Status**: PASS with minor warnings

## Recommendations
### Medium Priority
1. Consider adding more usage examples to README
2. agent-orchestrator could reference skill more explicitly
```

### Example 2: Validate Current Plugin
```
/validate-plugin
```

**Validates plugin in current working directory**

### Example 3: Validate Newly Created Plugin
```
/create-plugin test-plugin "Test plugin"
... plugin creation completes ...

/validate-plugin plugins/test-plugin
```

**Result**: Verify generated plugin meets all standards
