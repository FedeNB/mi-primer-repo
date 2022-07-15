from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField(required=True)
    camada = forms.IntegerField()


class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class CursoBusquedaFormulario(forms.Form):

    criterio = forms.CharField()