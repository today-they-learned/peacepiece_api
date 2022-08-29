from django.db import transaction
from rest_framework import serializers

from challenge.models import ChallengeSuggestion
from user.serializers import UserAbstractSerializer

from .challenge_serializer import ChallengeSerializer


class ChallengeSuggestionSerializer(serializers.ModelSerializer):
    """Serializer definition for ChallengeSuggestion Model."""

    challenge = ChallengeSerializer(read_only=True)
    suggester = UserAbstractSerializer(read_only=True)

    class Meta:
        """Meta definition for ChallengeSuggestionSerializer."""

        model = ChallengeSuggestion
        fields = [
            "id",
            "challenge",
            "suggester",
            "content",
            "feedback_cnt",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "challenge",
            "suggester",
            "feedback_cnt",
            "created_at",
            "updated_at",
        ]


class ChallengeSuggestionUpdateSerializer(ChallengeSuggestionSerializer):
    @transaction.atomic
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta(ChallengeSuggestionSerializer.Meta):
        fields = [
            "id",
            "suggester",
            "content",
            "feedback_cnt",
            "challenge",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "challenge",
            "created_at",
            "updated_at",
        ]
