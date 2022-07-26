from config.models import BaseModel
from django.db import models


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
        constraints = [
            models.UniqueConstraint(
                fields=["category", "challenge"],
                name="unique_category_by_challenge",
            )
        ]
