#!/usr/bin/env python3
"""
Validates YAML/JSON structure in plugin files
Usage: python validate-schemas.py <plugin-path>
Outputs JSON with validation results
"""

import json
import sys
from pathlib import Path
import re

def parse_frontmatter(content):
    """Extract and parse YAML frontmatter from markdown file"""
    # Look for frontmatter between --- markers
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if not match:
        return None, "No frontmatter found"

    yaml_content = match.group(1)
    # Simple YAML parser for our specific use case
    frontmatter = {}
    for line in yaml_content.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter, None

def validate_plugin_json(plugin_path):
    """Validate plugin.json structure"""
    plugin_json_path = plugin_path / ".claude-plugin" / "plugin.json"

    if not plugin_json_path.exists():
        return ["plugin.json not found"]

    issues = []
    try:
        with open(plugin_json_path, 'r') as f:
            data = json.load(f)

        # Check required fields
        required_fields = ['name', 'version', 'description', 'author']
        for field in required_fields:
            if field not in data:
                issues.append(f"plugin.json: Missing required field '{field}'")
            elif field == 'author' and not isinstance(data[field], dict):
                issues.append("plugin.json: 'author' must be an object with 'name' field")
            elif field == 'author' and 'name' not in data[field]:
                issues.append("plugin.json: 'author.name' is required")

    except json.JSONDecodeError as e:
        issues.append(f"plugin.json: Invalid JSON - {str(e)}")
    except Exception as e:
        issues.append(f"plugin.json: Error reading file - {str(e)}")

    return issues

def validate_agent_frontmatter(agent_file):
    """Validate agent file frontmatter"""
    issues = []
    try:
        with open(agent_file, 'r') as f:
            content = f.read()

        frontmatter, error = parse_frontmatter(content)
        if error:
            issues.append(f"{agent_file.name}: {error}")
            return issues

        # Check required fields
        required_fields = ['name', 'description', 'tools', 'color', 'model']
        for field in required_fields:
            if field not in frontmatter or not frontmatter[field]:
                issues.append(f"{agent_file.name}: Missing required field '{field}'")

    except Exception as e:
        issues.append(f"{agent_file.name}: Error reading file - {str(e)}")

    return issues

def validate_skill_frontmatter(skill_file):
    """Validate skill SKILL.md frontmatter"""
    issues = []
    try:
        with open(skill_file, 'r') as f:
            content = f.read()

        frontmatter, error = parse_frontmatter(content)
        if error:
            issues.append(f"{skill_file.parent.name}/SKILL.md: {error}")
            return issues

        # Check required fields
        required_fields = ['name', 'description']
        for field in required_fields:
            if field not in frontmatter or not frontmatter[field]:
                issues.append(f"{skill_file.parent.name}/SKILL.md: Missing required field '{field}'")

    except Exception as e:
        issues.append(f"{skill_file.parent.name}/SKILL.md: Error reading file - {str(e)}")

    return issues

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"valid": False, "issues": ["No plugin path provided"]}))
        return 1

    plugin_path = Path(sys.argv[1])
    if not plugin_path.exists():
        print(json.dumps({"valid": False, "issues": [f"Plugin directory does not exist: {plugin_path}"]}))
        return 1

    all_issues = []

    # Validate plugin.json
    all_issues.extend(validate_plugin_json(plugin_path))

    # Validate agent frontmatter
    agents_dir = plugin_path / "agents"
    if agents_dir.exists():
        for agent_file in agents_dir.glob("*.md"):
            all_issues.extend(validate_agent_frontmatter(agent_file))

    # Validate skill frontmatter
    skills_dir = plugin_path / "skills"
    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
                if skill_file.exists():
                    all_issues.extend(validate_skill_frontmatter(skill_file))

    # Output JSON result
    result = {
        "valid": len(all_issues) == 0,
        "issues": all_issues
    }
    print(json.dumps(result, indent=2))

    return 0 if result["valid"] else 1

if __name__ == '__main__':
    sys.exit(main())
