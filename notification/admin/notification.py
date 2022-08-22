from django.contrib import admin

from notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin View for Notification"""

    list_display = (
        "user",
        "category",
        "created_at",
        "updated_at",
    )
    ordering = ("created_at", "updated_at")
