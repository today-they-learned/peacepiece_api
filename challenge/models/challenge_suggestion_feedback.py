from django.db import models


class ChallengeSuggestionFeedback(models.Model):
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
