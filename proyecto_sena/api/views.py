from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuarios

# Vista para listar los usuarios
class ListarUsuarios(ListView):
    model = Usuarios
    template_name = 'usuario/listar.html'
    context_object_name = 'usuario'

# Vista para crear un usuario nuevo
class CrearUsuarios(CreateView):
    model = Usuarios
    fields = ['nombre', 'correo', 'cargo']
    template_name = 'usuario/formusuarios.html'
    success_url = reverse_lazy('listar_usuario')

# Vista para actualizar un usuario existente
class ActualizarUsuarios(UpdateView):
    model = Usuarios
    fields = ['nombre', 'correo', 'cargo']
    template_name = 'usuario/formusuarios.html'
    success_url = reverse_lazy('listar_usuario')

# Vista para eliminar un usuario
class EliminarUsuarios(DeleteView):
    model = Usuarios
    template_name = 'usuario/confirmar.html'
    success_url = reverse_lazy('listar_usuario')