from django.contrib import admin

from feedback.models import Feedback
from config.admin import linkify


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Admin View for Feedback"""

    list_display = (
        "id",
        "emoji",
    )

    ordering = ("id",)
