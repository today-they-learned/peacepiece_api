from django.contrib import admin

from challenge.models import ChallengeSuggestion


@admin.register(ChallengeSuggestion)
class ChallengeSuggestionAdmin(admin.ModelAdmin):
    """Admin View for ChallengeSuggestion"""

    list_display = ("challenge", "suggester", "content", "feedback_cnt")
    readonly_fields = ("challenge", "suggester")
    ordering = ("suggester", "feedback_cnt")
