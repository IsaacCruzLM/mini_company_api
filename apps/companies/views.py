"""Views for the companies app."""

from rest_framework import viewsets

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing company instances."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
