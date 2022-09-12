from config.admin import linkify
from django.contrib import admin

from notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin View for Notification"""

    list_display = (
        linkify("user"),
        linkify("contributor"),
        "notice_category",
        linkify("category"),
        linkify("challenge"),
        linkify("article"),
        "is_viewed",
        "created_at",
        "updated_at",
    )
    ordering = ("created_at", "updated_at")
