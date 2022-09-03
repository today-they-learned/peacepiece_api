from django.contrib import admin

from article.models import ArticleComment
from config.admin import linkify


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    """Admin View for ArticleComment"""

    list_display = (
        "id",
        linkify("article"),
        linkify("writer"),
        "content",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = (
        "article",
        "writer",
    )
