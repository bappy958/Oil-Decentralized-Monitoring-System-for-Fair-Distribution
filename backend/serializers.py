from rest_framework import serializers
from .models import Station, InventoryLog, Transaction

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'location', 'capacity', 'is_online', 'last_sync']

class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = ['id', 'station', 'level_liters', 'timestamp']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'station', 'transaction_id', 'amount_liters', 'timestamp', 'blockchain_hash', 'is_verified']
