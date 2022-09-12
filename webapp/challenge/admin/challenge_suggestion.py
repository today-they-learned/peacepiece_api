from config.admin import linkify
from django.contrib import admin

from challenge.models import ChallengeSuggestion, ChallengeSuggestionFeedback


def reset_counters(self, request, queryset):
    for challenge_suggestion in queryset:
        challenge_suggestion.reset_feedback_count()


def reset_feedback_count(self, request, queryset):
    for challenge_suggestion in queryset:
        challenge_suggestion.feedback_count = 0
        challenge_suggestion.save()


reset_feedback_count.short_description = "feedback_count 를 초기화합니다."


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
    actions = (reset_feedback_count,)
