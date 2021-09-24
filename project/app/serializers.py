from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import UserProf
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

class UserProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProf
        fields = '__all__'