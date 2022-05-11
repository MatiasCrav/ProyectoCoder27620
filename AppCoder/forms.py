from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormCurso(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()


class FormRegistrarse(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "email...", "style": "background-color: antiquewhite"}
        )
    )
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita la contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
