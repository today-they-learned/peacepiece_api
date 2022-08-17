from django.db import models

class ChallengeCategory(models.Model):
    """Model definition for ChallengeCategory"""

    title = models.CharField(
        max_length=50,
    )

    display_order = models.IntegerField(
    )

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
