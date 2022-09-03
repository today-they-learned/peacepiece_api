from django.contrib import admin

from config.admin import linkify
from feedback.models import ArticleFeedback


@admin.register(ArticleFeedback)
class ArticleFeedbackAdmin(admin.ModelAdmin):
    """Admin View for ArticleFeedback"""

    list_display = (
        "id",
        linkify("article"),
        linkify("feedback"),
        "count",
    )

    ordering = ("-count",)
