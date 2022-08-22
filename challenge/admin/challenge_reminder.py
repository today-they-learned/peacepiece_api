from django.contrib import admin

from config.admin import linkify
from challenge.models import ChallengeReminder


@admin.register(ChallengeReminder)
class ChallengeReminderAdmin(admin.ModelAdmin):
    """Admin View for ChallengeReminder"""

    list_display = (
        "id",
        linkify("user"),
        linkify("category"),
    )

    ordering = ("user",)
