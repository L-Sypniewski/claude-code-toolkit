# File Extraction

Extract and normalize feature requirements from a local specification file.

## Input

- **File path**: Path to feature specification file

## Supported Formats

- **Markdown** (`.md`): Parse sections, headings, lists
- **Plain text** (`.txt`): Extract paragraphs as content
- **Any text format**: Best-effort parsing

## Extraction Steps

1. **Verify file exists**:
   ```bash
   test -f "$FILE_PATH" && echo "exists"
   ```
   If not: Return error with path.

2. **Read file content** using Read tool

3. **Parse structure** based on format:
   - Markdown: Map headings to sections
   - Plain text: Group by paragraphs
   - Look for common patterns (User Stories, Requirements, etc.)

4. **Map to output format**:
   - Feature/Overview → FEATURE section
   - Examples/Scenarios → EXAMPLES section
   - Technical/Context → DOCUMENTATION section
   - Constraints/Notes → OTHER CONSIDERATIONS

## Output

```markdown
## FEATURE
[Extracted from Overview/Description sections]

## EXAMPLES
[From Examples/Scenarios/User Stories sections]

## DOCUMENTATION
[From Technical Context/References sections]

## OTHER CONSIDERATIONS
[From Constraints/Notes/Requirements sections]

---
**SOURCE**: file
**REFERENCE**: [file-path]
**COMPLETENESS**: [COMPLETE | INCOMPLETE]
**CRITICAL GAPS**: [List if incomplete]
```

## Error Handling

- **File not found**: Return error with exact path
- **Permission denied**: Note permission issue
- **Empty file**: Mark as INCOMPLETE, request content
- **Binary file**: Return error, not a text specification
