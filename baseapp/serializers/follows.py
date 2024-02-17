from rest_framework import serializers

from baseapp.models import Follows


class FollowersSerializer(serializers.ModelSerializer):
    follower = serializers.CharField(source='follower.username')
    leader = serializers.CharField(source='leader.username')

    class Meta:
        model = Follows
        exclude = ('id', )
