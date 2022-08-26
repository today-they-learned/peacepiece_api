from django.db import models

from config.models import BaseModel


class ChallengeCategory(BaseModel):
    """Model definition for ChallengeCategory"""

    category = models.ForeignKey(
        "challenge.Category",
        on_delete=models.CASCADE,
        related_name="challenge_categories",
    )

    challenge = models.ForeignKey(
        "challenge.Challenge",
        on_delete=models.CASCADE,
        related_name="challenge_categories",
    )

    class Meta:
        db_table = "challenge_categories"
        verbose_name = "ChallengeCategory"
        verbose_name_plural = "ChallengeCategories"
