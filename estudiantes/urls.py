from django.urls import path

from estudiantes.views import estudiante, EstudianteListView, EstudianteDetail

app_name = 'estudiantes'
urlpatterns = [
    # path('', estudiantes),
    path('view/', EstudianteListView.as_view()),
    path('view/<int:pk>', EstudianteDetail.as_view()),
    path('<estudiante_id>/', estudiante)
]



