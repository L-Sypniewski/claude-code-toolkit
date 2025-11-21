---
name: workflow-orchestrator
description: Coordinate context engineering pipeline workflows from GitHub issue to implementation. Use when managing complete context engineering workflows, orchestrating multi-agent pipelines, or coordinating issue→PRP→implementation workflows. Manages state and data flow between specialized skills, provides flexible invocation patterns, handles error recovery, and tracks workflow progress across all phases.
---

# Workflow Orchestrator

This skill coordinates the complete context engineering workflow, managing state and data flow between specialized skills with flexible invocation options.

## When to Use

- Processing `/execute-context-engineering <GitHub-issue-URL>` commands
- Coordinating complete issue-to-implementation pipelines
- Managing multi-skill workflows
- Handling workflow state and progress tracking
- Orchestrating error recovery and branching logic

## Workflow Architecture

### Four-Skill Orchestration

1. **github-issue-analyzer**: GitHub issue analysis and structured commenting
2. **prp-generator**: PRP creation from structured analysis
3. **prp-executor**: Implementation with validation gates
4. **workflow-orchestrator**: Workflow coordination and state management (this skill)

### Data Flow Management

- **Issue → Analysis**: GitHub URL → structured comment (FEATURE, EXAMPLES, DOCUMENTATION, OTHER CONSIDERATIONS)
- **Analysis → PRP**: Structured comment → comprehensive PRP file
- **PRP → Implementation**: PRP file → validated feature with tests
- **Implementation → Completion**: Validated feature → artifact cleanup

## Orchestration Patterns

### Complete Pipeline Execution

Execute end-to-end GitHub issue to implementation:

```
User Command: /execute-context-engineering <GitHub-issue-URL>

Orchestration Flow:
1. Invoke github-issue-analyzer → structured comment creation
2. Invoke prp-generator → PRP file generation
3. Invoke prp-executor → implementation with validation
4. Coordinate validation gates and artifact cleanup
5. Report completion status and results
```

**Progress Tracking**:
- Phase completion status
- Validation gate results
- Error identification and recovery
- Final workflow summary

### Partial Workflow Execution

Support individual workflow steps:

**Issue Analysis Only**:
```
Command: /initial-github-issue <GitHub-issue-URL>
Action: Invoke github-issue-analyzer
Output: Structured comment on GitHub issue
```

**PRP Generation Only**:
```
Command: /generate-prp <GitHub-issue-URL>
Action: Invoke prp-generator
Output: PRP file in PRPs/ directory
```

**PRP Execution Only**:
```
Command: /execute-prp <PRP-file>
Action: Invoke prp-executor
Output: Implemented feature with validation
```

## State Management

### Workflow State Tracking

Track progress across pipeline phases:

```
Workflow State:
{
  "issue_url": "<GitHub-issue-URL>",
  "current_phase": "analysis|prp_generation|implementation|validation",
  "phase_status": {
    "analysis": "pending|in_progress|complete|failed",
    "prp_generation": "pending|in_progress|complete|failed",
    "implementation": "pending|in_progress|complete|failed",
    "validation": "pending|in_progress|complete|failed"
  },
  "artifacts": {
    "structured_comment_url": "<comment-URL>",
    "prp_file": "<PRP-file-path>",
    "implementation_files": ["<file-paths>"]
  },
  "validation_results": {
    "build": "pass|fail",
    "tests": "pass|fail|skipped",
    "quality": "pass|fail"
  }
}
```

### Data Flow Coordination

**Between Skills**:
- Pass GitHub issue URL to analyzer
- Extract structured comment for PRP generator
- Provide PRP file to executor
- Collect validation results

**Error Handling**:
- Detect skill failures
- Provide error context
- Enable recovery workflows
- Report failures clearly

## Workflow Execution Steps

### 1. Issue Analysis Phase

**Invoke github-issue-analyzer**:
- Pass GitHub issue URL
- Wait for structured comment creation
- Verify comment posted successfully
- Extract comment URL for next phase

**Success Criteria**:
- Structured comment posted to issue
- All four sections complete (FEATURE, EXAMPLES, DOCUMENTATION, OTHER CONSIDERATIONS)
- Comment URL available for reference

### 2. PRP Generation Phase

**Invoke prp-generator**:
- Pass GitHub issue URL and comment reference
- Wait for PRP file creation
- Verify PRP file completeness
- Extract PRP file path for next phase

**Success Criteria**:
- PRP file created in PRPs/ directory
- All sections complete per template
- Validation gates defined
- Implementation guidance included

### 3. Implementation Phase

**Invoke prp-executor**:
- Pass PRP file path
- Monitor implementation progress
- Track validation checkpoint completion
- Collect implementation artifacts

**Success Criteria**:
- All PRP requirements implemented
- Validation gates passing
- Code follows conventions
- Documentation updated

### 4. Validation & Cleanup Phase

**Coordinate Final Validation**:
- Run complete validation suite
- Verify all tests passing
- Check code quality
- Confirm no breaking changes

**Cleanup Artifacts**:
- Remove temporary files
- Clean up debug artifacts
- Verify documentation updates
- Confirm repository clean state

**Success Criteria**:
- All validation gates pass
- No temporary artifacts remain
- Documentation complete
- Ready for PR/merge

## Error Recovery

### Common Failure Scenarios

**Analysis Phase Failure**:
- Retry with clarifying questions
- Request manual structured comment
- Fall back to manual PRP creation

**PRP Generation Failure**:
- Review codebase patterns again
- Request additional context
- Create simplified PRP

**Implementation Failure**:
- Identify specific validation failure
- Provide targeted fixes
- Re-run validation gates

**Validation Failure**:
- Analyze failure logs
- Apply targeted fixes
- Re-run specific validation gate

### Recovery Strategies

- **Partial Restart**: Resume from failed phase
- **Context Enhancement**: Provide additional information
- **Manual Intervention**: Request user guidance
- **Alternative Approach**: Try different implementation strategy

## Progress Reporting

### During Execution

Provide regular status updates:
- Current phase and progress
- Completed validation gates
- Artifacts created
- Estimated completion

### Upon Completion

Report comprehensive summary:
- Overall workflow status
- Phase completion details
- Validation results
- Artifacts created
- Next steps or issues

### Upon Failure

Report detailed failure information:
- Failed phase identification
- Error messages and logs
- Attempted recovery actions
- Recommended next steps

## Flexible Invocation

### Complete Pipeline

Best for:
- New feature implementation from GitHub issue
- First-time implementation workflows
- Complete end-to-end development

### Partial Workflows

Best for:
- Re-running specific phases
- Iterating on PRPs
- Debugging implementation issues
- Manual workflow control

## Quality Assurance

### Pre-Execution Validation

- Verify GitHub issue accessibility
- Check repository permissions
- Confirm validation commands available
- Validate PRP template accessibility

### Post-Execution Validation

- All phases completed successfully
- Artifacts created and accessible
- Validation gates passed
- Documentation updated
- Repository in clean state

## Integration Examples

### Example 1: Complete Workflow

```
User: /execute-context-engineering https://github.com/owner/repo/issues/123

Orchestrator:
1. Analyzes issue #123
2. Creates structured comment
3. Generates PRP file
4. Implements feature
5. Validates and cleans up
6. Reports completion
```

### Example 2: Partial Workflow

```
User: /generate-prp https://github.com/owner/repo/issues/123

Orchestrator:
1. Retrieves structured comment from issue #123
2. Generates PRP file
3. Reports PRP location
```

### Example 3: Error Recovery

```
Workflow fails at implementation phase

Orchestrator:
1. Identifies validation failure
2. Analyzes error logs
3. Applies targeted fix
4. Re-runs validation
5. Continues from implementation phase
```
