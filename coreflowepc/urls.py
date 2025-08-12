"""
URL configuration for coreflowepc project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # Use Allauth's default logout view
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("", include("casestudy.urls"), name="casestudy-urls"),
]

if settings.DEBUG:
    # Development: serve media files directly
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
