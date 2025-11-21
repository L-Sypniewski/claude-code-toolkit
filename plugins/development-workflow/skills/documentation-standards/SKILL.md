---
name: documentation-standards
description: Standards and templates for technical documentation including API docs, README files, and inline code comments. Use when writing or reviewing documentation.
---

# Documentation Standards

This skill provides guidelines for creating clear, maintainable technical documentation.

## README Structure

Every project should have a comprehensive README:

```markdown
# Project Name

Brief one-line description of what the project does.

## Features

- Key feature 1
- Key feature 2
- Key feature 3

## Installation

```bash
npm install project-name
```

## Quick Start

```javascript
const Project = require('project-name');

const instance = new Project();
instance.doSomething();
```

## Usage

### Basic Example
[Detailed usage example]

### Advanced Usage
[More complex scenarios]

## API Reference

See [API.md](./API.md) for detailed API documentation.

## Configuration

Configuration options and environment variables.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

MIT
```

## API Documentation

### Function/Method Documentation

```javascript
/**
 * Calculates the total price including tax.
 * 
 * @param {number} subtotal - The subtotal before tax
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.1 for 10%)
 * @returns {number} The total price including tax
 * @throws {Error} If subtotal is negative or taxRate is invalid
 * 
 * @example
 * calculateTotal(100, 0.1);  // Returns 110
 * calculateTotal(50, 0.05);  // Returns 52.5
 */
function calculateTotal(subtotal, taxRate) {
  if (subtotal < 0) {
    throw new Error('Subtotal cannot be negative');
  }
  if (taxRate < 0 || taxRate > 1) {
    throw new Error('Tax rate must be between 0 and 1');
  }
  return subtotal * (1 + taxRate);
}
```

### Python Docstrings

```python
def calculate_total(subtotal: float, tax_rate: float) -> float:
    """Calculate the total price including tax.
    
    Args:
        subtotal: The subtotal before tax
        tax_rate: The tax rate as a decimal (e.g., 0.1 for 10%)
        
    Returns:
        The total price including tax
        
    Raises:
        ValueError: If subtotal is negative or tax_rate is invalid
        
    Examples:
        >>> calculate_total(100, 0.1)
        110.0
        >>> calculate_total(50, 0.05)
        52.5
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")
    return subtotal * (1 + tax_rate)
```

## Inline Comments

### When to Comment

**Do comment**:
- Complex algorithms or business logic
- Non-obvious workarounds or hacks
- Performance optimizations
- Regex patterns
- Magic numbers or configuration values

**Don't comment**:
- Obvious code (`i++; // increment i`)
- What the code does (code should be self-documenting)
- Obsolete or outdated information

### Good Comment Examples

```javascript
// ✅ Explains WHY, not WHAT
// Using binary search instead of linear search because
// we expect the array to be sorted and contain 10k+ items
const index = binarySearch(sortedArray, target);

// ✅ Explains workaround
// Safari doesn't support lookbehind in regex, so we use
// this alternative approach. Remove once Safari adds support.
const result = alternativeRegexApproach(input);

// ✅ Explains business logic
// Discount applies only to orders over $100 placed on weekdays
// as per marketing campaign requirements (see JIRA-1234)
if (orderTotal > 100 && isWeekday(orderDate)) {
  applyDiscount(order);
}
```

```javascript
// ❌ Obvious, doesn't add value
// Get user by ID
const user = getUserById(userId);

// ❌ Explaining what instead of why
// Loop through array and add to sum
for (let item of items) {
  sum += item;
}
```

## Architecture Documentation

### Architecture Decision Records (ADRs)

```markdown
# ADR-001: Use PostgreSQL for Primary Database

## Status
Accepted

## Context
We need to choose a database for our application. Requirements:
- ACID compliance
- Complex queries with joins
- JSON support for flexible schemas
- Strong community support

## Decision
We will use PostgreSQL as our primary database.

## Consequences

### Positive
- Robust ACID guarantees
- Excellent JSON/JSONB support
- Rich ecosystem of tools
- Strong performance for complex queries

### Negative
- More complex than NoSQL for simple use cases
- Requires more careful schema design
- Horizontal scaling requires additional tools

## Alternatives Considered
- MongoDB: Rejected due to need for complex joins
- MySQL: PostgreSQL has better JSON support
```

## Changelog

Follow semantic versioning and keep a changelog:

```markdown
# Changelog

## [1.2.0] - 2025-11-21

### Added
- New feature for batch processing
- Support for custom validators

### Changed
- Improved error messages for validation failures
- Updated dependencies to latest versions

### Fixed
- Bug where timeout was not respected
- Memory leak in connection pool

### Deprecated
- `oldFunction()` will be removed in v2.0

## [1.1.0] - 2025-10-15
...
```

## Migration Guides

For breaking changes:

```markdown
# Migration Guide: v1.x to v2.0

## Breaking Changes

### 1. API Endpoint Changes

**Before (v1.x)**:
```javascript
api.getUser(userId)
```

**After (v2.0)**:
```javascript
api.users.get(userId)
```

**Migration**: Update all API calls to use the new namespace structure.

### 2. Configuration Format

**Before**: JSON configuration
**After**: YAML configuration

**Migration Steps**:
1. Convert your `config.json` to `config.yaml`
2. Update configuration loader in your code
3. See [config-converter tool](./tools/config-converter.js)
```

## Documentation Checklist

Before considering documentation complete:

- [ ] README exists with installation and quick start
- [ ] All public APIs are documented with examples
- [ ] Architecture decisions are recorded
- [ ] Breaking changes have migration guides
- [ ] Complex algorithms have explanatory comments
- [ ] Configuration options are documented
- [ ] Contributing guidelines exist
- [ ] License is specified
- [ ] Changelog is maintained

## Integration Points

Works with:
- `senior-engineer` agent for implementation docs
- `pull-request-creator` agent for PR descriptions
- `technical-architecture-advisor` for architecture docs
- Documentation review in code review process
