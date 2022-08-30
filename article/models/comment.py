from django.db import models

from config.models import BaseModel


class Comment(BaseModel):
    """Model definition for Comment"""

    writer = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments",
        verbose_name="작성자",
    )

    content = models.TextField(
        verbose_name="내용",
        null=True,
        blank=True,
        max_length=300,
    )

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
