from . import views
from django.urls import path

urlpatterns = [
    path('', views.CasestudyList.as_view(), name='home'),
    path('case-study/<slug:slug>/', views.casestudy_detail, name='casestudy_detail'),
    path('case-study/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('case-study/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('debug-session/', views.debug_session, name='debug_session'),
]
