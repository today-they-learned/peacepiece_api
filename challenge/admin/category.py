from django.contrib import admin

from challenge.models import ChallengeCategory

@admin.register(ChallengeCategory)
class ChallengeCategoryAdmin(admin.ModelAdmin):
    """Admin View for ChallengeCategory"""

    list_display = (
        'title',
    )

    ordering = (
        'display_order',
    )
