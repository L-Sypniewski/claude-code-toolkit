---
name: requirements-extraction
description: Extract and normalize feature requirements from various input sources (GitHub issues, text prompts, files). Auto-invoke when processing feature requests from any source. Provides consistent structured output for downstream planning.
---

# Requirements Extraction

Extract and normalize feature requirements from any input source into a consistent structured format for downstream planning workflows.

## Supported Sources

| Source | Input | Sub-skill |
|--------|-------|-----------|
| GitHub Issue | Issue number | [sources/github-issue.md](sources/github-issue.md) |
| Text Prompt | Feature description text | [sources/prompt.md](sources/prompt.md) |
| File | Path to specification file | [sources/file.md](sources/file.md) |

## Output Format

All sources normalize to this structure:

```markdown
## FEATURE
[Clear, concise description of what needs to be built]

## EXAMPLES
[Concrete usage scenarios and expected behaviors]

## DOCUMENTATION
[Technical context, existing code references, API docs]

## OTHER CONSIDERATIONS
[Performance, security, constraints, edge cases]

---
**SOURCE**: [github-issue | prompt | file]
**REFERENCE**: [Issue #X | N/A | path/to/file]
**COMPLETENESS**: [COMPLETE | INCOMPLETE]
**CRITICAL GAPS**: [List if incomplete]
```

## Extraction Process

1. **Invoke source-specific extraction** based on input type
2. **Structure content** into FEATURE/EXAMPLES/DOCUMENTATION/CONSIDERATIONS
3. **Assess completeness** - flag critical gaps
4. **Return normalized requirements** with metadata

## Handling Incomplete Requirements

If extraction returns `COMPLETENESS: INCOMPLETE`:
1. Invoke `feature-requirements-clarifier` agent
2. Ask targeted questions for critical gaps
3. Enrich requirements with user responses
4. Return complete requirements

See `requirements-clarification` skill for question patterns.

## Integration

**Called by**: `/feature-from-issue`, `/feature-from-prompt`, `/feature-from-file` commands

**Outputs to**: `feature-planning` skill workflow
