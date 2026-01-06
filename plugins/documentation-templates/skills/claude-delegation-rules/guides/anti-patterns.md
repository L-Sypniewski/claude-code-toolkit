# Delegation Anti-Patterns

Common mistakes to avoid when delegating between agents.

## ❌ Circular Delegation

```
Agent A → Agent B → Agent C → Agent A  (infinite loop)
```

**Problem**: Agents pass work back and forth indefinitely

**Fix**: Clear ownership and final decision maker

---

## ❌ Over-Delegation

```
Agent delegates every tiny decision
```

**Problem**: Too much overhead, slower execution, context switching

**Fix**: Delegate only when specialized expertise needed

**Rule of thumb**: If you can handle it in 2-3 steps, don't delegate

---

## ❌ Under-Context

```
@agent: "Please help"  (no context provided)
```

**Problem**: Receiving agent can't do effective work

**Fix**: Provide comprehensive context with every delegation:
- What you're trying to accomplish
- What you've tried
- Specific questions
- Success criteria

---

## ❌ Ambiguous Boundaries

```
Both Agent A and Agent B think they're responsible for task X
```

**Problem**: Duplicate work, conflicting outputs, confusion

**Fix**: Document clear responsibility boundaries in agent descriptions

**Example**:
```yaml
# senior-engineer.md
## When to Use
- Implementing new features
- Fixing bugs

## When NOT to Use
- High-level architecture decisions (use technical-architecture-advisor)
```

---

## ❌ Fire and Forget

```
Agent delegates and never checks outcome
```

**Problem**: No verification, broken workflows, lost context

**Fix**: Always verify delegation completed successfully before proceeding

---

## ❌ Context Hoarding

```
Agent keeps all context, delegates task without background
```

**Problem**: Receiving agent lacks info to do good work

**Fix**: Share relevant context, files, and constraints

---

## Self-Check Questions

Before delegating, ask:
1. Is specialized expertise truly needed?
2. Have I provided enough context?
3. Is it clear what success looks like?
4. Will I check the outcome before proceeding?
5. Are responsibility boundaries clear?
