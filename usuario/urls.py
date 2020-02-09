from django.urls import path
from usuario.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView
app_name = 'usuario'

urlpatterns = [
    path('usuario',UserListView.as_view() ,name='listar_usuarios'),
    path('criarusuario', UserCreateView.as_view(), name='criar_usuario'),
    path('usuario/<int:pk>/editar', UserUpdateView.as_view(), name= 'editar_usuario'),
    path('usuario/<int:pk>/apagar', UserDeleteView.as_view(),name= 'apagar_usuario'),
]