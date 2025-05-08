"""Models for the companies app."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Company(models.Model):
    """Model representing a company entity in the system."""

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name="companies")

    def __str__(self):
        """Return string representation of the company."""
        return self.name
