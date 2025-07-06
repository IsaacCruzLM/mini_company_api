"""Admin configuration for the projects app."""
from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for Project model."""

    list_display = ["title", "company", "status", "conclusion", "created_at"]
    list_filter = ["status", "conclusion", "company", "created_at"]
    search_fields = ["title", "notes"]
    ordering = ["-created_at"]
    filter_horizontal = ["transactions"]
