from django.urls import path
from .views import (
    ForDonorsListView,
    PostCreateView,
    DonationsListView,
    about, 
    home
)

app_name = 'posts'

urlpatterns = [
    path('',home, name = 'main-home'),
    path('post/new/',PostCreateView.as_view(template_name=""), name = 'donation-create'),
    path('about/',about, name = 'main-about'),
    path('dashboard/',DonationsListView.as_view(template_name="posts/dashboard.html"), name="ngo-dashboard"),
    path('donordashboard/<str:username>',ForDonorsListView.as_view(template_name="posts/donorDash.html"), name="donor-dashboard"),    

]