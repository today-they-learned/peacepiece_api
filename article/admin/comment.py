from django.contrib import admin

from article.models import Comment
from config.admin import linkify


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin View for Comment"""

    list_display = (
        "id",
        linkify("writer"),
        "content",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "writer",
        "content",
    )

    ordering = ("writer",)
