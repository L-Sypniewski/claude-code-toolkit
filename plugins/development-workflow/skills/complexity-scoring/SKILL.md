---
name: complexity-scoring
description: 0-8 point scoring system for feature complexity assessment. Auto-invoke when assessing complexity, determining architecture advisor involvement, or scoring features. Do NOT load for implementation or code review tasks.
---

# Complexity Scoring

Automated 0-8 point scoring system for determining feature complexity and architecture advisor involvement.

## Scoring System (0-8 points)

### 1. File Scope (0-2 points)

| Score | Criteria |
|-------|----------|
| 0 | Single file modification |
| 1 | 2-4 files |
| 2 | 5+ files or new directory structure |

**Signals**:
- Score 0: "update component", "fix function", "add endpoint"
- Score 1: "add feature to module", "connect services"
- Score 2: "new feature across app", "refactor system", "new module"

### 2. Pattern Introduction (0-2 points)

| Score | Criteria |
|-------|----------|
| 0 | Using existing patterns |
| 1 | Minor pattern variation |
| 2 | New architectural pattern |

**Signals**:
- Score 0: "similar to existing", "like other components", "follow pattern"
- Score 1: "adapt pattern", "extend approach", "modify slightly"
- Score 2: "new pattern", "introduce framework", "architectural change"

### 3. Integration Complexity (0-2 points)

| Score | Criteria |
|-------|----------|
| 0 | Isolated feature |
| 1 | Integration with 1-2 systems |
| 2 | Integration with 3+ systems or external APIs |

**Signals**:
- Score 0: "standalone", "no dependencies", "isolated component"
- Score 1: "connect to database", "use auth service", "call API"
- Score 2: "multiple APIs", "third-party services", "cross-system"

### 4. Breaking Changes (0-2 points)

| Score | Criteria |
|-------|----------|
| 0 | Backward compatible |
| 1 | Minor breaking changes (internal) |
| 2 | Major breaking changes or public API modifications |

**Signals**:
- Score 0: "add feature", "new endpoint", "extend functionality"
- Score 1: "change internal API", "refactor module", "rename"
- Score 2: "breaking change", "migration needed", "deprecate API"

## Threshold

| Total Score | Action |
|-------------|--------|
| 0-4 | Proceed with `senior-engineer` only |
| 5-8 | **Invoke `technical-architecture-advisor`** |

## Display Format

```
Complexity Assessment:
- File Scope: X/2
- Pattern Introduction: X/2
- Integration Complexity: X/2
- Breaking Changes: X/2
- TOTAL: X/8

Architecture Advisor: [Will be involved | Not needed]
```

## Examples

### Simple Feature (Score 2)

**Feature**: "Add CSV export button to user list"
- File Scope: 1 (button + export logic = 2 files)
- Pattern: 0 (follows existing export pattern)
- Integration: 0 (no external systems)
- Breaking: 0 (new feature, backward compatible)
- **Total: 2 - Senior engineer only**

### Medium Feature (Score 4)

**Feature**: "Add dark mode toggle with persistence"
- File Scope: 1 (settings, context, styles = 3-4 files)
- Pattern: 1 (minor variation on theme system)
- Integration: 1 (localStorage + database sync)
- Breaking: 0 (backward compatible)
- **Total: 4 - Senior engineer only**

### Complex Feature (Score 6)

**Feature**: "Real-time notifications with WebSockets"
- File Scope: 2 (server, client, multiple components = 5+ files)
- Pattern: 2 (new WebSocket infrastructure)
- Integration: 1 (WebSocket server + Redis pub/sub)
- Breaking: 1 (internal API changes for events)
- **Total: 6 - Architecture advisor involved**

### Major Feature (Score 8)

**Feature**: "Replace REST API with GraphQL"
- File Scope: 2 (entire API layer = many files)
- Pattern: 2 (new paradigm)
- Integration: 2 (all clients + multiple backends)
- Breaking: 2 (major public API change)
- **Total: 8 - Architecture advisor required**

## Scoring Hints

**When uncertain, score higher** - Better to involve architecture advisor unnecessarily than miss issues.

**Look for keywords**:
- High complexity: "architect", "refactor", "migrate", "replace", "infrastructure"
- Medium complexity: "integrate", "connect", "extend", "modify"
- Low complexity: "add", "fix", "update", "tweak", "adjust"

**Consider implicit complexity**:
- Testing requirements (new testing patterns = +1 pattern)
- Documentation needs (new docs structure = +1 file scope)
- Deployment changes (new infra = +1 integration)
