from django.db import models
from email.policy import default
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    usuario_email = models.CharField(max_length=50)
    usuario_direccion = models.CharField(max_length=150)
    usuario_telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Contrato(models.Model):
    rol = models.CharField(max_length=3)

    def __str__(self):
        return self.rol


class EmpleadoProfile(models.Model):
    empleado = models.OneToOneField(User, on_delete=models.CASCADE)
    empleado_email = models.CharField(max_length=50)
    empleado_direccion = models.CharField(max_length=150)
    empleado_telefono = models.CharField(max_length=15)
    empleado_sueldo = models.PositiveIntegerField()
    empleado_contrato = models.OneToOneField(Contrato, on_delete=models.CASCADE)

    def __str__(self):
        return self.empleado


class Videojuego(models.Model):
    juego_id = models.AutoField(primary_key=True)
    juego_nombre = models.CharField(max_length=50, default="")
    juego_precio=models.IntegerField()
    juego_descripcion=models.CharField( max_length=250)
    juego_cantidad= models.IntegerField()
    juego_estado = models.BooleanField(default=True)
    juego_image = models.ImageField(default="assets\\img\\GAME_DEFAULT.png", upload_to="assets\\img")
    
    def __str__(self):
        return self.juego_nombre


class Consola(models.Model):
    consola_id = models.AutoField(primary_key=True)
    consola_nombre = models.CharField(max_length=50, default="")
    consola_precio=models.IntegerField()
    consola_descripcion=models.CharField( max_length=250)
    consola_cantidad= models.IntegerField()
    consola_estado = models.BooleanField(default=True)
    consola_image = models.ImageField(default="assets\\img\\CONSOLA_DEFAULT.webp", upload_to="assets\\img")
    
    def __str__(self):
        return self.consola_nombre