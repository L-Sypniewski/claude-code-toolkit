---
description: Implement a feature from a text description with intelligent planning and validation
argument-hint: <feature-description>
---

# Feature From Prompt

Implement a feature from the text description: "$ARGUMENTS"

## Instructions

1. **Extract requirements** using `requirements-extraction` skill:
   - Source type: "prompt"
   - Feature description: $ARGUMENTS
   - Follow [sources/prompt.md](../skills/requirements-extraction/sources/prompt.md)

2. **If requirements INCOMPLETE**: Invoke `feature-requirements-clarifier` agent to resolve gaps.

3. **Execute feature planning** using `feature-planning` skill:
   - Pass normalized requirements
   - Source metadata: `prompt`, reference: N/A
   - Follow all phases with mandatory user approval

## Source Metadata

- **Type**: prompt
- **Reference**: N/A
- **Plan file**: `plans/feature-[title]-[date].md`
