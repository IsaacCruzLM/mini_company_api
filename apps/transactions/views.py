"""Views for the transactions app."""

from rest_framework import viewsets

from .models import TagTransactions, Transaction
from .serializers import TagTransactionsSerializer, TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing transaction instances."""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TagTransactionsViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing tag transactions instances."""

    queryset = TagTransactions.objects.all()
    serializer_class = TagTransactionsSerializer
