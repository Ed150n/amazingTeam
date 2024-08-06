from django.shortcuts import render,redirect
# tokens CSRF
from django.views.decorators.csrf import csrf_exempt

# Se usa para que solo usuarios autenticados pueden acceder a un template
from django.contrib.auth.decorators import login_required

#Importar los modelos
from Aplicaciones.Home.models import Usuario # Model Usuario de Home

# Create your views here.
@login_required
def inicio(request):
    return render(request,'inicio.html')

# Renderizar lista de usuarios
@login_required
def listadoUsuarios(request):
    usuariosBdd = Usuario.objects.all()
    return render(request,"listadoUsuarios.html",{'usuarios':usuariosBdd})