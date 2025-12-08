---
name: claude-delegation-rules
description: Agent delegation patterns for Claude Code. Use when designing agent systems or delegation workflows.
---

# Claude Delegation Rules

## Core Principles

1. **Single Responsibility**: Each agent has clear, focused purpose
2. **Explicit Activation**: Clear triggers (e.g., "Use PROACTIVELY for implement, fix, refactor")
3. **Clear Boundaries**: Define when to use and when NOT to use

## Delegation Patterns

1. **One-Way Handoff**: Agent completes work, hands off to next (sequential workflows)
2. **Consultation**: Agent seeks advice, then continues (specialized knowledge needed)
3. **Parallel Execution**: Multiple agents work simultaneously (independent tasks)
4. **Iterative Refinement**: Agent delegates, receives feedback, iterates (quality refinement)

## Context Handoff

**Include**: Purpose, current state, specific questions, success criteria, relevant files, constraints.
**Exclude**: Unnecessary history, unrelated code, ambiguous requirements.

## Agent Coordination

Use shared files (e.g., `.plans/feature-implementation.md`) to track multi-agent workflow status.

**Start**: @agent-name with task, context, deliverables, timeline.
**Complete**: Status, summary, deliverables, next steps, blockers.

## Anti-Patterns

- **Circular Delegation**: A→B→C→A (Fix: clear ownership)
- **Over-Delegation**: Delegating tiny decisions (Fix: delegate only for specialized expertise)
- **Under-Context**: No context provided (Fix: provide comprehensive context)
- **Ambiguous Boundaries**: Unclear responsibilities (Fix: document boundaries)

## Agent Types

- **Proactive**: Activates automatically (e.g., "Use PROACTIVELY for implement, fix")
- **Reactive**: Activates when requested
- **Coordinator**: Manages multi-agent workflows

## Verification

Test: clear activation, proper context, appropriate delegation, no loops, clean handoffs.
