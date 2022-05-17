from nntplib import ArticleInfo
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post
# Create your views here.

class PostDetailsView(DetailView):
    model = Post
    template_name = "blog/detailblog.html"

class PostListView(ListView):
    model = Post
    template_name = "blog/listblogs.html"