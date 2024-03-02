from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .follows import FollowersSerializer
from .user import UserCreateSerializer, UserDeleteSerializer, UserDetailViewSerializer
from ..models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create(password=make_password(password), **user_data)
        custom_user = CustomUser.objects.create(user=user, **validated_data)
        return custom_user


class CustomUserDeleteSerializer(serializers.ModelSerializer):
    user = UserDeleteSerializer()

    class Meta:
        model = CustomUser
        fields = ('id', )


class CustomUserDetailViewSerializer(serializers.ModelSerializer):
    user = UserDetailViewSerializer()
    # user_follow = FollowersSerializer()

    class Meta:
        model = CustomUser
        fields = ('description', 'user',
                  # 'user_follow'
                  )
