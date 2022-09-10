from config.models import BaseModel
from django.db import models


class ArticleFeedback(BaseModel):
    """Model definition for ArticleFeedback"""

    article = models.ForeignKey(
        "article.Article",
        on_delete=models.CASCADE,
        related_name="article_feedbacks",
    )

    feedback = models.ForeignKey(
        "feedback.Feedback",
        on_delete=models.CASCADE,
        related_name="article_feedbacks",
    )

    count = models.PositiveIntegerField(
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

    @classmethod
    def increment_feedback_count(cls, article, feedback):
        article_feedback, _ = cls.objects.get_or_create(
            article=article,
            feedback=feedback,
        )
        article_feedback.count += 1

        article_feedback.save()

    @classmethod
    def decrement_feedback_count(cls, article, feedback):
        article_feedback, _ = cls.objects.get_or_create(
            article=article,
            feedback=feedback,
        )
        article_feedback.count -= 1

        article_feedback.save()
        article_feedback.reset_feedback(article_feedback, feedback)

    @classmethod
    def reset_feedback(cls, article_feedback, feedback):
        if article_feedback.count == 0:
            article_feedback.delete()
            feedback.delete()
