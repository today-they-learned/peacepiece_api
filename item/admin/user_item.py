from django.contrib import admin

from config.admin import linkify
from item.models import UserItem


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
