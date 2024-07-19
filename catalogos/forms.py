from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#____ Contactos y comentarios
class Contacto(forms.Form):
    apellido = forms.CharField(max_length=50, required=True)
    ciudad   = forms.CharField(max_length=50, required=True)
    pais     = forms.CharField(max_length=50, required=True, label="País")
    correo   = forms.CharField(max_length=50, required=True)
    telefono = forms.CharField(max_length=50, required=True, label="Teléfono")
    mensaje  = forms.CharField(widget=forms.Textarea, max_length=500)

#____ Login y Registro
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, label="Nombre")
    last_name = forms.CharField(max_length=50, label="Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]

class UserEditForm(UserChangeForm):
    email =forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

#____ Avatar
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
