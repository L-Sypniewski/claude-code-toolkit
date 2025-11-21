---
name: github-issue-analyzer
description: Analyze GitHub issues and create structured analysis comments with FEATURE, EXAMPLES, DOCUMENTATION, and OTHER CONSIDERATIONS sections. Use when users need to analyze a GitHub issue comprehensively, extract requirements, or create structured problem decomposition for implementation planning. This skill processes GitHub issues and posts comprehensive structured comments that serve as the foundation for PRPs and implementation workflows.
---

# GitHub Issue Analyzer

This skill provides comprehensive GitHub issue analysis and structured commenting capabilities for context engineering workflows. It transforms raw GitHub issues into actionable, well-structured analysis that enables effective implementation planning.

## Core Capabilities

1. **Issue Comprehension**: Deep analysis of problem statements, requirements, and context
2. **Stakeholder Analysis**: Identification of users, use cases, and impact scenarios
3. **Technical Research**: Integration with documentation and best practices research
4. **Structured Output**: Creation of standardized analysis comments following proven patterns
5. **GitHub Integration**: Direct posting of analysis comments to GitHub issues

## When to Use This Skill

- Processing `/initial-github-issue <GitHub-issue-URL>` commands
- Analyzing GitHub issues before creating PRPs (Prompt-Response-Plans)
- Creating structured problem decomposition for complex features
- Extracting and organizing requirements from issue descriptions
- Establishing foundation for context engineering workflows

## Analysis Framework

### Sequential Analysis Process

1. **Issue Comprehension**: Understand the problem statement, requirements, and context
2. **Stakeholder Analysis**: Identify users, use cases, and impact scenarios
3. **Technical Research**: Research relevant libraries, frameworks, and best practices
4. **Scope Definition**: Determine feature boundaries, dependencies, and constraints
5. **Documentation Review**: Analyze existing project documentation and architectural patterns

### Research Integration

- Access up-to-date documentation for relevant technologies
- Apply systematic thinking to break down complex problems
- Research industry best practices and established patterns
- Validate approaches against current standards and project conventions

## Structured Comment Format

Create comprehensive structured comments following this exact format:

```markdown
## FEATURE

**Clear, concise description of what needs to be built:**

- Primary functionality and user value proposition
- Key user scenarios and use cases
- Success criteria and acceptance conditions
- Feature scope and boundaries

## EXAMPLES

**Concrete examples of the feature in action:**

- Specific user workflows and interaction patterns
- Input/output examples with realistic data
- Edge cases and boundary conditions
- Integration scenarios with existing features

## DOCUMENTATION

**Implementation guidance and architectural considerations:**

- Technical approach and architectural decisions
- Integration points with existing codebase
- Dependencies and prerequisites
- Performance and scalability considerations
- Security and accessibility requirements

## OTHER CONSIDERATIONS

**Additional factors that influence implementation:**

- Pragmatic testing strategy based on feature complexity and user impact
- Deployment and rollout considerations
- Maintenance and operational impact
- Future extensibility and evolution paths
- Risk assessment and mitigation strategies
```

## GitHub Integration Workflow

### Command Processing

When receiving a request to analyze a GitHub issue:

1. **Extract Issue Information**:
   - Parse the GitHub issue URL to identify owner, repo, and issue number
   - Retrieve complete issue details using GitHub API
   - Review existing comments to avoid duplication

2. **Comprehensive Analysis**:
   - Apply systematic thinking to understand the problem deeply
   - Research relevant technologies and patterns
   - Analyze integration points with existing project architecture
   - Consider user experience and business impact

3. **Structured Comment Creation**:
   - Generate comprehensive structured comment following the pattern above
   - Ensure all four sections (FEATURE, EXAMPLES, DOCUMENTATION, OTHER CONSIDERATIONS) are complete
   - Include specific, actionable information in each section

4. **Comment Posting**:
   - Post the structured comment to the GitHub issue
   - Verify successful posting and provide confirmation
   - Include link to the posted comment for reference

## Quality Guidelines

### Effective Analysis Characteristics

- **Comprehensive**: Covers all aspects of the feature without leaving ambiguity
- **Specific**: Uses concrete examples and realistic scenarios
- **Actionable**: Provides clear guidance for implementation
- **Contextual**: Considers existing codebase patterns and conventions
- **Research-backed**: Incorporates current best practices and documentation

### Common Pitfalls to Avoid

- Vague or abstract descriptions without concrete examples
- Missing consideration of edge cases or error scenarios
- Ignoring existing codebase patterns and conventions
- Insufficient research on relevant technologies
- Overlooking security, performance, or accessibility concerns

## Integration with Context Engineering Workflow

This skill is typically the first step in a complete context engineering pipeline:

1. **GitHub Issue Analysis** (this skill) → Structured comment creation
2. **PRP Generation** → Reads structured comment to create implementation plan
3. **TDD Implementation** → Follows PRP blueprint with validation gates
4. **Validation & Cleanup** → Ensures quality and removes temporary artifacts

## Output Format

The skill produces a structured comment posted directly to the GitHub issue with four main sections:

- **FEATURE**: What needs to be built and why
- **EXAMPLES**: How the feature works in practice
- **DOCUMENTATION**: Implementation guidance and architecture
- **OTHER CONSIDERATIONS**: Testing, deployment, and operational factors

This structured format ensures consistency and enables downstream processes (like PRP generation) to parse and utilize the analysis effectively.
