from django.core.management.base import BaseCommand

from backend.cron import cleanup_inventory_logs as cleanup_func


class Command(BaseCommand):
    help = 'Delete old InventoryLog records while keeping the latest record per station.'

    def handle(self, *args, **options):
        deleted_count = cleanup_func()
        self.stdout.write(self.style.SUCCESS(
            f'Deleted {deleted_count} old InventoryLog records.'
        ))
