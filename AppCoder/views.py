from django.shortcuts import render, redirect

from AppCoder.models import Curso, Estudiante, Entregable
from django.http import HttpResponse
from .forms import FormCurso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def crear_estudiante(request):
    estudiante = Estudiante(
        nombre="Juancito", apellido="Perez", email="juan.perez@gmail.com"
    )
    # Con .save() guardamos la instancia en la bd.
    estudiante.save()
    return HttpResponse(f"Se creó a {estudiante.nombre} {estudiante.apellido}")


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {"cursos": cursos})


def entregables(request):
    return render(request, "AppCoder/entregables.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")


# Les dejo una plantilla genérica con bootstrap
def plantilla(request):
    return render(request, "layout.html")


def crear_curso(request):
    if request.method == "POST":
        form = FormCurso(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            nombre = info.get("nombre")
            comision = info.get("comision")
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            # Se puede usar redirect() de django.shortcuts que nos permite ir a otra
            # url por su 'name'
            return redirect("Cursos")

    form = FormCurso()
    return render(request, "AppCoder/formCurso.html", {"form": form})


def buscar_curso(request):
    return render(request, "AppCoder/busquedaComision.html")


def resultado_busqueda_curso(request):
    if request.GET.get("comision"):
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__iexact=comision)
        return render(
            request,
            "AppCoder/resultadoBusquedaCursos.html",
            {"cursos": cursos, "comision": comision},
        )

    return redirect("BuscarCurso")


def eliminar_curso(request, id):
    # Uso Modelo.objects.get(campo=valor) para obtener una instancia de la BD
    curso = Curso.objects.get(id=id)
    curso.delete()
    # Vuelvo a la lista
    return redirect("Cursos")


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormCurso(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            curso.nombre = info["nombre"]
            curso.comision = info["comision"]

            curso.save()
            return redirect("Cursos")
        else:
            # Hubo algún error
            ...

    print(curso.nombre)
    mi_form = FormCurso(initial={"nombre": curso.nombre, "comision": curso.comision})
    return render(request, "AppCoder/formCurso.html", {"form": mi_form})


def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, "AppCoder/ver_curso.html", {"curso": curso})


# Uso CBV para entregables
class ListarEntregables(ListView):
    model = Entregable
    template_name = "AppCoder/entregables.html"


class VerEntregable(DetailView):
    model = Entregable
    template_name = "AppCoder/ver_entregable.html"


class EditarEntregable(UpdateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class CrearEntregable(CreateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class EliminarEntregable(DeleteView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
