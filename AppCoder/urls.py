from django.urls import path

# views de AppCoder
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("cursos/", views.cursos, name="Cursos"),
    path("entregables/", views.ListarEntregables.as_view(), name="Entregables"),
    path("estudiantes/", views.estudiantes, name="Estudiantes"),
    path("profesores/", views.profesores, name="Profesores"),
    path("plantilla/", views.plantilla),
    path("ver_curso/<id>", views.ver_curso, name="VerCurso"),
    path("crear_curso/", views.crear_curso, name="CrearCurso"),
    path("cursos/buscar/", views.buscar_curso, name="BuscarCurso"),
    path("cursos/resultado_buscar/", views.resultado_busqueda_curso, name="ResultBuscarCurso"),

    path("eliminar_curso/<id>", views.eliminar_curso, name="EliminarCurso"),
    path("editar_curso/<id>", views.editar_curso, name="EditarCurso"),
    path("ver_entregable/<pk>", views.VerEntregable.as_view(), name="VerEntregable"),
    path("editar_entregable/<pk>", views.EditarEntregable.as_view(), name="EditarEntregable"),
    path("crear_entregable/", views.CrearEntregable.as_view(), name="CrearEntregable"),
    path("eliminar_entregable/<pk>", views.EliminarEntregable.as_view(), name="EliminarEntregable"),
]