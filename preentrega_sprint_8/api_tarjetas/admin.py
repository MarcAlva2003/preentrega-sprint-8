from django.contrib import admin
from .models import Tarjeta

# Register your models here.
class TarjetaAdmin (admin.ModelAdmin):
    readonly_fields= ('fecha_vencimiento')
    admin.site.register(Tarjeta)
