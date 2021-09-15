# from rest_framework import serializers
# from .models import NewUser
# from rest_framework.authtoken.models import Token

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewUser
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
#     def create(self, validated_data):
#         profile = NewUser.objects.create_user(**validated_data)
#         Token.objects.create(user=profile)
#         return profile