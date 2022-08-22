from django.contrib import admin

# Register your models here.

from .models import Prestamo

class PrestamoAdmin (admin.ModelAdmin):
    readonly_fields= ('created-at',)
admin.site.register(Prestamo)