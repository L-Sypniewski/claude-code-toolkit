---
name: commit-conventions
description: Comprehensive commit message conventions and best practices following Conventional Commits specification for clear, semantic version control history
author: Claude Code Toolkit
---

# Commit Message Conventions

This skill provides comprehensive commit message guidelines following industry best practices and the Conventional Commits specification.

## Purpose

Automatically activated when:
- Writing commit messages
- Reviewing commit history
- Creating pull requests
- Generating changelogs
- Analyzing repository history
- Setting up commit hooks

## Conventional Commits Format

### Basic Structure

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Example:**
```
feat(auth): add JWT token validation

Implement JWT token validation middleware for API endpoints.
Tokens are validated against secret key and expiration time.

Closes #123
BREAKING CHANGE: API now requires authentication header
```

### Required Elements

**Type (Required):**
- Must be a noun
- Lowercase only
- Describes the kind of change

**Description (Required):**
- Short summary of the change
- Lowercase first letter (imperative mood)
- No period at the end
- Maximum 72 characters

**Optional Elements:**
- Scope: Component or module affected
- Body: Detailed explanation
- Footer: Breaking changes, issue references

## Commit Types

### Standard Types

**feat:**
- New feature for the user
- Adds functionality
- Triggers minor version bump (semantic versioning)

Examples:
```
feat: add user profile page
feat(api): add endpoint for user preferences
feat(auth): implement OAuth2 login flow
```

**fix:**
- Bug fix for the user
- Corrects existing functionality
- Triggers patch version bump

Examples:
```
fix: resolve memory leak in data processor
fix(ui): correct button alignment on mobile
fix(api): handle null response from external service
```

**docs:**
- Documentation only changes
- No code changes
- README, comments, API docs

Examples:
```
docs: update installation instructions
docs(api): add examples for authentication
docs: fix typo in contributing guide
```

**style:**
- Code style changes (formatting, white-space, etc.)
- No logic changes
- Does not affect meaning of code

Examples:
```
style: fix indentation in user service
style(css): reformat stylesheet with prettier
style: remove trailing whitespace
```

**refactor:**
- Code change that neither fixes bug nor adds feature
- Restructures existing code
- Improves code quality

Examples:
```
refactor: extract validation logic into separate module
refactor(auth): simplify token generation
refactor: rename variables for clarity
```

**perf:**
- Performance improvement
- Makes code faster
- Optimizes resource usage

Examples:
```
perf: optimize database query for user search
perf(rendering): reduce unnecessary re-renders
perf: add caching layer for API responses
```

**test:**
- Adding or updating tests
- No production code changes
- Test-related changes only

Examples:
```
test: add unit tests for user service
test(integration): add API endpoint tests
test: increase coverage for auth module
```

**build:**
- Build system or external dependency changes
- Package.json, webpack, build scripts
- CI/CD configuration

Examples:
```
build: update webpack configuration
build(deps): upgrade react to version 18
build: add npm script for production build
```

**ci:**
- CI/CD configuration changes
- GitHub Actions, Travis, CircleCI
- Automated pipeline changes

Examples:
```
ci: add automated testing workflow
ci(github): update deployment action
ci: configure code coverage reporting
```

**chore:**
- Maintenance tasks
- No production code changes
- Routine tasks, configuration

Examples:
```
chore: update dependencies
chore(config): update eslint rules
chore: clean up deprecated code
```

**revert:**
- Reverts a previous commit
- Should reference the reverted commit

Examples:
```
revert: revert "feat: add user profile page"

This reverts commit a1b2c3d4.
```

### Additional Types (Optional)

**security:**
- Security-related changes
- Vulnerability fixes
- Security improvements

Examples:
```
security: fix XSS vulnerability in user input
security(api): add rate limiting
```

**deps:**
- Dependency updates
- More specific than build

Examples:
```
deps: update lodash to 4.17.21
deps(dev): upgrade jest to latest version
```

**i18n:**
- Internationalization and localization

Examples:
```
i18n: add French translations
i18n(ui): update date formats for DE locale
```

## Scope Guidelines

### What is Scope?

Scope specifies the part of codebase affected by the commit.

**Scope Examples:**
- Module name: `(auth)`, `(payment)`, `(user)`
- Component: `(UserProfile)`, `(LoginForm)`
- Feature area: `(api)`, `(ui)`, `(database)`
- File/package: `(package.json)`, `(webpack)`

### Scope Best Practices

**Do:**
- Use consistent scopes across project
- Keep scopes short and clear
- Use lowercase for scopes
- Document common scopes in CONTRIBUTING.md

**Don't:**
- Use vague scopes: `(stuff)`, `(things)`
- Use very specific scopes: `(user-profile-header-button)`
- Mix scope naming conventions
- Use scopes inconsistently

**Example Scope Structure:**
```
(api)        - API layer
(ui)         - User interface
(database)   - Database layer
(auth)       - Authentication
(payment)    - Payment processing
(admin)      - Admin functionality
(config)     - Configuration
(tests)      - Test suite
```

## Description Guidelines

### Writing Good Descriptions

**Imperative Mood:**
Use imperative present tense ("add", not "added" or "adds")

✅ Good:
```
feat: add user authentication
fix: resolve database connection issue
refactor: simplify error handling
```

❌ Bad:
```
feat: added user authentication
fix: resolves database connection issue
refactor: simplified error handling
```

### Description Best Practices

**Do:**
- Start with lowercase
- Be clear and specific
- Keep under 72 characters
- Use imperative mood
- Focus on "what" not "how"

**Don't:**
- End with period
- Be vague ("fix stuff", "update things")
- Use past tense
- Include implementation details
- Exceed character limit

### Description Examples

**Too Vague:**
```
fix: fix bug
feat: add feature
update: update code
```

**Better:**
```
fix: resolve null pointer exception in user service
feat: add password reset functionality
refactor: extract validation into utility module
```

**Even Better with Scope:**
```
fix(auth): resolve null pointer exception in token validation
feat(user): add password reset functionality with email verification
refactor(validation): extract common validation logic into utility module
```

## Body Guidelines

### When to Add Body

**Add body when:**
- Need to explain "why" not just "what"
- Change is complex or non-obvious
- Multiple changes in one commit
- Context is important for future reference
- Breaking changes need explanation

**Can skip body when:**
- Change is simple and self-explanatory
- Description is sufficient
- Obvious bug fix
- Minor updates

### Body Structure

**Format:**
- Separate from description with blank line
- Wrap at 72 characters
- Can have multiple paragraphs
- Focus on motivation and context

**Example:**
```
refactor(cache): replace Redis with in-memory cache

The Redis dependency was causing deployment issues in serverless
environments. An in-memory cache is sufficient for our use case
as cache data doesn't need to persist across instances.

This change reduces external dependencies and simplifies deployment.
Performance testing shows no significant difference for our workload.
```

### Body Content

**Include:**
- Motivation for the change
- Contrast with previous behavior
- Side effects or consequences
- Link to related issues/docs
- Migration notes if applicable

**Example with Context:**
```
perf(api): implement connection pooling

Database connections were being created for each request, causing
performance degradation under load. Connection pooling reduces
connection overhead and improves response times.

Benchmark results:
- Before: 450ms average response time
- After: 85ms average response time

Closes #456
```

## Footer Guidelines

### Breaking Changes

**Format:**
```
BREAKING CHANGE: description of breaking change
```

**Example:**
```
feat(api): change authentication endpoint

BREAKING CHANGE: /auth/login endpoint now returns JWT token
in 'accessToken' field instead of 'token'. Update all API clients
to use the new field name.
```

**Multiple Breaking Changes:**
```
BREAKING CHANGE: /api/users endpoint requires authentication
BREAKING CHANGE: User model no longer includes 'age' field
```

### Issue References

**Closing Issues:**
```
Closes #123
Closes #123, #456
Fixes #789
Resolves #321
```

**Referencing Issues:**
```
Refs #123
See #456
Related to #789
```

**Multiple References:**
```
feat(user): add profile editing

Closes #123
Related to #456
See also #789
```

### Co-authors

**Format:**
```
Co-authored-by: Name <email@example.com>
Co-authored-by: Another Name <another@example.com>
```

**Example:**
```
feat(payments): integrate Stripe payment gateway

Implement Stripe integration for credit card payments.
Includes webhook handling for payment confirmations.

Co-authored-by: Jane Doe <jane@example.com>
Closes #567
```

## Complete Examples

### Simple Feature
```
feat(auth): add password strength validation
```

### Feature with Body
```
feat(notifications): add email notification system

Implement email notification system using SendGrid API.
Users can now receive notifications for important events
such as password changes and account updates.

Closes #234
```

### Bug Fix with Breaking Change
```
fix(api)!: correct user data serialization

Fix incorrect date formatting in user API responses.
Dates now follow ISO 8601 standard format.

BREAKING CHANGE: Date fields in API responses now return
ISO 8601 format (YYYY-MM-DD) instead of Unix timestamps.
Update all clients to parse new date format.

Fixes #345
```

### Refactor with Detailed Body
```
refactor(database): migrate from MongoDB to PostgreSQL

Migrate data layer from MongoDB to PostgreSQL for better
relational data handling and transaction support.

Changes include:
- Updated schema to use SQL tables
- Implemented database migrations
- Updated all queries and data access layer
- Added connection pooling
- Updated tests for new database

Migration guide available in docs/migration.md

BREAKING CHANGE: Database configuration format has changed.
See docs/migration.md for upgrade instructions.

Closes #678
Related to #645, #712
```

### Performance Improvement
```
perf(search): optimize search query with indexes

Add database indexes on commonly searched fields to improve
search performance. Query time reduced from 2s to 200ms for
typical searches.

Benchmarks:
- User search: 2000ms → 180ms (90% faster)
- Product search: 1500ms → 220ms (85% faster)

Closes #891
```

## Commit Message Checklist

Before committing, verify:

- [ ] Type is appropriate and correct
- [ ] Scope is relevant (if used)
- [ ] Description is clear and concise
- [ ] Description uses imperative mood
- [ ] Description is under 72 characters
- [ ] Body explains "why" if needed
- [ ] Breaking changes are documented
- [ ] Issues are referenced appropriately
- [ ] No typos or grammatical errors
- [ ] Follows project conventions

## Tools and Automation

### Commitizen

**Install:**
```bash
npm install -g commitizen cz-conventional-changelog
```

**Usage:**
```bash
git cz  # Instead of git commit
```

### Commitlint

**Install:**
```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional
```

**Configure (.commitlintrc.json):**
```json
{
  "extends": ["@commitlint/config-conventional"]
}
```

**Git Hook:**
```bash
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
```

### Semantic Release

Automatically determines version and generates changelog based on commits.

**Install:**
```bash
npm install --save-dev semantic-release
```

## Anti-Patterns

**Avoid:**
- Vague messages: "fix bug", "update stuff"
- Past tense: "fixed bug", "added feature"
- Combining unrelated changes
- Missing type prefix
- Unclear descriptions
- Overly long descriptions
- Missing breaking change documentation
- Inconsistent formatting
- Personal notes in commits

## Team Guidelines

### Establish Standards

**Document in CONTRIBUTING.md:**
- Required commit format
- Approved types and scopes
- When to use breaking changes
- Issue reference format
- Examples of good commits

### Enforce with Tools

- Commitlint for validation
- Git hooks for automation
- PR templates with commit guidelines
- CI checks for commit format
- Code review checklist

### Training

- Share commit examples
- Review commits in team meetings
- Provide feedback on commit messages
- Create commit message guides
- Use commitizen for consistency

## Benefits of Good Commit Messages

**For Development:**
- Easy to review changes
- Quick to understand history
- Simple to revert changes
- Automated changelog generation
- Semantic versioning automation

**For Team:**
- Better collaboration
- Clear communication
- Knowledge sharing
- Onboarding new members
- Understanding decisions

**For Project:**
- Professional appearance
- Better documentation
- Easier maintenance
- Simplified debugging
- Clear project evolution

## Usage by Agents

This skill is automatically available to:
- All agents when creating commits
- **pull-request-creator** when analyzing commits for PR descriptions
- **senior-engineer** when committing code changes
- Any agent performing git operations

The skill ensures consistent, professional commit messages across all development activities.
