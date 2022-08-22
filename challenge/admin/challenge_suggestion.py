from django.contrib import admin

from config.admin import linkify
from challenge.models import ChallengeSuggestion


@admin.register(ChallengeSuggestion)
class ChallengeSuggestionAdmin(admin.ModelAdmin):
    """Admin View for ChallengeSuggestion"""

    list_display = (
        "id",
        linkify("challenge"),
        linkify("suggester"),
        "content",
        "feedback_cnt",
    )
    readonly_fields = ("challenge", "suggester")
    ordering = ("suggester", "feedback_cnt")
