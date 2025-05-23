"""Users app configuration."""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration class for users application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
