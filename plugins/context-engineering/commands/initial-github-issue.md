---
description: Transform a GitHub issue to follow the INITIAL.md format for context engineering workflow
argument-hint: <github-issue-url>
---

# Format GitHub Issue for Context Engineering

## GitHub Issue URL: $ARGUMENTS

Transform a GitHub issue to follow the INITIAL.md format for context engineering workflow.

```initial.md
## FEATURE:

[Insert your feature here]

## EXAMPLES:

[Provide and explain examples that you have in the `examples/` folder]

## DOCUMENTATION:

[List out any documentation (web pages, sources for an MCP server like Crawl4AI RAG, etc.) that will need to be referenced during development]

## OTHER CONSIDERATIONS:

[Any other considerations or specific requirements - great place to include gotchas that you see AI coding assistants miss with your projects a lot]
```

## CRITICAL: Follow INITIAL.md Best Practices

When executing this command, you MUST follow these specific rules:

### FEATURE Section Rules

- ❌ **NEVER write vague descriptions** like "Build a web scraper" or "Create a contact form"
- ✅ **ALWAYS be specific and comprehensive** like "Build an async web scraper using BeautifulSoup that extracts product data from e-commerce sites, handles rate limiting, and stores results in PostgreSQL"
- Include specific technologies, libraries, and integration points
- Define exact functionality, validation, error handling, and UX requirements

### EXAMPLES Section Rules

- **Leverage the examples/ folder** - always check for relevant patterns
- **Provide specific file references** - not generic descriptions
- **Explain what aspects to mimic** - styling, validation, state management, etc.
- Reference existing components in the REWOS codebase that follow similar patterns

### DOCUMENTATION Section Rules

- **Include ALL relevant resources** with direct URLs
- API documentation with specific section links
- Library guides (Astro.js, React, Zod, Cloudflare Workers, etc.)
- MCP server documentation when applicable
- Database schemas (Strapi content types)

### OTHER CONSIDERATIONS Rules

- **Capture project-specific details** that AI agents commonly miss
- Authentication requirements, API keys, permissions
- Rate limits and quotas (especially Cloudflare Workers constraints)
- Performance requirements (Lighthouse scores, Core Web Vitals)
- Common pitfalls specific to REWOS architecture
- Browser compatibility and accessibility requirements

### CRITICAL: Ask for Missing Information - Never Assume

**When information is missing or unclear, STOP and ask for clarification:**

- ❌ **NEVER make assumptions** about missing requirements
- ❌ **NEVER fill in blanks** with generic or guessed information
- ✅ **ALWAYS ask specific questions** to get missing details
- ✅ **IDENTIFY gaps** and request clarification before proceeding

**Common areas that need clarification:**

- **User interactions**: What exactly should happen when user does X?
- **Data sources**: Where does the data come from? What's the schema?
- **Integration requirements**: How should this connect to existing systems?
- **Performance constraints**: Are there specific speed/size requirements?
- **Validation rules**: What are the exact validation requirements?
- **Error scenarios**: How should errors be handled and displayed?
- **Responsive behavior**: How should this work across different screen sizes?
- **Authentication/permissions**: Who can access this feature and how?

**Ask questions like:**

- "The issue mentions 'form validation' - what specific validation rules are needed?"
- "You mentioned 'data processing' - what's the expected data format and source?"
- "For the responsive design - are there specific breakpoint requirements?"
- "What authentication method should be used for this feature?"
- "Are there specific performance or accessibility requirements?"

## Process

1. **Extract Issue Information**

   - Parse the GitHub issue URL to get owner, repo, and issue number
   - Fetch the current issue content using GitHub MCP
   - Preserve the original issue description

2. **Analyze Issue for Completeness**

   - Analyze the original issue description for specificity and completeness
   - **CRITICAL: Identify missing or unclear information**
   - Check for gaps in user interactions, data sources, validation rules, etc.
   - **If information is missing: STOP and ask specific clarifying questions**
   - Only proceed once all necessary details are clarified

3. **Enhance Issue Content (Only After Clarification)**

   - Transform vague requirements into specific, comprehensive descriptions
   - Research the codebase for relevant patterns and examples
   - Identify documentation and resources needed for implementation
   - Determine project-specific constraints and potential pitfalls

4. **Create Context Engineering Format**

   - Add a comment to the GitHub issue with the enhanced, formatted content
   - Use the INITIAL.md structure with best practices:
     - **FEATURE**: Specific, comprehensive functionality description (not vague)
     - **EXAMPLES**: Concrete file references from examples/ and existing codebase
     - **DOCUMENTATION**: Complete list of URLs for APIs, libraries, guides
     - **OTHER CONSIDERATIONS**: Authentication, performance, pitfalls, constraints

5. **GitHub MCP Integration**
   - Use the GitHub MCP server to add a formatted comment to the issue
   - Preserve original content by keeping it intact in the issue description
   - The formatted comment becomes the context engineering specification

## Implementation Steps

1. **Parse Issue URL**

   ```
   Extract: owner, repo, issue_number from URL pattern:
   https://github.com/{owner}/{repo}/issues/{issue_number}
   ```

2. **Fetch Issue Content**

   ```
   Use GitHub MCP to get issue title and body content
   ```

3. **Generate Formatted Comment**

   ```
   Create a comment with this template following INITIAL.md best practices:

   ---
   # Context Engineering Specification

   ## FEATURE
   **Transform the original issue description to be specific and comprehensive:**

   ❌ Avoid: Vague descriptions like "Build a contact form"
   ✅ Provide: "Build an async contact form component for Astro.js that validates email/phone fields using Zod schemas, integrates with Cloudflare Workers for submission processing, handles spam protection with Turnstile, and provides real-time validation feedback with accessible error messages"

   **Requirements:**
   - Include specific technologies and libraries to be used
   - Define exact functionality and behavior
   - Specify integration points with existing REWOS architecture
   - Detail validation, error handling, and user experience requirements

   ## EXAMPLES
   **Leverage the examples/ folder and existing codebase patterns:**

   - **Specific file references:** `examples/[relevant-pattern]/[file].tsx`
   - **Existing components to follow:** `astro/src/components/[ComponentName]/`
   - **Pattern explanations:** What aspects should be mimicked (styling, validation, state management)
   - **Architecture patterns:** Reference similar implementations in the codebase

   **Example format:**
   ```

   Follow the pattern established in:

   - `astro/src/components/ContactForm.astro` for form structure
   - `examples/form-validation/zod-schema.ts` for validation patterns
   - `astro/src/utils/component-to-html.ts` for HTML generation patterns

   ```

   ## DOCUMENTATION
   **Include ALL relevant resources with specific URLs:**

   - **API Documentation:** Direct links to relevant API sections
   - **Library Guides:** Astro.js, React, Zod, Cloudflare Workers documentation
   - **MCP Server Documentation:** If using GitHub, Playwright, or other MCP servers
   - **Database Schemas:** Strapi content type definitions
   - **Deployment Docs:** Cloudflare Pages/Workers specific documentation

   **Example format:**
   ```

   - Astro Forms: https://docs.astro.build/en/guides/server-side-rendering/#form-actions
   - Zod Validation: https://zod.dev/?id=basic-usage
   - Cloudflare Workers: https://developers.cloudflare.com/workers/runtime-apis/request/
   - Strapi API: https://docs.strapi.io/dev-docs/api/rest

   ```

   ## OTHER CONSIDERATIONS
   **Capture important implementation details:**

   - **Authentication Requirements:** API keys, user sessions, permissions
   - **Rate Limits/Quotas:** Cloudflare Workers limits, API rate limits
   - **Common Pitfalls:** REWOS-specific gotchas that AI agents commonly miss
   - **Performance Requirements:** Bundle size, loading time, Core Web Vitals impact
   - **Browser Compatibility:** Specific browser support requirements
   - **Accessibility:** WCAG compliance, screen reader support
   - **Responsive Design:** Breakpoint-specific behavior, container queries usage
   - **Integration Constraints:** How this affects existing Astro/Strapi integration

   **Example format:**
   ```

   - Cloudflare Workers have 10ms CPU time limit for form processing
   - Must use CSS container queries (not viewport queries) for responsive behavior
   - REWOS project requires Lighthouse score >95 - optimize for Core Web Vitals
   - Form validation must work without JavaScript (progressive enhancement)
   - Spam protection: Use Turnstile, not reCAPTCHA (brand consistency)

   ```

   ---
   *This comment contains the context engineering specification for this feature following INITIAL.md best practices.*
   ```

4. **Add Comment to Issue**
   ```
   Use GitHub MCP to post the formatted comment to the issue
   ```

## Expected Outcome

### If Issue Has Complete Information:

- Original issue description remains unchanged
- New comment contains the INITIAL.md formatted specification
- Comment can be referenced by the `generate-prp` command
- Workflow can proceed with GitHub issue as the source of truth

### If Issue Has Missing Information:

- **Command pauses and asks for clarification** with specific questions
- User provides missing details in response
- **Only then** proceeds to create the formatted comment
- Ensures comprehensive context before moving to PRP generation

**Key Principle**: Better to ask questions upfront than implement based on assumptions.

## Error Handling

- Validate GitHub URL format
- Check if issue exists and is accessible
- Handle authentication errors gracefully
- Provide clear feedback if formatting fails

## Usage Example

```
/initial-github-issue https://github.com/owner/repo/issues/123
```

This will fetch issue #123, analyze its content, and add a formatted comment following the context engineering principles.

## Additional instructions

Use sequential thinking, context7 MCPs to solve the problem using latest documentation and best practices. Ultrathink the approach and a plan.
