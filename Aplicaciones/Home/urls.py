# Importar path
from django.urls import path
# Importar las views
from .import views

# Crear un arreglo
urlpatterns = [
    path('',views.portada, name='portada'),
    #Indice Kathe
    path('indice/',views.indice, name='indice'),
    #Nosotros Kathe
    path('nosotros/',views.nosotros, name='nosotros'),
    #Registro Xav
    path('registro/',views.registro, name='registro'),
    #LOGIN
    path('validarLogeo/',views.validarLogeo, name='validarLogeo'),

    # CERRAR SESION
    path('cerrarSesion/',views.cerrarSesion, name='cerrarSesion'),

    #*********************************************USUARIO***********************************************
    # INSERTAR
    path('insertarUsuario/',views.insertarUsuario, name='insertarUsuario'),

    # TEMPLATE UNIDADES
    path('unidadUno/',views.unidadUno, name='unidadUno'),
]

