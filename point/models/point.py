from django.db import models
from user.models import User


class Point(models.Model):
    """Model definition for Point"""

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="points",
        verbose_name="user",
    )
    pointable_type = models.CharField(
        max_length=10,
    )
    pointable_id = models.IntegerField()
    amount = models.IntegerField()
