#!/usr/bin/env python3
"""
Documentation linting script for OpenMS-docs.
Checks for common style and consistency issues.
"""

import os
import re
import sys
from pathlib import Path


class DocLinter:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def check_file(self, filepath):
        """Check a single file for issues."""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')

        for i, line in enumerate(lines, 1):
            # Check for trailing whitespace
            if line.endswith(' ') or line.endswith('\t'):
                self.errors.append(f"{filepath}:{i}: Trailing whitespace")

            # Check for insecure HTTP links (excluding specific domains)
            if 'http://' in line and not any(x in line for x in ['localhost', 'openms.org', 'openms.de', 'rforge.net']):
                self.warnings.append(f"{filepath}:{i}: Consider using HTTPS instead of HTTP")

            # Check for inconsistent terminology
            if re.search(r'\b(openMS|Openms)\b', line):
                # Check if it's not in a URL, path, filename, or image directive
                if not re.search(r'(https?://|\.openms|/openms|openms-|openms\.|image::|\.\.\s+figure::|\{image\})', line):
                    self.errors.append(f"{filepath}:{i}: Use 'OpenMS' instead of variant spelling")

            if re.search(r'\b(Toppview)\b', line):
                # Check if it's not in a URL, path, or image
                if not re.search(r'(https?://|/toppview|toppview-|image::|\.\.\s+figure::)', line, re.IGNORECASE):
                    self.errors.append(f"{filepath}:{i}: Use 'TOPPView' (correct capitalization)")

            # Check for TODO/FIXME in markdown comments (but allow in code blocks)
            if re.search(r'<!--.*TODO.*-->', line) or re.search(r'<!--.*FIXME.*-->', line):
                self.warnings.append(f"{filepath}:{i}: TODO/FIXME comment found - consider creating an issue")

    def check_directory(self, directory):
        """Check all documentation files in a directory."""
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md') or file.endswith('.rst'):
                    filepath = os.path.join(root, file)
                    self.check_file(filepath)

    def report(self):
        """Print the linting report."""
        print(f"\n{'='*60}")
        print("OpenMS Documentation Linting Report")
        print(f"{'='*60}\n")

        if self.errors:
            print(f"❌ ERRORS ({len(self.errors)}):")
            for error in self.errors[:20]:  # Show first 20
                print(f"   {error}")
            if len(self.errors) > 20:
                print(f"   ... and {len(self.errors) - 20} more")
            print()

        if self.warnings:
            print(f"⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings[:20]:  # Show first 20
                print(f"   {warning}")
            if len(self.warnings) > 20:
                print(f"   ... and {len(self.warnings) - 20} more")
            print()

        if not self.errors and not self.warnings:
            print("✅ No issues found! Documentation looks good.")
            print()

        return len(self.errors)


def main():
    """Main entry point."""
    linter = DocLinter()

    # Check docs directory
    docs_dir = Path(__file__).parent / 'docs'
    if docs_dir.exists():
        linter.check_directory(docs_dir)
    else:
        print(f"Error: docs directory not found at {docs_dir}")
        return 1

    # Generate report
    error_count = linter.report()

    # Return error code if errors found
    return 1 if error_count > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
