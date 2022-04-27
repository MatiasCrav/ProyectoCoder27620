from django.urls import path

# views de AppCoder
from AppCoder import views

urlpatterns = [
    path("", views.inicio),
    path("crear_juan/", views.crear_estudiante),
    path("curso/", views.curso),
    path("entregable/", views.entregable),
    path("estudiante/", views.estudiante),
    path("profesor/", views.profesor),
    path("plantilla/", views.plantilla)
]