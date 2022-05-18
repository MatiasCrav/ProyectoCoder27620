from django.db import models
from django.contrib.auth.models import User


# Heredamos de models.Model para que la clase sea un "modelo" y se use para crear una
# tabla en la base de datos. Cada vez que se hace un cambio hay que correr
# "python manage.py makemigrations" y "python manage.py migrate" para aplicarlos a la bd.
class Profesor(models.Model):
    # CharField = campo de texto
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    profesion = models.CharField(max_length=200)
    # EmailField = campo de email
    email = models.EmailField(max_length=200)
    # Hay más tipos de campos: Integer (números enteros), Date (fecha), etc...

    def __str__(self):
        return f"[Profe] {self.nombre} {self.apellido}"

    # Para que diga 'Profesores' en lugar de 'Profesors' en el admin
    class Meta:
        verbose_name_plural = "profesores"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()

    # Podemos crearles __str__ como cualquier clase
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.comision}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        if self.entregado:
            return f"{self.nombre} ✔"
        else:
            return f"{self.nombre} ✘"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)