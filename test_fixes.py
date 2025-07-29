#!/usr/bin/env python
"""
Test script to verify all Django fixes are working correctly
"""
import os
import sys
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

def test_everything():
    print("=== DJANGO CONFIGURATION TEST ===")
    
    # Test settings
    from django.conf import settings
    print(f"✓ DEBUG: {settings.DEBUG}")
    print(f"✓ SECRET_KEY configured: {'*' * 20 if settings.SECRET_KEY else 'NOT SET'}")
    print(f"✓ Database: {settings.DATABASES['default']['ENGINE']}")
    
    # Test models
    print("\n=== MODEL TESTS ===")
    from casestudy.models import Casestudy, Client, Location, Industry
    print(f"✓ Case Studies: {Casestudy.objects.count()}")
    print(f"✓ Clients: {Client.objects.count()}")
    print(f"✓ Locations: {Location.objects.count()}")
    print(f"✓ Industries: {Industry.objects.count()}")
    
    # Test URLs
    print("\n=== URL TESTS ===")
    from django.urls import reverse
    
    try:
        home_url = reverse('home')
        print(f"✓ Home URL: {home_url}")
    except Exception as e:
        print(f"✗ Home URL error: {e}")
    
    try:
        if Casestudy.objects.exists():
            case = Casestudy.objects.first()
            detail_url = reverse('casestudy_detail', args=[case.slug])
            print(f"✓ Detail URL: {detail_url}")
        else:
            print("! No case studies to test detail URL")
    except Exception as e:
        print(f"✗ Detail URL error: {e}")
    
    # Test views
    print("\n=== VIEW TESTS ===")
    try:
        from casestudy.views import CasestudyList, CasestudyDetail
        print("✓ Views imported successfully")
    except Exception as e:
        print(f"✗ View import error: {e}")
    
    # Test admin
    print("\n=== ADMIN TESTS ===")
    try:
        from casestudy.admin import CasestudyAdmin
        print("✓ Admin configuration imported successfully")
    except Exception as e:
        print(f"✗ Admin import error: {e}")
    
    print("\n=== ALL TESTS COMPLETED ===")

if __name__ == "__main__":
    try:
        test_everything()
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        sys.exit(1)
