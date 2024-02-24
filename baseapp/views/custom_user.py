from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from baseapp.models import CustomUser, Follows
from baseapp.serializers import CustomUserCreateSerializer, CustomUserDetailViewSerializer, FollowersSerializer


class CustomUserRegistrateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer


class CustomUserDetailView(viewsets.ViewSet):
    queryset = CustomUser.objects.all()

    lookup_field = 'username'

    def retrieve(self, request, username=None):
        user = (self.queryset.filter(user__username=username)
                .select_related('user')
                .get())
        user_data = CustomUserDetailViewSerializer(user).data
        return Response(user_data)

    @action(
        methods=['get'],
        detail=False,
        url_path=r'follows'
    )
    def get_user_follows(self, request):
        if request.user.is_authenticated:
            follows = Follows.objects.filter(follower=request.user.id)
            return Response(FollowersSerializer(follows, many=True).data)

        else:
            return Response('User is not authenticated')
