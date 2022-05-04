from django import forms

class FormCurso(forms.Form):
    nombre = forms.CharField(max_length=255)
    comision = forms.IntegerField()
