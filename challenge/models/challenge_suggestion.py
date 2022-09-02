from django.db import models

from config.models import BaseModel

from .challenge_suggestion_feedback import ChallengeSuggestionFeedback


class ChallengeSuggestion(BaseModel):
    """Model definition for ChallengeSuggestion"""

    challenge = models.OneToOneField(
        "challenge.Challenge",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="챌린지",
        related_name="challenge_suggestion",
    )
    suggester = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="challenge_suggestions",
        verbose_name="제안자",
    )
    content = models.TextField(
        verbose_name="내용",
        null=True,
        blank=True,
        max_length=300,
    )
    feedback_count = models.PositiveIntegerField(
        verbose_name="피드백 개수",
        default=0,
    )

    class Meta:
        db_table = "challenge_suggestions"
        verbose_name = "ChallengeSuggestion"
        verbose_name_plural = "ChallengeSuggestion"

    def increment_feedback_count(self):
        self.feedback_count += 1
        self.save()

    def decrement_feedback_count(self):
        self.feedback_count -= 1
        self.save()

    def reset_feedback_count(self):
        self.feedback_count = ChallengeSuggestionFeedback.objects.filter(suggestion=self).count()
        self.save()
