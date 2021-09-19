from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProf
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        #password
        user.save()
        Token.objects.create(user=user)
        return user

class UserProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProf
        fields = '__all__'