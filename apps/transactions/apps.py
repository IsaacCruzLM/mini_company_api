"""Configuration module for the transactions app."""
from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    """Configuration class for the transactions application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.transactions"
