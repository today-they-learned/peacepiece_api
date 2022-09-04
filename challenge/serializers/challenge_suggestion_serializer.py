from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from challenge.models import ChallengeSuggestion
from config.serializers import BaseModelSerializer
from user.serializers import UserAbstractSerializer

from .challenge_serializer import ChallengeSerializer


class ChallengeSuggestionSerializer(BaseModelSerializer):
    """Serializer definition for ChallengeSuggestion Model."""

    challenge = ChallengeSerializer(read_only=True)
    suggester = UserAbstractSerializer(read_only=True)
    is_feedbacked = serializers.SerializerMethodField(source="is_feedbacked")

    class Meta:
        """Meta definition for ChallengeSuggestionSerializer."""

        model = ChallengeSuggestion
        fields = [
            "id",
            "challenge",
            "suggester",
            "content",
            "is_feedbacked",
            "feedback_count",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "challenge",
            "suggester",
            "feedback_count",
            "created_at",
            "updated_at",
        ]

    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_is_feedbacked(self, challenge_suggestion) -> bool:
        if self.is_anonymous_user:
            return False
        return challenge_suggestion.challenge_suggestion_feedback.filter(user=self.current_user).exists()
