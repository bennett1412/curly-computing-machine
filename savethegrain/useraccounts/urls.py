from django.urls import path
from .views import (
    signup
)

app_name = 'useraccounts'

urlpatterns = [
    path('',signup,name="signup"),
]