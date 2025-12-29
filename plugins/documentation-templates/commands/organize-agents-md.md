---
name: organize-agents-md
description: Analyze and reorganize large AGENTS.md files into efficient modular structure with nested files and references to save context window space
args:
  - name: path
    description: Path to the AGENTS.md file or directory containing it (defaults to current directory)
    required: false
---

Analyze and reorganize AGENTS.md file at {{path | default: "."}} to improve organization and reduce context window consumption.

**Delegation**: The `agents-md-organizer` agent will:
1. Analyze the current AGENTS.md structure and size
2. Identify organizational opportunities (nested files, extracted details, subproject separation)
3. Propose a reorganization plan with expected improvements
4. Execute the reorganization with your approval
5. Validate that all content is preserved and properly referenced

The agent uses patterns from the `agents-md-organization` skill to create an efficient, maintainable structure that reduces context window usage by 60-75% while preserving all valuable information.

**Expected Outcomes:**
- Root AGENTS.md reduced to 200-400 lines (overview + references)
- Detailed content extracted to separate files (docs/, subdirectories)
- Nested AGENTS.md files for subprojects (if applicable)
- Clear navigation with working references
- Significant context window savings

**Use Cases:**
- AGENTS.md is too large (>500 lines)
- Multiple technology stacks mixed together
- Monorepo with distinct subprojects
- Extensive testing guidelines in root file
- Difficult to find specific information

Run: `/organize-agents-md` to organize AGENTS.md in current directory
Run: `/organize-agents-md path/to/directory` to organize AGENTS.md in specific location
