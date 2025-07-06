"""Models for the transactions app."""
from django.db import models

from apps.companies.models import Company


# Create your models here.
class Transaction(models.Model):
    """Model representing a financial transaction in the system."""

    STATUS_CHOICES = [
        ("expense", "Expense"),
        ("income", "Income"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="transactions"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the transaction."""
        return f"{self.title} - {self.company.name}"


class TagTransactions(models.Model):
    """Model representing tags for financial transactions."""

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  # HEX color format #RRGGBB
    transactions = models.ManyToManyField(Transaction, related_name="tags", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the tag."""
        return self.name

    class Meta:
        """Meta class for TagTransactions model."""

        verbose_name = "Tag Transaction"
        verbose_name_plural = "Tag Transactions"
