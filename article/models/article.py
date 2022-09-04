from django.core.exceptions import ValidationError
from django.db import models, transaction

from challenge.models import Challenge
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

    challenge = models.ForeignKey(
        "challenge.Challenge",
        on_delete=models.SET_NULL,
        null=True,
        related_name="articles",
    )

    content = models.TextField(
        verbose_name="내용",
        null=True,
        blank=True,
        max_length=300,
    )

    images = models.ManyToManyField(
        "file_manager.Image",
        related_name="articles",
        through="file_manager.ArticleImage",
        through_fields=("article", "image"),
    )

    class Meta:
        db_table = "articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        constraints = [
            models.UniqueConstraint(
                fields=["writer", "challenge"],
                name="unique_challenge_article_by_user",
            )
        ]

    def validate_challenge(self):
        if not isinstance(self.challenge, Challenge):
            raise ValidationError({"challenge": "없는 챌린지입니다."})

        if self.challenge.is_ended:
            raise ValidationError({"challenge": "종료한 챌린지입니다."})

    def clean(self):
        self.validate_challenge()

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        return super().save(force_insert, force_update, using, update_fields)
