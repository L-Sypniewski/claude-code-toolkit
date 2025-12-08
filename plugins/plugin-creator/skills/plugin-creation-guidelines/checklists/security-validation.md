# Security Validation Checklist

Comprehensive security validation guidelines for plugin components.

## Bash Script Security

### Issues to Check

- ✅ Input sanitization for user-provided arguments
- ✅ No direct shell injection vulnerabilities (`eval`, unquoted `$VAR`)
- ✅ Proper quoting for file paths with spaces
- ✅ Validation of file existence before operations
- ✅ No destructive operations without confirmation
- ✅ Use of `set -euo pipefail` for safety
- ✅ Restricted to necessary permissions

### Example: Good Practice

```bash
#!/bin/bash
set -euo pipefail

# Validate input
if [[ -z "${1:-}" ]]; then
  echo "Error: Argument required"
  exit 1
fi

# Sanitize and quote
FILE_PATH="${1}"
if [[ ! -f "$FILE_PATH" ]]; then
  echo "Error: File not found: $FILE_PATH"
  exit 1
fi

# Safe operation with quoting
cat "$FILE_PATH"
```

### Example: Bad Practice

```bash
#!/bin/bash
# No input validation
# No quoting (breaks with spaces)
cat $1
```

## Python Script Security

### Issues to Check

- ✅ Input validation and type checking
- ✅ No `eval()` or `exec()` on user input
- ✅ Proper exception handling
- ✅ Safe file operations (no arbitrary writes)
- ✅ No command injection via `os.system()` or `subprocess` with `shell=True`
- ✅ Use of `subprocess.run()` with list arguments
- ✅ Path validation (no directory traversal)

### Example: Good Practice

```python
import subprocess
import sys
from pathlib import Path

def process_file(file_path: str) -> None:
    """Process file safely with validation."""
    # Validate input
    if not file_path:
        raise ValueError("File path required")

    # Path validation
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # Safe subprocess call (no shell=True)
    result = subprocess.run(
        ["cat", str(path)],
        capture_output=True,
        text=True,
        check=True
    )
    print(result.stdout)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <file_path>")
        sys.exit(1)

    try:
        process_file(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
```

### Example: Bad Practice

```python
import os
import sys

# No validation, command injection vulnerability
os.system(f"cat {sys.argv[1]}")
```

## Agent Prompt Security

### Issues to Check

- ✅ No direct execution of user-provided code without validation
- ✅ Explicit warnings about destructive operations
- ✅ Confirmation gates for sensitive actions
- ✅ GET-only navigation for web crawling (no POST/PUT/DELETE)
- ✅ Rate limiting for API calls
- ✅ No hardcoded credentials or secrets
- ✅ Validation of external URLs before fetching

### Example: Good Practice

```markdown
## Safety Protocol

**Critical Safety Rules**:
- **Never** execute destructive operations without user confirmation
- **Always** use GET-only requests for web navigation
- **Always** validate and sanitize user input
- **Never** store or log sensitive information
- **Always** rate limit external API calls

**Confirmation Gates**:
Before performing destructive actions (delete, modify production data), use AskUserQuestion:
- Describe the action clearly
- Show what will be affected
- Require explicit confirmation
```

## Skill Content Security

### Issues to Check

- ✅ No example code with security vulnerabilities
- ✅ Templates include input validation
- ✅ Best practices emphasize security
- ✅ Warning about common pitfalls
- ✅ Safe defaults in examples

## Command Security

### Issues to Check

- ✅ Argument validation before delegation
- ✅ No direct shell execution of arguments
- ✅ Clear warnings about required permissions
- ✅ Documentation of sensitive operations

## Security Best Practices

1. **Input Validation**: Always validate and sanitize user input
2. **Least Privilege**: Grant minimum permissions necessary
3. **Safe Defaults**: Use secure defaults in all examples
4. **Explicit Confirmations**: Require user confirmation for destructive operations
5. **No Secrets**: Never hardcode credentials or sensitive data
6. **Safe APIs**: Use safe APIs (subprocess with list args, not shell commands)
7. **Path Validation**: Validate paths to prevent directory traversal
8. **Error Handling**: Handle errors gracefully without exposing sensitive info
