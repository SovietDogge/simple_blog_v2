from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import CustomUser, Follows
from .serializers import FollowersSerializer, CustomUserSerializer


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


class CustomUserRegistrateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
