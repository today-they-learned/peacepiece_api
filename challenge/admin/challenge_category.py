from django.contrib import admin

from challenge.models import ChallengeCategory

@admin.register(ChallengeCategory)
class ChallengeCategoryAdmin(admin.ModelAdmin):
    """Admin View for Challenge"""

    list_display = (
        'category',
        'challenge',
    )

    ordering = (
        'challenge',
    )
