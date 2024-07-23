from django.shortcuts import render

# Create your views here.
def portada(request):
    return render(request,'Inicio/portada.html')