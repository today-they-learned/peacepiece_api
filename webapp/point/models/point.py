from config.models import BaseModel
from django.db import models
from user.models import User


class Point(BaseModel):
    """Model definition for Point"""

    POINT_CATEGORY_CHOICES = (
        ("buy_item", "아이템 구매"),
        ("prove_challenge", "챌린지 인증 글 작성"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="points",
        null=True,
    )
    challenge = models.ForeignKey(
        "challenge.Challenge",
        on_delete=models.SET_NULL,
        null=True,
        related_name="points",
        blank=True,
    )
    article = models.ForeignKey(
        "article.Article",
        on_delete=models.SET_NULL,
        null=True,
        related_name="points",
        blank=True,
    )
    item = models.ForeignKey(
        "item.Item",
        on_delete=models.SET_NULL,
        null=True,
        related_name="points",
        blank=True,
    )
    point_category = models.CharField(
        choices=POINT_CATEGORY_CHOICES,
        max_length=30,
        verbose_name="포인트 종류",
        null=True,
    )
    amount = models.IntegerField(default=0)

    class Meta:
        db_table = "points"
        verbose_name = "Point"
        verbose_name_plural = "Points"
