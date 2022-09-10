from config.admin import linkify
from django.contrib import admin
from feedback.models import ArticleUserFeedback


@admin.register(ArticleUserFeedback)
class ArticleUserFeedbackAdmin(admin.ModelAdmin):
    """Admin View for ArticleUserFeedback"""

    list_display = (
        "id",
        linkify("article"),
        linkify("user"),
        linkify("feedback"),
    )

    ordering = ("article",)
