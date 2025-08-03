"""
Custom middleware for serving media files when DEBUG=False
"""
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.deprecation import MiddlewareMixin
from django.views.static import serve


class MediaFilesMiddleware(MiddlewareMixin):
    """
    Middleware to serve media files when DEBUG=False for deployment
    """
    def process_request(self, request):
        if request.path.startswith(settings.MEDIA_URL):
            # Remove the MEDIA_URL prefix to get the relative path
            document_root = settings.MEDIA_ROOT
            path = request.path[len(settings.MEDIA_URL):]
            
            try:
                return serve(request, path, document_root=document_root)
            except Http404:
                # File not found, let Django handle it normally
                pass
        
        return None
