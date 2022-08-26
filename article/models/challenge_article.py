from django.db import models

from config.models import BaseModel
from user.models import User

class ChallengeArticle(BaseModel):
    """Model definition for ChallengeArticle"""

    article = models.ForeignKey(
        'article.Article',
        on_delete=models.SET_NULL,
        null=True,
        related_name="challenge_article",
    )

    challenge = models.ForeignKey(
        'challenge.Challenge',
        on_delete=models.SET_NULL,
        null=True,
        related_name="challenge_article",
    )

    class Meta:
        db_table = "challenge_article"
        verbose_name = "ChallengeArticle"
        verbose_name_plural = "ChallengeArticles"
