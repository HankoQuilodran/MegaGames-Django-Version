from django.urls import path
from . import views

urlpatterns = [
    path("dash/", views.index, name="dash"),
    path("videojuegos/", views.videojuegos, name="videojuegos"),
    path("consolas/", views.consolas, name="consolas"),
    path("users/", views.users, name="users"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
]