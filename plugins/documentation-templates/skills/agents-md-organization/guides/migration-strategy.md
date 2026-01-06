# Migration Strategy: Organizing Large AGENTS.md

Step-by-step guide to reorganize an existing large AGENTS.md file.

## Step 1: Identify Sections

Categorize current content:
- [ ] General architecture (keep in root)
- [ ] Core standards (keep in root)
- [ ] Quality gates (keep in root)
- [ ] Detailed conventions (move to separate file)
- [ ] Testing details (move to separate file or tests/AGENTS.md)
- [ ] Technology-specific details (move to separate files)
- [ ] Subproject details (move to nested AGENTS.md)

## Step 2: Create Structure

```bash
# Create directories
mkdir -p docs
mkdir -p .github/agents  # Optional: isolate from root

# Create detail files
touch docs/architecture.md
touch docs/coding-standards.md
touch docs/testing-guide.md
```

## Step 3: Extract Content

Move detailed sections to appropriate files, keeping structure:

**Before (Large AGENTS.md):**
```markdown
# Project - Development Guide

## Coding Standards
[10 pages of detailed conventions]

## Testing
[15 pages of testing details]
```

**After (Organized):**

**AGENTS.md:**
```markdown
# Project - Development Guide

## Coding Standards
Core principles: SOLID, KISS, YAGNI

**Detailed conventions**: [docs/coding-standards.md](docs/coding-standards.md)

## Testing
Use xUnit with AwesomeAssertions.

**Detailed guidelines**: [docs/testing-guide.md](docs/testing-guide.md)
```

**docs/coding-standards.md:**
```markdown
# Coding Standards

[10 pages of detailed conventions]
```

**docs/testing-guide.md:**
```markdown
# Testing Guide

[15 pages of testing details]
```

## Step 4: Add Navigation

Include clear references in root AGENTS.md:

```markdown
## Quick Links
- [Architecture Details](docs/architecture.md)
- [Coding Standards](docs/coding-standards.md)
- [Testing Guide](docs/testing-guide.md)
- [Backend Instructions](backend/AGENTS.md)
- [Frontend Instructions](frontend/AGENTS.md)
```

## Step 5: Validate

After migration:
- [ ] Root AGENTS.md is concise and scannable
- [ ] All links work correctly
- [ ] No content was lost
- [ ] Navigation is clear and consistent
- [ ] Each file has a clear purpose

## Common Migration Issues

### Duplicate Content
**Problem**: Same information in multiple places
**Solution**: Keep in one canonical location, reference from others

### Broken Links
**Problem**: References point to moved content
**Solution**: Update all internal links after reorganization

### Orphaned Files
**Problem**: Detail files not referenced from root
**Solution**: Add Quick Links section with all references

### Over-Splitting
**Problem**: Too many small files, hard to navigate
**Solution**: Combine related content into logical groupings
