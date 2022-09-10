from challenge.models import ChallengeSuggestion, ChallengeSuggestionFeedback
from config.admin import linkify
from django.contrib import admin


def reset_counters(self, request, queryset):
    for challenge_suggestion in queryset:
        challenge_suggestion.reset_feedback_count()


@admin.register(ChallengeSuggestion)
class ChallengeSuggestionAdmin(admin.ModelAdmin):
    """Admin View for ChallengeSuggestion"""

    list_display = (
        "id",
        linkify("challenge"),
        linkify("suggester"),
        "content",
        "feedback_count",
    )
    readonly_fields = ("challenge", "suggester")
    ordering = ("suggester", "feedback_count")
