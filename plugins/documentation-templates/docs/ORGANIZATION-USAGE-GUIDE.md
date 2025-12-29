# AGENTS.MD Organization Feature - Usage Guide

## What's New

The documentation-templates plugin now includes comprehensive tools for organizing large AGENTS.md files into efficient, modular structures that save 60-75% context window space.

## Problem Solved

Large AGENTS.md files (>500 lines) create several issues:
- **Context Window Waste**: Agents load entire file even when only part is relevant
- **Mixed Concerns**: General architecture mixed with detailed implementation specifics
- **Hard to Maintain**: Difficult to update specific sections
- **Overwhelming**: Too much information at once

## Solution: Modular Organization

New tools help you reorganize AGENTS.md using:
1. **Nested AGENTS.md files** for subprojects (backend/, frontend/, infra/)
2. **Referenced detail files** (docs/coding-standards.md, docs/testing-guide.md)
3. **Clear navigation** with quick links
4. **Automatic merging** by AI agents (more specific contexts override general ones)

## Components Added

### 1. Agent: `agents-md-organizer`
**File**: `plugins/documentation-templates/agents/agents-md-organizer.md`

Expert agent that:
- Analyzes current AGENTS.md structure
- Identifies organizational opportunities
- Proposes reorganization plan with expected savings
- Executes reorganization with user approval
- Validates all content is preserved

### 2. Skill: `agents-md-organization`
**File**: `plugins/documentation-templates/skills/agents-md-organization/SKILL.md`

Comprehensive knowledge base covering:
- 4 organization patterns with use cases
- Migration strategy (step-by-step)
- Best practices (DO/DON'T)
- Real-world examples
- Context window efficiency metrics

### 3. Command: `/organize-agents-md`
**File**: `plugins/documentation-templates/commands/organize-agents-md.md`

Easy-to-use command:
```bash
# Organize AGENTS.md in current directory
/organize-agents-md

# Organize in specific location
/organize-agents-md path/to/project
```

### 4. Example: Complete Before/After
**File**: `plugins/documentation-templates/examples/ORGANIZED-STRUCTURE-EXAMPLE.md`

Real-world example showing:
- Original 1200-line AGENTS.md
- Reorganized structure (root + nested + referenced)
- Complete file contents for all components
- 60-75% context window savings

## Organization Patterns

### Pattern 1: Root + Referenced Details
**Use when**: Single project with detailed conventions (500-1000 lines)

**Structure**:
```
/
├── AGENTS.md              # 200-300 lines (overview)
└── docs/
    ├── architecture.md
    ├── coding-standards.md
    └── testing-guide.md
```

### Pattern 2: Nested AGENTS.md for Subprojects
**Use when**: Monorepo with distinct components

**Structure**:
```
/
├── AGENTS.md              # 200 lines (general)
├── backend/
│   ├── AGENTS.md          # Backend specifics
│   └── src/
├── frontend/
│   ├── AGENTS.md          # Frontend specifics
│   └── src/
└── docs/
    └── architecture.md
```

### Pattern 3: Category-Based Organization
**Use when**: Complex project with many technology domains

**Structure**:
```
/
├── AGENTS.md              # Overview + references
└── .github/
    └── agents/
        ├── architecture.md
        ├── coding-standards.md
        ├── testing-guide.md
        └── deployment.md
```

### Pattern 4: Tests Subdirectory Pattern
**Use when**: Extensive testing guidelines (>30% of content)

**Structure**:
```
/
├── AGENTS.md              # Overview (200 lines)
├── tests/
│   ├── AGENTS.md          # Comprehensive testing (400 lines)
│   └── ...
└── docs/
    └── coding-standards.md
```

## Usage Workflow

### Step 1: Check if Organization is Needed

Run this command to check AGENTS.md size:
```bash
wc -l AGENTS.md
```

**If >500 lines**: Consider reorganization

### Step 2: Run Organization Command

```bash
/organize-agents-md
```

The agent will:
1. Analyze current structure
2. Show analysis report with issues and recommendations
3. Present reorganization plan
4. Ask for approval
5. Execute reorganization
6. Validate results

### Step 3: Review Changes

Check the new structure:
- Root AGENTS.md should be 200-400 lines
- Detailed content in separate files
- Clear navigation with links
- All original content preserved

### Step 4: Update Team

Inform team about new structure:
- Quick links section shows where to find details
- Nested AGENTS.md files for subprojects
- Referenced detail files for comprehensive information

## Benefits

### Context Window Efficiency
- **Before**: 1200 lines loaded every time (100% usage)
- **After**: 200-500 lines depending on location (25-40% usage)
- **Savings**: 60-75% reduction

### Maintainability
- Easier to update specific sections
- Clear separation of concerns
- No duplication between files

### Developer Experience
- Faster to find information
- Clear navigation structure
- Better onboarding for new team members

### AI Agent Performance
- Load only relevant context
- Faster processing
- More accurate responses (less noise)

## Resources

- **Skill Documentation**: `skills/agents-md-organization/SKILL.md`
- **Agent Documentation**: `agents/agents-md-organizer.md`
- **Complete Example**: `examples/ORGANIZED-STRUCTURE-EXAMPLE.md`
- **Official Spec**: https://agents.md/
- **GitHub Guide**: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

---

**Version**: 1.4.0
**Plugin**: documentation-templates
**Repository**: https://github.com/L-Sypniewski/claude-code-toolkit
