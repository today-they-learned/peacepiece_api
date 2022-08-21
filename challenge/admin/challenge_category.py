from django.contrib import admin

from config.admin import linkify
from challenge.models import ChallengeCategory


@admin.register(ChallengeCategory)
class ChallengeCategoryAdmin(admin.ModelAdmin):
    """Admin View for Challenge"""

    list_display = (
        "id",
        linkify("category"),
        linkify("challenge"),
    )

    ordering = ("challenge",)
