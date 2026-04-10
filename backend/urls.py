from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StationViewSet, InventoryLogViewSet, TransactionViewSet, SensorUpdateViewSet

router = DefaultRouter()
router.register(r'stations', StationViewSet)
router.register(r'inventory-logs', InventoryLogViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'sensor-updates', SensorUpdateViewSet, basename='sensor-update')

urlpatterns = [
    path('', include(router.urls)),
]