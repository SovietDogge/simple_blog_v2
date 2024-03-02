from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data, **kwargs):
        password = validated_data.pop('password')

        user = User.objects.create_user(**validated_data)
        user.set_password(make_password(password))
        user.save()
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password')
        return data


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class UserDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password')


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
