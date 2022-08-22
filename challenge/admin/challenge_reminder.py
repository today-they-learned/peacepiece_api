from django.contrib import admin

from challenge.models import ChallengeReminder
from config.admin import linkify


@admin.register(ChallengeReminder)
class ChallengeReminderAdmin(admin.ModelAdmin):
    """Admin View for ChallengeReminder"""

    list_display = (
        "id",
        linkify("user"),
        linkify("category"),
    )

    ordering = ("user",)
