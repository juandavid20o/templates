from django.urls import path
from .views import ListarUsuarios, CrearUsuarios, ActualizarUsuarios, EliminarUsuarios

urlpatterns = [
    path('', ListarUsuarios.as_view(), name='listar_usuario'),
    path('crear/', CrearUsuarios.as_view(), name='crear_usuario'),
    path('editar/<int:pk>/', ActualizarUsuarios.as_view(), name='actualizar_usuario'),
    path('eliminar/<int:pk>/', EliminarUsuarios.as_view(), name='eliminar_usuario'),
]