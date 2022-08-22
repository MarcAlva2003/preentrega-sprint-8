from rest_framework import serializers
from .models import Cliente
from django.contrib.auth.models import User

class ClienteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cliente
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "owner",
        )

class UserSerializer(serializers.ModelSerializer):
    clientes = serializers.PrimaryKeyRelatedField(many=True, queryset=Cliente.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'clientes']



