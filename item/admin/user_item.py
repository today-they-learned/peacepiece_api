from django.contrib import admin

from item.models import UserItem
from config.admin import linkify


@admin.register(UserItem)
class UserItemAdmin(admin.ModelAdmin):
    """Admin View for UserItem"""

    list_display = (
        "id",
        linkify("user"),
        linkify("item"),
        "count",
    )

    ordering = ("user",)
