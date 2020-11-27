from django.db import models

# Create your models here.



class Estudiante(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    direccion=models.CharField(max_length=300)
    telefono=models.CharField(max_length=12)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre



