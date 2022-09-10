from datetime import timedelta

from config.models import BaseModel, ModelManager
from django.db import models
from django.db.models import Q
from django.utils.timezone import now


class ChallengeModelManager(ModelManager):
    def ended(self):
        return super().get_queryset().filter(end_at__lt=now().date())

    def daily(self):
        today = now().date()
        return super().get_queryset().filter(end_at=today, start_at=today)

    def weekly(self):
        today = now().date()
        return (
            super()
            .get_queryset()
            .filter(
                ~(Q(end_at=today, start_at=today))
                & Q(start_at__lte=today, start_at__gte=today + timedelta(days=7), end_at__gte=today)
            )
        )

    def is_progressing(self):
        today = now().date()
        return super().get_queryset().filter(start_at__lte=today, end_at__gte=today)


class Challenge(BaseModel):
    """Model definition for Challenge"""

    objects = ChallengeModelManager()

    title = models.CharField(
        max_length=50,
    )

    description = models.TextField()

    categories = models.ManyToManyField(
        "challenge.Category",
        related_name="challenges",
        through="challenge.ChallengeCategory",
    )

    prover_cnt = models.PositiveIntegerField(default=0)

    point = models.PositiveIntegerField(default=0)

    start_at = models.DateField()

    end_at = models.DateField()

    thumbnail = models.OneToOneField(
        "file_manager.Image",
        related_name="challenge",
        verbose_name="썸네일",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    images = models.ManyToManyField(
        "file_manager.Image",
        related_name="challenges",
        through="file_manager.ChallengeImage",
        through_fields=("challenge", "image"),
    )

    class Meta:
        db_table = "challenges"
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"

    @property
    def is_ended(self):
        return self.end_at and self.end_at <= now().date()
