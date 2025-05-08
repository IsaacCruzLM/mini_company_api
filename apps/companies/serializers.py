"""Serializers for the companies app models."""
from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for the Company model."""

    class Meta:
        """Meta class to define model and fields for serialization."""

        model = Company
        fields = ["id", "name", "created_at", "users"]
