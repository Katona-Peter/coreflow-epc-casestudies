from django.core.management.base import BaseCommand
import cloudinary
import cloudinary.uploader
import os
from casestudy.models import Casestudy

class Command(BaseCommand):
    help = 'Upload images to Cloudinary and update case studies'

    def handle(self, *args, **options):
        self.stdout.write("=== Uploading Images to Cloudinary ===")
        
        # Get credentials from environment variables
        import os
        cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME')
        api_key = os.environ.get('CLOUDINARY_API_KEY')
        api_secret = os.environ.get('CLOUDINARY_API_SECRET')
        
        self.stdout.write(f"Cloud Name: {cloud_name}")
        self.stdout.write(f"API Key: {api_key}")
        
        if not all([cloud_name, api_key, api_secret]):
            self.stdout.write(self.style.ERROR("❌ Missing Cloudinary credentials in environment variables!"))
            self.stdout.write("Please check your env.py file or environment variables.")
            return
        
        # Configure Cloudinary
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True
        )
        
        static_images_path = 'static/images'
        
        if not os.path.exists(static_images_path):
            self.stdout.write(self.style.ERROR(f"Directory {static_images_path} not found!"))
            return
        
        # Get all image files
        image_files = [f for f in os.listdir(static_images_path) 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        self.stdout.write(f"Found {len(image_files)} images to upload")
        
        uploaded_images = {}
        
        for image_file in image_files:
            if image_file == 'default.png':
                continue  # Skip default image
                
            try:
                image_path = os.path.join(static_images_path, image_file)
                self.stdout.write(f"Uploading {image_file}...")
                
                # Upload to Cloudinary
                result = cloudinary.uploader.upload(
                    image_path,
                    public_id=f"case_studies/{image_file.split('.')[0]}",
                    folder="case_studies"
                )
                
                uploaded_images[image_file] = result['secure_url']
                self.stdout.write(self.style.SUCCESS(f"✅ Uploaded: {result['secure_url']}"))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Failed to upload {image_file}: {str(e)}"))
        
        # Update case studies with Cloudinary URLs
        image_mapping = {
            'Electric Arc Furnace (EAF) Expansion Project': 'electric-arc-furnace-eaf-expansion-project.png',
            'Emergency Drainage & Venting System': 'Emergency-Drainage-Venting-System.png',
            'Fire & Gas Detection Network': 'Fire-Gas-Detection.png',
            'Floating Roof Storage System': 'floating-roof.png',
            'Hazardous Waste Neutralization Unit': 'hazardous-waste-neutralization-unit.png',
            'Iron Ore Pelletizing Plant': 'iron-ore-pelletizing.png',
            'Modular Carbon Capture Utilization (CCU) Unit': 'modular-carbon-capture-utilization-ccu-unit.png',
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
                    self.stdout.write(self.style.SUCCESS(f"✅ Updated {title} with Cloudinary URL"))
                except Casestudy.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"⚠️ Case study '{title}' not found"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"❌ Error updating {title}: {str(e)}"))
        
        self.stdout.write(self.style.SUCCESS(f"\n✅ Successfully uploaded {len(uploaded_images)} images to Cloudinary!"))
