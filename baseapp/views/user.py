from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from baseapp.serializers import UserViewSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        serializer = UserViewSerializer(self.queryset, many=True)
        return Response(serializer.data)
