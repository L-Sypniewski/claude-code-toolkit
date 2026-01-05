# Basic AGENTS.md Template

A well-structured AGENTS.md follows this pattern:

```markdown
# ProjectName - Development Guide

**Stack**: [Tech stack components]
**Principles**: [Core development principles, e.g., SOLID, KISS, YAGNI]

## Project Overview

[Brief description of architecture and approach]

## Repository Structure

- `path/to/main/`: [Description]
- `path/to/tests/`: [Description]
- `path/to/config/`: [Description]

## Key Commands

```bash
# Core commands
[build command]
[test command]
[format command]

# Additional tools
[migration/deployment commands]
[additional commands]
```

## Quality Gates (Required)

Define the quality standards that must be met:

### Code Quality
- [ ] Build succeeds without errors
- [ ] All tests pass
- [ ] Code formatting/linting passes
- [ ] No compiler warnings

### Testing Requirements
- [ ] Integration tests for key workflows (favor sociable tests over isolated unit tests)
- [ ] Avoid excessive mocking - test real collaborations
- [ ] All edge cases and error paths covered

### Code Review Standards
- [ ] Follows project conventions
- [ ] No code smells or anti-patterns
- [ ] Proper error handling
- [ ] Security considerations addressed

## Coding Conventions (Optional)

[Project-specific coding standards]

## Testing Guidelines (Optional)

[Testing expectations]
```

## Key Sections Explained

### 1. Title and Metadata (Required)
**Format**: `# ProjectName - Development Guide`

Include **Stack** and **Principles** at the top for quick reference.

### 2. Project Overview (Required)
Brief architectural summary - what type of project, key technologies, approach.

### 3. Repository Structure (Required)
Map of directories with brief descriptions. Helps agents understand where code lives.

### 4. Key Commands (Required)
Copy-paste commands for:
- Building the project
- Running tests
- Formatting code
- Database migrations or other critical operations

### 5. Quality Gates (Required)
Define quality standards that code must meet:
- **Code Quality**: Build, test, lint requirements
- **Testing Requirements**: Coverage thresholds, test types needed
- **Code Review Standards**: Conventions, patterns, security checks

### 6. Optional Sections
Add as needed:
- **Coding Conventions**: Project-specific rules
- **Testing Guidelines**: Reference separate tests/AGENTS.md for detailed testing guidelines
