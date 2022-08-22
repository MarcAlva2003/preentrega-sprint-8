from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    dni = models.IntegerField()
    direccion = models.TextField(max_length=50)
    tipo_cliente = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='clientes',on_delete=models.CASCADE)

class Meta:
    ordering = ("-created_at",)
    verbose_name = "Cliente"
    verbose_name_plural = "Clientes"

def __str__(self):
    return self.nombre