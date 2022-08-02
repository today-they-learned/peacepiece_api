from django.contrib import admin
from challenge.models import ChallengeMission

@admin.register(ChallengeMission)
class ChallengeMissionAdmin(admin.ModelAdmin):
    """Admin View for Mission"""

    list_display = (
        "title",
    )

