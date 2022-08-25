from django.contrib import admin

from article.models import ChallengeArticle
from config.admin import linkify


@admin.register(ChallengeArticle)
class ChallengeArticleAdmin(admin.ModelAdmin):
    """Admin View for ChallengeArticle"""

    list_display = (
        'id',
        linkify('article'),
        linkify('challenge'),
    )

    ordering = ("article",)
