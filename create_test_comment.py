import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreflowepc.settings')
django.setup()

from casestudy.models import Casestudy, Comment
from django.contrib.auth.models import User

# Get first case study
casestudy = Casestudy.objects.first()
print(f'Found case study: {casestudy.title}')

# Check if any users exist
users = User.objects.all()
if users.exists():
    user = users.first()
    print(f'Found user: {user.username}')
    
    # Create a test comment
    comment = Comment.objects.create(
        casestudy=casestudy,
        author=user,
        content='This is a test comment to verify the comment display functionality.',
        approved=True
    )
    print(f'Created comment: {comment.id}')
else:
    print('No users found. Need to create a user first.')

# Show current comments
comments = Comment.objects.all()
print(f'Total comments in database: {comments.count()}')
for comment in comments:
    print(f'Comment {comment.id}: {comment.content} by {comment.author} (approved: {comment.approved})')
