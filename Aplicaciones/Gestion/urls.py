# Importar path
from django.urls import path
# Importar las views
from .import views

# Crear un arreglo
urlpatterns = [ 
    path('inicio/',views.inicio, name='inicio'),
]