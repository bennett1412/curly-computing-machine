from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    about
)

app_name = 'post'

urlpatterns = [
    path('',PostListView.as_view(), name = 'main-home'),
    path('post/new/',PostCreateView.as_view(), name = 'donation-create'),
    path('about/',about, name = 'main-about')
]