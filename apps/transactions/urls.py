"""URL configuration for the transactions app."""

from rest_framework.routers import DefaultRouter

from .views import TagTransactionsViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r"", TransactionViewSet)
router.register(r"tags", TagTransactionsViewSet)

urlpatterns = router.urls
