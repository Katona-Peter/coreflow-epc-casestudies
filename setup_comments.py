# Simple Django shell commands to create test data for comments

# First, create a superuser if one doesn't exist
# python manage.py createsuperuser

# Then, in Django shell (python manage.py shell):
from casestudy.models import Casestudy, Comment
from django.contrib.auth.models import User

# Get or create a user
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com'}
)
if created:
    user.set_password('testpass123')
    user.save()

# Get the first case study
casestudy = Casestudy.objects.first()

# Create some test comments
Comment.objects.create(
    casestudy=casestudy,
    author=user,
    content='This is a great case study! Very informative.',
    approved=True
)

Comment.objects.create(
    casestudy=casestudy,
    author=user,
    content='Looking forward to more details about this project.',
    approved=True
)

Comment.objects.create(
    casestudy=casestudy,
    author=user,
    content='This comment is waiting for approval.',
    approved=False
)

print("Test comments created successfully!")
