from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from baseapp.models import Follows
from baseapp.serializers import FollowersSerializer


class FollowsViewSet(viewsets.ViewSet):
    queryset = Follows.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            leader = User.objects.filter(username=request.data['username']).get()
            bound = Follows.objects.create(follower=request.user,
                                           leader=leader)
            return Response(FollowersSerializer(bound).data)
        else:
            return Response('User is not authenticated')

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            follows = Follows.objects.filter(follower=request.user.id)
            return Response(FollowersSerializer(follows, many=True).data)

        else:
            return Response('User is not authenticated')

