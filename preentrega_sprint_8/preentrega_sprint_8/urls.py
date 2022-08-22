from django.contrib import admin
from django.urls import path
from api_tarjetas.views import TarjetasDeCliente
from sucursales.views import SucursalLists,SucursalDetails
from clientes.views import ClienteLists,ClienteDetails,UserDetail,UserList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tarjetas-cliente/<int:customer_id>', TarjetasDeCliente.as_view()),
    path('api/sucursales/',SucursalLists.as_view()),
    path('api/sucursales/<int:pk>/',SucursalDetails.as_view()),
    path('api/clientes/',ClienteLists.as_view()),
    path('api/clientes/<int:pk>/',ClienteDetails.as_view()),
    path('api/users/', UserList.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),

]
    