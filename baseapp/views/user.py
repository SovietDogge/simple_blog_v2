from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from baseapp.models import Follows
from baseapp.serializers import UserViewSerializer, FollowersSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        serializer = UserViewSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=['POST'],
        detail=False,
        url_path=r'(?P<username>[\w-]+)/follow'
    )
    def create_follow(self, request, username=None):
        if request.user.is_authenticated:
            leader = User.objects.filter(username=request.data['username']).get()
            bound = Follows.objects.create(follower=request.user,
                                           leader=leader)
            return Response(FollowersSerializer(bound).data)
        else:
            return Response('User is not authenticated')

    def destroy(self, request, pk=None):
        if request.user.is_authenticated:
            request.user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

