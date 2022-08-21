from django.shortcuts import render


from sucursales.models import Sucursal
from sucursales.serializers import SucursalSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class SucursalLists(APIView):
    def post(self, request, format=None):
        serializer = SucursalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request): # nuevo
        libros = Sucursal.objects.all().order_by('created_at')
        serializer = SucursalSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# una sucursal
class SucursalDetails(APIView):
    def get(self, request, pk):
        sucursal = Sucursal.objects.filter(pk=pk).first()
        serializer = SucursalSerializer(sucursal)
        if sucursal:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#una sucursal