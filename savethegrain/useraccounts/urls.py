from django.urls import path
from .views import (
    signup
)

app_name = 'posts'

urlpatterns = [
    path('',signup,name="sign-up"),
]