from django.contrib import admin

from challenge.models import Challenge
from file_manager.models import Image


class ImageInline(admin.TabularInline):
    model = Challenge.images.through


def copy_challenge(modeladmin, request, queryset):
    for challenge in queryset:
        if challenge.thumbnail:
            temp_image = Image(file=challenge.thumbnail.file, uploader=challenge.thumbnail.uploader)
            temp_image.save()
            challenge.thumbnail = temp_image
        challenge.pk = None
        challenge.save()


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
    inlines = (ImageInline,)

    readonly_fields = ("prover_cnt",)

    ordering = (
        "start_at",
        "end_at",
    )

    actions = [copy_challenge]
