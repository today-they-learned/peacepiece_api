from django.contrib import admin

from challenge.models import ChallengeSuggestion, ChallengeSuggestionFeedback
from config.admin import linkify


def reset_counters(self, request, queryset):
    for challenge_suggestion in queryset:
        challenge_suggestion.feedback_count = ChallengeSuggestionFeedback.objects.filter(
            suggestion=challenge_suggestion
        ).count()
        challenge_suggestion.save()


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
