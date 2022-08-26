from django.contrib import admin

from challenge.models import Challenge


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    """Admin View for Challenge"""

    list_display = (
        "id",
        "title",
        "start_at",
        "end_at",
        "prover_cnt",
    )

    readonly_fields = ("prover_cnt",)

    ordering = (
        "start_at",
        "end_at",
    )
