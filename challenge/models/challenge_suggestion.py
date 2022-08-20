from django.db import models


class ChallengeSuggestion(models.Model):
    """Model definition for ChallengeSuggestion"""

    challenge = models.ForeignKey(
        "challenge.Challenge",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="챌린지",
        related_name="challenge_suggestion",
    )
    suggester = models.ForeignKey(
        "user.User",
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