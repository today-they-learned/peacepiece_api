from django.db import models

class ChallengeCategory(models.Model):
    """Model definition for ChallengeCategory"""

    category = models.ForeignKey(
        'challenge.Category',
        on_delete=models.CASCADE,
    )

    challenge = models.ForeignKey(
        'challenge.Challenge',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "challenge_category"
        verbose_name = "ChallengeCategory"
        verbose_name_plural = "ChallengeCategories"
