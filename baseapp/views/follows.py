from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response

from baseapp.models import Follows
from baseapp.serializers import FollowersSerializer


class FollowsViewSet(generics.CreateAPIView):
    queryset = Follows
    serializer_class = FollowersSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            leader = User.objects.filter(id=request.data['user_id']).get()
            bound = self.queryset.objects.create(follower=request.user,
                                                 leader=leader)
            return Response(self.serializer_class(bound).data)
        else:
            return 'No such a user'
