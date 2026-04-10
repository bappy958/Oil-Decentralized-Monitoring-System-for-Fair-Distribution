from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Station, InventoryLog, Transaction
from .serializers import StationSerializer, InventoryLogSerializer, TransactionSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    @action(detail=True, methods=['get'])
    def inventory_history(self, request, pk=None):
        station = self.get_object()
        logs = station.logs.all()[:50]  # Last 50 logs
        serializer = InventoryLogSerializer(logs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def recent_transactions(self, request, pk=None):
        station = self.get_object()
        txs = station.transactions.all()[:20]
        serializer = TransactionSerializer(txs, many=True)
        return Response(serializer.data)

class InventoryLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class SensorUpdateViewSet(viewsets.ViewSet):
    """
    Endpoint for NodeMCU to push sensor data
    """
    def create(self, request):
        station_id = request.data.get('station_id')
        level = request.data.get('level_liters')
        
        try:
            station = Station.objects.get(id=station_id)
            InventoryLog.objects.create(station=station, level_liters=level)
            station.is_online = True
            station.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        except Station.DoesNotExist:
            return Response({"error": "Station not found"}, status=status.HTTP_404_NOT_FOUND)
