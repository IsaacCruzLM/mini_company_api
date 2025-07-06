"""Models for the project app."""
from django.db import models

from apps.companies.models import Company
from apps.transactions.models import Transaction


# Create your models here.
class Project(models.Model):
    """Model representing a project in the system."""

    STATUS_CHOICES = [
        ("not_started", "Not Started"),
        ("analyzing", "Analyzing"),
        ("in_development", "In Development"),
        ("testing", "Testing"),
        ("finished", "Finished"),
    ]

    title = models.CharField(max_length=255)
    notes = models.TextField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="projects"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="not_started"
    )
    conclusion = models.BooleanField(default=False)
    transactions = models.ManyToManyField(
        Transaction, related_name="projects", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the project."""
        return f"{self.title} - {self.company.name}"

    class Meta:
        """Meta class for Project model."""

        verbose_name = "Project"
        verbose_name_plural = "Projects"
