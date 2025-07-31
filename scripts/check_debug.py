#!/usr/bin/env python3
"""
Django DEBUG Setting Checker
============================

This script checks if DEBUG is set to True in Django settings files.
It can be used as a pre-commit hook, CI/CD check, or manual verification.

Usage:
    python check_debug.py [--strict] [--path <settings_path>]

Options:
    --strict    Exit with error code 1 if DEBUG=True is found
    --path      Specify a custom path to settings file
"""

import os
import re
import sys
import argparse
from pathlib import Path


class DebugChecker:
    def __init__(self, strict_mode=False, custom_path=None):
        self.strict_mode = strict_mode
        self.custom_path = custom_path
        self.errors_found = []
        
    def find_settings_files(self):
        """Find all Django settings.py files in the project."""
        if self.custom_path:
            if os.path.exists(self.custom_path):
                return [self.custom_path]
            else:
                print(f"❌ Custom path not found: {self.custom_path}")
                return []
        
        settings_files = []
        project_root = Path.cwd()
        
        # Search for settings.py files, excluding virtual environments
        for settings_file in project_root.rglob("settings.py"):
            # Skip files in virtual environments or git directories
            if any(part in settings_file.parts for part in ['.venv', 'venv', '.git', '__pycache__']):
                continue
            settings_files.append(str(settings_file))
            
        return settings_files
    
    def check_debug_setting(self, file_path):
        """Check if DEBUG is set to True in a settings file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                lines = content.split('\n')
                
            # Patterns to match DEBUG = True (with various whitespace)
            debug_patterns = [
                r'^\s*DEBUG\s*=\s*True\s*$',           # DEBUG = True
                r'^\s*DEBUG\s*=\s*True\s*#.*$',        # DEBUG = True # comment
                r'^\s*DEBUG\s*=\s*[1-9]\d*\s*$',       # DEBUG = 1, 2, etc.
            ]
            
            issues = []
            for line_num, line in enumerate(lines, 1):
                for pattern in debug_patterns:
                    if re.match(pattern, line):
                        issues.append({
                            'file': file_path,
                            'line': line_num,
                            'content': line.strip(),
                            'type': 'DEBUG_TRUE'
                        })
                        
            return issues
            
        except Exception as e:
            return [{
                'file': file_path,
                'line': 0,
                'content': f"Error reading file: {e}",
                'type': 'READ_ERROR'
            }]
    
    def run_check(self):
        """Run the DEBUG setting check."""
        print("🔍 Django DEBUG Setting Checker")
        print("=" * 50)
        
        settings_files = self.find_settings_files()
        
        if not settings_files:
            print("ℹ️  No Django settings.py files found.")
            return 0
        
        print(f"📄 Found {len(settings_files)} settings file(s):")
        for file_path in settings_files:
            print(f"   • {file_path}")
        print()
        
        all_issues = []
        
        for file_path in settings_files:
            print(f"🔍 Checking: {file_path}")
            issues = self.check_debug_setting(file_path)
            
            if issues:
                all_issues.extend(issues)
                for issue in issues:
                    if issue['type'] == 'DEBUG_TRUE':
                        print(f"   ❌ Line {issue['line']}: {issue['content']}")
                    else:
                        print(f"   ⚠️  {issue['content']}")
            else:
                print("   ✅ DEBUG=False (OK)")
        
        if all_issues:
            self.print_summary(all_issues)
            return 1 if self.strict_mode else 0
        else:
            print("\n🎉 All checks passed! DEBUG=False in all settings files.")
            return 0
    
    def print_summary(self, issues):
        """Print a summary of found issues."""
        print("\n" + "=" * 50)
        print("🚫 ISSUES FOUND:")
        print("=" * 50)
        
        debug_issues = [i for i in issues if i['type'] == 'DEBUG_TRUE']
        
        if debug_issues:
            print("❌ DEBUG=True found in the following files:")
            for issue in debug_issues:
                print(f"   📄 {issue['file']} (line {issue['line']})")
                print(f"      → {issue['content']}")
            
            print("\n🔧 RECOMMENDED FIXES:")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("1. Set DEBUG = False in your settings.py file(s)")
            print("2. Use environment variables for DEBUG in production:")
            print("   DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'")
            print("3. Create local_settings.py for development (add to .gitignore)")
            print("4. Use different settings files for different environments")
            
            if self.strict_mode:
                print("\n💥 STRICT MODE: Exiting with error code 1")
            else:
                print("\n⚠️  WARNING MODE: Continuing with warning")


def main():
    parser = argparse.ArgumentParser(
        description="Check Django settings for DEBUG=True",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python check_debug.py                    # Check all settings files
    python check_debug.py --strict           # Exit with error if DEBUG=True
    python check_debug.py --path settings.py # Check specific file
        """
    )
    
    parser.add_argument(
        '--strict', 
        action='store_true',
        help='Exit with error code 1 if DEBUG=True is found'
    )
    
    parser.add_argument(
        '--path',
        type=str,
        help='Path to specific settings file to check'
    )
    
    args = parser.parse_args()
    
    checker = DebugChecker(strict_mode=args.strict, custom_path=args.path)
    exit_code = checker.run_check()
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
