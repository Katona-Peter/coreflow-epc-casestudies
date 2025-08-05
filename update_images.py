#!/usr/bin/env python
"""
Script to update case study images with static image filenames.
Run this after changing the model field from ImageField to CharField.
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

from casestudy.models import Casestudy

# Image mapping based on your static/images directory
IMAGE_MAPPING = {
    'floating-roof': 'floating-roof.png',
    'fire-gas-detection': 'Fire-Gas-Detection.png', 
    'emergency-drainage': 'Emergency-Drainage-Venting-System.png',
    'hazardous-waste': 'hazardous-waste-neutralization-unit.png',
    'iron-ore': 'iron-ore-pelletizing.png',
    'electric-arc': 'electric-arc-furnace-eaf-expansion-project.png',
    'tailings': 'Tailings-Reprocessing.png',
    'solid-waste': 'solid-waste-processing-plant.png',
    'skid-mounted': 'skid-mounted-process-plant.png',
    'renewable-energy': 'renewable-energy-microgrid.png',
    'carbon-capture': 'modular-carbon-capture-utilization-ccu-unit.png',
}

def update_case_study_images():
    """Update case studies with appropriate image filenames."""
    print("🔄 Updating case study images...")
    
    for casestudy in Casestudy.objects.all():
        slug = casestudy.slug
        
        # Try to find a matching image
        image_filename = None
        
        # Check for exact matches or partial matches
        for key, filename in IMAGE_MAPPING.items():
            if key in slug or slug in key:
                image_filename = filename
                break
        
        # If no specific match, assign default
        if not image_filename:
            image_filename = 'default.png'
        
        # Update the case study
        casestudy.casestudyimage = image_filename
        casestudy.save()
        
        print(f"✓ {casestudy.title}: {image_filename}")
    
    print("🎉 Image update complete!")

if __name__ == "__main__":
    update_case_study_images()
