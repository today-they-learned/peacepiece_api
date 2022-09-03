from django.contrib import admin

from config.admin import linkify
from item.models import ItemCondition


@admin.register(ItemCondition)
class ItemConditionAdmin(admin.ModelAdmin):
    """Admin View for ItemCondition"""

    list_display = (
        "id",
        linkify("item"),
        linkify("pre_item_condition"),
        "max_count",
    )

    ordering = ("item",)
