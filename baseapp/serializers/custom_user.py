from django.contrib.auth.models import User
from rest_framework import serializers

from .user import UserCreateSerializer, UserDeleteSerializer, UserDetailViewSerializer
from ..models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        custom_user = CustomUser.objects.create(user=user, **validated_data)
        return custom_user


class CustomUserDeleteSerializer(serializers.ModelSerializer):
    user = UserDeleteSerializer()

    class Meta:
        model = CustomUser
        fields = ('id', )


class CustomUserDetailViewSerializer(serializers.ModelSerializer):
    user = UserDetailViewSerializer()

    class Meta:
        model = CustomUser
        fields = ('description', 'user')
