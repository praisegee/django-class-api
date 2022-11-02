from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "last_login"]


class PostSerializer(serializers.ModelSerializer):
    creator = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = "__all__"
