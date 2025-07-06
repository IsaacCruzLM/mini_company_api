"""Admin configuration for the transactions app."""
from django.contrib import admin

from .models import TagTransactions, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin interface for Transaction model."""

    list_display = ["title", "company", "status", "created_at"]
    list_filter = ["status", "company", "created_at"]
    search_fields = ["title", "description"]
    ordering = ["-created_at"]


@admin.register(TagTransactions)
class TagTransactionsAdmin(admin.ModelAdmin):
    """Admin interface for TagTransactions model."""

    list_display = ["name", "color", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]
    ordering = ["-created_at"]
    filter_horizontal = ["transactions"]
