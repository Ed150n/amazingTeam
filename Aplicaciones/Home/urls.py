# Importar path
from django.urls import path
# Importar las views
from .import views

# Crear un arreglo
urlpatterns = [
    path('',views.portada, name='portada'),
    #Indice Kathe
    path('indice/',views.indice,name='indice'),
]

