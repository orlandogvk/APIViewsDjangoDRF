from django.urls import path

from materias.views import materia, MateriaListView, MateriasDetail

app_name = 'materias'
urlpatterns = [
    # path('', materias),
    path('view/', MateriaListView.as_view()),
    path('view/<int:pk>', MateriasDetail.as_view()),
    path('<materia_id>/', materia)
]

