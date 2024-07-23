from django.shortcuts import render

# Create your views here.
def portada(request):
    return render(request,'Inicio/portada.html')

#Indice Kathe
def indice(request):
    return render(request,'Inicio/indice.html')

#nosotros Kathe
def nosotros(request):
    return render(request,'Inicio/nosotros.html')