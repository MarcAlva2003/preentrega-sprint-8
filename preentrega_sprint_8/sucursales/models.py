from django.db import models

class Sucursal(models.Model):
    branch_number = models.CharField(max_length=10)
    branch_name = models.CharField(max_length=50)
    branch_address_id = models.CharField(max_length=5)
    direccion_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
    def __str__(self):
        return self.branch_name
