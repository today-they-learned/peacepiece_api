from django.db import models

from config.models import BaseModel


class Feedback(BaseModel):
    """Model definition for Feedback"""

    emoji = models.CharField(
        max_length=30,
        unique=True,
    )

    class Meta:
        db_table = "feedbacks"
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
