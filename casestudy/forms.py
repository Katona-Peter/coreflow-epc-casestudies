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


def test_comment_form():
    """
    Simple test function for CommentForm validation.
    
    This function can be called to quickly test the CommentForm functionality.
    Returns a tuple of (success: bool, results: list).
    """
    test_results = []
    
    # Test 1: Valid data
    try:
        form_data = {'content': 'This is a valid test comment.'}
        form = CommentForm(data=form_data)
        if form.is_valid():
            test_results.append(("Valid data test", True, "Form accepts valid content"))
        else:
            test_results.append(("Valid data test", False, f"Form errors: {form.errors}"))
    except Exception as e:
        test_results.append(("Valid data test", False, f"Exception: {str(e)}"))
    
    # Test 2: Empty content
    try:
        form_data = {'content': ''}
        form = CommentForm(data=form_data)
        if not form.is_valid() and 'content' in form.errors:
            test_results.append(("Empty content test", True, "Form correctly rejects empty content"))
        else:
            test_results.append(("Empty content test", False, "Form should reject empty content"))
    except Exception as e:
        test_results.append(("Empty content test", False, f"Exception: {str(e)}"))
    
    # Test 3: Field configuration
    try:
        form = CommentForm()
        if 'content' in form.fields and len(form.fields) == 1:
            test_results.append(("Field configuration test", True, "Form has correct fields"))
        else:
            test_results.append(("Field configuration test", False, f"Unexpected fields: {list(form.fields.keys())}"))
    except Exception as e:
        test_results.append(("Field configuration test", False, f"Exception: {str(e)}"))
    
    # Test 4: Model integration
    try:
        form = CommentForm()
        if form._meta.model == Comment and form._meta.fields == ('content',):
            test_results.append(("Model integration test", True, "Form correctly configured with Comment model"))
        else:
            test_results.append(("Model integration test", False, f"Model: {form._meta.model}, Fields: {form._meta.fields}"))
    except Exception as e:
        test_results.append(("Model integration test", False, f"Exception: {str(e)}"))
    
    # Calculate success rate
    passed = sum(1 for _, success, _ in test_results if success)
    total = len(test_results)
    
    return passed == total, test_results


# Example usage for manual testing:
if __name__ == "__main__":
    success, results = test_comment_form()
    print("CommentForm Test Results:")
    print("=" * 40)
    for test_name, passed, message in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
        print(f"   {message}")
    print("=" * 40)
    print(f"Overall: {'✅ ALL TESTS PASSED' if success else '❌ SOME TESTS FAILED'}")
