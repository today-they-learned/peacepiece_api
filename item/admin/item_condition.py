from django.contrib import admin

from item.models import ItemCondition
from config.admin import linkify


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
