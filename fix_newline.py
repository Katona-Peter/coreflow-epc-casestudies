#!/usr/bin/env python3
"""
Script to add a newline at the end of views.py to fix PEP8 W292 error
"""

file_path = 'casestudy/views.py'

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if file ends with newline
if not content.endswith('\n'):
    # Add newline at the end
    content += '\n'
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Added newline at end of file to fix W292 error")
else:
    print("File already ends with newline")
