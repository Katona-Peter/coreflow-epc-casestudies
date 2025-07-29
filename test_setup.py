#!/usr/bin/env python
"""
Test script to verify Django setup and case study data
"""
import os
import sys
import django

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

def test_models():
    """Test if models are working correctly"""
    try:
        from casestudy.models import Casestudy, Client, Location, Industry
        
        print("=== MODEL TESTS ===")
        print(f"Clients: {Client.objects.count()}")
        print(f"Locations: {Location.objects.count()}")
        print(f"Industries: {Industry.objects.count()}")
        print(f"Case Studies: {Casestudy.objects.count()}")
        
        if Casestudy.objects.exists():
            first_case = Casestudy.objects.first()
            print(f"\nFirst case study:")
            print(f"  Title: {first_case.title}")
            print(f"  Slug: {first_case.slug}")
            print(f"  Client: {first_case.client}")
            print(f"  Location: {first_case.location}")
            print(f"  Industry: {first_case.industry}")
        
        return True
    except Exception as e:
        print(f"Model test failed: {e}")
        return False

def test_urls():
    """Test if URLs are working correctly"""
    try:
        from django.urls import reverse
        
        print("\n=== URL TESTS ===")
        home_url = reverse('home')
        print(f"Home URL: {home_url}")
        
        # Test detail URL if we have case studies
        from casestudy.models import Casestudy
        if Casestudy.objects.exists():
            first_case = Casestudy.objects.first()
            detail_url = reverse('casestudy', args=[first_case.slug])
            print(f"Detail URL: {detail_url}")
        
        return True
    except Exception as e:
        print(f"URL test failed: {e}")
        return False

def test_views():
    """Test if views can be imported"""
    try:
        from casestudy.views import CasestudyList, CasestudyDetail
        print("\n=== VIEW TESTS ===")
        print("Views imported successfully")
        return True
    except Exception as e:
        print(f"View test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Django setup...")
    
    all_tests_passed = True
    all_tests_passed &= test_models()
    all_tests_passed &= test_urls()
    all_tests_passed &= test_views()
    
    if all_tests_passed:
        print("\n✓ All tests passed! Your Django setup is working correctly.")
    else:
        print("\n✗ Some tests failed. Check the errors above.")
