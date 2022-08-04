from django.db import models
from user.models import User


class Point(models.Model):
    """Model definition for Point"""

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="point",
    )
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "point"
        verbose_name = "Point"
        verbose_name_plural = "Points"
