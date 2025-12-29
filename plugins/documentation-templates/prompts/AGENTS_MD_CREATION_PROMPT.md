````markdown
# Universal AGENTS.md Creation Prompt

You are tasked with creating a comprehensive AGENTS.md file for this repository. AGENTS.md serves as a "README for agents" - providing the detailed context, commands, and conventions that autonomous coding agents need to work effectively on the project, complementing (not replacing) human-focused documentation.

For format standards and examples, refer to the official documentation at https://agents.md/

Use sequential thinking, context7 to solve the problem using latest documentation and best practices.

## Before You Begin

**Create a detailed plan as a markdown file** before starting work. This plan should outline:
- Discovery steps you'll take to understand the project
- Sections you plan to include and why
- Validation checkpoints to ensure accuracy
- Expected timeline and milestones

Track your progress against this plan throughout the work to ensure comprehensive coverage.

## Your Methodology

### 1. **Discovery Phase**
- Use semantic search and file exploration to understand the project structure, technologies, and conventions
- Read existing documentation (README.md, contributing guidelines, package files, config files)
- Identify the primary technology stack, build tools, testing frameworks, and deployment methods
- Look for existing agent-specific documentation (.github/copilot-instructions.md, .cursorrules, etc.)
- **Assess project complexity**: Single project vs monorepo with subprojects (backend, frontend, infra)
- **Evaluate documentation needs**: Will AGENTS.md be large (>500 lines)? Consider organization strategy

### 2. **Validation Phase (Critical)**
- **Cross-reference documentation claims with actual codebase** - this is essential for accuracy
- Verify package manager usage by checking lock files and project configurations
- Confirm testing framework names by examining test project files and dependencies
- Validate build commands by checking build configuration files and scripts
- Ensure dependency management approach matches actual implementation

### 3. **Organization Strategy (New!)**

**Before creating content**, decide on organization approach:

**For Simple Projects (<500 lines expected):**
- Create single root AGENTS.md with all content

**For Complex Projects (>500 lines or monorepo):**
- Use **modular organization** with nested structure
- Reference the `agents-md-organization` skill for patterns
- Consider:
  - **Pattern 1: Root + Referenced Details** - Extract detailed sections to docs/ files
  - **Pattern 2: Nested AGENTS.md** - Create subdirectory AGENTS.md for subprojects
  - **Pattern 3: Category-Based** - Organize by concern type
  - **Pattern 4: Tests Subdirectory** - Extensive testing guidelines in tests/AGENTS.md

**Benefits of Modular Organization:**
- 60-75% context window reduction
- Better maintainability
- Clearer navigation
- Agents load only relevant context

**Examples:**
- Monorepo → Root AGENTS.md (200 lines) + backend/AGENTS.md + frontend/AGENTS.md
- Detailed conventions → Root AGENTS.md references docs/coding-standards.md
- Extensive testing → Root references tests/AGENTS.md

### 4. **Structure Creation**
Follow this proven structure, adapting sections as needed:

## Required Sections Template

```markdown
# [Project Name] Agent Playbook

Welcome! This guide provides everything an autonomous coding agent needs to succeed in this repository. Treat this as living documentation—update as the project evolves.

## TL;DR
- Primary stack: [Key technologies and frameworks]
- Essential quality gates: [Critical build/test/lint commands]
- Key constraints: [Important limitations or requirements]
- [Most critical rules agents must follow]

## Repository at a Glance
- [Brief description of each major directory/component]
- [Note primary development workflows]

## Environment & Setup
### Required tooling
- [List prerequisites and versions if specific]

### Repository configuration
- [Environment files, secrets, local setup steps]

### [Technology-specific setup sections as needed]

## Running the App
### [Organize by logical components - frontend/backend, services, etc.]
- [Commands to start each part]

### Tooling & automation
- [Development tools, testing utilities, debugging aids]

## Quality Gates ✅
### [Organize by workspace/technology]
- [Required commands for each area]

### [Additional quality assurance steps]

### Reporting
- Agents must fix every failure before completion and report Build, Lint/Typecheck, and Tests as PASS/FAIL in the final summary.

## Coding Standards & Patterns
- [Language-specific conventions]
- [Architecture principles]
- [Code organization rules]
- [Performance considerations]

## [Technology-Specific Rules]
[Add sections as needed for UI frameworks, databases, etc.]

## Testing Expectations
### [Organize by test types or components]
- [Testing frameworks and assertion libraries used]
- [Test organization and naming conventions]
- [Coverage requirements]

### [Integration/E2E testing guidance]

### General guidance
- [Universal testing principles]
- [How to handle test failures]

## Data & Integrations
### [Database/storage systems]
### [External service integrations]
### [API patterns and conventions]

## Deployment & Ops
### [Local development workflow]
### [CI/CD pipeline information]
### [Deployment targets and processes]

## Agent Workflow Tips
- Maintain an explicit TODO list with the provided task tool—exactly one item may be "in-progress" at any time.
- Use sequential reasoning when tasks are multi-step; document key assumptions in the final summary.
- Never edit notebooks outside the dedicated notebook editor.
- Run the smallest relevant test subset, but do not skip required quality gates for touched areas.
- When adding new run commands, document them here so future agents inherit the knowledge.

## Common Pitfalls & Edge Cases
- [Technology-specific gotchas]
- [Integration challenges]
- [Performance bottlenecks to avoid]

## Need Help?
- [References to additional documentation]
- [Architecture diagrams or design docs]
- Update this file whenever you discover new rules, commands, or best practices—AGENTS.md is the canonical playbook for automation.
```

## Critical Requirements

### Accuracy Over Assumptions
- **Never guess** package manager, testing framework, or build tool names
- **Always verify** commands work in the actual codebase
- **Cross-check** version numbers, dependency names, and file paths
- **Validate** that quality gate commands actually succeed

### Technology-Agnostic Principles
- Focus on **methodology** rather than specific tech stack details
- Organize by **logical project boundaries** (frontend/backend, services, etc.) when it improves clarity
- Use **universal concepts** (build, test, deploy, quality gates) while filling in project-specific details
- Include **workflow patterns** that help any agent work efficiently

### Agent-Specific Concerns
- Include commands that agents can run programmatically
- Document quality gates that agents must pass before completing work
- Note automation workflows (CI/CD, review apps, deployment patterns)
- Specify error handling expectations and failure recovery

### Living Documentation
- Emphasize that this file should be updated when new patterns emerge
- Include instructions for agents to maintain accuracy
- Design for evolution as the project grows

## Validation Checklist

Before finalizing, verify:
- [ ] All commands are accurate and runnable
- [ ] Package managers and build tools match actual usage
- [ ] Testing frameworks and assertion libraries are correctly named
- [ ] File paths and directory structures are accurate
- [ ] Quality gate commands actually pass
- [ ] Technology stack description matches codebase reality
- [ ] No contradictions between different sections

## Additional Resources

- Official format documentation: https://agents.md/
- Examples from 20k+ open source projects: https://github.com/search?q=path%3AAGENTS.md&type=code
- **NEW: Organization patterns**: Reference `agents-md-organization` skill for modular structure
- **NEW: Organized example**: See `examples/ORGANIZED-STRUCTURE-EXAMPLE.md` for complete before/after

**Consider running `/organize-agents-md` after creation if the file becomes large (>500 lines).**

Remember: This AGENTS.md will be used by autonomous agents who cannot ask clarifying questions. Accuracy and completeness are essential for successful automation.
````