from django.shortcuts import render
from usuario.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from usuario.forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'Usuario/usuario.html'

class UserCreateView(CreateView):
    model = User
    template_name = 'Usuario/create.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('usuario:listar_usuarios')

class UserUpdateView(UpdateView):
    model = User
    template_name = 'Usuario/editarusuario.html'
    fields = ['username', 'email','password']
    success_url = reverse_lazy('usuario:listar_usuarios')
    
class UserDeleteView(DeleteView):
    model= User
    template_name = 'Usuario/apagarusuario.html'
    context_object_name = 'usuario'
    success_url = reverse_lazy('usuario:listar_usuarios')

class UserDetailView(DetailView):
    model = User
    template_name = 'Usuario/detalhesusuario.html'
    context_object_name = 'users'

class UserLoginView(LoginView):    
    template_name = "Usuario/loginusuario.html"


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass