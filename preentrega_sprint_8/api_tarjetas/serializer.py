from rest_framework import serializers
from .models import Tarjeta

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"
        read_only_fields = (
            "customer_id",
        )