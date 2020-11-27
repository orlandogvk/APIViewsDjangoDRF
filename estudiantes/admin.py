from django.contrib import admin
from estudiantes.models import Estudiante

# Register your models here.



class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "direccion", "telefono")
    search_fields = ("nombre", "apellido")

admin.site.register(Estudiante,EstudiantesAdmin)


