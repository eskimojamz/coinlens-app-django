from rest_framework import viewsets, permissions, authentication
from django.contrib.auth.models import User
from .models import UserProf
from .serializers import UserSerializer, UserProfSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfViewSet(viewsets.ModelViewSet):
    queryset = UserProf.objects.all()
    serializer_class = UserProfSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        user = UserProf.objects.get(user=self.request.user)
        serializer = UserProfSerializer(instance=user, data=request.data)
        
        serializer.save()

        return Response(serializer.data)