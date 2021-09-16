from rest_framework import viewsets
from .models import UserProf
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProf.objects.all()
    serializer_class = UserSerializer