#!/usr/bin/env python
"""
Simple script to manually create case studies one by one
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

def main():
    try:
        from casestudy.models import Casestudy, Client, Location, Industry
        
        print("=== Manual Case Study Creation ===")
        print("🧹 Clearing existing case studies...")
        Casestudy.objects.all().delete()
        
        # Test creating one case study
        print("Creating test objects...")
        client_obj, _ = Client.objects.get_or_create(client='SteelTech Industries')
        location_obj, _ = Location.objects.get_or_create(location='Birmingham, United Kingdom')
        industry_obj, _ = Industry.objects.get_or_create(industry='Steel Manufacturing')
        
        print("Creating case study...")
        casestudy = Casestudy(
            title='Electric Arc Furnace (EAF) Expansion Project',
            slug='electric-arc-furnace-eaf-expansion-project',
            client=client_obj,
            location=location_obj,
            industry=industry_obj,
            description='Test description for EAF project',
            excerpt='State-of-the-art 150-ton electric arc furnace expansion'
        )
        casestudy.save()
        
        print(f"✅ SUCCESS! Created: {casestudy.title}")
        print(f"Total case studies: {Casestudy.objects.count()}")
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
