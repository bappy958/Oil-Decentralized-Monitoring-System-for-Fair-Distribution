import logging

from django.db.models import OuterRef, Subquery

from .models import InventoryLog

logger = logging.getLogger(__name__)


def cleanup_inventory_logs():
    """Delete old inventory logs while keeping the latest log per station."""
    latest_per_station = InventoryLog.objects.filter(
        station=OuterRef('station')
    ).order_by('-timestamp')

    latest_ids = InventoryLog.objects.filter(
        id=Subquery(latest_per_station.values('id')[:1])
    ).values_list('id', flat=True)

    deleted_count, _ = InventoryLog.objects.exclude(id__in=latest_ids).delete()
    logger.info(
        'Deleted %d old InventoryLog records while keeping the latest record per station.',
        deleted_count,
    )
    return deleted_count
