from challenge.models import Challenge
from django.contrib import admin


class ImageInline(admin.TabularInline):
    model = Challenge.images.through


def copy_challenge(modeladmin, request, queryset):
    for challenge in queryset:
        challenge.deep_copy()


def reset_prover_count(modeladmin, request, queryset):
    for challenge in queryset:
        challenge.reset_prover_count()


copy_challenge.short_description = "챌린지를 복사합니다."
reset_prover_count.short_description = "인증자 수를 초기화합니다."


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    """Admin View for Challenge"""

    actions = [copy_challenge, reset_prover_count]
    list_display = (
        "id",
        "title",
        "start_at",
        "end_at",
        "prover_cnt",
        "point",
    )
    inlines = (ImageInline,)

    readonly_fields = ()

    ordering = (
        "start_at",
        "end_at",
    )
