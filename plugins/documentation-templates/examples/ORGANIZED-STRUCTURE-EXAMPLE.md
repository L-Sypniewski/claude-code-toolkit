# Example: Organized AGENTS.md Structure

This example demonstrates how to organize a large AGENTS.md file using nested structure and modular references.

## Scenario

Project: Full-stack web application with backend (Node.js), frontend (React), and comprehensive testing.

**Original State:**
- Single AGENTS.md: 1200 lines
- Mixed backend, frontend, and testing details
- Difficult to find specific information
- High context window consumption

**Organized State:**
- Root AGENTS.md: 250 lines (overview + references)
- backend/AGENTS.md: 300 lines (backend specifics)
- frontend/AGENTS.md: 350 lines (frontend specifics)
- docs/testing-guide.md: 400 lines (detailed testing)
- docs/deployment.md: 200 lines (deployment procedures)

**Result:** 60-75% context window reduction in typical usage

---

## Root AGENTS.md (250 lines)

```markdown
# MyApp - Development Guide

## TL;DR
- **Stack**: Node.js backend, React frontend, PostgreSQL, Jest/React Testing Library
- **Structure**: Monorepo with backend/ and frontend/ subdirectories
- **Quality Gates**: Build, test, and lint must pass before completion

## Quick Links
- [Backend Instructions](backend/AGENTS.md) - Node.js API server
- [Frontend Instructions](frontend/AGENTS.md) - React SPA
- [Testing Guide](docs/testing-guide.md) - Comprehensive testing patterns
- [Deployment Guide](docs/deployment.md) - CI/CD and deployment procedures
- [Architecture Details](docs/architecture.md) - System architecture and design decisions

## Repository Structure

```
/
├── AGENTS.md                    # This file - overview and general standards
├── backend/                     # Node.js API
│   ├── AGENTS.md                # Backend-specific instructions
│   └── src/
├── frontend/                    # React SPA
│   ├── AGENTS.md                # Frontend-specific instructions
│   └── src/
├── docs/
│   ├── architecture.md          # Architecture details
│   ├── testing-guide.md         # Testing patterns and standards
│   └── deployment.md            # Deployment procedures
└── package.json
```

## General Coding Standards

**Core Principles:**
- SOLID, KISS, YAGNI
- Consistency over innovation
- Favor descriptive names over comments
- Async/await for all I/O operations

**For detailed conventions:**
- Backend: See [backend/AGENTS.md](backend/AGENTS.md#coding-conventions)
- Frontend: See [frontend/AGENTS.md](frontend/AGENTS.md#coding-conventions)

## Quality Gates ✅

### Full Stack Build & Test
```bash
# From root
npm run build        # Build both backend and frontend
npm test             # Run all tests
npm run lint         # Lint all code
```

### Component-Specific
- Backend: See [backend/AGENTS.md](backend/AGENTS.md#quality-gates)
- Frontend: See [frontend/AGENTS.md](frontend/AGENTS.md#quality-gates)

## Testing Overview

- **Backend**: Jest for API and integration tests
- **Frontend**: Jest + React Testing Library for components
- **E2E**: Playwright for end-to-end workflows

**For comprehensive testing guidelines:** See [docs/testing-guide.md](docs/testing-guide.md)

## Deployment

- **Environment**: AWS (ECS for backend, S3/CloudFront for frontend)
- **CI/CD**: GitHub Actions
- **Process**: Automated on merge to main

**For detailed procedures:** See [docs/deployment.md](docs/deployment.md)

## Working with Subprojects

When working in backend/ or frontend/:
1. The local AGENTS.md provides component-specific context
2. Refer back to this root file for general standards
3. Both contexts are automatically merged by AI agents

## Agent Workflow Tips

- Run tests in the specific component you're working on first
- Use component-specific commands (see subproject AGENTS.md files)
- Update the relevant AGENTS.md when adding new patterns or commands
```

---

## backend/AGENTS.md (300 lines)

```markdown
# Backend - Development Guide

> **Note:** Inherits general standards from root [AGENTS.md](../AGENTS.md)

## TL;DR
- **Stack**: Node.js 20, Express, PostgreSQL, Jest
- **Testing**: Jest for unit and integration tests
- **Key Commands**: `npm run dev`, `npm test`, `npm run lint`

## Setup

```bash
cd backend
npm install
cp .env.example .env
npm run db:migrate
```

## Running

```bash
npm run dev          # Start dev server (hot reload)
npm run dev:debug    # Start with debugger
npm start            # Start production server
```

## Quality Gates ✅

```bash
npm run build        # TypeScript compilation
npm test             # Run tests
npm run lint         # ESLint
npm run type-check   # TypeScript type checking
```

All must pass before completing work on backend.

## Backend-Specific Coding Conventions

### API Design
- RESTful endpoints
- Use standard HTTP methods (GET, POST, PUT, DELETE)
- Return consistent error responses
- Use middleware for authentication

### Database Access
- Use repository pattern
- Always use parameterized queries
- Handle connection errors gracefully
- Close connections in finally blocks

### Error Handling
```typescript
// Standard error response format
{
  error: {
    message: "User-friendly message",
    code: "ERROR_CODE",
    details: { /* additional context */ }
  }
}
```

### Logging
- Use Winston logger
- Log levels: error, warn, info, debug
- Include request ID in all logs
- Never log sensitive data (passwords, tokens)

### Async Patterns
```typescript
// Always use async/await, not callbacks
async function getUserById(id: string): Promise<User> {
  try {
    return await userRepository.findById(id);
  } catch (error) {
    logger.error('Error fetching user', { id, error });
    throw new NotFoundError(`User ${id} not found`);
  }
}
```

## Testing Patterns

### Unit Tests
```typescript
describe('UserService', () => {
  it('should create user with valid data', async () => {
    const userData = { email: 'test@example.com', name: 'Test' };
    const user = await userService.create(userData);
    expect(user).toHaveProperty('id');
    expect(user.email).toBe(userData.email);
  });
});
```

### Integration Tests
- Use Testcontainers for PostgreSQL
- Reset database between tests
- Test full request/response cycle

**For comprehensive testing guidelines:** See [../docs/testing-guide.md](../docs/testing-guide.md#backend-testing)

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user

### Users
- `GET /api/users` - List users
- `GET /api/users/:id` - Get user by ID
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user

## See Also
- [Root AGENTS.md](../AGENTS.md) - General project standards
- [Frontend AGENTS.md](../frontend/AGENTS.md) - Frontend instructions
- [Testing Guide](../docs/testing-guide.md) - Detailed testing patterns
- [API Documentation](../docs/api-documentation.md) - Complete API reference
```

---

## frontend/AGENTS.md (350 lines)

```markdown
# Frontend - Development Guide

> **Note:** Inherits general standards from root [AGENTS.md](../AGENTS.md)

## TL;DR
- **Stack**: React 18, TypeScript, Vite, TailwindCSS, React Query
- **Testing**: Jest + React Testing Library
- **Key Commands**: `npm run dev`, `npm test`, `npm run build`

## Setup

```bash
cd frontend
npm install
cp .env.example .env
```

## Running

```bash
npm run dev          # Start dev server (http://localhost:5173)
npm run build        # Build for production
npm run preview      # Preview production build
```

## Quality Gates ✅

```bash
npm run build        # Vite build
npm test             # Run tests
npm run lint         # ESLint
npm run type-check   # TypeScript type checking
npm run format:check # Prettier formatting
```

All must pass before completing work on frontend.

## Frontend-Specific Coding Conventions

### Component Structure
```typescript
// Use functional components with hooks
import { useState, useEffect } from 'react';
import { useQuery } from '@tanstack/react-query';

interface UserProfileProps {
  userId: string;
}

export function UserProfile({ userId }: UserProfileProps) {
  const { data: user, isLoading } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  if (isLoading) return <LoadingSpinner />;
  if (!user) return <NotFound />;

  return (
    <div className="user-profile">
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

### File Organization
```
src/
├── components/          # Reusable components
│   ├── ui/              # Base UI components (Button, Input, etc.)
│   └── features/        # Feature-specific components
├── pages/               # Page components (one per route)
├── hooks/               # Custom hooks
├── api/                 # API client functions
├── utils/               # Utility functions
└── types/               # TypeScript type definitions
```

### State Management
- **Local State**: useState for component-only state
- **Server State**: React Query for API data
- **Global State**: Context API for auth, theme, etc.
- **Form State**: React Hook Form for forms

### Styling
- **Primary**: TailwindCSS utility classes
- **Components**: Shadcn/ui component library
- **Custom**: CSS modules for complex styles
- **Dark Mode**: Use Tailwind dark: variants

```tsx
// Example with TailwindCSS
<button className="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg">
  Click Me
</button>
```

### TypeScript Usage
- Always define prop interfaces
- Use strict mode
- Avoid `any` type
- Use generics for reusable components

### API Integration
```typescript
// Use React Query for API calls
import { useMutation, useQueryClient } from '@tanstack/react-query';

function useCreateUser() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (userData: CreateUserData) => api.users.create(userData),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });
}
```

## Testing Patterns

### Component Tests
```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { UserProfile } from './UserProfile';

describe('UserProfile', () => {
  it('renders user information', async () => {
    render(<UserProfile userId="123" />);
    
    expect(await screen.findByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });

  it('handles user not found', async () => {
    render(<UserProfile userId="invalid" />);
    
    expect(await screen.findByText('User not found')).toBeInTheDocument();
  });
});
```

### Hook Tests
```typescript
import { renderHook, waitFor } from '@testing-library/react';
import { useUser } from './useUser';

describe('useUser', () => {
  it('fetches user data', async () => {
    const { result } = renderHook(() => useUser('123'));
    
    await waitFor(() => expect(result.current.isSuccess).toBe(true));
    expect(result.current.data).toHaveProperty('name');
  });
});
```

**For comprehensive testing guidelines:** See [../docs/testing-guide.md](../docs/testing-guide.md#frontend-testing)

## Accessibility

- Use semantic HTML elements
- Include ARIA labels when needed
- Test keyboard navigation
- Ensure color contrast meets WCAG AA
- Use react-aria for complex interactive components

## Performance

- Lazy load routes with React.lazy()
- Memoize expensive computations with useMemo
- Optimize images (WebP format, responsive sizes)
- Use React Query caching effectively
- Monitor bundle size with vite-plugin-inspect

## See Also
- [Root AGENTS.md](../AGENTS.md) - General project standards
- [Backend AGENTS.md](../backend/AGENTS.md) - Backend API reference
- [Testing Guide](../docs/testing-guide.md) - Detailed testing patterns
- [Component Library](../docs/component-library.md) - UI component documentation
```

---

## docs/testing-guide.md (400 lines)

```markdown
# Testing Guide

> **Note:** Referenced from [AGENTS.md](../AGENTS.md)

This document provides comprehensive testing guidelines for the entire project.

## Testing Philosophy

- **Test Behavior, Not Implementation**: Focus on what the code does, not how it does it
- **Write Tests First**: TDD when possible, at minimum test immediately after implementation
- **Favor Integration Over Unit**: Test real collaborations, avoid excessive mocking
- **Maintainable Tests**: Tests should be easy to understand and update
- **Fast Feedback**: Tests should run quickly for rapid iteration

## Test Structure

All tests follow AAA pattern:

```typescript
describe('Feature', () => {
  it('should do something', () => {
    // Arrange - Set up test data and conditions
    const input = createTestData();
    
    // Act - Perform the action being tested
    const result = performAction(input);
    
    // Assert - Verify the outcome
    expect(result).toBe(expected);
  });
});
```

## Backend Testing

### Unit Tests

Test individual functions and methods in isolation:

```typescript
describe('UserService.validateEmail', () => {
  it('should accept valid email', () => {
    expect(validateEmail('test@example.com')).toBe(true);
  });

  it('should reject invalid email', () => {
    expect(validateEmail('invalid')).toBe(false);
  });
});
```

### Integration Tests

Test multiple components working together:

```typescript
describe('User API Integration', () => {
  let db: TestDatabase;
  let api: TestApiClient;

  beforeAll(async () => {
    db = await createTestDatabase();
    api = createApiClient();
  });

  afterAll(async () => {
    await db.cleanup();
  });

  it('should create and retrieve user', async () => {
    // Create user
    const createResponse = await api.post('/api/users', {
      email: 'test@example.com',
      name: 'Test User'
    });
    expect(createResponse.status).toBe(201);
    
    const userId = createResponse.data.id;
    
    // Retrieve user
    const getResponse = await api.get(`/api/users/${userId}`);
    expect(getResponse.status).toBe(200);
    expect(getResponse.data.email).toBe('test@example.com');
  });
});
```

### Database Tests

Use Testcontainers for real PostgreSQL:

```typescript
import { PostgreSqlContainer } from 'testcontainers';

describe('UserRepository', () => {
  let container: PostgreSqlContainer;
  let repository: UserRepository;

  beforeAll(async () => {
    container = await new PostgreSqlContainer().start();
    const db = await createDatabase(container.getConnectionUri());
    repository = new UserRepository(db);
  });

  afterAll(async () => {
    await container.stop();
  });

  it('should find user by email', async () => {
    await repository.create({ email: 'test@example.com', name: 'Test' });
    const user = await repository.findByEmail('test@example.com');
    expect(user).toBeDefined();
  });
});
```

## Frontend Testing

### Component Tests

Test React components with React Testing Library:

```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { UserList } from './UserList';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } }
  });
  
  return ({ children }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('UserList', () => {
  it('renders list of users', async () => {
    render(<UserList />, { wrapper: createWrapper() });
    
    expect(await screen.findByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('Jane Smith')).toBeInTheDocument();
  });

  it('filters users by search term', async () => {
    render(<UserList />, { wrapper: createWrapper() });
    
    const searchInput = screen.getByPlaceholderText('Search users...');
    fireEvent.change(searchInput, { target: { value: 'John' } });
    
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
      expect(screen.queryByText('Jane Smith')).not.toBeInTheDocument();
    });
  });
});
```

### Hook Tests

Test custom hooks:

```typescript
import { renderHook, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useUsers } from './useUsers';

const createWrapper = () => {
  const queryClient = new QueryClient();
  return ({ children }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('useUsers', () => {
  it('fetches users on mount', async () => {
    const { result } = renderHook(() => useUsers(), {
      wrapper: createWrapper()
    });
    
    expect(result.current.isLoading).toBe(true);
    
    await waitFor(() => {
      expect(result.current.isSuccess).toBe(true);
      expect(result.current.data).toHaveLength(2);
    });
  });
});
```

### Accessibility Tests

Use jest-axe for accessibility testing:

```typescript
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { UserProfile } from './UserProfile';

expect.extend(toHaveNoViolations);

describe('UserProfile Accessibility', () => {
  it('should have no accessibility violations', async () => {
    const { container } = render(<UserProfile userId="123" />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
```

## E2E Testing

Use Playwright for end-to-end tests:

```typescript
import { test, expect } from '@playwright/test';

test.describe('User Management', () => {
  test('should create new user', async ({ page }) => {
    await page.goto('/users');
    
    await page.click('button:has-text("Add User")');
    await page.fill('input[name="email"]', 'newuser@example.com');
    await page.fill('input[name="name"]', 'New User');
    await page.click('button:has-text("Save")');
    
    await expect(page.locator('text=New User')).toBeVisible();
  });

  test('should validate required fields', async ({ page }) => {
    await page.goto('/users');
    
    await page.click('button:has-text("Add User")');
    await page.click('button:has-text("Save")');
    
    await expect(page.locator('text=Email is required')).toBeVisible();
  });
});
```

## Mocking Strategies

### API Mocking

Use MSW (Mock Service Worker) for API mocking:

```typescript
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json([
      { id: '1', name: 'John Doe', email: 'john@example.com' },
      { id: '2', name: 'Jane Smith', email: 'jane@example.com' }
    ]));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

### Minimal Mocking

Prefer real implementations:

```typescript
// ❌ Don't: Mock everything
jest.mock('./userRepository');
jest.mock('./emailService');
jest.mock('./logger');

// ✅ Do: Use real implementations
const repository = new UserRepository(testDb);
const emailService = new FakeEmailService(); // Test double
const logger = createNullLogger(); // Silent logger for tests
```

## Test Coverage

- Aim for 80% code coverage
- Focus on critical paths and edge cases
- Don't chase 100% coverage at expense of test quality

## Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage

# Run specific test file
npm test UserService.test.ts

# Run tests matching pattern
npm test -- --testNamePattern="should create user"
```

## Best Practices

### DO
✅ Test user-visible behavior
✅ Use descriptive test names
✅ Keep tests independent
✅ Clean up after tests
✅ Use real data when possible
✅ Test error cases

### DON'T
❌ Test implementation details
❌ Share state between tests
❌ Mock everything
❌ Write brittle tests
❌ Ignore flaky tests
❌ Skip error scenarios

## Common Pitfalls

### Async Issues
```typescript
// ❌ Wrong: Missing await
it('should fetch user', () => {
  const user = fetchUser('123');
  expect(user.name).toBe('John');
});

// ✅ Correct: Use async/await
it('should fetch user', async () => {
  const user = await fetchUser('123');
  expect(user.name).toBe('John');
});
```

### Race Conditions
```typescript
// ❌ Wrong: No waiting for update
fireEvent.click(saveButton);
expect(screen.getByText('Saved')).toBeInTheDocument();

// ✅ Correct: Wait for update
fireEvent.click(saveButton);
await waitFor(() => {
  expect(screen.getByText('Saved')).toBeInTheDocument();
});
```

## See Also
- [Root AGENTS.md](../AGENTS.md) - General project overview
- [Backend AGENTS.md](../backend/AGENTS.md) - Backend testing specifics
- [Frontend AGENTS.md](../frontend/AGENTS.md) - Frontend testing specifics
- [CI/CD Guide](./deployment.md) - Automated testing in CI
```

---

## Summary

This organized structure provides:

✅ **Context Window Efficiency**: 60-75% reduction (250 lines root vs 1200 lines original)
✅ **Clear Navigation**: Quick links to all relevant documentation
✅ **Subproject Isolation**: Separate AGENTS.md for backend and frontend
✅ **Detailed References**: Comprehensive guides extracted to docs/
✅ **Maintainability**: Easy to update specific sections without affecting others
✅ **Agent Efficiency**: Agents load only relevant context for current location

**Usage Pattern:**
- Working on root-level concerns → Load root AGENTS.md (250 lines)
- Working in backend → Load backend/AGENTS.md (300 lines) + root context
- Working in frontend → Load frontend/AGENTS.md (350 lines) + root context
- Need testing details → Reference docs/testing-guide.md (400 lines)
- Need deployment info → Reference docs/deployment.md (200 lines)

**Result:** Agents consume 200-500 lines instead of 1200 lines in typical scenarios.
