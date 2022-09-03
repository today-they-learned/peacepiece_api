from django.contrib import admin

from feedback.models import ArticleFeedback
from config.admin import linkify


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
