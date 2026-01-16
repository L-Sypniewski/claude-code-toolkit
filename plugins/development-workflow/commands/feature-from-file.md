---
description: Implement a feature from a local file specification with intelligent planning and validation
argument-hint: <path-to-feature-file>
---

# Feature From File

Implement a feature from the specification file: $ARGUMENTS

## Instructions

1. **Verify file exists**:
   ```bash
   test -f "$ARGUMENTS" && echo "exists" || echo "not found"
   ```
   If not found: Show error and exit.

2. **Extract requirements** using `requirements-extraction` skill:
   - Source type: "file"
   - File path: $ARGUMENTS
   - Follow [sources/file.md](../skills/requirements-extraction/sources/file.md)

3. **If requirements INCOMPLETE**: Invoke `feature-requirements-clarifier` agent to resolve gaps.

4. **Execute feature planning** using `feature-planning` skill:
   - Pass normalized requirements
   - Source metadata: `file`, reference: $ARGUMENTS
   - Follow all phases with mandatory user approval

## Source Metadata

- **Type**: file
- **Reference**: $ARGUMENTS (file path)
- **Plan file**: `plans/feature-[title]-[date].md`

## Supported File Formats

- **Markdown** (`.md`): Preferred, supports structured sections
- **Plain text** (`.txt`): Simple feature descriptions
- **Any text format**: Parser will extract content
