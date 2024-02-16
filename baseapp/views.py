from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer


class FollowersViewSet(viewsets.ViewSet):

    def create(self, request):
        pass


class CustomUserViewSet(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

