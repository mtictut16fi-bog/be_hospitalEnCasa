from rest_framework import serializers
from hospitalBackend.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'rol', 'username', 'password','nombre','apellido','e_mail','celular','direccion']