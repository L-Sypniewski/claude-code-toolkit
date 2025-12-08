# UI/UX Audit

Conduct a comprehensive, screenshot-based UI/UX audit of a local web application.

## Target: $ARGUMENTS

If no URL is provided, default to `http://localhost:3000/`

## Audit Workflow

1. **Site Crawling**
   - Use Playwright to discover all accessible pages
   - Use safe GET-only navigations
   - Do NOT submit forms or trigger destructive actions
   - Skip logout links and destructive action buttons

2. **Parallel Page Auditing**
   - Spawn a parallel agent for each discovered page
   - Each agent captures screenshots for all viewports
   - Each agent performs visual UI/UX analysis
   - Results appended incrementally to shared markdown file

3. **Error State Simulation** (when applicable)
   - Use Playwright route interception to simulate errors
   - Force 500 responses, block requests, return empty data
   - Do NOT perform actual destructive actions

## Viewports to Test

| Category | Dimensions | Description |
|----------|------------|-------------|
| Mobile | 428×926 | Large phone |
| Tablet Portrait | 768×1024 | iPad portrait |
| Tablet Landscape | 1024×768 | iPad landscape |
| Desktop | 1160×720 | Small desktop |
| Large Desktop | 1920×1080 | Full HD |

## Evaluation Criteria

For each page at each viewport, evaluate:

### Visual Design
- Visual hierarchy and typographic scale
- Spacing rhythm and layout density
- Grid alignment and proportional structure
- Color contrast and visual weight distribution

### Interaction Design
- Navigation clarity and active states
- Component affordance and interaction cues
- Feedback states (hover, focus, active, disabled, loading)
- Dialog/modal behavior and transitions

### Responsive Behavior
- Adaptation at each breakpoint
- Touch target sizing on mobile
- Content overflow handling
- Layout pattern appropriateness

### Content & States
- Empty states and zero-data views
- Error and failure states
- Loading experiences
- Information architecture clarity

### Consistency
- Cross-page component consistency
- Spacing and typography uniformity
- Color application consistency
- Microinteraction patterns

## Output Requirements

**Use professional UI/UX terminology only**

- ✅ "Increase heading weight differentiation"
- ✅ "Apply consistent 8px spacing rhythm"
- ✅ "Strengthen primary CTA visual weight"
- ❌ "Change the CSS to..."
- ❌ "Modify the HTML..."

**Recommendations must be actionable design guidance, not implementation instructions.**

## Delegation

Use the `ui-ux-audit-orchestrator` agent to execute this workflow. The orchestrator will:
1. Crawl the site to discover pages
2. Spawn `ui-ux-page-auditor` agents for parallel page analysis
3. Compile cross-page consistency findings
4. Generate executive summary

## Additional Instructions

Use sequential thinking to plan the audit approach. Reference the `ui-ux-audit-guidelines` skill for evaluation criteria and professional terminology.
