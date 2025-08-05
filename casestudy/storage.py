"""
Custom storage for handling file uploads based on environment
- Development: Save to media directory
- Heroku: Save to static directory and serve via WhiteNoise
"""
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class HerokuCompatibleImageStorage(FileSystemStorage):
    """
    Storage that adapts to the deployment environment:
    - Development: Uses standard media directory
    - Heroku: Uses static directory for persistence with WhiteNoise
    """
    def __init__(self, location=None, base_url=None):
        # Check if we're on Heroku
        on_heroku = os.environ.get('ON_HEROKU', False)
        
        if on_heroku:
            # Heroku: Save to staticfiles directory
            if location is None:
                location = os.path.join(settings.STATIC_ROOT, 'uploads')
            if base_url is None:
                base_url = f"{settings.STATIC_URL}uploads/"
        else:
            # Development: Use standard media directory
            if location is None:
                location = settings.MEDIA_ROOT
            if base_url is None:
                base_url = settings.MEDIA_URL
                
        super().__init__(location=location, base_url=base_url)
    
    def url(self, name):
        """Return appropriate URL based on environment"""
        on_heroku = os.environ.get('ON_HEROKU', False)
        
        if on_heroku:
            # Heroku: Serve via static URL
            return f"{settings.STATIC_URL}uploads/{name}"
        else:
            # Development: Serve via media URL
            return f"{settings.MEDIA_URL}{name}"


# Keep old class name for backward compatibility
StaticImageStorage = HerokuCompatibleImageStorage
