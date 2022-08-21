from venv import CORE_VENV_DEPS
from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    numero_tarjeta = models.IntegerField()
    cvv = models.IntegerField()
    fecha_emision = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    tipo_tarjeta = models.TextField(max_length=20)
    marca_tarjeta = models.TextField(max_length=20)
    account_id = models.IntegerField()
    customer_id = models.IntegerField()

class Meta:
    ordering = ("-customer_id",)
    verbose_name = "Tarjeta"
    verbose_name_plural = "Tarjetas"

def __str__(self):
    return self.title