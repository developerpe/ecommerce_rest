from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self,value):
        # custom validation
        if 'developer' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')

        return value

    def validate_email(self,value):
        # custom validation
        if value == '':
            raise serializers.ValidationError('Tiene que indicar un correo')
        
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('El email no puede contener el nombre')

        return value

    def validate(self,data):
        return data


    def create(self,validated_data):
        return self.model.objects.create(**validated_data)