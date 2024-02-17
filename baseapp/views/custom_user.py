from rest_framework import generics

from baseapp.models import CustomUser
from baseapp.serializers import CustomUserSerializer


class CustomUserRegistrateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
