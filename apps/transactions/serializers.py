"""Serializers for the transactions app models."""
from rest_framework import serializers

from .models import TagTransactions, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for the Transaction model."""

    class Meta:
        """Meta class to define model and fields for serialization."""

        model = Transaction
        fields = ["id", "title", "description", "company", "status", "created_at"]


class TagTransactionsSerializer(serializers.ModelSerializer):
    """Serializer for the TagTransactions model."""

    class Meta:
        """Meta class to define model and fields for serialization."""

        model = TagTransactions
        fields = ["id", "name", "color", "transactions", "created_at"]
