---
name: ui-design-guidelines
description: Frontend UI design principles, aesthetic heuristics, and design spec templates. Use when: designing UI layouts, refining visual aesthetics, creating design briefs, or specifying component styles. Do NOT use for: code implementation, UI/UX audits, or accessibility compliance.
---

# UI Design Guidelines

Practical guidance for creating polished, modern frontend UI designs with clear visual hierarchy, consistent systems, and implementation-ready specifications.

## Design Discovery

Start by aligning on context before proposing UI direction:

- **Product goals**: What outcome should the UI drive (conversion, productivity, trust)?
- **Target audience**: Skill level, expectations, device usage, accessibility needs.
- **Brand personality**: Friendly, premium, utilitarian, playful, enterprise, etc.
- **Constraints**: Existing design system, component library, technical limits.
- **Success signals**: What visual/interaction improvements matter most?

## Visual System Foundations

Define the system before individual screens:

### Layout & Spacing
- Use a consistent spacing scale (4/8/12/16/24/32/48/64).
- Establish grid and container widths early (mobile-first with max-widths).
- Prioritize whitespace for readability and breathing room.

### Typography
- Establish a typographic scale (H1-H6, body, labels, captions).
- Use 2 font weights per family to keep hierarchy crisp.
- Target readable line lengths (45–80 characters).

### Color
- Define neutral base scale + 1 primary + 1 accent.
- Reserve saturated colors for emphasis and state feedback.
- Ensure contrast is intentional and supports hierarchy.

### Iconography & Imagery
- Keep icon style consistent (stroke vs filled, rounded vs sharp).
- Use imagery as structural support, not decoration.

## Component & Pattern Guidance

Specify component behavior and states to reduce implementation ambiguity:

- **Buttons**: Primary vs secondary vs tertiary hierarchy, size variants.
- **Forms**: Label placement, helper text, validation messaging.
- **Navigation**: Clear active states, predictable hierarchy.
- **Cards & lists**: Consistent padding, alignment, and elevation rules.
- **Tables**: Row density rules, hover affordances, sticky headers if needed.

## Interaction & Motion

- Use motion for clarity and feedback, not decoration.
- Keep transitions short (120–200ms) and consistent.
- Specify hover, focus, active, loading, empty, and error states.

## Responsive Design Priorities

- Define content priority per breakpoint.
- Avoid layout reflows that change meaning between breakpoints.
- Ensure touch target size (44px minimum) on mobile.

## Accessibility Considerations (Design-Level)

- Provide sufficient contrast for key text and actions.
- Ensure focus visibility is planned in the visual system.
- Avoid relying solely on color to convey status.

## Output Template: UI Design Spec

Use this format for handoff:

```markdown
# UI Design Spec – [Feature/Screen]

## 1. Goal & Context
- Objective:
- Primary users:
- Brand attributes:
- Constraints:

## 2. Visual Direction
- Layout structure:
- Spacing rhythm:
- Typographic hierarchy:
- Color usage:
- Visual emphasis hierarchy:

## 3. Component Guidance
- Primary components:
- States (hover, active, loading, empty, error):
- Iconography/imagery notes:

## 4. Interaction & Motion
- Key interactions:
- Motion guidelines:

## 5. Responsive Behavior
- Mobile layout priorities:
- Tablet adjustments:
- Desktop enhancements:

## 6. Accessibility Notes
- Contrast expectations:
- Focus visibility:
- Touch target sizing:

## 7. Open Questions
- [Anything needing confirmation]
```

## Design Quality Checklist

- [ ] Clear visual hierarchy with a single focal point
- [ ] Consistent spacing scale applied across components
- [ ] Typography supports quick scanning and readability
- [ ] Color usage reinforces hierarchy and actions
- [ ] All component states are specified
- [ ] Responsive behavior preserves meaning and priority
- [ ] Accessibility considerations addressed at design level

## Integration Points

Works with:
- `frontend-ui-designer` agent for detailed design specs
- `senior-engineer` agent for implementation handoff
- `screenshot-comparator` agent for visual verification
