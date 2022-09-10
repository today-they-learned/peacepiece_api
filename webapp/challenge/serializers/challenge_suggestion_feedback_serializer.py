from challenge.models import ChallengeSuggestionFeedback
from config.serializers import BaseModelSerializer
from user.serializers import UserAbstractSerializer

from .challenge_suggestion_serializer import ChallengeSuggestionSerializer


class ChallengeSuggestionFeedbackSerializer(BaseModelSerializer):
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
