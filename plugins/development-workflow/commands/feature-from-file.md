---
description: Implement a feature from a local file specification with intelligent planning and validation
argument-hint: <path-to-feature-file>
---

# Feature From File

Implement features from local file specifications with intelligent planning, validation, and execution.

## Usage

```bash
/feature-from-file docs/feature-requests/dark-mode.md
```

```bash
/feature-from-file features/auth-improvements.txt
```

The command accepts any file path. Relative paths resolved from current working directory.

## How It Works

This command is a thin wrapper that:
1. Verifies the file exists and is readable
2. Delegates requirements analysis to `feature-issue-analyzer` agent
3. Invokes the `feature-planning` skill for the complete workflow

## Supported File Formats

- **Markdown** (`.md`): Preferred, supports structured sections
- **Plain text** (`.txt`): Simple feature descriptions
- **Any text format**: Analyzer will parse and structure content

## Input Phase

### 1. Verify File Exists

Check that $ARGUMENTS points to a readable file.
If file doesn't exist: Show error with file path, exit workflow.

### 2. Delegate to feature-issue-analyzer Agent

Use Task tool to invoke `feature-issue-analyzer` with:
- File path: $ARGUMENTS
- Source type: "file"

The analyzer will:
- Read file content using Read tool
- Parse content (handles markdown, plain text, structured formats)
- Structure into FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS format
- Return normalized requirements with completeness status

### 3. Handle Incomplete Requirements

If `feature-issue-analyzer` returns `COMPLETENESS: INCOMPLETE`:
- Invoke `feature-requirements-clarifier` agent with the gaps
- Get enriched requirements via clarifying questions
- Continue with complete requirements

If file is empty:
- Analyzer detects empty content
- Asks user to provide feature description via prompt
- Can fallback to feature-from-prompt workflow

### 4. Continue with Feature Planning Workflow

Pass the normalized requirements and source metadata to the `feature-planning` skill workflow:
- Source type: "file"
- Source reference: File path ($ARGUMENTS)
- Requirements: [structured output from analyzer]

The `feature-planning` skill handles all subsequent phases:
- Complexity assessment (0-8 scoring)
- Implementation planning (senior-engineer + optional arch advisor)
- Plan file creation
- Plan validation
- User approval
- Implementation delegation
- Completion options

## Output

- **Plan file**: `plans/feature-[title]-[date].md`
- **Source field**: "File: [file-path]"
- **Original file**: Preserved as specification reference

## Recommended File Structure

While the analyzer can parse any format, this structure works best:

```markdown
# Feature: Dark Mode Toggle

## Overview
Add dark mode toggle in application settings with persistent user preference storage.

## User Stories
- As a user, I want to enable dark mode so that I can reduce eye strain
- As a user, I want my theme preference saved so that it persists across sessions

## Requirements
- Toggle switch in Settings page
- Preference stored in localStorage and database
- System preference detection (prefers-color-scheme)

## Examples
### Enabling Dark Mode
1. User navigates to Settings
2. Clicks "Dark Mode" toggle
3. Theme switches immediately

## Technical Context
- React 18.2 with Context API for theme state
- CSS custom properties for theming

## Constraints
- Maintain WCAG AA contrast ratios
- No flash of wrong theme on load
```

## When to Use

**Use feature-from-file when**:
- Feature spec already exists in a file
- Team uses file-based feature requests
- Want version-controlled feature specifications
- Detailed spec requires formatting/structure
- Multiple stakeholders contribute to spec

**Use feature-from-issue when**:
- Feature tracked in GitHub issues
- Want team visibility through GitHub

**Use feature-from-prompt when**:
- Quick, ad-hoc feature requests
- Simple features not needing documentation

## Benefits of File-Based Specifications

**Version Control**:
- Feature specs tracked in git
- Changes visible in diffs

**Collaboration**:
- Team members can draft detailed specs
- Can iterate on spec before implementation

**Reusability**:
- Save common feature patterns
- Organizational knowledge base

## Error Handling

**File Not Found**:
```
Error: Feature specification file not found: features/missing.md
Please check the file path and try again.
```

**File Read Error**:
```
Error: Cannot read file: features/protected.md
Permission denied. Check file permissions.
```

## Example Workflow

```bash
$ /feature-from-file features/dark-mode.md

Reading feature specification: features/dark-mode.md
[Analyzer parses file]

Requirements Analysis Complete!
- Feature: Dark Mode Toggle in Settings
- Source: File: features/dark-mode.md

[Continues with feature-planning workflow...]
- Complexity Score: 4/8
- Architecture advisor: Not needed
- Plan created: plans/feature-dark-mode-toggle-20260105.md
- Validation: ✅ APPROVED

Ready to proceed with implementation?
> Yes, proceed with senior-engineer

[Implementation...]

Implementation complete!
- Plan: plans/feature-dark-mode-toggle-20260105.md
- Original spec: features/dark-mode.md
- Status: Completed

What would you like to do next?
> Create pull request

[PR created: #42]
Done! Pull request created: #42

Note: Original specification preserved at features/dark-mode.md
```

## Related Commands

- `/feature-from-issue` - Same workflow, GitHub issue input
- `/feature-from-prompt` - Same workflow, text input
- `/resume-feature` - Resume interrupted workflow from plan file

## See Also

- `feature-planning` skill - Complete workflow documentation
- `feature-issue-analyzer` agent - Requirements normalization
- `complexity-scoring` skill - Complexity assessment details
