# Text Prompt Extraction

Extract and normalize feature requirements from a text description.

## Input

- **Feature description**: Text provided by user as command argument

## Extraction Steps

1. **Analyze description** for key components:
   - Core functionality requested
   - Any examples mentioned
   - Technical constraints specified
   - Performance/security requirements

2. **Structure content** into normalized format:
   - Identify primary feature goal
   - Extract any implicit requirements
   - Note technical context clues

3. **Assess completeness**:
   - Is the feature clear and actionable?
   - Are critical details missing?
   - Can implementation proceed?

## Output

```markdown
## FEATURE
[Structured description from prompt]

## EXAMPLES
[Extracted scenarios, or "None provided - will clarify"]

## DOCUMENTATION
[Technical context from prompt, or "To be determined"]

## OTHER CONSIDERATIONS
[Constraints mentioned, or "To be clarified"]

---
**SOURCE**: prompt
**REFERENCE**: N/A
**COMPLETENESS**: [COMPLETE | INCOMPLETE]
**CRITICAL GAPS**: [List if incomplete]
```

## Completeness Heuristics

**Likely COMPLETE** if prompt includes:
- Clear feature goal
- Specific behavior description
- Some technical context

**Likely INCOMPLETE** if prompt:
- Is too vague ("add search")
- Lacks scope definition
- Missing critical technical details
