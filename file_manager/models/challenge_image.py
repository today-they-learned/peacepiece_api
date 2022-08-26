from django.db import models

from config.models import BaseModel


class ChallengeImage(BaseModel):
    """Model definition for ChallengeImage"""

    image = models.ForeignKey(
        "file_manager.Image",
        on_delete=models.CASCADE,
        related_name="challenge_images",
    )

    challenge = models.ForeignKey(
        "challenge.Challenge",
        on_delete=models.CASCADE,
        related_name="challenge_images",
    )

    class Meta:
        db_table = "challenge_images"
        verbose_name = "ChallengeImage"
        verbose_name_plural = "ChallengeImages"
