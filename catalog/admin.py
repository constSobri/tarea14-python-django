from django.contrib import admin

# Register your models here.
from .models import Directores, Genero, Pelicula

admin.site.register(Pelicula)
admin.site.register(Directores)
admin.site.register(Genero)
