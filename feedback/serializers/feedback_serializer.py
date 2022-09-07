from rest_framework import serializers

from feedback.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """Serializer definition for Feedback Model."""

    class Meta:
        """Meta definition for FeedbackSerializer."""

        model = Feedback
        fields = [
            "id",
            "emoji",
        ]

        read_only_fields = [
            "id",
            "emoji",
        ]
