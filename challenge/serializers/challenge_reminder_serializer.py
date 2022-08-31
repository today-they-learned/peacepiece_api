from rest_framework import serializers

from challenge.models import Category, ChallengeReminder

from .category_serializer import CategorySerializer


class ChallengeReminderSerializer(serializers.ModelSerializer):
    """Serializer definition for ChallengeReminder Model."""

    category = CategorySerializer(
        read_only=True,
    )

    category_id = serializers.PrimaryKeyRelatedField(
        source="category",
        queryset=Category.objects.all(),
        write_only=True,
    )

    class Meta:
        model = ChallengeReminder

        fields = [
            "id",
            "category",
            "category_id",
            "created_at",
            "updated_at",
        ]
