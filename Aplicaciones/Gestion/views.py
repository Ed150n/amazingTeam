from django.shortcuts import render,redirect
# tokens CSRF
from django.views.decorators.csrf import csrf_exempt

# Se usa para que solo usuarios autenticados pueden acceder a un template
from django.contrib.auth.decorators import login_required
# Muestra mensajes
from django.contrib import messages

#Importar los modelos
from Aplicaciones.Home.models import Usuario # Model Usuario de Home

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

# Renderizar lista de usuarios

def listadoUsuarios(request):
    usuariosBdd = Usuario.objects.all()
    return render(request,"Usuario/listadoUsuarios.html",{'usuarios':usuariosBdd})
#RENDERIZAR FORMULARIO AGREGAR USUARIO
def nuevoUsuario(request):
    return render(request,'Usuario/nuevoUsuario.html')
# INSERTAR USUARIO
def insertarUsuario(request):
    primerNombre = request.POST["primerNombre"]
    segundoNombre = request.POST["segundoNombre"]
    apellidoPaterno = request.POST["apellidoPaterno"]
    apellidoMaterno = request.POST["apellidoMaterno"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    foto = request.POST.get("foto")
    email = request.POST["email"]
    usuario = request.POST["usuario"]
    contraseña = request.POST["contraseña"]
    rol = request.POST["rol"]
    Usuario.objects.create(primerNombre=primerNombre,segundoNombre=segundoNombre,apellidoPaterno=apellidoPaterno,
                                          apellidoMaterno=apellidoMaterno,direccion=direccion,telefono=telefono,fotografia=foto,
                                          email=email,usuario=usuario,contraseña=contraseña,rol=rol)
    messages.success(request,"Usuario registrado exitosamente")
    return redirect('registro')
#RENDERIZAR FORMULARIO EDITAR USUARIO
def editarUsuario(request,idUsuario):
    usuarioEditar = Usuario.objects.get(id=idUsuario)
    return render(request,'Usuario/editarUsuario.html',{'usuarioEditar':usuarioEditar})
# EDITAR USUARIO