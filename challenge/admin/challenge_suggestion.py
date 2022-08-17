from django.contrib import admin

from challenge.models import ChallengeSuggestion


@admin.register(ChallengeSuggestion)
class ChallengeSuggestionAdmin(admin.ModelAdmin):
    """Admin View for ChallengeSuggestion"""

    list_display = ("suggester", "content", "feedback_cnt")
    readonly_fields = ("suggester",)
    ordering = ("suggester", "feedback_cnt")
