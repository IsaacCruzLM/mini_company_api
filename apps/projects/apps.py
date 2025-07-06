"""Configuration module for the projects app."""
from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    """Configuration class for the projects application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.projects"
