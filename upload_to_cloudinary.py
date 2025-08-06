#!/usr/bin/env python
"""
Upload images to Cloudinary and update case studies
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

import cloudinary
import cloudinary.uploader
from casestudy.models import Casestudy

# Cloudinary configuration
cloudinary.config(
    cloud_name='dxy6qkvvr',
    api_key='475639282489246',
    api_secret='JwqWJehhIo8klbtUrG4ZAuaean0',
    secure=True
)

def upload_images_to_cloudinary():
    """Upload all images from static/images to Cloudinary"""
    
    static_images_path = 'static/images'
    
    if not os.path.exists(static_images_path):
        print(f"❌ Directory {static_images_path} not found!")
        return
    
    # Get all PNG/JPG files
    image_files = [f for f in os.listdir(static_images_path) 
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    print(f"Found {len(image_files)} images to upload:")
    
    uploaded_images = {}
    
    for image_file in image_files:
        if image_file == 'default.png':
            continue  # Skip default image
            
        try:
            image_path = os.path.join(static_images_path, image_file)
            print(f"Uploading {image_file}...")
            
            # Upload to Cloudinary
            result = cloudinary.uploader.upload(
                image_path,
                public_id=f"case_studies/{image_file.split('.')[0]}",
                folder="case_studies"
            )
            
            uploaded_images[image_file] = result['secure_url']
            print(f"✅ Uploaded: {result['secure_url']}")
            
        except Exception as e:
            print(f"❌ Failed to upload {image_file}: {str(e)}")
    
    return uploaded_images

def update_case_studies_with_cloudinary_urls(uploaded_images):
    """Update case studies with Cloudinary URLs"""
    
    # Image mapping for case studies
    image_mapping = {
        'Electric Arc Furnace (EAF) Expansion Project': 'electric-arc-furnace-eaf-expansion-project.png',
        'Emergency Drainage & Venting System': 'Emergency-Drainage-Venting-System.png',
        'Fire & Gas Detection System': 'Fire-Gas-Detection.png',
        'Floating Roof Tank Upgrade': 'floating-roof.png',
        'Hazardous Waste Neutralization Unit': 'hazardous-waste-neutralization-unit.png',
        'Iron Ore Pelletizing Plant': 'iron-ore-pelletizing.png',
        'Modular Carbon Capture & Utilization (CCU) Unit': 'modular-carbon-capture-utilization-ccu-unit.png',
        'Renewable Energy Microgrid': 'renewable-energy-microgrid.png',
        'Skid-Mounted Process Plant': 'skid-mounted-process-plant.png',
        'Solid Waste Processing Plant': 'solid-waste-processing-plant.png',
        'Tailings Reprocessing Facility': 'Tailings-Reprocessing.png',
    }
    
    for title, image_file in image_mapping.items():
        if image_file in uploaded_images:
            try:
                case_study = Casestudy.objects.get(title=title)
                case_study.casestudyimage = uploaded_images[image_file]
                case_study.save()
                print(f"✅ Updated {title} with Cloudinary URL")
            except Casestudy.DoesNotExist:
                print(f"❌ Case study '{title}' not found")
            except Exception as e:
                print(f"❌ Error updating {title}: {str(e)}")

if __name__ == "__main__":
    print("=== Cloudinary Image Upload ===")
    print("✅ Cloudinary credentials configured!")
    print("Starting image upload process...\n")
    
    # Upload images and update case studies
    uploaded_images = upload_images_to_cloudinary()
    if uploaded_images:
        update_case_studies_with_cloudinary_urls(uploaded_images)
        print(f"\n✅ Successfully uploaded {len(uploaded_images)} images to Cloudinary!")
    else:
        print("\n❌ No images were uploaded")
