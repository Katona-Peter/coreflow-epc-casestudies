"""
Minimal working test for CommentForm to identify issues
"""
from django.test import TestCase
from django.contrib.auth.models import User
from casestudy.forms import CommentForm
from casestudy.models import Comment, Casestudy, Client, Location, Industry


class MinimalCommentFormTest(TestCase):
    """Minimal test to isolate issues"""

    def setUp(self):
        """Minimal setup"""
        self.user = User.objects.create_user(
            username='minimal_testuser',
            email='minimal@example.com',
            password='testpass123'
        )
        
        self.client = Client.objects.create(client='Minimal Client')
        self.location = Location.objects.create(location='Minimal Location')
        self.industry = Industry.objects.create(industry='Minimal Industry')
        
        self.casestudy = Casestudy.objects.create(
            title='Minimal Case Study',
            slug='minimal-case-study',
            client=self.client,
            location=self.location,
            industry=self.industry,
            description='Minimal description.',
            excerpt='Minimal excerpt.'
        )

    def test_form_instantiation(self):
        """Test basic form creation"""
        form = CommentForm()
        self.assertIsNotNone(form)

    def test_form_has_content_field(self):
        """Test form has content field"""
        form = CommentForm()
        self.assertIn('content', form.fields)

    def test_valid_form_data(self):
        """Test form with valid data"""
        form = CommentForm(data={'content': 'Valid comment'})
        self.assertTrue(form.is_valid())

    def test_empty_form_data(self):
        """Test form with empty data"""
        form = CommentForm(data={'content': ''})
        self.assertFalse(form.is_valid())

    def test_form_save(self):
        """Test form save functionality"""
        form = CommentForm(data={'content': 'Test save comment'})
        self.assertTrue(form.is_valid())
        
        comment = form.save(commit=False)
        comment.author = self.user
        comment.casestudy = self.casestudy
        comment.save()
        
        self.assertEqual(comment.content, 'Test save comment')
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.casestudy, self.casestudy)
