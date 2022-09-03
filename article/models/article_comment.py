from django.db import models

from config.models import BaseModel


class ArticleComment(BaseModel):
    """Model definition for ArticleComment"""

    article = models.ForeignKey(
        "article.Article",
        on_delete=models.SET_NULL,
        null=True,
        related_name="article_comments",
    )

    writer = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="article_comments",
        verbose_name="작성자",
    )

    content = models.TextField(
        verbose_name="내용",
        null=True,
        blank=True,
        max_length=300,
    )

    class Meta:
        db_table = "article_comments"
        verbose_name = "ArticleComment"
        verbose_name_plural = "ArticleComments"
