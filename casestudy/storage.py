"""
Custom storage for saving uploaded files to static directory
This allows uploaded images to persist on Heroku with WhiteNoise
"""
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.storage import StaticFilesStorage


class StaticImageStorage(FileSystemStorage):
    """
    Custom storage that saves files to the static directory
    instead of media directory for Heroku compatibility
    """
    def __init__(self, location=None, base_url=None):
        if location is None:
            location = os.path.join(settings.BASE_DIR, 'static')
        if base_url is None:
            base_url = settings.STATIC_URL
        super().__init__(location=location, base_url=base_url)
    
    def url(self, name):
        """Return URL for uploaded file"""
        # Remove 'static/' from the beginning if present
        if name.startswith('static/'):
            name = name[7:]  # Remove 'static/' prefix
        return f"{settings.STATIC_URL}{name}"
