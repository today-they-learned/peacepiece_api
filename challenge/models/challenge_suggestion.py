from django.db import models

from user.models import User


class ChallengeSuggestion(models.Model):
    """Model definition for ChallengeSuggestion"""

    suggester = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="challenge_suggestion",
        verbose_name="제안자",
    )
    content = models.TextField(
        verbose_name="내용",
        null=True,
        blank=True,
        max_length=300,
    )
    feedback_cnt = models.PositiveIntegerField(
        verbose_name="피드백 개수",
        default=0,
    )

    class Meta:
        db_table = "challenge_suggestion"
        verbose_name = "ChallengeSuggestion"
        verbose_name_plural = "ChallengeSuggestion"
