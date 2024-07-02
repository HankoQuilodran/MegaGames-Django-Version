from django.contrib import admin
from .models import Videojuego,EmpleadoProfile, Consola, UserProfile

# Register your models here.

admin.site.site_header = "Sitio admin"

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("usuario", "usuario_email", "usuario_direccion", "usuario_telefono")
    search_fields = ["usuario"]

class EmpleadoProfileAdmin(admin.ModelAdmin):
    model = EmpleadoProfile
    list_display = ("empleado", "empleado_email", "empleado_direccion", "empleado_telefono", "empleado_sueldo", "empleado_contrato")
    search_fields = ["empleado"]

class VideojuegotAdmin(admin.ModelAdmin):
    model = Videojuego
    list_display = ("juego_nombre", "juego_precio", "juego_descripcion", "juego_cantidad", "juego_estado", "juego_image")
    search_fields = ["juego_nombre"]

class ConsolaAdmin(admin.ModelAdmin):
    model = Consola
    list_display = ("consola_nombre", "consola_precio", "consola_descripcion", "consola_cantidad", "consola_estado", "consola_image")
    search_fields = ["consola_nombre"]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmpleadoProfile, EmpleadoProfileAdmin)
admin.site.register(Videojuego, VideojuegotAdmin)
admin.site.register(Consola, ConsolaAdmin)