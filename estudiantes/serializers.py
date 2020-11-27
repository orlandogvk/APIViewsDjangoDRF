from rest_framework import serializers
from estudiantes.models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id', 'nombre', 'apellido', 'direccion', 'telefono')


