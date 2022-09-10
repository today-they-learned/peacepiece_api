from django.contrib import admin

from config.admin import linkify
from file_manager.models import ArticleImage


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    """Admin View for ArticleImage"""

    list_per_page = 10
    list_display = (
        "id",
        linkify("image"),
        linkify("article"),
    )
    ordering = ("created_at", "updated_at")
