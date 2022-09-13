from datetime import timedelta

from config.models import BaseModel, ModelManager
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.db.models import Q
from django.utils.timezone import now
from file_manager.models import Image


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
                & Q(start_at__lte=today, end_at__lte=today + timedelta(days=7), end_at__gte=today)
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
        return self.end_at and self.end_at < now().date()

    @property
    def is_not_start(self):
        return self.start_at and self.start_at > now().date()

    @property
    def is_valid_period(self):
        return self.start_at <= self.end_at

    def validate_challenge(self):
        if not self.is_valid_period:
            raise ValidationError({"end_at": "유효하지 않은 챌린지 기간입니다."})

    def clean(self):
        self.validate_challenge()

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        return super().save(force_insert, force_update, using, update_fields)

    def deep_copy(self):
        if self.thumbnail is not None:
            new_image = Image(file=self.thumbnail.file, uploader=self.thumbnail.uploader)
            new_image.save()
            self.thumbnail = new_image
        self.pk = None
        self.save()

    def reset_prover_count(self):
        self.prover_cnt = self.articles.count()
        self.save()
