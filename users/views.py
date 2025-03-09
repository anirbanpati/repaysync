from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.permissions import AllowAny

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
