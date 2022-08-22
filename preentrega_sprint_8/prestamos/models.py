from asyncio.windows_events import NULL
from django.db import models
from django.utils import timezone
# Create your models here.

class Prestamo(models.Model):

    loan_total=models.FloatField(default=0)
    loanType=models.TextField(max_length=40, default='Personales')
    loan_month=models.IntegerField(default=1)
    id_cliente=models.IntegerField(default= NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created_at",) 
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"

    def __str__(self):
        return self.loan_total,self.created_at