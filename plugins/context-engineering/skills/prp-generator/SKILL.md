---
name: prp-generator
description: Generate Product Requirements Prompts (PRPs) from GitHub issue analysis. Use when users need to transform structured GitHub issue analysis into comprehensive implementation blueprints with validation loops. Creates context-dense PRPs specifically designed for AI coding assistants, including detailed pseudocode, integration patterns, and progressive validation checkpoints. Use for /generate-prp commands or when creating implementation plans from structured requirements.
---

# PRP Generator

This skill generates AI-focused Product Requirements Prompts (PRPs) that transform structured GitHub issue analysis into comprehensive, context-dense implementation blueprints.

## When to Use

- Processing `/generate-prp <GitHub-issue-URL>` commands
- Creating implementation blueprints from structured issue analysis
- Transforming requirements into AI-ready implementation guides
- Establishing validation loops and success criteria
- Generating self-contained implementation context

## PRP Generation Process

### 1. Retrieve Structured Analysis

- Fetch GitHub issue and locate structured analysis comment
- Parse FEATURE, EXAMPLES, DOCUMENTATION, and OTHER CONSIDERATIONS sections
- Extract requirements, constraints, and implementation guidance

### 2. Conduct Research

**Codebase Analysis**:
- Search for similar features and implementation patterns
- Identify integration points and files to modify
- Note existing conventions and architectural patterns
- Review test patterns for validation approach

**External Research**:
- Library documentation with specific URLs
- Implementation examples and best practices
- Common pitfalls and anti-patterns
- Version compatibility and dependencies

### 3. Create PRP File

Generate comprehensive PRP following this structure:

```markdown
# Product Requirements Prompt: [Feature Name]

## Goal
**Clear, specific end state**: [What exactly should be built]
**Success Definition**: [Measurable, testable outcomes]

## Why (Business Context)
**User Value**: [Direct user benefit]
**Business Impact**: [Project/organization value]
**Priority Rationale**: [Why now vs other features]

## What (Technical Implementation)

### User-Visible Behavior
**Primary User Flow**:
1. [Step-by-step interaction]
2. [System response]
3. [Completion state]

**Edge Cases & Error Handling**:
- [Error scenarios and behaviors]
- [Validation failures]
- [Recovery mechanisms]

### Technical Requirements

#### Architecture Integration
**Existing Patterns**: [Reference similar implementations]
**Integration Points**: [Files/components to modify]
**Dependencies**: [Required libraries/services]

#### Implementation Approach
**Core Components**:
```pseudocode
function componentName(parameters) {
  // Detailed logic with validation
  // Error handling patterns
  // Existing conventions
}
```

**Data Flow**:
- Input validation patterns
- Data transformation steps
- Output formatting

#### Validation Strategy

**Code Quality Validation**:
- [ ] Follows project conventions
- [ ] Types properly defined
- [ ] Linting passes
- [ ] Import patterns correct

**Build Validation** (mandatory):
- [ ] Code builds successfully
- [ ] Types validated
- [ ] No compilation errors

**Optional E2E Testing**:
- [ ] Critical workflows tested (when valuable)
- [ ] Feature integrates correctly (when complex)
- [ ] Accessibility verified (for user-facing features)

## Implementation Context

### Codebase Patterns
**Similar Implementations**: [Existing reference features]
**Code Conventions**: [Project-specific patterns]
**Architecture Decisions**: [Relevant constraints]

### Anti-Patterns to Avoid
- [Known problematic patterns]
- [Performance pitfalls]
- [Security vulnerabilities]
- [Maintenance challenges]

### Integration Points
**Files to Modify**: [Specific file paths]
**New Files to Create**: [File structure]
**Dependencies to Add**: [Required packages]

## Validation Gates

**Project-Specific Commands**:
```bash
# [Build command]
# [Test command]
# [Lint command]
```

**Success Criteria**:
- [ ] All validation gates pass
- [ ] Feature works as specified
- [ ] Integration successful
- [ ] Documentation updated
```

### 4. Include Critical Context

**Documentation Links**: Specific URLs with sections
**Code Examples**: Real snippets from codebase
**Gotchas**: Library quirks and version issues
**Patterns**: Existing approaches to follow

## Context Engineering Principles

1. **Context is King**: Provide comprehensive, information-dense context
2. **Validation Loops**: Include progressive validation (Syntax → Build → Tests)
3. **Information Dense**: Pack maximum relevant context into guidance
4. **Progressive Success**: Structure with incremental validation checkpoints
5. **Self-Contained**: Enable autonomous AI implementation

## Quality Checklist

Before finalizing the PRP:

- [ ] All necessary context included for autonomous implementation
- [ ] Validation gates are executable and clearly defined
- [ ] References existing codebase patterns
- [ ] Clear, step-by-step implementation path
- [ ] Error handling documented
- [ ] Edge cases covered
- [ ] Dependencies identified
- [ ] Success criteria measurable

## Output Location

Save PRP as: `PRPs/{feature-name}.md`

## Integration with Workflow

1. **GitHub Issue Analysis** → Structured comment
2. **PRP Generation** (this skill) → Implementation blueprint
3. **TDD Implementation** → Follows PRP with validation gates
4. **Validation & Cleanup** → Quality assurance and artifact removal
