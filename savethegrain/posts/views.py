from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import (
    ListView,
    CreateView,
)
from .models import post
from .forms import PostCreateForm

# Create your views here.

class PostListView(ListView):
    model =  post 
    template_name = 'post/base.html'
    context_object_name = "posts"
    ordering = ["-pub_date"]

class PostCreateView(LoginRequiredMixin,CreateView):
    model =  post
    form_class = PostCreateForm

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)    


def about(response):
    return HttpResponse("<h1>About</h1>")            