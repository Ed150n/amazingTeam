from urllib import request
from django.shortcuts import render,redirect
from django.http import JsonResponse

# Libreria Autenticacion
from django.contrib.auth import authenticate, login,logout

# Se usa para que solo usuarios autenticados pueden acceder a un template
from django.contrib.auth.decorators import login_required

# Importe para mensajes
from django.contrib import messages
# tokens CSRF
from django.views.decorators.csrf import csrf_exempt
#Importar los modelos
from .models import Usuario

# Create your views here.
def portada(request):
    return render(request,'Inicio/portada.html')

# Registro Kathe/Xav
def registro(request):
    return render(request,'Inicio/registro.html')

# Indice Kathe
def indice(request):
    return render(request,'Inicio/indice.html')

# nosotros Kathe
def nosotros(request):
    return render(request,'Inicio/nosotros.html')
# unidadUno kathe


# FUNCION PARA CERRAR SESION
def cerrarSesion(request):
    logout(request)
    return redirect('portada')

# VALIDAR CORREO O USUARIO DEL LOGEO XAV
def validarLogeo(request):
    usu=request.POST["user"]
    con=request.POST["password"]

    producto = Usuario.objects.filter(usuario=usu,contraseña=con).first()
    if producto:
        messages.success(request,"Inicio de Sesión con exito.")
        return redirect('unidadUno')
    else:
        messages.error(request,"ERROR, Intente nuevamente.")
        return redirect('login')

#*******************************************USUARIO********************************************#

# Insertar con AJAX XAV
def insertarUsuario(request):
    primerNombre = request.POST["primerNombre"]
    segundoNombre = request.POST["segundoNombre"]
    apellidoPaterno = request.POST["apellidoPaterno"]
    apellidoMaterno = request.POST["apellidoMaterno"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    foto = request.FILES.get("foto")
    email = request.POST["email"]
    usuario = request.POST["usuario"]
    contraseña = request.POST["contraseña"]
    rol = request.POST["rol"]
    #Insercion
    Usuario.objects.create(primerNombre=primerNombre,segundoNombre=segundoNombre,apellidoPaterno=apellidoPaterno,
                                          apellidoMaterno=apellidoMaterno,direccion=direccion,telefono=telefono,fotografia=foto,
                                          email=email,usuario=usuario,contraseña=contraseña,rol=rol)
    messages.success(request,"Usuario registrado exitosamente")
    return redirect('registro')


# TEMPLATE UNIDADES
@login_required
def unidadUno(request):
    return render(request,'Unidades/unidadUno/unidadUno.html')

#kathe pagina1
@login_required
def paginaUno(request):
    return render(request, "Unidades/unidadUno/pagina1.html")
