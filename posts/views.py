from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views import generic
from posts.models import Posts
from django.urls import reverse_lazy
from posts.forms import CreatePostForm

class PostListView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'Postt/post.html'
    
class PostCreateView(generic.CreateView):
    model = Posts
    template_name = 'Postt/createpost.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts:posts_blog')

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'Postt/apagarpost.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('posts:posts_blog')

class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'Postt/editarpost.html'
    fields = ['text', 'imagem']
    success_url = reverse_lazy('posts:posts_blog')