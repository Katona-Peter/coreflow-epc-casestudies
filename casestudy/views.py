from django.shortcuts import render
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
