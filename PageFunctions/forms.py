from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Videojuego, Consola


class UserRegistry(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = [
            "juego_nombre",
            "juego_precio",
            "juego_descripcion",
            "juego_cantidad",
            "juego_estado",
            "juego_image"
        ]

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = [
            "consola_nombre",
            "consola_precio",
            "consola_descripcion",
            "consola_cantidad",
            "consola_estado",
            "consola_image"
        ]
