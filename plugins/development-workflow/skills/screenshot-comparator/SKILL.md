---
name: screenshot-comparator
description: Create before/after screenshot comparisons for PRs and issues. Use when visual regression testing or UI change documentation is needed. Takes screenshots using Playwright at user-specified pages and viewports, comparing current branch against master. Manages git state safely, captures consistent screenshots, and creates formatted comparison comments on GitHub.
---

# Screenshot Comparator

Visual comparison specialist creating before/after screenshot documentation for PRs and issues.

## When to Use

- Visual regression testing for UI changes
- Documenting visual differences in PRs
- Validating CSS or layout changes
- Comparing responsive designs
- Creating visual change documentation

## Core Capabilities

1. **Screenshot Capture**: Automated screenshots using Playwright
2. **Git State Management**: Safe branch switching and restoration
3. **Comparison Generation**: Before/after visual comparisons
4. **GitHub Integration**: Formatted comments with screenshot uploads
5. **Multi-Viewport Support**: Desktop, mobile, tablet views

## Screenshot Comparison Process

### 1. Parse User Requirements

**Extract Information**:
- Target pages/routes to capture
- Required viewports (desktop, mobile, tablet)
- Base URL and port
- Target PR or issue number

**Example Request**:
"Create before/after screenshots for homepage and about page at desktop and mobile views for PR #123"

**Parsed**:
- Pages: `/`, `/about`
- Viewports: desktop (1920x1080), mobile (375x667)
- Target: PR #123

### 2. Capture Before Screenshots (Baseline)

**Git State Management**:
```bash
# Check for uncommitted changes
has_changes=$(git status --porcelain)

# Stash if needed
if [ -n "$has_changes" ]; then
    git stash push -m "screenshot-temp-$(date +%s)"
    stashed=true
fi

# Restore to master state
git restore . -s master
```

**Screenshot Capture**:
- Wait for dev server to reflect changes
- Take screenshots for each page/viewport
- Save with descriptive names: `before_{page}_{viewport}.png`
- Ensure consistent capture settings

### 3. Capture After Screenshots (Current)

**Restore Working State**:
```bash
# Restore to current state
git restore .

# Pop stash if created
if [ "$stashed" = true ]; then
    git stash pop
fi
```

**Screenshot Capture**:
- Wait for dev server to reflect current changes
- Take identical screenshots with same parameters
- Save with matching names: `after_{page}_{viewport}.png`
- Maintain consistency with before captures

### 4. Create Comparison Comment

**Upload Screenshots**:
- Upload all before/after screenshots to GitHub
- Get URLs for embedding in comments

**Generate Comment**:
- Create formatted before/after comparison
- Post to specified PR or issue

## Playwright Screenshot Usage

### Screenshot Parameters

**Viewport Sizes**:
- **Desktop**: 1920x1080 (standard desktop)
- **Tablet**: 768x1024 (iPad portrait)
- **Mobile**: 375x667 (iPhone SE)
- **Custom**: User-specified dimensions

**Capture Settings**:
- Full page screenshots or viewport-only
- Wait for network idle before capture
- Handle loading states properly
- Consistent timing between captures

### Example Playwright Calls

```typescript
// Desktop screenshot
await page.setViewportSize({ width: 1920, height: 1080 });
await page.goto(url);
await page.waitForLoadState('networkidle');
await page.screenshot({ path: 'before_homepage_desktop.png', fullPage: true });

// Mobile screenshot
await page.setViewportSize({ width: 375, height: 667 });
await page.goto(url);
await page.waitForLoadState('networkidle');
await page.screenshot({ path: 'before_homepage_mobile.png', fullPage: true });
```

## Git State Management

### Safe State Operations

**Before Baseline Capture**:
1. Check for uncommitted changes
2. Stash if necessary (with timestamp)
3. Restore to master branch state
4. Verify restoration successful
5. Wait for dev server reload

**After Baseline Capture**:
1. Restore to original working state
2. Pop stash if created
3. Verify restoration successful
4. Wait for dev server reload

### Error Handling

**Stash Failures**:
- Verify stash created successfully
- Handle conflicts on pop
- Provide clear error messages

**Restore Failures**:
- Check for untracked files
- Handle merge conflicts
- Ensure clean state before/after

## Comment Format

### Simple Before/After Layout

```markdown
## 📸 Before/After Screenshots

### Homepage
**Desktop (1920x1080)**
| Before | After |
|--------|-------|
| ![Before](before_homepage_desktop.png) | ![After](after_homepage_desktop.png) |

**Mobile (375x667)**
| Before | After |
|--------|-------|
| ![Before](before_homepage_mobile.png) | ![After](after_homepage_mobile.png) |

### About Page
**Desktop (1920x1080)**
| Before | After |
|--------|-------|
| ![Before](before_about_desktop.png) | ![After](after_about_desktop.png) |

**Mobile (375x667)**
| Before | After |
|--------|-------|
| ![Before](before_about_mobile.png) | ![After](after_about_mobile.png) |

---
_Screenshots taken from master vs current changes_
```

### Enhanced Layout with Annotations

```markdown
## 📸 Visual Regression Testing

### Summary
Comparing visual changes for:
- ✅ Homepage redesign
- ✅ About page layout update
- ⚠️ Note: Header styling changed intentionally

### Homepage

#### Desktop View (1920x1080)
<table>
  <tr>
    <th>Before (master)</th>
    <th>After (current)</th>
  </tr>
  <tr>
    <td><img src="before_homepage_desktop.png" width="400"/></td>
    <td><img src="after_homepage_desktop.png" width="400"/></td>
  </tr>
</table>

**Changes**:
- Updated hero section layout
- New call-to-action buttons
- Improved spacing and typography

#### Mobile View (375x667)
<table>
  <tr>
    <th>Before (master)</th>
    <th>After (current)</th>
  </tr>
  <tr>
    <td><img src="before_homepage_mobile.png" width="200"/></td>
    <td><img src="after_homepage_mobile.png" width="200"/></td>
  </tr>
</table>

**Changes**:
- Responsive navigation menu
- Optimized mobile layout
- Touch-friendly button sizes

---
_Automated visual regression testing via Playwright_
```

## Naming Convention

### Screenshot Files

**Pattern**: `{stage}_{page}_{viewport}.png`

**Components**:
- `stage`: "before" or "after"
- `page`: Sanitized page name (remove slashes, special chars)
- `viewport`: "desktop", "mobile", "tablet", or custom

**Examples**:
- `before_homepage_desktop.png`
- `after_about_mobile.png`
- `before_products_list_tablet.png`

### Page Name Sanitization

```bash
# Convert /products/list to products_list
page_name=$(echo "$page" | sed 's|/|_|g' | sed 's|^_||')

# Handle home page
if [ "$page" == "/" ]; then
    page_name="homepage"
fi
```

## Workflow Example

### Complete Process

```bash
# 1. Parse requirements
pages=("/" "/about")
viewports=("desktop:1920x1080" "mobile:375x667")
pr_number=123

# 2. Save current state
git stash push -m "screenshot-temp-$(date +%s)"

# 3. Capture baseline (master)
git restore . -s master
sleep 2  # Wait for dev server reload

for page in "${pages[@]}"; do
  for viewport in "${viewports[@]}"; do
    # Capture screenshot
    playwright screenshot --url "http://localhost:3000$page" \
      --viewport "$viewport" \
      --output "before_${page}_${viewport}.png"
  done
done

# 4. Restore and capture current
git restore .
git stash pop
sleep 2  # Wait for dev server reload

for page in "${pages[@]}"; do
  for viewport in "${viewports[@]}"; do
    # Capture screenshot
    playwright screenshot --url "http://localhost:3000$page" \
      --viewport "$viewport" \
      --output "after_${page}_${viewport}.png"
  done
done

# 5. Upload and create comment
# Upload screenshots to GitHub
# Generate markdown comment
# Post to PR #123
```

## Best Practices

### Screenshot Quality

- Use consistent viewport sizes
- Wait for page load completion
- Handle dynamic content appropriately
- Capture full page when relevant
- Maintain aspect ratios

### Comparison Clarity

- Use side-by-side layout
- Label clearly (before/after)
- Include viewport information
- Add annotations for significant changes
- Provide context in comments

### Git Safety

- Always check for uncommitted changes
- Use timestamped stash names
- Verify restorations successful
- Handle errors gracefully
- Clean up temporary artifacts

### Performance

- Batch screenshot captures efficiently
- Reuse browser instances
- Minimize dev server reloads
- Cache unchanged screenshots
- Optimize upload sizes

## Error Handling

### Common Issues

**Dev Server Not Ready**:
- Wait for server startup
- Verify port availability
- Check for startup errors
- Increase wait times if needed

**Git State Conflicts**:
- Resolve stash conflicts
- Handle untracked files
- Clean working directory
- Provide clear error messages

**Screenshot Failures**:
- Retry on timeout
- Handle page load errors
- Verify URL accessibility
- Check Playwright installation

## Integration with Other Skills

- **pr-creator**: Enhance PRs with visual documentation
- **code-reviewer**: Support visual regression review
- **senior-engineer**: Validate UI implementation

## Quality Checklist

Before posting comparison:

- [ ] All screenshots captured successfully
- [ ] Before/after pairs match (same pages/viewports)
- [ ] Git state restored correctly
- [ ] Screenshots uploaded to GitHub
- [ ] Comment formatted properly
- [ ] Annotations added for clarity
- [ ] No temporary files left behind
- [ ] Dev server returned to normal state

## Anti-Patterns to Avoid

- Taking screenshots without waiting for page load
- Inconsistent viewport sizes between before/after
- Not handling git state safely
- Forgetting to restore working state
- Missing error handling
- Poor naming conventions
- Unclear comparison layout
- Not documenting intentional changes
