from django.shortcuts import render
from django.views import generic
from .models import Casestudy

class CasestudyList(generic.ListView):
    queryset = Casestudy.objects.all()
    template_name = "casestudy_list/index.html"
    paginate_by = 4
