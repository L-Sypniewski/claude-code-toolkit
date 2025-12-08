---
name: ui-ux-audit-guidelines
description: UI/UX audit methodology and design vocabulary. Use when conducting UI/UX audits. Do NOT use for code reviews, WCAG audits, or performance analysis.
---

# UI/UX Audit Guidelines

## Audit Viewports

Mobile: 428×926 | Tablets: 768×1024, 1024×768 | Desktop: 1160×720, 1920×1080

## Evaluation Categories

1. **Visual Hierarchy & Typography**: Heading hierarchy, typographic scale, weight contrast, font pairing, line height, measure
2. **Spacing & Layout**: Vertical rhythm, gutters, whitespace, padding/margin, visual density, proximity
3. **Grid & Alignment**: Grid structure, column spans, edge/baseline alignment, container widths
4. **Color & Contrast**: Contrast ratios, color weight, accent usage, semantic colors
5. **Navigation**: Active states, discoverability, labeling, breadcrumbs, wayfinding
6. **Component Affordance**: Clickability cues, hover/focus states, touch targets, interactive signifiers
7. **Feedback States**: Hover, focus, active, disabled, loading indicators, state transitions
8. **Dialogs & Modals**: Positioning, backdrop, focus trap, scroll lock, close handling, transitions
9. **Responsive**: Breakpoints, content reflow, mobile touch targets, layout adaptation
10. **Cross-Page Consistency**: Component styling, spacing scale, typography, colors, patterns
11. **Empty & Error States**: Zero-data views, onboarding, error messages, recovery paths
12. **Loading**: Skeletons, spinners, progress indicators, content jumps, perceived performance
13. **Information Architecture**: Content grouping, labeling, cognitive load, hierarchy
14. **Microinteractions**: Feedback animations, easing, timing, state transitions
15. **Large Viewport**: Max-width constraints, content centering, widescreen optimization

## Recommendations

Use design language, not code. Good: "Establish 8px spacing scale", "Increase heading weight to 600". Avoid: "Change CSS", "Add padding: 16px".

## Error State Simulation

Use Playwright route interception: API failures (500), network errors (block endpoints), slow loading (delays), empty data (empty arrays).
