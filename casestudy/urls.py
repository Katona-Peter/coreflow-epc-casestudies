from . import views
from django.urls import path

urlpatterns = [
    path('', views.CasestudyList.as_view(), name='home'),
]