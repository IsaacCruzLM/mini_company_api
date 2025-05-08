"""Configuration module for the companies app."""
from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    """Configuration class for the companies application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.companies"
