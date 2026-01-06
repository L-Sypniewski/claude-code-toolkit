---
name: requirements-clarification
description: Question templates and patterns for clarifying incomplete feature requirements. Auto-invoke when asking clarifying questions, resolving ambiguities, or enriching vague requirements. Do NOT load for implementation, code review, or validation tasks.
---

# Requirements Clarification

This skill provides structured patterns for asking clarifying questions when feature requirements are incomplete, vague, or ambiguous.

## When to Ask Questions

### DO Ask About:
- **Scope boundaries**: What's included vs. excluded
- **User experience**: Where, when, how users interact
- **Data persistence**: How and where data is stored
- **Integration points**: What systems/APIs are involved
- **Breaking changes**: Impact on existing functionality
- **Performance requirements**: Speed, scale, resource constraints

### DON'T Ask About:
- **Implementation details**: Let planning phase determine
- **Industry standards**: Use defaults (e.g., WCAG AA, REST conventions)
- **Code structure**: Architecture advisor will guide
- **Minor preferences**: Only ask if affects complexity/scope

## Question Templates by Category

### Scope & Boundaries

**Template**:
```
Question: "What's the scope of [feature]?"
Header: "Scope"
Options:
- "[Minimal scope]" (Faster, limited functionality)
- "[Standard scope]" (Recommended - balanced)
- "[Comprehensive scope]" (Full-featured, more complex)
- "Custom scope" (Let me specify)
```

**Examples**:
- Dark mode: "Entire app vs. specific pages?"
- Search: "Single resource type vs. global search?"
- Export: "Current view vs. all data?"

### User Interface & Placement

**Template**:
```
Question: "Where should [UI element] be located?"
Header: "Placement"
Options:
- "[Primary location]" (Recommended - standard placement)
- "[Alternative location]" (Different UX pattern)
- "[Multiple locations]" (More visible, more work)
```

**Examples**:
- Settings toggle: "Settings page vs. header vs. both?"
- Action button: "List view vs. detail view vs. both?"
- Notification display: "Toast vs. banner vs. modal?"

### Data & Persistence

**Template**:
```
Question: "How should [data] be stored/persisted?"
Header: "Persistence"
Options:
- "Client-side only" (localStorage/sessionStorage)
- "Server-side only" (Database)
- "Both client + server" (Recommended - instant + synced)
- "No persistence" (Session only)
```

**Examples**:
- User preferences: "localStorage vs. database vs. both?"
- Form drafts: "Persist vs. session only?"
- Filters/sorting: "Remember vs. reset?"

### Integration & Dependencies

**Template**:
```
Question: "What should [feature] integrate with?"
Header: "Integration"
Options:
- "Isolated feature" (No dependencies)
- "[System A]" (Single integration)
- "[System A] + [System B]" (Multiple integrations)
- "Custom integrations" (Let me specify)
```

**Examples**:
- Notifications: "In-app only vs. email vs. SMS vs. all?"
- Authentication: "Local only vs. OAuth vs. SSO?"
- Analytics: "None vs. GA vs. custom?"

### Behavior & Timing

**Template**:
```
Question: "When should [action] happen?"
Header: "Trigger"
Options:
- "Immediately" (Real-time)
- "On user action" (Manual trigger)
- "Scheduled/background" (Async)
- "Conditional" (Based on criteria)
```

**Examples**:
- Data sync: "Real-time vs. on save vs. periodic?"
- Validation: "On blur vs. on submit vs. real-time?"
- Email notifications: "Immediate vs. daily digest?"

### Compatibility & Migration

**Template**:
```
Question: "How should we handle existing [data/users/functionality]?"
Header: "Migration"
Options:
- "No migration needed" (New feature, no existing data)
- "Automatic migration" (Convert automatically)
- "Manual migration" (User/admin action required)
- "Gradual rollout" (Optional adoption)
```

**Examples**:
- New data model: "Migrate existing records vs. new only?"
- Breaking API changes: "Version both vs. force upgrade?"
- UI redesign: "Replace immediately vs. opt-in beta?"

## Best Practices

### Make Questions Actionable

**Bad**:
```
Question: "What do you want?"
Options: "I don't know", "Whatever you think is best"
```

**Good**:
```
Question: "Where should the export button be placed?"
Options:
- "In the toolbar above the table" (Recommended)
- "As a dropdown in each row"
- "Both toolbar and row actions"
```

### Provide Context in Options

**Bad**:
```
Options:
- "Option A"
- "Option B"
- "Option C"
```

**Good**:
```
Options:
- "localStorage only" (Fast, client-side, no backend changes)
- "Database only" (Syncs across devices, requires backend)
- "Both" (Recommended - instant + persistent)
```

### Mark Recommended Defaults

Guide users toward best practices:
```
- "Settings page" (Recommended - standard location for preferences)
- "Header" (More visible but unconventional)
```

### Use Multi-Select When Appropriate

If options aren't mutually exclusive:
```
Question: "Which notification channels should be supported?"
MultiSelect: true
Options:
- "In-app notifications"
- "Email notifications"
- "Push notifications"
- "SMS notifications"
```

### Keep Headers Short

Headers display as chips/tags - max 12 characters:
- ✅ "Placement", "Storage", "Scope"
- ❌ "Where should it go", "How to store data"

## Question Sequencing

### Start with Critical Decisions

Order questions by impact on complexity/architecture:

1. **Scope** - Defines overall size/complexity
2. **Integration** - Affects architecture
3. **Data/persistence** - Affects backend changes
4. **UI/placement** - Affects user experience
5. **Edge cases** - Affects implementation details

### Use Conditional Questions

If answer to one question determines need for another:

```
Q1: "Scope of dark mode?"
Answer: "Entire application"

Q2 (follow-up): "Should we support per-component theme overrides?"
[Only asked if scope is "entire application"]
```

### Batch Related Questions

Ask multiple questions together when they're related:

```
AskUserQuestion:
  Questions:
    1. "Where should toggle be placed?" [Placement]
    2. "How should preference be stored?" [Persistence]
    3. "What's the scope?" [Coverage]
```

This is better than asking separately (fewer interruptions).

## Handling Answers

### Parse "Other" Responses

When user selects "Other" and provides custom text:
- Parse the text for intent
- Ask follow-up if still unclear
- Incorporate into structured requirements

### Validate Combinations

Some answer combinations may conflict:
```
If: Scope = "Entire application"
And: Storage = "No persistence"
Then: Warn - "Full-app dark mode without persistence means users must re-enable every session. Recommend adding persistence."
```

### Synthesize into Requirements

Convert answers into structured format:

**Questions**:
- Placement: "Settings page"
- Persistence: "Both localStorage + database"
- Scope: "Entire application"

**Synthesized Requirement**:
```
FEATURE: Implement dark mode toggle in Settings page with full application coverage.
- Toggle control in Settings → Appearance section
- Preference stored in localStorage for instant application
- Preference synced to user profile database for cross-device persistence
- All UI components and pages support dark theme
```

## Common Feature Categories & Key Questions

### Theme/Appearance Features
- Placement of toggle control?
- Persistence approach?
- Scope (all pages vs. specific)?
- System preference detection?

### CRUD Features
- Which entities/resources?
- Required fields vs. optional?
- Validation rules?
- Permissions/authorization?

### Search/Filter Features
- What can be searched?
- Search scope (global vs. local)?
- Filter options?
- Results display/pagination?

### Export/Import Features
- Format(s) supported?
- What data/scope?
- Client-side vs. server-side?
- File size limits?

### Notification Features
- Channels (in-app/email/push/SMS)?
- Trigger events?
- Frequency/batching?
- User preferences for opt-out?

### Authentication/Authorization Features
- Method (local/OAuth/SAML/SSO)?
- Integration with existing system?
- Session management approach?
- Password requirements?

### Integration Features
- Which external systems/APIs?
- Authentication for APIs?
- Error handling approach?
- Fallback behavior?

## Example: Complete Clarification Flow

**Input**: GitHub issue says "add CSV export"

**Agent Analysis**:
- Missing: What data? Where's the button? Format details?
- Critical gaps: Scope, placement, format options

**Questions Asked**:
```
Question 1: "What data should be exportable to CSV?"
Header: "Export Scope"
Options:
- "Current page/view only" (Recommended - simpler)
- "All data with current filters"
- "Entire dataset" (May need pagination/batching)

User Answer: "Current page/view only"

Question 2: "Where should the export button be placed?"
Header: "Placement"
Options:
- "Toolbar above the data table" (Recommended)
- "Dropdown menu"
- "Both toolbar and dropdown"

User Answer: "Toolbar above the data table"

Question 3: "Should the export include all columns or let users choose?"
Header: "Columns"
Options:
- "All visible columns" (Recommended - matches view)
- "All columns including hidden"
- "Let user select columns" (More flexible, more complex)

User Answer: "All visible columns"
```

**Structured Output**:
```markdown
## FEATURE
Add CSV export functionality to [data table/list].
- Export button in toolbar above data table
- Exports currently visible data (respects filters/pagination)
- Includes all visible columns in current view
- Filename: [entity-name]-export-YYYY-MM-DD.csv
- UTF-8 encoding with BOM for Excel compatibility

## EXAMPLES
1. User viewing filtered product list (50 items, 8 visible columns)
   - Clicks "Export CSV" button in toolbar
   - Browser downloads: products-export-2026-01-05.csv
   - File contains 50 rows + header row with 8 columns

2. User viewing single page of paginated results
   - Current page shows 25 of 500 total items
   - Export includes only 25 visible items
   - User can navigate pages and export separately if needed

## DOCUMENTATION
- Client-side CSV generation for small datasets (<10k rows)
- Server-side generation if dataset exceeds 10k rows
- UTF-8 with BOM for Excel compatibility
- RFC 4180 CSV format compliance

## OTHER CONSIDERATIONS
- No permissions needed (user can already view this data)
- Performance: Client-side OK for typical page sizes
- Testing: Verify special characters, commas, newlines in data
- Mobile: Download behavior varies by mobile browser
```

## Integration Points

### Used By
- `feature-issue-analyzer` agent when analyzing vague requirements
- Any agent needing to clarify user intent
- Planning agents that discover ambiguities

### Works With
- `AskUserQuestion` tool (the mechanism for asking)
- `mcp__sequentialthinking__sequentialthinking` (for analyzing when to ask)
- Requirements analysis workflows

### Provides
- Question templates and patterns
- Best practices for clarification
- Common feature category patterns
- Answer synthesis guidance
