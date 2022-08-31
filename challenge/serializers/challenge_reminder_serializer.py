from rest_framework import serializers

from challenge.models import ChallengeReminder

from .category_serializer import CategorySerializer


class ChallengeReminderSerializer(serializers.ModelSerializer):
    """Serializer definition for ChallengeReminder Model."""

    category = CategorySerializer(
        read_only=True,
    )

    class Meta:
        model = ChallengeReminder

        fields = [
            "id",
            "category",
            "created_at",
            "updated_at",
        ]
