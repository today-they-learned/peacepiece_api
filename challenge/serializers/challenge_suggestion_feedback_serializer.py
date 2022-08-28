from rest_framework import serializers

from challenge.models import ChallengeSuggestion, ChallengeSuggestionFeedback
from user.serializers import UserAbstractSerializer

from .challenge_suggestion_serializer import ChallengeSuggestionSerializer


class ChallengeSuggestionFeedbackSerializer(serializers.ModelSerializer):
    """Serializer definition for ChallengeSuggestionFeedback Model."""

    suggestion = ChallengeSuggestionSerializer(read_only=True)
    suggestion_id = serializers.PrimaryKeyRelatedField(
        source="suggestion", queryset=ChallengeSuggestion.objects.all(), write_only=True
    )
    user = UserAbstractSerializer(read_only=True)

    class Meta:
        """Meta definition for ChallengeSuggestionFeedbackSerializer."""

        model = ChallengeSuggestionFeedback
        fields = [
            "id",
            "suggestion",
            "suggestion_id",
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
