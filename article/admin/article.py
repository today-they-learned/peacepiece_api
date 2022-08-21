from django.contrib import admin

from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin View for Article"""

    list_display = (
        "writer",
        "content",
    )

    readonly_fields = (
        "writer",
        "content",
    )

    ordering = ("writer",)
