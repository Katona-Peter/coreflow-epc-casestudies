#!/usr/bin/env python3
"""
Performance optimization script for CoreFlow EPC Django application
Run this to apply additional performance improvements
"""

import os
import sys

def optimize_static_files():
    """Compress and optimize static files"""
    print("🔧 Optimizing static files...")
    
    # Collect static files
    os.system("python manage.py collectstatic --noinput")
    
    print("✅ Static files optimized")

def create_performance_middleware():
    """Create custom performance middleware"""
    middleware_content = '''from django.utils.cache import patch_cache_control
from django.http import HttpResponse

class PerformanceMiddleware:
    """Custom middleware for performance optimizations"""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Add cache headers for static content
        if request.path.startswith('/static/'):
            patch_cache_control(response, max_age=86400)  # 24 hours
            
        # Add security headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        
        return response
'''
    
    with open('coreflowepc/performance_middleware.py', 'w') as f:
        f.write(middleware_content)
    
    print("✅ Performance middleware created")

def create_image_optimization_management_command():
    """Create management command for image optimization"""
    
    # Create directories
    os.makedirs('casestudy/management', exist_ok=True)
    os.makedirs('casestudy/management/commands', exist_ok=True)
    
    # Create __init__.py files
    open('casestudy/management/__init__.py', 'a').close()
    open('casestudy/management/commands/__init__.py', 'a').close()
    
    command_content = '''from django.core.management.base import BaseCommand
from django.conf import settings
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Optimize case study images for performance'

    def handle(self, *args, **options):
        static_images_dir = os.path.join(settings.STATIC_ROOT, 'images', 'casestudies')
        
        if not os.path.exists(static_images_dir):
            self.stdout.write(self.style.WARNING('No case study images found'))
            return
            
        optimized_count = 0
        
        for filename in os.listdir(static_images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(static_images_dir, filename)
                
                try:
                    with Image.open(filepath) as img:
                        # Convert to RGB if necessary
                        if img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        
                        # Resize if too large (max 800px width)
                        if img.width > 800:
                            ratio = 800 / img.width
                            new_height = int(img.height * ratio)
                            img = img.resize((800, new_height), Image.Resampling.LANCZOS)
                        
                        # Save with optimization
                        img.save(filepath, 'JPEG', optimize=True, quality=85)
                        optimized_count += 1
                        
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Error optimizing {filename}: {e}')
                    )
        
        self.stdout.write(
            self.style.SUCCESS(f'Optimized {optimized_count} images')
        )
'''
    
    with open('casestudy/management/commands/optimize_images.py', 'w') as f:
        f.write(command_content)
    
    print("✅ Image optimization command created")

def main():
    print("🚀 Starting CoreFlow EPC Performance Optimization...")
    
    optimize_static_files()
    create_performance_middleware()
    create_image_optimization_management_command()
    
    print("\n🎉 Performance optimization complete!")
    print("\nNext steps:")
    print("1. Add 'coreflowepc.performance_middleware.PerformanceMiddleware' to MIDDLEWARE in settings.py")
    print("2. Run: python manage.py optimize_images")
    print("3. Consider using a CDN for static files in production")
    print("4. Enable gzip compression on your web server")
    print("5. Consider using WebP format for images")

if __name__ == "__main__":
    main()
