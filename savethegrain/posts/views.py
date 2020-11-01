from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest
from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.models import User
from .models import post
from .forms import PostCreateForm

# Create your views here.

class DonationsListView(ListView):
    model =  post 
    template_name = 'posts/base.html'
    context_object_name = "posts"
    #ordering = ["-pub_date"]

    def get_query_set(self):
        return post.objects.filter(user_type="donor")

class ForDonorsListView(ListView):
    model =  post 
    template_name = 'posts/donorDash.html'
    context_object_name = "posts"
    #ordering = ["-pub_date"]
    
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(Donor=user).order_by('-pub_date')      

class PostCreateView(LoginRequiredMixin,CreateView):
    model =  post
    form_class = PostCreateForm

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)    


def about(response):
    return HttpResponse("<h1>About</h1>")

def home(response):
    return render(response,'posts/base.html',{})

