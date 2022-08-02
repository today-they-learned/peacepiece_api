from django.contrib import admin
from challenge.models import Challenge

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    """Admin View for Challenge"""

    list_display = (
        "title",
        "category",
    )
