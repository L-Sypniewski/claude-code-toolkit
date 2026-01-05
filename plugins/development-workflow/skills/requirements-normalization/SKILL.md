---
name: requirements-normalization
description: Output format, templates, and examples for structuring feature requirements. Auto-invoke when normalizing feature requirements, structuring input, or analyzing GitHub issues for feature workflows. Do NOT load for implementation, code review, or planning tasks.
---

# Requirements Normalization

Standard format and patterns for structuring feature requirements from any input source.

## Output Format

All inputs normalized to this structure:

```markdown
## FEATURE
[Clear, concise description of what needs to be built. Be specific about:
- Core functionality
- User-visible behavior
- Expected outcomes
- Success criteria]

## EXAMPLES
[Concrete examples of the feature in action:
- Usage scenarios
- Input/output examples
- User interaction flows
- Edge cases to consider]

## DOCUMENTATION
[Technical implementation guidance:
- Relevant existing code/patterns
- Technology choices and constraints
- Integration points with existing systems
- Architectural considerations
- Links to relevant documentation]

## OTHER CONSIDERATIONS
[Additional factors that influence implementation:
- Performance requirements
- Security implications
- Backwards compatibility
- Migration needs
- Testing strategy
- Deployment considerations]
```

## Completeness Status

Append status indicator at end of output:

```markdown
---
**COMPLETENESS**: COMPLETE | INCOMPLETE
**CRITICAL GAPS**: [List if incomplete]
**RECOMMENDATION**: [Next step]
```

**COMPLETE**: All sections have sufficient detail for complexity scoring and planning.

**INCOMPLETE**: Critical gaps exist that affect scope/architecture:
- List specific gaps
- Recommend `feature-requirements-clarifier` agent

## Good vs Bad Examples

### FEATURE Section

**Bad** (vague):
```
Add authentication to the app
```

**Good** (specific):
```
Implement JWT-based authentication with:
- User registration and login endpoints (Express.js)
- Password hashing using bcrypt (12 rounds)
- JWT access tokens (15min expiry) and refresh tokens (7 days)
- Protected route middleware
- Session management in Redis
```

### EXAMPLES Section

**Bad** (vague):
```
Users can log in
```

**Good** (concrete):
```
1. New user registration:
   POST /api/auth/register
   Body: { email: "user@example.com", password: "secure123" }
   Response: { token: "jwt...", user: { id, email } }

2. Login flow:
   POST /api/auth/login
   Body: { email: "user@example.com", password: "secure123" }
   Response: { token: "jwt...", refreshToken: "..." }
```

### DOCUMENTATION Section

**Bad** (generic):
```
Use standard authentication patterns
```

**Good** (specific):
```
- Express.js middleware: https://expressjs.com/en/guide/using-middleware.html
- Existing auth pattern: src/middleware/auth.ts
- JWT spec: https://tools.ietf.org/html/rfc7519
- Similar implementation: examples/auth-flow/
```

### OTHER CONSIDERATIONS Section

**Bad** (generic):
```
Make it secure
```

**Good** (specific):
```
- Security: Rate limiting on auth endpoints (10 attempts/15min)
- Performance: Cache JWT validation in Redis (5min TTL)
- Compatibility: Must work with existing session-based admin panel
- Migration: Script to migrate existing user passwords
- Testing: Unit tests for middleware, integration for full flow
```

## Handling Incomplete Input

When input is vague (e.g., "implement dark mode"):

```markdown
## FEATURE
Implement dark mode functionality for the application.

## EXAMPLES
_No examples provided in input._

## DOCUMENTATION
**General Resources**:
- React Context API: https://react.dev/learn/passing-data-deeply-with-context
- CSS custom properties: https://developer.mozilla.org/...

_Specific technical approach requires clarification._

## OTHER CONSIDERATIONS
_Requires clarification on scope and constraints._

---
**COMPLETENESS**: INCOMPLETE
**CRITICAL GAPS**:
- Placement: Where should the toggle be located?
- Persistence: How should preference be stored?
- Scope: Which pages/components need dark mode?
- System preference: Detect prefers-color-scheme?

**RECOMMENDATION**: Invoke `feature-requirements-clarifier` agent.
```

## Quality Checklist

Before returning, verify:
- [ ] FEATURE is specific and actionable (not vague)
- [ ] EXAMPLES have concrete scenarios (if available)
- [ ] DOCUMENTATION references actual resources and code
- [ ] OTHER CONSIDERATIONS captures project-specific details
- [ ] COMPLETENESS status is accurate
- [ ] CRITICAL GAPS are specific questions (if incomplete)
