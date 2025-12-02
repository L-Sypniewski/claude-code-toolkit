# UI/UX Audit Plugin

Screenshot-based UI/UX audit workflow with parallel page analysis, multi-viewport testing, and non-destructive error state simulation using Playwright.

## Overview

This plugin provides comprehensive visual and interaction design auditing capabilities for local web applications. It uses Playwright to crawl sites, capture screenshots at multiple viewports, and generate professional UI/UX audit reports.

## Features

- **Automated Page Discovery**: Crawl web applications to discover all accessible pages
- **Multi-Viewport Testing**: Test across mobile, tablet, and desktop viewports
- **Parallel Auditing**: Spawn multiple agents for efficient page-by-page analysis
- **Non-Destructive**: Uses GET-only navigation and route interception for error simulation
- **Professional Terminology**: Reports use design language, not implementation details
- **Incremental Output**: Results written progressively during audit

## Components

### Agents

| Agent | Description |
|-------|-------------|
| `ui-ux-audit-orchestrator` | Crawls sites, coordinates parallel audits, compiles cross-page findings |
| `ui-ux-page-auditor` | Audits individual pages across all viewports |

### Skills

| Skill | Description |
|-------|-------------|
| `ui-ux-audit-guidelines` | Professional audit methodology, evaluation criteria, and design vocabulary |

### Commands

| Command | Description |
|---------|-------------|
| `/ui-ux-audit [url]` | Initiate comprehensive UI/UX audit (defaults to `https://localhost:7201/`) |

## Usage

### Basic Audit

```bash
/ui-ux-audit https://localhost:3000/
```

### Audit with Specific Pages

```
Audit the following pages on localhost:3000:
- /
- /about
- /pricing
- /dashboard

Focus on mobile and desktop viewports.
```

### Error State Testing

```
Audit https://localhost:3000/ and simulate error states:
- API failures (500 errors)
- Empty data responses
- Slow loading scenarios
```

## Viewports Tested

| Category | Dimensions | Use Case |
|----------|------------|----------|
| Mobile | 428×926 | Large phone (iPhone 14 Pro Max) |
| Tablet Portrait | 768×1024 | iPad in portrait orientation |
| Tablet Landscape | 1024×768 | iPad in landscape orientation |
| Desktop | 1160×720 | Small laptop/desktop |
| Large Desktop | 1920×1080 | Full HD displays |

## Evaluation Criteria

The audit evaluates pages against these professional UI/UX criteria:

### Visual Design
- Visual hierarchy and typographic scale
- Spacing rhythm, layout density, and vertical/horizontal balance
- Alignment, grid adherence, and proportional structure
- Color contrast and visual weight distribution

### Interaction Design
- Navigation clarity (active states, discoverability, labeling)
- Component affordance and interaction clarity
- Feedback states (hover, focus, active, disabled, loading)
- Dialog and modal behavior

### Responsive Behavior
- Responsive adaptation at each breakpoint
- Touch target sizing on mobile devices
- Content overflow and layout patterns
- Large viewport optimization

### Content & States
- Empty states and zero-data views
- Error and failure state handling
- Loading experiences (spinners vs skeletons)
- Information architecture clarity

### Consistency
- Cross-page component consistency
- Spacing and typography uniformity
- Color application consistency
- Microinteraction and transition patterns

## Output Format

The audit produces a structured markdown file with:

1. **Executive Summary**: Overall health score and key findings
2. **Pages Audited Summary**: Issue counts per page
3. **Cross-Page Consistency Issues**: Patterns across the site
4. **Detailed Page Audits**: Per-page, per-viewport findings
5. **Screenshot Gallery**: All captured screenshots organized by page

### Sample Output Structure

```markdown
# UI/UX Audit Report

**Target**: https://localhost:3000/
**Date**: 2025-01-15
**Pages Audited**: 8

## Executive Summary

### Overall Health Score
Good - Minor consistency issues, strong fundamentals

### Key Findings
1. Inconsistent spacing scale between header and content sections
2. Missing hover states on secondary navigation items
3. Typography scale needs adjustment for mobile readability

## Detailed Findings

# Page – /dashboard

## Viewport: 428×926 (Mobile)

### Issues Found

#### Visual Hierarchy
- Heading levels lack sufficient weight differentiation

#### Spacing and Layout
- Card padding inconsistent with page margins

### Recommended Improvements
1. Increase heading weight from 500 to 600 for better hierarchy
2. Standardize card padding to match 16px page margin
```

## Safety Features

- **GET-only Navigation**: Never submits forms or triggers state changes
- **Route Interception**: Error states simulated without real destructive actions
- **Skip Destructive Links**: Automatically avoids logout and delete actions
- **External Link Filtering**: Only audits pages within the target domain

## Integration

This plugin works well with:

- `development-workflow` plugin for implementing audit recommendations
- `screenshot-comparator` agent for before/after visual testing
- Any Playwright-enabled environment

## Requirements

- Claude Code with Playwright MCP server enabled
- Local web application running on accessible port
- Write access for output markdown file

## License

MIT License - See [LICENSE](../../LICENSE) for details.
