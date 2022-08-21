from rest_framework import serializers
from .models import Sucursal

#class SucursalSerializer(serializers.Serializer):
#    branch_number = serializers.CharField(max_length=10)
#    branch_name = serializers.CharField(max_length=50)
#    branch_address_id = serializers.CharField(max_length=5)
#    direccion_id = serializers.CharField(max_length=50)
#    created_at = serializers.DateTimeField(read_only=True)
#    updated_at = serializers.DateTimeField(read_only=True)

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
        read_only_fields = (
        "id",
        "created_at",
        "updated_at",
        )