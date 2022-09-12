from django.contrib import admin

from challenge.models import Challenge


class ImageInline(admin.TabularInline):
    model = Challenge.images.through


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    """Admin View for Challenge"""

    list_display = (
        "id",
        "title",
        "start_at",
        "end_at",
        "prover_cnt",
        "point",
    )
    inlines = (ImageInline,)

    readonly_fields = ("prover_cnt",)

    ordering = (
        "start_at",
        "end_at",
    )
