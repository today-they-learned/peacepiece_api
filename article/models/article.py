from django.db import models

from config.models import BaseModel


class Article(BaseModel):
    """Model definition for Article"""

    writer = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="articles",
        verbose_name="작성자",
    )

    content = models.TextField(
        verbose_name="내용",
        null=True,
        blank=True,
        max_length=300,
    )

    images = models.ManyToManyField(
        "file_manager.Image",
        related_name="images",
        through="file_manager.ArticleImage",
        through_fields=("article", "image"),
    )

    class Meta:
        db_table = "articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
