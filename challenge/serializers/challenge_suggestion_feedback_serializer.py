from rest_framework import serializers

from challenge.models import ChallengeSuggestionFeedback
from challenge.serializers import ChallengeSuggestionSerializer
from user.serializers import UserAbstractSerializer


class ChallengeSuggestionFeedbackSerializer(serializers.ModelSerializer):
    """Serializer definition for ChallengeSuggestionFeedback Model."""

    suggestion = ChallengeSuggestionSerializer(read_only=True)
    user = UserAbstractSerializer(read_only=True)

    class Meta:
        """Meta definition for ChallengeSuggestionFeedbackSerializer."""

        model = ChallengeSuggestionFeedback
        fields = [
            "id",
            "suggestion",
            "user",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "suggestion",
            "user",
            "created_at",
            "updated_at",
        ]
