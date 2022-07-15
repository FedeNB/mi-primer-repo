from django.contrib import admin
from django.urls import path
from mi_app.views import saludar_a, listar_cursos, listar_estudiantes, mostrar_index



urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('saludar/persona/<nombre>', saludar_a),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),

]
