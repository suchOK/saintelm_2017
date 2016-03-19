from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post
# Create your views here.

class PostsListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'