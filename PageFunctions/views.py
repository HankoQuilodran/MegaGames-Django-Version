from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegistry, VideojuegoForm, ConsolaForm
from .models import Videojuego, Consola


@login_required
def index(request):
    videojuegos = Videojuego.objects.all()
    users = User.objects.all()
    consolas = Consola.objects.all()
    videojuegos_cantidad = len(Videojuego.objects.all())
    users_cantidad = len(User.objects.all())
    consolas_cantidad = len(Consola.objects.all())

    context = {
        "title": "Pagina principal",
        "videojuegos": videojuegos,
        "usuarios": users,
        "consolas": consolas,
        "videojuegos_cantidad": videojuegos_cantidad,
        "usuarios_cantidad": users_cantidad,
        "consolas_cantidad": consolas_cantidad
    }
    return render(request, "index.html", context)

def videojuegos(request):
    videojuegos = Videojuego.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("videojuegos")
    else:
        form = VideojuegoForm()
    context = {"title": "videojuegos",
               "videojuegos": videojuegos,
               "form": form}
    return render(request, "videojuegos.html", context)

def consolas(request):
    consolas = Consola.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = ConsolaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("consolas")
    else:
        form = ConsolaForm()
    context = {"title": "consola",
               "consolas": consolas,
               "form": form}
    return render(request, "consolas.html", context)


@login_required
def users(request):
    users = User.objects.all()
    context = {"title": "Usuarios", "usuarios": users}
    return render(request, "users.html", context)

def user(request):
    context = {"profile": "User Profile"}
    return render(request, "user.html", context)

def register(request):
    if request.method == "POST":
        form = UserRegistry(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistry()
    context = {"register": "Register", "form": form}
    return render(request, "register.html", context)


@login_required(login_url='acceso_usuario')
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def carrito(request):
    videojuegos = Videojuego.objects.all()
    context = {
        "title": "Pagina principal",
        "videojuegos": videojuegos}
    return render(request, "carrito.html", context)