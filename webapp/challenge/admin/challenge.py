from django.contrib import admin

from challenge.models import Challenge
from file_manager.models import Image


class ImageInline(admin.TabularInline):
    model = Challenge.images.through


def deep_copy(self):
    if self.thumbnail is not None:
        new_image = Image(file=self.thumbnail.file, uploader=self.thumbnail.uploader)
        new_image.save()
        self.thumbnail = new_image
    self.pk = None
    self.save()


def copy_challenge(modeladmin, request, queryset):
    for challenge in queryset:
        deep_copy(challenge)


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
