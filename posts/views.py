from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Posts


class PostListView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'Postt/post.html'