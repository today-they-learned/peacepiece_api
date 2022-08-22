from django.db import models
from config.models import BaseModel


class ChallengeReminder(BaseModel):
    """Model definition for ChallengeReminder"""

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        "challenge.Category",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "challenge_reminder"
        verbose_name = "ChallengeReminder"
        verbose_name_plural = "ChallengeReminders"
