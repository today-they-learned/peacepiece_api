from config.models import BaseModel
from django.db import models


class ArticleImage(BaseModel):
    """Model definition for ArticleImage"""

    image = models.ForeignKey(
        "file_manager.Image",
        on_delete=models.CASCADE,
        related_name="article_images",
    )

    article = models.ForeignKey(
        "article.Article",
        on_delete=models.CASCADE,
        related_name="article_images",
    )

    class Meta:
        db_table = "article_images"
        verbose_name = "ArticleImage"
        verbose_name_plural = "ArticleImages"
