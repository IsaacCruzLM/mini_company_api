"""Serializers for users app."""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""

    class Meta:
        """Meta class for UserSerializer configuration."""

        model = get_user_model()
        fields = ("id", "username", "email")
