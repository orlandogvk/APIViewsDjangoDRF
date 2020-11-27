from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profesores.models import Profesor
from profesores.serializers import ProfesorSerializer

# GET, POST, PUT, DELETE Generic

class ProfesorListView(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class ProfesoresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

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
def profesor(request,profesor_id):

    profesor_obj = get_object_or_404(Profesor, id=profesor_id)

    if request.method == 'GET':
        serialized = ProfesorSerializer(profesor_obj)
        return Response(status=status.HTTP_201_CREATED, data=serialized.data)
    elif request.method == 'PUT':
        serialized = ProfesorSerializer(instance=profesor_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=profesor.errors)
    elif request.method == 'DELETE':
        profesor_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
