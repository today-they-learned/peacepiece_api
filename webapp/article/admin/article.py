from article.models import Article
from config.admin import linkify
from django.contrib import admin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin View for Article"""

    list_display = (
        "id",
        linkify("writer"),
        linkify("challenge"),
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        # "writer",
        "content",
    )

    ordering = ("writer",)
