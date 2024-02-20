from django.contrib.auth.models import User
from rest_framework import generics, viewsets
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
            return 'No such a user'
