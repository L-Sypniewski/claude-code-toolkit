---
description: Implement a feature from a local file specification with intelligent planning and validation
argument-hint: <path-to-feature-file>
---

# Feature From File

Comprehensive workflow for implementing features from local file specifications. Same intelligent planning and validation as feature-from-issue, but reads requirements from a local file.

## Usage

```bash
/feature-from-file docs/feature-requests/dark-mode.md
```

```bash
/feature-from-file features/auth-improvements.txt
```

The command accepts any file path. Relative paths resolved from current working directory.

## Supported File Formats

- **Markdown** (`.md`): Preferred, supports structured sections
- **Plain text** (`.txt`): Simple feature descriptions
- **Any text format**: Analyzer will parse and structure content

## Workflow

This command follows the **same workflow as feature-from-issue** with one key difference: the input source.

### Input Phase Difference

**Instead of**:
- Fetching GitHub issue via API
- Posting analysis comment to issue

**This command**:
- Reads feature specification from file path ($ARGUMENTS)
- Delegates to feature-issue-analyzer with source type "file"
- Analyzer parses file content and structures into FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS format
- Preserves file path in plan metadata for reference

### Identical Phases

All other phases are **exactly the same**:

1. **Requirements Analysis**: feature-issue-analyzer normalizes file content
2. **Complexity Assessment**: Same 0-8 point scoring system
3. **Implementation Planning**: senior-engineer + optional arch advisor
4. **Plan File Creation**: `plans/feature-[title]-[date].md`
5. **Plan Validation**: feature-plan-validator checks completeness/feasibility/clarity
6. **User Approval**: Review plan and approve implementation
7. **Implementation**: Delegate to approved agent
8. **Completion**: Optional code review / PR creation

## Detailed Workflow

### PHASE 1: Requirements Analysis

1. **Verify File Exists**
   Check that $ARGUMENTS points to a readable file.
   If file doesn't exist: Show error with file path, exit workflow.

2. **Delegate to feature-issue-analyzer Agent**
   Use Task tool to invoke `feature-issue-analyzer` with:
   - File path: $ARGUMENTS
   - Source type: "file"

   The analyzer will:
   - Read file content using Read tool
   - Parse content (handles markdown, plain text, structured formats)
   - Structure into FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS format
   - Return normalized requirements

3. **Create TodoWrite for Progress Tracking**
   (Same as feature-from-issue)

### PHASE 2-8: Identical to feature-from-issue

Follow the exact same workflow as `/feature-from-issue` from Phase 2 onwards:

- Calculate complexity score (0-8 points)
- Delegate to planning agents (senior-engineer + optional arch advisor based on complexity)
- Create plan file with all sections
- Validate plan (completeness, feasibility, clarity)
- Get user approval
- Delegate to implementation agent
- Monitor progress via plan file
- Offer post-implementation options (code review, PR creation)

**Plan file structure** is identical except:
- **Source** field shows: "File: [file-path]" instead of "GitHub Issue #X"
- Metadata includes reference to original file
- No GitHub comment posting in completion phase

## Recommended File Structure

While the analyzer can parse any format, this structure works best:

```markdown
# Feature: Dark Mode Toggle

## Overview
Add dark mode toggle in application settings with persistent user preference storage.

## User Stories
- As a user, I want to enable dark mode so that I can reduce eye strain
- As a user, I want my theme preference saved so that it persists across sessions
- As a user, I want dark mode to apply immediately without reload

## Requirements
- Toggle switch in Settings page
- Preference stored in localStorage and database
- Smooth theme transition animations
- System preference detection (prefers-color-scheme)
- All UI components support both themes

## Examples
### Enabling Dark Mode
1. User navigates to Settings
2. Clicks "Dark Mode" toggle
3. Theme switches immediately
4. Preference saved to localStorage and API

### First Visit
1. New user visits app
2. System preference detected (dark/light)
3. Theme applied automatically
4. Notification shown: "We detected you prefer [theme]"

## Technical Context
- React 18.2 with Context API for theme state
- CSS custom properties for theming (themes.css)
- Existing light theme defined
- PostgreSQL for user preferences
- API endpoint: PATCH /api/user/preferences

## Constraints
- Maintain WCAG AA contrast ratios
- Support mobile (touch targets ≥44x44px)
- No flash of wrong theme on load
- Browser support: Modern browsers (no IE11)

## Success Criteria
- Theme toggle works immediately
- Preference persists across sessions
- System preference detected and respected
- All components look correct in both themes
- Smooth transitions (no jarring flashes)
```

## Example File Formats

### Simple Plain Text
```
Add pagination to user list.

Show 25 users per page with next/prev buttons.
Keep current filters and sorting when paging.
Display "Page X of Y" and total user count.

Should work on mobile and desktop.
Use existing table component.
```

### Markdown with Sections
```markdown
# CSV Export Feature

## Description
Add "Export to CSV" button to user reports page.

## Functionality
- Button next to report title
- Downloads CSV with all visible columns
- Filename: report-name-YYYY-MM-DD.csv
- Include column headers

## Technical Notes
- Use existing report data endpoint
- Client-side CSV generation (small datasets)
- Server-side generation for >10k rows
- UTF-8 encoding with BOM for Excel

## Testing
- Test with special characters in data
- Test with large datasets (performance)
- Test download on different browsers
```

### Structured with Examples
```markdown
# Real-Time Notifications

## Feature
WebSocket-based notification system for messages, mentions, and alerts.

## Components
1. Toast notifications (temporary, bottom-right)
2. Notification center (persistent, accessible from icon)
3. Browser notifications (with permission handling)

## Example Flows
### New Message
1. User receives message from another user
2. Toast appears: "[Name] sent you a message"
3. Notification added to center (unread badge)
4. If browser perms granted: Browser notification

### Mention
1. User mentioned in comment
2. Toast: "You were mentioned in [context]"
3. Click toast: Navigate to mentioned location

## Fallback
For browsers without WebSocket support:
- Poll every 30 seconds
- Show banner: "Using polling mode (limited support)"

## Dependencies
- ws library for WebSocket server
- Socket.io for client
- Redis for pub/sub (multi-server support)
```

## Benefits of File-Based Specifications

**Version Control**:
- Feature specs tracked in git
- Changes visible in diffs
- Can review historical feature requests

**Collaboration**:
- Team members can draft detailed specs
- Can iterate on spec before implementation
- Template-based feature requests

**Reusability**:
- Save common feature patterns
- Organizational knowledge base
- Reference implementations

**Offline Work**:
- Draft features without internet
- Work in preferred editor
- Batch multiple features

## When to Use feature-from-file

**Use feature-from-file when**:
- Feature spec already exists in a file
- Team uses file-based feature requests
- Want version-controlled feature specifications
- Detailed spec requires formatting/structure
- Multiple stakeholders contribute to spec
- Building feature request template system

**Use feature-from-issue when**:
- Feature tracked in GitHub issues
- Want team visibility through GitHub
- Issue has valuable discussion context

**Use feature-from-prompt when**:
- Quick, ad-hoc feature requests
- Simple features not needing documentation
- Conversational feature definition

## Integration with Other Commands

**Creating specifications**:
```bash
# Create spec file
echo "# My Feature\n..." > features/my-feature.md

# Implement from file
/feature-from-file features/my-feature.md
```

**Batch processing** (manual):
```bash
# Process multiple features
/feature-from-file features/feature-1.md
# ... after completion ...
/feature-from-file features/feature-2.md
```

**After completion**:
- Can create GitHub issue to track post-implementation
- Can create PR with `/create-pr`
- Original file remains as specification reference

**Resumability**:
- If interrupted: `/resume-feature plans/feature-[name]-[date].md`
- Plan file references original spec file in metadata

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

**Empty File**:
- Analyzer detects empty content
- Asks user to provide feature description via prompt
- Can fallback to feature-from-prompt workflow

**Ambiguous Content**:
- Analyzer structures what it can
- Flags missing information
- Asks clarifying questions
- User provides additional context

## Example Workflow

```bash
$ /feature-from-file features/dark-mode.md

Reading feature specification: features/dark-mode.md
[Analyzer parses file]

Requirements Analysis Complete!
- Feature: Dark Mode Toggle in Settings
- Source: File: features/dark-mode.md
- Complexity Score: 4/8
- Architecture advisor: Not needed

Creating implementation plan...
[Senior engineer creates plan]

Plan created: plans/feature-dark-mode-toggle-20260105.md
Original spec: features/dark-mode.md

[Validator checks plan]
Validation: ✅ APPROVED

Ready to proceed with implementation?
> Yes, proceed with senior-engineer

[Implementation begins]
Implementing feature according to plan...
[Progress updates in real-time]

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

## Tips for Creating Feature Files

### Use Descriptive Filenames
**Bad**: `feature1.md`, `new-thing.txt`
**Good**: `dark-mode-toggle.md`, `csv-export-reports.md`

### Include Context
Don't assume knowledge—include relevant background even if "everyone knows."

### Show Examples
Concrete examples are better than abstract descriptions.

### Specify Success Criteria
What does "done" look like? Make it measurable.

### Note Constraints
Browser support, performance requirements, compatibility needs.

### Link to Resources
Reference relevant docs, similar implementations, design mockups.

### Keep It Updated
If spec changes before implementation, update the file.

## Comparison Matrix

| Aspect | feature-from-issue | feature-from-prompt | feature-from-file |
|--------|-------------------|---------------------|-------------------|
| **Input** | GitHub issue # | Text description | File path |
| **Requires** | Internet, GitHub access | Nothing | File exists locally |
| **Tracking** | GitHub issue | None (unless created) | File (optional git) |
| **Format** | GitHub markdown | Free text | Any text format |
| **Collaboration** | GitHub comments | Real-time conversation | File-based review |
| **Persistence** | GitHub (permanent) | Conversation only | File (version controlled) |
| **Complexity** | Same algorithm | Same algorithm | Same algorithm |
| **Planning** | Same process | Same process | Same process |
| **Output** | Plan + issue link | Plan only | Plan + file ref |
