from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from materias.serializers import MateriaSerializer
from materias.models import Materia


# GET, POST, PUT, DELETE Generic

class MateriaListView(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class MateriasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

# @api_view(['GET', 'POST'])
# def estudiantes(request):
#     if request.method =='GET':
#         estudiantes = Estudiante.objects.all()
#         serialized = EstudianteSerializer(estudiantes, many=True)
#         return Response(status=status.HTTP_200_OK, data=serialized.data)
#     elif request.method == 'POST':
#         estudiante=EstudianteSerializer(data=request.data)
#         if estudiante.is_valid():
#             estudiante.save()
#             return Response(status=status.HTTP_201_CREATED, data={'detail': 'Created'})
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=estudiante.errors)

@api_view(['GET', 'PUT', 'DELETE'])

def materia(request,materia_id):

    materia_obj = get_object_or_404(Materia, id=materia_id)

    if request.method == 'GET':
        serialized = MateriaSerializer(materia_obj)
        return Response(status=status.HTTP_201_CREATED, data=serialized.data)
    elif request.method == 'PUT':
        serialized = MateriaSerializer(instance=materia_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=materia.errors)
    elif request.method == 'DELETE':
        materia_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
