"""Views for the projects app."""

from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing project instances."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
