---
name: security-best-practices
description: Comprehensive security best practices and vulnerability prevention guidelines for secure software development across all layers of the application stack
author: Claude Code Toolkit
---

# Security Best Practices

This skill provides comprehensive security guidelines and best practices that are automatically activated during code review, implementation, and security analysis tasks.

## Purpose

Automatically activated when:
- Reviewing code for security vulnerabilities
- Implementing authentication or authorization
- Handling sensitive data
- Processing user input
- Making security-related design decisions
- Conducting security audits

## OWASP Top 10 Prevention

### 1. Injection Attacks Prevention

**SQL Injection:**
- Always use parameterized queries or prepared statements
- Never concatenate user input into SQL queries
- Use ORM frameworks with built-in protection
- Apply principle of least privilege for database accounts
- Validate and sanitize all database inputs

**Command Injection:**
- Avoid system calls with user input
- Use built-in library functions instead of shell commands
- Sanitize all input used in system commands
- Use allowlists for permitted values
- Escape special characters properly

**XSS (Cross-Site Scripting):**
- Encode all output data
- Use Content Security Policy (CSP) headers
- Sanitize user input on both client and server
- Use frameworks with automatic XSS protection
- Avoid `innerHTML`, use `textContent` or sanitizers

### 2. Broken Authentication

**Password Security:**
- Enforce strong password requirements
- Use bcrypt, Argon2, or PBKDF2 for hashing
- Never store passwords in plain text
- Implement account lockout after failed attempts
- Use multi-factor authentication (MFA)
- Implement secure password reset flows

**Session Management:**
- Generate strong, random session IDs
- Set secure session timeout values
- Regenerate session ID after login
- Use HTTP-only and Secure flags on cookies
- Implement proper logout functionality
- Protect against session fixation attacks

**Token Security:**
- Use secure, signed tokens (JWT with proper algorithms)
- Implement token expiration and refresh mechanisms
- Store tokens securely (never in localStorage for sensitive apps)
- Validate token signatures server-side
- Use short-lived access tokens with refresh tokens

### 3. Sensitive Data Exposure

**Data Encryption:**
- Encrypt sensitive data at rest using AES-256
- Use TLS 1.2+ for data in transit
- Never store sensitive data unnecessarily
- Implement proper key management
- Use hardware security modules (HSM) for key storage when possible

**Secure Data Handling:**
- Mask sensitive data in logs
- Implement data retention policies
- Sanitize data before logging
- Use secure deletion methods
- Avoid caching sensitive data

**API Security:**
- Use HTTPS exclusively for APIs
- Implement proper authentication (OAuth 2.0, API keys)
- Rate limit API endpoints
- Validate and sanitize all API inputs
- Return generic error messages (avoid information disclosure)

### 4. XML External Entities (XXE)

**XML Processing:**
- Disable DTD processing in XML parsers
- Use less complex data formats like JSON when possible
- Keep XML processors updated
- Implement allowlisting for XML inputs
- Use secure XML parser configurations

### 5. Broken Access Control

**Authorization:**
- Implement deny-by-default access control
- Use role-based access control (RBAC)
- Verify permissions on server-side
- Never rely on client-side authorization
- Implement proper ownership checks
- Use attribute-based access control (ABAC) for complex scenarios

**Path Traversal Prevention:**
- Validate and sanitize file paths
- Use allowlists for permitted directories
- Avoid user-controllable file paths
- Use built-in path manipulation functions
- Implement chroot jails when appropriate

### 6. Security Misconfiguration

**Configuration Management:**
- Remove default credentials
- Disable unnecessary services and features
- Use secure default configurations
- Keep all software updated
- Implement security headers (CSP, HSTS, X-Frame-Options)
- Regular security audits and scans

**Error Handling:**
- Don't expose stack traces to users
- Log errors securely
- Use generic error messages
- Implement proper exception handling
- Monitor and alert on security events

### 7. Cross-Site Request Forgery (CSRF)

**CSRF Protection:**
- Use anti-CSRF tokens for state-changing operations
- Validate origin and referer headers
- Use SameSite cookie attribute
- Implement double-submit cookie pattern
- Require re-authentication for sensitive operations

### 8. Using Components with Known Vulnerabilities

**Dependency Management:**
- Keep all dependencies updated
- Use automated vulnerability scanning (Dependabot, Snyk)
- Remove unused dependencies
- Monitor security advisories
- Use lock files for reproducible builds
- Regularly audit third-party libraries

### 9. Insufficient Logging & Monitoring

**Security Logging:**
- Log all authentication attempts
- Log authorization failures
- Log input validation failures
- Include relevant context in logs
- Protect log integrity
- Implement log retention policies
- Set up alerting for suspicious activities

**Monitoring:**
- Monitor for unusual patterns
- Track failed login attempts
- Detect SQL injection attempts
- Monitor for data exfiltration
- Implement real-time alerting

### 10. Server-Side Request Forgery (SSRF)

**SSRF Prevention:**
- Validate and sanitize all URLs
- Use allowlists for permitted domains
- Disable unnecessary URL schemas
- Implement network segmentation
- Validate response data
- Use DNS pinning when appropriate

## Secure Coding Practices

### Input Validation

**Validation Strategy:**
- Validate all input on server-side
- Use allowlists over blocklists
- Validate data type, length, format, and range
- Reject invalid input, don't try to fix it
- Validate file uploads (type, size, content)
- Use schema validation for complex inputs

### Output Encoding

**Context-Specific Encoding:**
- HTML encode for HTML context
- URL encode for URL parameters
- JavaScript encode for JavaScript context
- CSS encode for CSS context
- Use proper JSON encoding
- Context-aware output encoding

### Cryptography

**Encryption Best Practices:**
- Use well-tested cryptographic libraries
- Never implement custom crypto algorithms
- Use proper key sizes (AES-256, RSA-2048+)
- Use secure random number generators
- Implement proper IV/nonce generation
- Use authenticated encryption (GCM, CCM)
- Never hard-code cryptographic keys

**TLS/SSL:**
- Use TLS 1.2 or higher
- Disable weak cipher suites
- Implement certificate pinning for mobile apps
- Validate certificates properly
- Use perfect forward secrecy (PFS)

### Authentication & Authorization

**Secure Authentication:**
- Implement rate limiting on authentication endpoints
- Use CAPTCHA for repeated failed attempts
- Implement account enumeration prevention
- Use secure password reset mechanisms
- Log all authentication events
- Implement multi-factor authentication

**Authorization Checks:**
- Verify authorization on every request
- Use centralized authorization logic
- Implement principle of least privilege
- Check both authentication and authorization
- Never trust client-side authorization

## API Security

### REST API Security

**API Best Practices:**
- Use OAuth 2.0 or API keys for authentication
- Implement rate limiting and throttling
- Validate content-type headers
- Use CORS properly
- Implement request size limits
- Version APIs properly
- Document security requirements

### GraphQL Security

**GraphQL-Specific:**
- Implement query complexity limits
- Prevent query depth attacks
- Use persisted queries
- Implement proper authorization checks on fields
- Rate limit by query cost
- Disable introspection in production

## Secure Development Lifecycle

### Design Phase

- Threat modeling
- Security requirements gathering
- Privacy by design
- Secure architecture review
- Risk assessment

### Implementation Phase

- Follow secure coding guidelines
- Use security linters and SAST tools
- Perform code reviews with security focus
- Implement security unit tests
- Use safe APIs and libraries

### Testing Phase

- Security testing (DAST, SAST, IAST)
- Penetration testing
- Vulnerability scanning
- Fuzz testing
- Security regression testing

### Deployment Phase

- Secure configuration management
- Security hardening
- Monitoring and alerting setup
- Incident response planning
- Security documentation

## Security Checklist

When implementing or reviewing code, verify:

- [ ] All user input is validated and sanitized
- [ ] Sensitive data is encrypted at rest and in transit
- [ ] Authentication is implemented securely
- [ ] Authorization checks are enforced on server-side
- [ ] CSRF protection is implemented
- [ ] XSS prevention measures are in place
- [ ] SQL injection prevention (parameterized queries)
- [ ] Security headers are configured
- [ ] Error messages don't leak sensitive information
- [ ] Dependencies are up-to-date and scanned
- [ ] Logging captures security-relevant events
- [ ] Secrets are not hard-coded
- [ ] Rate limiting is implemented
- [ ] File uploads are validated and secured
- [ ] API endpoints are properly secured

## Common Vulnerabilities to Avoid

**Code-Level Vulnerabilities:**
- Buffer overflows
- Integer overflows
- Race conditions
- Use-after-free errors
- Null pointer dereferences
- Uninitialized variables

**Web Application Vulnerabilities:**
- Open redirects
- Clickjacking
- DOM-based XSS
- Insecure deserialization
- XML injection
- LDAP injection

**Infrastructure Vulnerabilities:**
- Exposed sensitive files (.env, .git)
- Directory listing enabled
- Weak TLS configuration
- Missing security headers
- Information disclosure

## Security Tools and Resources

**Static Analysis:**
- SonarQube
- Semgrep
- CodeQL
- Bandit (Python)
- ESLint security plugins

**Dynamic Analysis:**
- OWASP ZAP
- Burp Suite
- Metasploit
- SQLMap

**Dependency Scanning:**
- Dependabot
- Snyk
- OWASP Dependency-Check
- npm audit / pip-audit

## Emergency Response

**Incident Response:**
- Have an incident response plan
- Document security contacts
- Implement rapid patching procedures
- Maintain security rollback capabilities
- Conduct post-incident reviews

## Usage by Agents

This skill is automatically available to:
- **senior-engineer** - During implementation of security-sensitive features
- **code-reviewer** - During security-focused code reviews
- **technical-architecture-advisor** - When evaluating security architecture

The skill ensures consistent security practices across all development activities.
