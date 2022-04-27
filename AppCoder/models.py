from django.db import models


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


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    # Podemos crearles __str__ como cualquier clase
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
