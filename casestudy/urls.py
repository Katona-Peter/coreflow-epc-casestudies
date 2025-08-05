from . import views
from django.urls import path
from .debug_views import debug_info

urlpatterns = [
    path('', views.CasestudyList.as_view(), name='home'),
    path('health/', views.health_check, name='health_check'),
    path('test/', views.simple_test, name='simple_test'),
    path('simple-home/', views.simple_home, name='simple_home'),
    path('debug/', debug_info, name='debug_info'),  # Debug URL for troubleshooting
    path('<slug:slug>/', views.casestudy_detail, name='casestudy_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
