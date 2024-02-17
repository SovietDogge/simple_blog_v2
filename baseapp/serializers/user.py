from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


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
