from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin (admin.ModelAdmin):
    admin.site.register(Cliente)
