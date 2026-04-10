from django.contrib import admin

# Register your models here.

from .models import Station, InventoryLog, Transaction

admin.site.register(Station)
admin.site.register(InventoryLog)      
admin.site.register(Transaction)
