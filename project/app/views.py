from rest_framework import viewsets, permissions, authentication
from django.contrib.auth.models import User
from .models import UserProf
from .serializers import UserSerializer, UserProfSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)


class UserProfViewSet(viewsets.ModelViewSet):
    queryset = UserProf.objects.all()
    serializer_class = UserProfSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

