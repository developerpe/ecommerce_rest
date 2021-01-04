from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'nombre_usuario': instance['username'],
            'correo_electronico': instance['email'],
            'clave': instance['password']
        }


