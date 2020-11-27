from django.db import models
from estudiantes.models import Estudiante


# Create your models here.



class Materia(models.Model):
    nombre=models.CharField(max_length=200)
    salon=models.CharField(max_length=12)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    estudiantes = models.ManyToManyField(Estudiante, related_name='estudiantes')

    def __str__(self):
        return self.nombre

