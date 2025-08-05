from django.db import models
from django.contrib.auth.models import User
import os
from .storage import StaticImageStorage


def casestudy_image_path(instance, filename):
    """Generate upload path for case study images to static directory."""
    # Get file extension
    ext = filename.split('.')[-1]
    # Create filename using case study slug and original extension
    filename = f"{instance.slug}.{ext}"
    # Return path: static/images/casestudies/slug.ext (saved to STATIC_ROOT)
    return os.path.join('static', 'images', 'casestudies', filename)


class Client(models.Model):
    client = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.client


class Location(models.Model):
    location = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.location


class Industry(models.Model):
    industry = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.industry


class Casestudy(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client_casestudy"
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="location_casestudy"
    )
    description = models.TextField()
    excerpt = models.TextField(null=True, blank=True)
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, related_name="industry_casestudy"
    )
    casestudyimage = models.ImageField(
        upload_to=casestudy_image_path,
        storage=StaticImageStorage(),
        null=True,
        blank=True,
        help_text="Upload an image for this case study. Image will be saved "
                  "to static directory for Heroku compatibility."
    )

    class Meta:
        ordering = ['title']  # Order by title alphabetically
        verbose_name_plural = "Case Studies"

    def __str__(self):
        return self.title


class Comment(models.Model):
    casestudy = models.ForeignKey(
        Casestudy, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.author}"
