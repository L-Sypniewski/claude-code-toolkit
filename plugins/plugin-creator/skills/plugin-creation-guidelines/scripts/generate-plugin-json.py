#!/usr/bin/env python3
"""
Generates plugin.json from template with variable substitution
Usage: python generate-plugin-json.py --name "plugin-name" --description "Description" --author "Author" --keywords "key1,key2,key3"
"""

import argparse
import json
import re
import sys

def validate_kebab_case(name):
    """Validate that name is in kebab-case format"""
    pattern = r'^[a-z][a-z0-9]*(-[a-z0-9]+)*$'
    return re.match(pattern, name) is not None

def main():
    parser = argparse.ArgumentParser(description='Generate plugin.json from template')
    parser.add_argument('--name', required=True, help='Plugin name (kebab-case)')
    parser.add_argument('--description', required=True, help='Plugin description')
    parser.add_argument('--author', required=True, help='Author name')
    parser.add_argument('--keywords', required=True, help='Comma-separated keywords')
    parser.add_argument('--repository', default='https://github.com/L-Sypniewski/claude-code-toolkit', help='Repository URL')

    args = parser.parse_args()

    # Validate plugin name
    if not validate_kebab_case(args.name):
        print("Error: Plugin name must be in kebab-case (lowercase, hyphens only)", file=sys.stderr)
        print("Example: my-plugin, api-tester, code-analyzer", file=sys.stderr)
        sys.exit(1)

    # Parse keywords
    keywords = [k.strip() for k in args.keywords.split(',') if k.strip()]
    if not keywords:
        print("Error: At least one keyword required", file=sys.stderr)
        sys.exit(1)

    # Build plugin.json
    plugin_data = {
        "name": args.name,
        "version": "1.0.0",
        "description": args.description,
        "author": {
            "name": args.author
        },
        "keywords": keywords,
        "license": "MIT",
        "repository": args.repository,
        "homepage": f"{args.repository}/tree/master/plugins/{args.name}"
    }

    # Output JSON to stdout
    print(json.dumps(plugin_data, indent=2))

    return 0

if __name__ == '__main__':
    sys.exit(main())
