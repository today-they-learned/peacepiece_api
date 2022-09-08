from django.db import models

from article.models import Article
from config.models import BaseModel


class Notification(BaseModel):
    """Model definition for Notification"""

    NOTICE_CATEGORY_CHOICES = (
        ("challenge", "챌린지 인증글 댓글 알림"),
        ("piece", "피스글 댓글 알림"),
        ("category", "카테고리 챌린지 알림"),
    )

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    contributor = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        null=True,
    )

    notice_category = models.CharField(choices=NOTICE_CATEGORY_CHOICES, max_length=30, verbose_name="알림 종류")

    challenge = models.ForeignKey(
        "challenge.Challenge",
        on_delete=models.CASCADE,
        null=True,
    )

    category = models.ForeignKey(
        "challenge.Category",
        on_delete=models.CASCADE,
        null=True,
    )

    article = models.ForeignKey(
        "article.Article",
        on_delete=models.CASCADE,
        null=True,
    )

    is_viewed = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "notifications"
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    @classmethod
    def create_article_notification(cls, contributor, article, user, notice_category):
        Notification(user=user, contributor=contributor, notice_category=notice_category, article=article).save()
