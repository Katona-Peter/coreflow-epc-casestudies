#!/usr/bin/env python
"""
Check current case study data and fix issues.
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

from casestudy.models import Casestudy

def check_case_studies():
    """Check current case studies in database."""
    print("🔍 Current Case Studies in Database:")
    print("=" * 50)
    
    for cs in Casestudy.objects.all():
        print(f"Title: {cs.title}")
        print(f"Slug: {cs.slug}")
        print(f"Image: {cs.casestudyimage}")
        print("-" * 30)
    
    print(f"\nTotal: {Casestudy.objects.count()} case studies")

if __name__ == "__main__":
    check_case_studies()
