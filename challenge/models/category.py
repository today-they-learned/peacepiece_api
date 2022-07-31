from django.db import models

class ChallengeCategory(models.Model):
    """Model definition for Category"""

    title = models.CharField(
        max_length = 10
    )
