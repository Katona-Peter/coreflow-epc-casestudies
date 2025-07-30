from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Casestudy
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

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.casestudy = casestudy
            comment.save()
            messages.add_message(request, messages.SUCCESS,'Comment submitted and awaiting approval')
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