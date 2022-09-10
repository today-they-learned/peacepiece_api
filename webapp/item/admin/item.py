from django.contrib import admin
from item.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Admin View for Item"""

    list_display = (
        "id",
        "name",
        "point",
        "category",
    )

    ordering = ("point",)
