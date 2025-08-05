#!/usr/bin/env python
"""
Quick database check.
"""

import os
import sys
import django

# Add the project directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

from casestudy.models import Casestudy

print("🔍 Case Studies in Database:")
print("=" * 40)

count = Casestudy.objects.count()
print(f"Total: {count}")

if count > 0:
    for i, cs in enumerate(Casestudy.objects.all()[:5], 1):
        print(f"{i}. {cs.title}")
        print(f"   Image: '{cs.casestudyimage}'")
        print(f"   Slug: {cs.slug}")
        print()
else:
    print("❌ No case studies found!")
    print("You need to run: python load_case_studies.py")
