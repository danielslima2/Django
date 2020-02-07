from django.urls import path
from posts.views import PostListView, PostCreateView, PostDeleteView, PostUpdateView

app_name = 'posts'

urlpatterns = [
    path('posts',PostListView.as_view() ,name='posts_blog'),
    path('criarpost', PostCreateView.as_view(), name='criar_posts'),
    path('posts/<int:pk>/apagar', PostDeleteView.as_view(), name = 'apagar_post'),
    path('posts/<int:pk>/editar', PostUpdateView.as_view(), name= 'editar_post'),
]