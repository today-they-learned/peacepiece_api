from django.contrib import admin

from config.admin import linkify
from file_manager.models import ChallengeImage


@admin.register(ChallengeImage)
class ChallengeImageAdmin(admin.ModelAdmin):
    """Admin View for ChallengeImage"""

    list_per_page = 10
    list_display = (
        "id",
        linkify("image"),
        linkify("challenge"),
    )
    ordering = ("created_at", "updated_at")
