from django.db import models

# CREAR CLASE USUARIO
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=30)
    segundoNombre = models.CharField(max_length=30)
    apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fotografia = models.FileField(upload_to='usuarios', null=True,blank=True)
    email = models.CharField(max_length=50)
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=10)
    rol = models.CharField(max_length=15)

    # Mejorar presentacion de los datos
    def __str__(self):
        fila = "{0}: {1} {2} - {3}"
        return fila.format(self.id,self.primerNombre,self.apellidoPaterno,self.rol)
    