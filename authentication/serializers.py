from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .model import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('username','password')
