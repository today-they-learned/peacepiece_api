from django.db import transaction
from rest_framework import serializers

from challenge.models import ChallengeSuggestion
from user.serializers import UserAbstractSerializer


class ChallengeSuggestionSerializer(serializers.ModelSerializer):
    suggester = UserAbstractSerializer(read_only=True)

    # # TODO: challenge 연결
    # challenge = ChallengeSerializer(read_only=True)
    # challenge_id = serializers.PrimaryKeyRelatedField(
    #     source='challenge',
    #     queryset=Challenge.objects.all(),
    #     write_only=True,
    # )

    class Meta:
        model = ChallengeSuggestion
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
