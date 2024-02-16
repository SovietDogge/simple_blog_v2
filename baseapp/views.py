from rest_framework import viewsets
from rest_framework.response import Response

from baseapp.serializers import CustomUserSerializer


class FollowersViewSet(viewsets.ViewSet):

    def create(self, request):
        pass


class CustomUserViewSet(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        return Response(CustomUserSerializer(data))
