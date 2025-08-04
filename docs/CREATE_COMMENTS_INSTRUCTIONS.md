# Instructions to create test comments for your Django project

## Method 1: Using Django Admin (Recommended)

1. Start your Django development server:
   python manage.py runserver

2. Go to: http://127.0.0.1:8000/admin/

3. Log in with your admin credentials

4. Click on "Comments" under the CASESTUDY section

5. Click "Add Comment"

6. Fill in:
   - Casestudy: Select any case study from the dropdown
   - Author: Select a user (create one if needed)
   - Content: Write "This is a test comment to verify functionality."
   - Approved: Check this box to make it visible
   - Created on: Will be set automatically

7. Click "Save"

## Method 2: Using Django Shell

1. Open Django shell:
   python manage.py shell

2. Run these commands:

```python
from casestudy.models import Casestudy, Comment
from django.contrib.auth.models import User

# Get first case study
casestudy = Casestudy.objects.first()

# Get or create a test user
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'User'}
)

# Create approved comment
Comment.objects.create(
    casestudy=casestudy,
    author=user,
    content='This is a test comment that should be visible!',
    approved=True
)

# Create unapproved comment
Comment.objects.create(
    casestudy=casestudy,
    author=user,
    content='This comment is waiting for approval.',
    approved=False
)

print("Comments created successfully!")
```

## After creating comments:

Visit any case study detail page and you should see:
- Debug info showing comment counts
- Approved comments visible to all users
- Unapproved comments only visible to their authors

The template is now fixed and ready to display comments properly!
