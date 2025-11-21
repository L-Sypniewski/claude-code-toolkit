---
name: prp-executor
description: Execute Product Requirements Prompts (PRPs) using pragmatic development methodology. Use when implementing features from PRP files with flexible testing approaches based on complexity and value. Orchestrates complete implementation workflow from PRP analysis through validation gate completion and artifact cleanup. Use for /execute-prp commands or when implementing features with structured validation checkpoints.
---

# PRP Executor

This skill executes AI-focused Product Requirements Prompts through pragmatic development approaches with flexible validation strategies.

## When to Use

- Implementing features from structured PRPs
- When users ask to "implement this PRP" or "execute the implementation plan"
- Executing phased development with validation gates
- Managing implementation-to-completion workflows
- Balancing thoroughness with development velocity
- Following a PRP blueprint with incremental validation

## Execution Workflow

### Phase 1: PRP Analysis & Planning

**PRP File Processing**:

1. **Read and Parse PRP**:
   - Extract implementation phases and validation checkpoints
   - Identify technical requirements and success criteria
   - Map integration points and file modifications

2. **Create Todo Plan**:
   - Break down PRP phases into actionable tasks
   - Include validation checkpoints as distinct items
   - Map validation gates for each component

3. **Setup Context**:
   - Analyze existing codebase patterns referenced in PRP
   - Identify files to modify and new files to create
   - Validate dependencies and integration requirements

### Phase 2: Foundation Implementation

**Standard Implementation Approach**:

1. **IMPLEMENT**: Build feature following existing patterns
2. **VALIDATE**: Run build validation to ensure code quality
3. **TEST**: Add optional E2E tests for complex features when valuable
4. **DOCUMENT**: Update relevant documentation

**Validation Checkpoint**:
- [ ] Code quality validation passes
- [ ] Core functionality working as specified
- [ ] Integration points correctly implemented
- [ ] Build validation passes (mandatory)
- [ ] Optional E2E tests implemented where valuable

### Phase 3: Enhancement Implementation

**Advanced Features & Edge Cases**:

- Build features incrementally with build validation
- Add complexity with appropriate validation checkpoints
- Focus on user-critical functionality and error handling

**Validation Checkpoint**:
- [ ] Advanced features implemented correctly
- [ ] Edge cases handled appropriately
- [ ] Performance requirements met
- [ ] Error handling provides good UX

### Phase 4: Integration & Polish

**System Integration and Final Validation**:

1. **E2E Testing**: Execute tests based on feature category
2. **Cross-Browser Testing**: Validate per feature category
3. **Performance Validation**: Verify performance expectations
4. **Accessibility Testing**: Validate inclusive design

**Final Validation Checkpoint**:
- [ ] E2E tests passing (when implemented)
- [ ] Cross-browser testing completed per category
- [ ] Performance benchmarks met
- [ ] Accessibility standards validated
- [ ] All PRP success criteria fulfilled

## Pragmatic Validation Framework

### Validation Decision Framework

**Build Validation** (Primary Method):
- Type checking and compilation
- Linting and code style
- Syntax validation
- Mandatory for all changes

**Optional E2E Testing**:
- Use for complex interactive features
- When tests add significant value
- For critical user workflows
- Skip for simple styling or low-risk changes

### Feature Categorization Testing

**🔴 CRITICAL Features**:
- Test on ALL browsers: Chrome, Firefox, Safari, Edge
- Test on ALL mobile devices: iOS Safari, Android Chrome
- Execute complete accessibility testing
- Validate performance benchmarks on all platforms
- Consider E2E tests for critical workflows

**🟡 STANDARD Features**:
- Test on main browsers: Chrome, Firefox
- Test on one mobile platform
- Execute core accessibility testing
- Validate performance on primary platforms
- Consider E2E tests for key workflows when valuable

**🟢 EDGE CASE Features**:
- Test on one browser (Chrome desktop)
- Execute basic functionality validation
- Focus on manual testing
- Skip automated E2E tests unless critical

## Project-Specific Validation Gates

Execute project validation suite before completion:

```bash
# Example: Frontend Validation
cd frontend && npm run build

# Example: Backend Validation
cd backend && npm run build

# Example: Optional E2E Tests
cd tests && npm test
```

**Validation Requirements**:
- All validation commands pass without errors
- Build processes complete successfully
- Optional test suites pass (when implemented)
- No breaking changes to existing functionality

## Implementation Best Practices

### Code Quality

- Follow existing codebase patterns and conventions
- Use proper typing and error handling
- Include inline documentation for complex logic
- Keep functions focused and maintainable

### Incremental Progress

- Implement in small, testable increments
- Validate each increment with build validation
- Commit working code frequently
- Document progress in todo plan

### Error Handling

- Implement proper error boundaries
- Provide clear user feedback
- Log errors for debugging
- Handle edge cases gracefully

### Performance

- Optimize critical paths
- Lazy load non-essential resources
- Cache appropriately
- Monitor build size and runtime performance

## Artifact Cleanup

After implementation completion:

### Temporary Files

- Remove temporary test files
- Clean up debug logs
- Delete unused imports
- Remove commented-out code

### Documentation

- Update relevant documentation
- Add inline comments for complex logic
- Update README if needed
- Document breaking changes

### Final Validation

Run complete validation suite:
- [ ] All builds pass
- [ ] Tests pass (when implemented)
- [ ] Linting passes
- [ ] No temporary artifacts remain
- [ ] Documentation updated

## Quality Checklist

Before marking PRP as complete:

- [ ] All PRP requirements implemented
- [ ] Validation gates passing
- [ ] Edge cases handled
- [ ] Error handling robust
- [ ] Performance acceptable
- [ ] Accessibility validated
- [ ] Documentation updated
- [ ] Temporary artifacts cleaned
- [ ] Code follows conventions
- [ ] Integration points working

## Integration with Workflow

1. **GitHub Issue Analysis** → Structured comment
2. **PRP Generation** → Implementation blueprint
3. **PRP Execution** (this skill) → Feature implementation
4. **Validation & Cleanup** → Quality assurance
