from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mi_app.models import Curso, Estudiante, Profesor
from mi_app.forms import CursoBusquedaFormulario, CursoFormulario, EstudianteFormulario, ProfesorFormulario

# Create your views here.


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola mundo {fecha_hora_ahora}")


def saludar_a(request, nombre):
    return HttpResponse(f"Hola, como  estas {nombre.capitalize()}")



def mostrar_index(request):
    return render(request, "mi_app/index.html", {})




def listar_cursos(request):
    context = {}

    context["cursos"] = Curso.objects.all()
    return render(request, "mi_app/lista_cursos.html", context)


def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)

def listar_profesores(request):
    context = {}
    context["profesores"] = Profesor.objects.all()
    return render(request, "mi_app/lista_profesores.html", context) 


def formulario_curso(request):

    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()

            return render(request, "mi_app/curso_formulario.html", {"mensaje":"agregado con exito!"})
    else:
        mi_formulario = CursoFormulario()
        return render(request, "mi_app/curso_formulario.html", {"mi_formulario": mi_formulario})




def formulario_estudiante(request):

    if request.method == "POST":
        mi_formulario_estudiante = EstudianteFormulario(request.POST)
        if mi_formulario_estudiante.is_valid:
            datos = mi_formulario_estudiante.cleaned_data
            estudiante = Estudiante(nombre=datos["nombre"], apellido=datos["apellido"], email=datos["email"])
            estudiante.save()

            return render(request, "mi_app/estudiante_formulario.html", {"mensaje":"agregado con exito!"})
    else:
        mi_formulario_estudiante = EstudianteFormulario()
        return render(request, "mi_app/estudiante_formulario.html", {"mi_formulario_estudiante": mi_formulario_estudiante})  





def formulario_profesor(request):

    if request.method == "POST":
        mi_formulario_profesor = ProfesorFormulario(request.POST)
        if mi_formulario_profesor.is_valid:
            datos = mi_formulario_profesor.cleaned_data
            profesor = Profesor(nombre=datos["nombre"], apellido=datos["apellido"], email=datos["email"])
            profesor.save()

            return render(request, "mi_app/profesor_formulario.html", {"mensaje":"agregado con exito!"})
    else:
        mi_formulario_profesor = ProfesorFormulario()
        return render(request, "mi_app/profesor_formulario.html", {"mi_formulario_profesor": mi_formulario_profesor}) 








def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()


    if request.GET:    
        busqueda_formulario = CursoBusquedaFormulario(request.GET)
        if busqueda_formulario.is_valid():
            cursos = Curso.objects.filter(nombre=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario, "cursos": cursos})


    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})






