from django.contrib import admin

from challenge.models import ChallengeReminder

@admin.register(ChallengeReminder)
class ChallengeReminderAdmin(admin.ModelAdmin):
    """Admin View for ChallengeReminder"""

    list_display = (
        'user',
        'category',
    )

    ordering = (
        'user',
    )
