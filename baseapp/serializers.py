from rest_framework import serializers
from django.contrib.auth.models import User

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        custom_user = CustomUser.objects.create(user=user, **validated_data)
        return custom_user
