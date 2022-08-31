from django.db import models

from config.models import BaseModel


class ArticleFeedback(BaseModel):
    """Model definition for ArticleFeedback"""

    article = models.ForeignKey(
        'article.Article',
        on_delete=models.CASCADE,
        related_name='feedbacks',
    )

    feedback = models.ForeignKey(
        'feedback.Feedback',
        on_delete=models.CASCADE,
        related_name='feedbacks',
    )

    count = models.IntegerField(
        default=0,
    )

    class Meta:
        db_table = "article_feedbacks"
        verbose_name = "ArticleFeedback"
        verbose_name_plural = "ArticleFeedbacks"
        constraints = [
            models.UniqueConstraint(
                fields=["article", "feedback"],
                name="unique_feedback_article",
            )
        ]
