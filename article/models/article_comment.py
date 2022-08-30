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

    comment = models.ForeignKey(
        "article.Comment",
        on_delete=models.SET_NULL,
        null=True,
        related_name="article_comments",
    )

    class Meta:
        db_table = "article_comments"
        verbose_name = "ArticleComment"
        verbose_name_plural = "ArticleComments"
