from django.db import models

from config.models import BaseModel
from user.models import User


class Article(BaseModel):
    """Model definition for Article"""

    writer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="article",
        verbose_name="작성자",
    )

    content = models.TextField(
        verbose_name="내용",
        null=True,
        blank=True,
        max_length=300,
    )

    class Meta:
        db_table = "article"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
