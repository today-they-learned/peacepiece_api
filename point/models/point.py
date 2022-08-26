from django.db import models

from config.models import BaseModel
from user.models import User


class Point(BaseModel):
    """Model definition for Point"""

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="points",
        null=True,
    )
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "points"
        verbose_name = "Point"
        verbose_name_plural = "Points"
