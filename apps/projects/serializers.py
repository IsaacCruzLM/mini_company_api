"""Serializers for the projects app models."""
from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the Project model."""

    class Meta:
        """Meta class to define model and fields for serialization."""

        model = Project
        fields = [
            "id",
            "title",
            "notes",
            "company",
            "status",
            "conclusion",
            "transactions",
            "created_at",
        ]
