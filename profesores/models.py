from django.db import models
from materias.models import Materia

# Create your models here.



class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    materias = models.ManyToManyField(Materia, related_name='materias')

