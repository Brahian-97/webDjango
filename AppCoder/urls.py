from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('', inicio),
    path('cursos/',cursos),
    path('entregables/', entregables),
    path('estudiantes/',estudiantes),
    path('profesores/', profesores),
    path('home/',home),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiante/', buscar_estudiante),
]

