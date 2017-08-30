from django.contrib import admin
from marcas.models import (
    Marca, Modelo)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    pass
