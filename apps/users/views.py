"""Views for users app."""

from rest_framework import generics, permissions

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserListView(generics.ListAPIView):
    """ViewSet for viewing and editing user instances."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
