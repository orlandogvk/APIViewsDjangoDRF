from django.contrib import admin
from materias.models import Materia
# Register your models here.



class MateriasAdmin(admin.ModelAdmin):
    list_display =("nombre","salon")
    search_fields =("nombre",)

admin.site.register(Materia,MateriasAdmin)

