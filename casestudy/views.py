from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Casestudy, Comment
from .forms import CommentForm

class CasestudyList(generic.ListView):
    queryset = Casestudy.objects.all()
    template_name = "casestudy/index.html"
    context_object_name = "casestudy_list"
    paginate_by = 4

class CasestudyDetail(generic.DetailView):
    model = Casestudy
    template_name = "casestudy/casestudy_detail.html"

def casestudy_detail(request, slug):
    
    queryset = Casestudy.objects.all()
    casestudy = get_object_or_404(queryset, slug=slug)
    comments = casestudy.comments.all().order_by("-created_on")
    comment_count = casestudy.comments.filter(approved=True).count()
    
    # Check if user has pending comments for informational message
    if request.user.is_authenticated:
        user_pending_comments = casestudy.comments.filter(
            author=request.user, 
            approved=False
        ).count()
        
        if user_pending_comments > 0:
            messages.add_message(
                request, 
                messages.INFO,
                f'You have {user_pending_comments} comment(s) awaiting approval on this case study. Approved comments will appear in the discussion below.'
            )

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.add_message(
                request, 
                messages.WARNING,
                'You must be logged in to submit a comment. Please log in or register to join the discussion.'
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
                    f'Your comment has been submitted successfully! It will be reviewed by our team and published once approved. Thank you for contributing to the discussion about "{casestudy.title}".'
                )
                # Clear the form by redirecting to the same page
                return HttpResponseRedirect(reverse('casestudy_detail', args=[slug]))
            else:
                messages.add_message(
                    request, 
                    messages.ERROR,
                    'There was an error submitting your comment. Please check your input and try again.'
                )
    else:
        comment_form = CommentForm()

    return render(
        request,
        "casestudy/casestudy_detail.html",
        {"casestudy": casestudy,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form}
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
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
                f'Your comment has been updated successfully! The updated comment will be reviewed again and published once approved.'
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
                    'There was an error updating your comment. Please check your input and try again.'
                )

    return HttpResponseRedirect(reverse('casestudy_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Casestudy.objects.all()
    casestudy = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, 
            messages.SUCCESS, 
            f'Your comment has been permanently deleted from the discussion about "{casestudy.title}". This action cannot be undone.'
        )
    else:
        messages.add_message(
            request, 
            messages.ERROR, 
            'Permission denied: You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('casestudy_detail', args=[slug]))