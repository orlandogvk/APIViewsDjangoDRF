from django.urls import path

from profesores.views import profesor, ProfesorListView, ProfesoresDetail

app_name = 'profesores'
urlpatterns = [
    # path('', profesores),
    path('view/', ProfesorListView.as_view()),
    path('view/<int:pk>', ProfesoresDetail.as_view()),
    path('<profesor_id>/', profesor)
]

