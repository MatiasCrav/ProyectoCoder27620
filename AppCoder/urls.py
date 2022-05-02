from django.urls import path

# views de AppCoder
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("crear_juan/", views.crear_estudiante),
    path("cursos/", views.cursos, name="Cursos"),
    path("entregables/", views.entregables, name="Entregables"),
    path("estudiantes/", views.estudiantes, name="Estudiantes"),
    path("profesores/", views.profesores, name="Profesores"),
    path("plantilla/", views.plantilla)
]