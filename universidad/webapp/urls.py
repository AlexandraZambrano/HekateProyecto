from django.contrib import admin
from django.urls import path

from webapp.views import *

urlpatterns = [
    path('', login),
    path('registration/', registration),
    path('docente/', docente),
    path('perfil/', perfil),
    path('estudiantes/', estudiantes, name="estudiante"),
    path('estudiantes/NuevoEstudiante/', estudianteNuevo, name="nuevoEstudiante"),
    path('estudiantes/editar/<int:id>', editarEstudiante),
    path('estudiantes/eliminarestudiante/<int:id>', eliminarEstudiante),
]