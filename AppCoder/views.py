from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from AppCoder.models import Avatar, Curso, Entregable, Estudiante

from .forms import FormCurso, FormEditarUsuario, FormRegistrarse


def inicio(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)[0].imagen.url
        return render(request, "AppCoder/inicio.html", {"avatar": avatar})

    return render(request, "AppCoder/inicio.html")


@login_required
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


@login_required
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


@login_required
def eliminar_curso(request, id):
    # Uso Modelo.objects.get(campo=valor) para obtener una instancia de la BD
    curso = Curso.objects.get(id=id)
    curso.delete()
    # Vuelvo a la lista
    return redirect("Cursos")


@login_required
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


class EditarEntregable(LoginRequiredMixin, UpdateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class CrearEntregable(LoginRequiredMixin, CreateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class EliminarEntregable(LoginRequiredMixin, DeleteView):
    model = Entregable
    success_url = "/AppCoder/entregables/"


def registrarse(request):
    if request.method == "POST":
        form = FormRegistrarse(data=request.POST)
        if form.is_valid():
            form.save()
            # Uso el 'username' del form para obtener el usuario y loguearlo
            username = form.cleaned_data["username"]
            user = User.objects.get(username=username)
            login(request, user)

            # Vuelvo a inicio
            return redirect("Inicio")
        else:
            error = True

    else:
        error = False
        form = FormRegistrarse()

    return render(request, "AppCoder/registrarse.html", {"form": form, "error": error})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request, user)
                return redirect("Inicio")

    # Si no me enviaron datos o me los enviaron mal voy al form
    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"form": form})


# Puedo usar la funcion logout() de django.contrib.auth para cerrar sesión
def logout_request(request):
    logout(request)
    return redirect("Inicio")


@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        # Me guardo la info antes de pasarla al formulario para poder
        # chequear si el nombre de usuario es el mismo al de antes.
        post_data = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password1": request.POST.get("password1"),
            "password2": request.POST.get("password2"),
        }
        # Si es el mismo username lo mando vacio para que no me de error
        # por ya existir un usuario con ese username.
        if post_data.get("username") == usuario.username:
            post_data["username"] = None
        form = FormEditarUsuario(data=post_data)
        if form.is_valid():
            info = form.cleaned_data

            email = info.get("email")
            if email:
                usuario.email = email

            username = info.get("username")
            if username:
                usuario.username = username

            pass1 = info.get("password1")
            pass2 = info.get("password2")
            if pass1 and pass2:
                # uso set_password para setear la nueva contraseña encriptada
                usuario.set_password(pass1)
                # set password cierra sesion así que vuelvo a hacer login
                login(request, usuario)

            usuario.save()
            # Vuelvo a inicio
            return redirect("Inicio")
        else:
            error = True

    else:
        error = False
        form = FormEditarUsuario(
            # El form comienza con los campos propios completos
            # (excepto la contraseña)
            initial={
                "username": usuario.username,
                "email": usuario.email,
            }
        )

    return render(request, "AppCoder/formPerfil.html", {"form": form, "error": error})
