from django.contrib import admin
from profesores.models import Profesor

# Register your models here.



class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "direccion", "telefono")
    search_fields = ("nombre", "apellido")

admin.site.register(Profesor,ProfesoresAdmin)


