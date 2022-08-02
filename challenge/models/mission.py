from django.db import models
from .challenge import Challenge

class ChallengeMission(models.Model):
    """Model definition for Mission"""

    challenge = models.ForeignKey(
       Challenge,
       on_delete = models.CASCADE,
       related_name = "missions",
       verbose_name = "challenge"
   )

    title = models.CharField(
        max_length = 30
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    point = models.IntegerField(
    )
