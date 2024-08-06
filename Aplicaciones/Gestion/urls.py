# Importar path
from django.urls import path
# Importar las views
from .import views

# Crear un arreglo
urlpatterns = [ 
    path('inicio/',views.inicio, name='inicio'),
    
    #****************************************************USUARIO*********************************************************
    # LISTADO USUARIOS
    path('listadoUsuarios/',views.listadoUsuarios, name='listadoUsuarios'),
    # FORMULARIO NUEVO USUARIO
    path('nuevoUsuario/',views.nuevoUsuario, name='nuevoUsuario'),
    # INSERTAR USUARIO
    path('insertarUsuario/',views.insertarUsuario, name='insertarUsuario'),
    # FORMULARIO EDITAR USUARIO
    path('editarUsuario/<idUsuario>',views.editarUsuario, name='editarUsuario'),
]