from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from estudiantes.models import Estudiante
from estudiantes.serializers import EstudianteSerializer


# GET, POST, PUT, DELETE Generic

class EstudianteListView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

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
def estudiante(request,estudiante_id):

    estudiante_obj = get_object_or_404(Estudiante, id=estudiante_id)

    if request.method == 'GET':
        serialized = EstudianteSerializer(estudiante_obj)
        return Response(status=status.HTTP_201_CREATED, data=serialized.data)
    elif request.method == 'PUT':
        serialized = EstudianteSerializer(instance=estudiante_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=estudiante.errors)
    elif request.method == 'DELETE':
        estudiante_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
