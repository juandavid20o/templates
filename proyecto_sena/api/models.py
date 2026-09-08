from django.db import models

# Definimos una clase llamada Usuarios.
class Usuarios(models.Model):
    # Crear los campos de la tabla.
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100, unique=True)
    cargo = models.CharField(max_length=50)

    # Este método define cómo se mostrará un objeto (retorna el nombre).
    def __str__(self):
        return self.nombre