"""
Forms for the casestudy application.

This module contains Django forms for handling user input related to case
studies, including comment forms for user engagement and feedback.
"""

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for creating and editing comments on case studies.

    This ModelForm provides a user interface for submitting comments on case
    study posts. It includes validation and handles the content field from
    the Comment model.
    """

    class Meta:
        """Meta configuration for CommentForm."""
        model = Comment
        fields = ('content',)
