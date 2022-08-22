from django.contrib import admin
from django.urls import path
from api_tarjetas.views import TarjetasDeCliente
from sucursales.views import SucursalLists,SucursalDetails
from prestamos.views import PrestamoPost,PrestamoDetails


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tarjetas-cliente/<int:customer_id>', TarjetasDeCliente.as_view()),
    path('api/sucursales/',SucursalLists.as_view()),
    path('api/sucursales/<int:pk>/',SucursalDetails.as_view()),
    path('api/prestamopost/', PrestamoPost.as_view()),
    path('api/prestamodelete/<int:pk>',PrestamoDetails.as_view()),

]
    