from challenge.models import ChallengeSuggestionFeedback
from django.contrib import admin


@admin.register(ChallengeSuggestionFeedback)
class ChallengeSuggestionFeedbackAdmin(admin.ModelAdmin):
    """Admin View for ChallengeSuggestionFeedback"""

    list_display = ("suggestion", "user")
