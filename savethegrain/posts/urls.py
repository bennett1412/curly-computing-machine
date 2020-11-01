from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    about, 
    home
)

app_name = 'posts'

urlpatterns = [
    path('',home, name = 'main-home'),
    path('post/new/',PostCreateView.as_view(template_name=""), name = 'donation-create'),
    path('about/',about, name = 'main-about'),
    path('dashboard',PostListView.as_view(template_name="posts/dashboard.html"), name="dashboard")
]