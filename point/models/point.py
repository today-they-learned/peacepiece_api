from django.db import models
from user.models import User


class Point(models.Model):
    """Model definition for Point"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="points",
    )
    pointable_type = models.CharField(
        max_length=10,
    )
    pointable_id = models.IntegerField()
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "point"
        verbose_name = "Point"
        verbose_name_plural = "Points"
