from config.admin import linkify
from django.contrib import admin

from challenge.models import ChallengeSuggestion, ChallengeSuggestionFeedback


def reset_counters(self, request, queryset):
    for challenge_suggestion in queryset:
        challenge_suggestion.reset_feedback_count()


reset_counters.short_description = "feedback_count를 초기화합니다."


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
    actions = (reset_counters,)
