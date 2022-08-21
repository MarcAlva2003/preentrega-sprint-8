from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_tarjetas.models import Tarjeta
from api_tarjetas.serializer import TarjetaSerializer

# Create your views here.
# OBTENER TARJETAS ASOCIADAS A UN CLIENTE
class TarjetasDeCliente(APIView):
    def get(self, request, customer_id):
        tarjeta = Tarjeta.objects.filter(customer_id=customer_id)
        serializer = TarjetaSerializer(tarjeta, many =  True)
        if tarjeta:
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)
    
# class TarjetasDeCliente(APIView):
#     def get(self, request):
#         libros = Tarjeta.objects.all().order_by('created_at')
#         serializer = TarjetaSerializer(libros, many =  True)
#         return Response(serializer.data, status=status.HTTP_200_OK)