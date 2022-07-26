from config.models import BaseModel
from django.db import models


class ChallengeReminder(BaseModel):
    """Model definition for ChallengeReminder"""

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="challenge_reminders",
    )

    category = models.ForeignKey(
        "challenge.Category",
        on_delete=models.CASCADE,
        related_name="challenge_reminders",
    )

    class Meta:
        db_table = "challenge_reminders"
        verbose_name = "ChallengeReminder"
        verbose_name_plural = "ChallengeReminders"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "category"],
                name="unique_category_by_user",
            )
        ]
