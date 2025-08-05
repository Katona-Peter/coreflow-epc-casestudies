"""
Management command to copy media files to static directory for Heroku deployment.

This command ensures that uploaded images are included in static files
so they can be served by WhiteNoise on Heroku.
"""

import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """
    Copy media files to static directory for Heroku deployment.
    
    Usage: python manage.py collectmedia
    """
    help = 'Copy media files to static directory for Heroku deployment'

    def handle(self, *args, **options):
        """Execute the command."""
        # Define source and destination directories
        media_root = settings.MEDIA_ROOT
        static_uploads = os.path.join(settings.BASE_DIR, 'static', 'uploads')
        
        # Create uploads directory if it doesn't exist
        os.makedirs(static_uploads, exist_ok=True)
        
        # Check if media directory exists and has files
        if not os.path.exists(media_root):
            self.stdout.write(
                self.style.WARNING(f'Media directory does not exist: {media_root}')
            )
            return
        
        # Copy files from media to static/uploads
        copied_files = 0
        for root, dirs, files in os.walk(media_root):
            for file in files:
                source_path = os.path.join(root, file)
                # Maintain directory structure relative to media root
                rel_path = os.path.relpath(source_path, media_root)
                dest_path = os.path.join(static_uploads, rel_path)
                
                # Create destination directory if needed
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok=True)
                
                # Copy file if it doesn't exist or is newer
                if not os.path.exists(dest_path) or \
                   os.path.getmtime(source_path) > os.path.getmtime(dest_path):
                    shutil.copy2(source_path, dest_path)
                    copied_files += 1
                    self.stdout.write(f'Copied: {rel_path}')
        
        if copied_files > 0:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully copied {copied_files} media files to static/uploads/')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('No new media files to copy.')
            )
