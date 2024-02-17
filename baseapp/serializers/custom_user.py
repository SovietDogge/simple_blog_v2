from django.contrib.auth.models import User
from rest_framework import serializers

from .user import UserCreateSerializer
from ..models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        custom_user = CustomUser.objects.create(user=user, **validated_data)
        return custom_user
