from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .models import Casestudy, Comment
from .forms import CommentForm


class CasestudyList(generic.ListView):
    queryset = Casestudy.objects.select_related('client', 'location', 'industry').order_by("title")
    template_name = "casestudy/index.html"
    paginate_by = 4
    context_object_name = "casestudy_list"


class CasestudyDetail(generic.DetailView):
    model = Casestudy
    template_name = "casestudy/casestudy_detail.html"


def casestudy_detail(request, slug):
    """
    Display an individual case study with comments and comment form.
    Handle comment submission, validation, and user feedback messages.
    """
    queryset = Casestudy.objects.select_related(
        'client', 'location', 'industry'
    ).prefetch_related('comments').all()
    casestudy = get_object_or_404(queryset, slug=slug)
    
    # Show approved comments + user's own pending comments
    if request.user.is_authenticated:
        from django.db.models import Q
        comments = casestudy.comments.select_related('author').filter(
            Q(approved=True) | Q(author=request.user, approved=False)
        ).order_by("-created_on")
    else:
        comments = casestudy.comments.select_related('author').filter(
            approved=True
        ).order_by("-created_on")
    
    comment_count = casestudy.comments.filter(approved=True).count()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.WARNING,
                'You must be logged in to submit a comment. Please log '
                'in or register to join the discussion.'
            )
        else:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.casestudy = casestudy
                comment.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f'Your comment has been submitted successfully! It will '
                    f'be reviewed by our team and published once approved. '
                    f'Thank you for contributing to the discussion about '
                    f'"{casestudy.title}".'
                )
                # Clear the form by redirecting to the same page
                return HttpResponseRedirect(
                    reverse('casestudy_detail', args=[slug])
                )
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'There was an error submitting your comment. Please '
                    'check your input and try again.'
                )
    else:
        comment_form = CommentForm()

    return render(
        request,
        "casestudy/casestudy_detail.html",
        {
            "casestudy": casestudy,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        }
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit comments.

    Allows authenticated users to edit their own comments.
    Edited comments require re-approval.
    """
    if request.method == "POST":
        queryset = Casestudy.objects.all()
        casestudy = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.casestudy = casestudy
            comment.approved = False  # Re-approval required after edit
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your comment has been updated successfully! The updated '
                'comment will be reviewed again and published once approved.'
            )
        else:
            if comment.author != request.user:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Permission denied: You can only edit your own comments.'
                )
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'There was an error updating your comment. Please '
                    'check your input and try again.'
                )

    return HttpResponseRedirect(reverse('casestudy_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comment.
    Allows authenticated users to delete their own comments.
    Deletion is permanent and cannot be undone.
    """
    queryset = Casestudy.objects.all()
    casestudy = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            f'Your comment has been permanently deleted from the '
            f'discussion about "{casestudy.title}". This action '
            f'cannot be undone.'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Permission denied: You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('casestudy_detail', args=[slug]))


def custom_logout(request):
    """Custom logout view to ensure proper logout and message"""
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
    return redirect('home')
