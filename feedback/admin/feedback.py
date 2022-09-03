from django.contrib import admin

from config.admin import linkify
from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Admin View for Feedback"""

    list_display = (
        "id",
        "emoji",
    )

    ordering = ("id",)
