from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Casestudy

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

    return render(
        request,
        "casestudy/casestudy_detail.html",
        {"casestudy": casestudy},
    )