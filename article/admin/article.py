from django.contrib import admin

from article.models import Article
from config.admin import linkify


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin View for Article"""

    list_display = (
        "id",
        linkify("writer"),
        "content",
        # "created_at",
        # "updated_at",
    )

    readonly_fields = (
        "writer",
        "content",
    )

    ordering = ("writer",)
