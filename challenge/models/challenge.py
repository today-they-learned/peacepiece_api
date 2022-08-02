from django.db import models
from user.models import User
from .category import ChallengeCategory

class Challenge(models.Model):
    """Model definition for Challenge"""

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="challenges",
        verbose_name="owner",
    )

    title = models.CharField(
        max_length=30,
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        ChallengeCategory,
        on_delete = models.CASCADE
    )

    start_at = models.DateTimeField(
        auto_now_add=True,
    )

    end_at = models.DateTimeField(
    )

    total_point = models.IntegerField(
        # 미션들의 포인트의 합
    )

    # tags =
