from feedback.models import ArticleFeedback
from rest_framework import serializers

from .feedback_serializer import FeedbackSerializer


class ArticleFeedbackSerializer(serializers.ModelSerializer):
    """Serializer definition for ArticleFeedback Model."""

    feedback = FeedbackSerializer(read_only=True)
    is_feedbacked = serializers.SerializerMethodField()

    class Meta:
        """Meta definition for ArticleFeedbackSerializer."""

        model = ArticleFeedback

        fields = [
            "feedback",
            "count",
            "is_feedbacked",
        ]

        read_only_fields = [
            "feedback",
            "count",
            "is_feedbacked",
        ]

    def get_is_feedbacked(self, article_feedback):
        feedback_ids_by_user = self.context.get("feedback_ids_by_user", [])

        return article_feedback.feedback_id in feedback_ids_by_user
