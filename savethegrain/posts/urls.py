from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    about
)

app_name = 'posts'

urlpatterns = [
    path('',PostListView.as_view(template_name="posts/base.html"), name = 'main-home'),
    path('post/new/',PostCreateView.as_view(template_name=""), name = 'donation-create'),
    path('about/',about, name = 'main-about')
]