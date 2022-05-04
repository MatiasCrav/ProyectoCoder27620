from django.shortcuts import render, redirect

from AppCoder.models import Curso, Estudiante
from django.http import HttpResponse
from .forms import FormCurso


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
    return render(request, "AppCoder/cursos.html")


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
