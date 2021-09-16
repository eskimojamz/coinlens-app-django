from rest_framework import serializers
from .models import UserProf
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProf
        fields = ['id', 'username', 'email', 'password', 'followed_coins']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        user = UserProf.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user