from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.response import Response

from baseapp.models import CustomUser
from baseapp.serializers import CustomUserCreateSerializer, CustomUserDetailViewSerializer


class CustomUserRegistrateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer


class CustomUserDetailView(viewsets.ViewSet):
    queryset = CustomUser.objects.all()

    lookup_field = 'username'

    def retrieve(self, request, username=None):
        user = CustomUser.objects.filter(user__username=username).select_related('user').get()
        user_data = CustomUserDetailViewSerializer(user).data
        return Response(user_data)
