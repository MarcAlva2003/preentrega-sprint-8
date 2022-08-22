from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin (admin.ModelAdmin):
    readonly_fields = ('created-at','updated-at')
admin.site.register(Cliente)
