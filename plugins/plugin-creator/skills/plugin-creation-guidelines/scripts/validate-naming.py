#!/usr/bin/env python3
"""
Validates naming conventions for plugin components
Usage: python validate-naming.py <plugin-path>
Outputs JSON with validation results
"""

import json
import os
import re
import sys
from pathlib import Path

def is_kebab_case(name):
    """Check if name is in kebab-case format"""
    pattern = r'^[a-z][a-z0-9]*(-[a-z0-9]+)*$'
    return re.match(pattern, name) is not None

def is_snake_case(name):
    """Check if name is in snake_case format"""
    pattern = r'^[a-z][a-z0-9]*(_[a-z0-9]+)*$'
    return re.match(pattern, name) is not None

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"valid": False, "issues": ["No plugin path provided"]}))
        return 1

    plugin_path = Path(sys.argv[1])
    if not plugin_path.exists():
        print(json.dumps({"valid": False, "issues": [f"Plugin directory does not exist: {plugin_path}"]}))
        return 1

    issues = []

    # Validate plugin directory name
    plugin_name = plugin_path.name
    if not is_kebab_case(plugin_name):
        issues.append(f"Plugin name '{plugin_name}' is not kebab-case")

    # Validate agent file names
    agents_dir = plugin_path / "agents"
    if agents_dir.exists():
        for agent_file in agents_dir.glob("*.md"):
            agent_name = agent_file.stem  # filename without extension
            if not is_kebab_case(agent_name):
                issues.append(f"Agent '{agent_name}' is not kebab-case")

    # Validate skill directory names
    skills_dir = plugin_path / "skills"
    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_name = skill_dir.name
                if not is_kebab_case(skill_name):
                    issues.append(f"Skill '{skill_name}' is not kebab-case")

    # Validate command file names (kebab-case or snake_case allowed)
    commands_dir = plugin_path / "commands"
    if commands_dir.exists():
        for command_file in commands_dir.glob("*.md"):
            command_name = command_file.stem
            if not is_kebab_case(command_name) and not is_snake_case(command_name):
                issues.append(f"Command '{command_name}' is not kebab-case or snake_case")

    # Output JSON result
    result = {
        "valid": len(issues) == 0,
        "issues": issues
    }
    print(json.dumps(result, indent=2))

    return 0 if result["valid"] else 1

if __name__ == '__main__':
    sys.exit(main())
