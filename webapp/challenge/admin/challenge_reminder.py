from challenge.models import ChallengeReminder
from config.admin import linkify
from django.contrib import admin


@admin.register(ChallengeReminder)
class ChallengeReminderAdmin(admin.ModelAdmin):
    """Admin View for ChallengeReminder"""

    list_display = (
        "id",
        linkify("user"),
        linkify("category"),
    )

    ordering = ("user",)
