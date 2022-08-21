from django.db import models

class Challenge(models.Model):
    """Model definition for Challenge"""

    title = models.CharField(
        max_length = 50,
    )

    description = models.TextField(
    )

    categories = models.ManyToManyField(
        'challenge.Category',
        related_name = 'challenges',
        through = 'challenge.ChallengeCategory'
    )

    prover_cnt = models.PositiveIntegerField(
        default = 0
    )

    point = models.PositiveIntegerField(
        default = 0
    )

    start_at = models.DateTimeField(
    )

    end_at = models.DateTimeField(
    )

    class Meta:
        db_table = "challenge"
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"
