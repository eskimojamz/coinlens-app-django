from rest_framework import viewsets, permissions, authentication
from .models import UserProf
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProf.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)