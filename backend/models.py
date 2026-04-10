from django.db import models
from django.utils import timezone

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.FloatField(help_text="Total capacity in Liters")
    is_online = models.BooleanField(default=False)
    last_sync = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InventoryLog(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='logs')
    level_liters = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

class Transaction(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='transactions')
    transaction_id = models.CharField(max_length=50, unique=True)
    amount_liters = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)
    blockchain_hash = models.CharField(max_length=64, blank=True)
    is_verified = models.BooleanField(default=True)

    class Meta:
        ordering = ['-timestamp']
