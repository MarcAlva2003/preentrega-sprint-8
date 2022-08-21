from django.contrib import admin
from django.urls import path
from api_tarjetas.views import TarjetasDeCliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tarjetas-cliente/<int:customer_id>', TarjetasDeCliente.as_view()),
]
    