---
name: refactoring-patterns
description: Common refactoring patterns and techniques for improving code quality, reducing complexity, and enhancing maintainability. Use when planning or executing code refactoring.
---

# Refactoring Patterns

This skill provides proven patterns for safe, effective code refactoring.

## Core Refactoring Principles

1. **Red-Green-Refactor**: Ensure tests pass before and after refactoring
2. **Small Steps**: Make incremental changes, commit frequently
3. **One Thing at a Time**: Refactor OR add features, not both
4. **Maintain Behavior**: External behavior stays the same

## Common Code Smells

### Long Method

**Smell**: Method exceeds 20-30 lines or does too many things

**Refactor**: Extract Method

```javascript
// Before
function processOrder(order) {
  // Validate
  if (!order.items || order.items.length === 0) {
    throw new Error('No items');
  }
  // Calculate
  let total = 0;
  for (let item of order.items) {
    total += item.price * item.quantity;
  }
  // Apply discount
  if (order.customer.vip) {
    total *= 0.9;
  }
  // Save
  database.save(order);
  return total;
}

// After
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order);
  saveOrder(order);
  return total;
}

function validateOrder(order) {
  if (!order.items || order.items.length === 0) {
    throw new Error('No items');
  }
}

function calculateTotal(order) {
  const subtotal = order.items.reduce(
    (sum, item) => sum + (item.price * item.quantity), 0
  );
  return applyDiscount(subtotal, order.customer);
}

function applyDiscount(amount, customer) {
  return customer.vip ? amount * 0.9 : amount;
}
```

### Duplicated Code

**Smell**: Same code structure appears in multiple places

**Refactor**: Extract common code

```javascript
// Before
function calculateShippingCost(order) {
  if (order.weight > 10) {
    return order.weight * 2.5 + 5;
  }
  return order.weight * 2.5;
}

function calculateHandlingFee(order) {
  if (order.weight > 10) {
    return order.weight * 0.5 + 2;
  }
  return order.weight * 0.5;
}

// After
function calculateWeightBasedFee(weight, rate, surcharge = 0) {
  const baseFee = weight * rate;
  return weight > 10 ? baseFee + surcharge : baseFee;
}

function calculateShippingCost(order) {
  return calculateWeightBasedFee(order.weight, 2.5, 5);
}

function calculateHandlingFee(order) {
  return calculateWeightBasedFee(order.weight, 0.5, 2);
}
```

### Large Class

**Smell**: Class has too many responsibilities

**Refactor**: Extract Class

```javascript
// Before
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }
  
  validateEmail() { /* ... */ }
  sendEmail(subject, body) { /* ... */ }
  hashPassword(password) { /* ... */ }
  checkPassword(password) { /* ... */ }
}

// After
class User {
  constructor(name, email, authenticator, emailService) {
    this.name = name;
    this.email = email;
    this.authenticator = authenticator;
    this.emailService = emailService;
  }
  
  sendEmail(subject, body) {
    this.emailService.send(this.email, subject, body);
  }
  
  authenticate(password) {
    return this.authenticator.verify(this.email, password);
  }
}

class EmailService {
  send(to, subject, body) { /* ... */ }
  validate(email) { /* ... */ }
}

class Authenticator {
  hash(password) { /* ... */ }
  verify(email, password) { /* ... */ }
}
```

### Feature Envy

**Smell**: Method uses more data from another class than its own

**Refactor**: Move Method

```javascript
// Before
class Order {
  constructor(customer, items) {
    this.customer = customer;
    this.items = items;
  }
  
  calculateDiscount() {
    if (this.customer.vip) {
      return this.customer.yearsActive * 0.01;
    }
    return 0;
  }
}

// After
class Order {
  constructor(customer, items) {
    this.customer = customer;
    this.items = items;
  }
  
  calculateDiscount() {
    return this.customer.getDiscountRate();
  }
}

class Customer {
  constructor(vip, yearsActive) {
    this.vip = vip;
    this.yearsActive = yearsActive;
  }
  
  getDiscountRate() {
    return this.vip ? this.yearsActive * 0.01 : 0;
  }
}
```

## Refactoring Techniques

### Replace Conditional with Polymorphism

```javascript
// Before
function getSpeed(vehicle) {
  switch(vehicle.type) {
    case 'car':
      return vehicle.enginePower * 2;
    case 'bike':
      return vehicle.enginePower * 3;
    case 'truck':
      return vehicle.enginePower * 1.5;
  }
}

// After
class Vehicle {
  getSpeed() { throw new Error('Must implement'); }
}

class Car extends Vehicle {
  getSpeed() { return this.enginePower * 2; }
}

class Bike extends Vehicle {
  getSpeed() { return this.enginePower * 3; }
}

class Truck extends Vehicle {
  getSpeed() { return this.enginePower * 1.5; }
}
```

### Introduce Parameter Object

```javascript
// Before
function createOrder(customerName, customerEmail, customerAddress,
                    itemName, itemPrice, itemQuantity) {
  // ...
}

// After
function createOrder(customer, item) {
  // customer: { name, email, address }
  // item: { name, price, quantity }
}
```

### Replace Magic Numbers with Named Constants

```javascript
// Before
function calculatePrice(quantity) {
  if (quantity > 100) {
    return quantity * 9.99 * 0.9;
  }
  return quantity * 9.99;
}

// After
const UNIT_PRICE = 9.99;
const BULK_THRESHOLD = 100;
const BULK_DISCOUNT = 0.9;

function calculatePrice(quantity) {
  const basePrice = quantity * UNIT_PRICE;
  return quantity > BULK_THRESHOLD ? basePrice * BULK_DISCOUNT : basePrice;
}
```

## Refactoring Strategy

### 1. Understand the Code

Before refactoring:
- [ ] Read and understand the existing code
- [ ] Identify all test coverage
- [ ] Document current behavior
- [ ] Note any dependencies

### 2. Ensure Test Coverage

- [ ] Add tests if missing
- [ ] Verify all tests pass
- [ ] Consider adding characterization tests

### 3. Plan Refactoring

- [ ] Identify specific smells to address
- [ ] Choose appropriate refactoring patterns
- [ ] Plan sequence of small steps
- [ ] Consider creating feature flag if risky

### 4. Execute Incrementally

- [ ] Make one change at a time
- [ ] Run tests after each change
- [ ] Commit working code frequently
- [ ] Roll back if tests fail

### 5. Verify and Clean Up

- [ ] All tests pass
- [ ] Code is clearer and simpler
- [ ] No performance regression
- [ ] Update documentation

## Safe Refactoring Checklist

- [ ] Tests exist and pass before starting
- [ ] Each refactoring step is small and focused
- [ ] Tests pass after each step
- [ ] Behavior remains unchanged
- [ ] Performance is not degraded
- [ ] Code is more maintainable
- [ ] Team has reviewed changes

## Integration Points

Works with:
- `senior-engineer` agent for refactoring execution
- `technical-architecture-advisor` for large-scale refactoring
- `/refactoring-plan` command for structured refactoring
- `code-reviewer` agent for validating improvements
