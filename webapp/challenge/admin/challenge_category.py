from challenge.models import ChallengeCategory
from config.admin import linkify
from django.contrib import admin


@admin.register(ChallengeCategory)
class ChallengeCategoryAdmin(admin.ModelAdmin):
    """Admin View for Challenge"""

    list_display = (
        "id",
        linkify("category"),
        linkify("challenge"),
    )

    ordering = ("challenge",)
