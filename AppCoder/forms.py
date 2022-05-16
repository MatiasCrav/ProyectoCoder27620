from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormCurso(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()


class FormRegistrarse(UserCreationForm):
    email = forms.EmailField(
        # Se puede especificar como tiene que ser el widget y los atributos del tag en
        # el html
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


class FormEditarUsuario(UserCreationForm):
    # Les pongo a todos required=False para que no sean obligatorios
    username = forms.CharField(max_length=255, label="Username", required=False)
    email = forms.EmailField(label="Email", required=False)
    password1 = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, required=False
    )
    password2 = forms.CharField(
        label="Repita la contraseña", widget=forms.PasswordInput, required=False
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {k: "" for k in fields}
