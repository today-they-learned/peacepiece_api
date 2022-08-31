from django.db import models

from config.models import BaseModel


class ArticleUserFeedback(BaseModel):
    """Model definition for ArticleUserFeedback"""

    article = models.ForeignKey(
        'article.Article',
        on_delete=models.CASCADE,
        related_name='user_feedbacks',
    )

    feedback = models.ForeignKey(
        'feedback.Feedback',
        on_delete=models.CASCADE,
        related_name='user_feedbacks',
    )

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='user_feedbacks',
    )

    class Meta:
        db_table = "article_user_feedbacks"
        verbose_name = "ArticleUserFeedback"
        verbose_name_plural = "ArticleUserFeedbacks"
        constraints = [
            models.UniqueConstraint(
                fields=["article", "feedback", "user"],
                name="unique_feedback_article_by_user",
            )
        ]
