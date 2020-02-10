from django.urls import path
from usuario.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserDetailView, UserLoginView, UserLogoutView
app_name = 'usuario'

urlpatterns = [
    path('usuario',UserListView.as_view() ,name='listar_usuarios'),
    path('criarusuario', UserCreateView.as_view(), name='criar_usuario'),
    path('usuario/<int:pk>/editar', UserUpdateView.as_view(), name= 'editar_usuario'),
    path('usuario/<int:pk>/apagar', UserDeleteView.as_view(),name= 'apagar_usuario'),
    path('usuario/<int:pk>/detalhes', UserDetailView.as_view(), name= 'detalhes_usuario'),
    path('loginusuario', UserLoginView.as_view(), name = 'login_usuario'),
    path('logoutusuario', UserLogoutView.as_view(), name = 'logout_usuario'),
]