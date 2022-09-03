from django.db import models, transaction

from config.models import BaseModel


class ChallengeSuggestionFeedback(BaseModel):
    """Model definition for ChallengeSuggestionFeedback"""

    suggestion = models.ForeignKey(
        "challenge.ChallengeSuggestion",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="챌린지 제안",
        related_name="challenge_suggestion_feedbacks",
    )
    user = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="challenge_suggestion_feedbacks",
        verbose_name="피드백 유저",
    )

    class Meta:
        db_table = "challenge_suggestion_feedbacks"
        verbose_name = "ChallengeSuggestionFeedback"
        verbose_name_plural = "ChallengeSuggestionFeedback"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "suggestion"],
                name="unique_suggestion_by_user",
            )
        ]

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.suggestion.reset_feedback_count()
        super().save(force_insert, force_update, using, update_fields)

    @transaction.atomic
    def delete(self, using=None, keep_parents=False):
        self.suggestion.reset_feedback_count()
        super().delete(using, keep_parents)
