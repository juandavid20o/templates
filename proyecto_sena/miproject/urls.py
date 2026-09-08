# Permite utilizar el panel de administración de Django.
from django.contrib import admin

# Importa include para incluir las URL de otra aplicación.
from django.urls import path, include

## importar las vistas de la app (ajustado)
from api.views import ListarUsuarios

# Lista donde se definen las URL principales del proyecto
urlpatterns = [
    # Ruta para acceder al panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Incluye todas las URL definidas en tu app 'api'
    path('', include('api.urls')),
]