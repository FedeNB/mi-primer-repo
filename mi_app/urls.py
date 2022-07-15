from django.contrib import admin
from django.urls import path
from mi_app.views import formulario_curso, saludar_a, listar_cursos, listar_estudiantes, mostrar_index, listar_profesores, formulario_curso, formulario_busqueda, formulario_estudiante, formulario_profesor  



urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('saludar/persona/<nombre>', saludar_a),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('listar-profesores/', listar_profesores),
    path('formulario-curso/', formulario_curso),
    path('formulario-buscar/', formulario_busqueda),
    path('formulario-estudiante/', formulario_estudiante),
    path('formulario-profesor/', formulario_profesor),
]







