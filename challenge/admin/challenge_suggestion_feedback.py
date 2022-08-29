from django.contrib import admin

from challenge.models import ChallengeSuggestionFeedback


@admin.register(ChallengeSuggestionFeedback)
class ChallengeSuggestionFeedbackAdmin(admin.ModelAdmin):
    """Admin View for ChallengeSuggestionFeedback"""

    list_display = ("suggestion", "user")
