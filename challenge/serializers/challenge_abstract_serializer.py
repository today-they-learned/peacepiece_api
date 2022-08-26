from rest_framework import serializers

from challenge.models import Challenge
from file_manager.serializers import ImageSerializer

from .category_serializer import CategorySerializer


class ChallengeAbstractSerializer(serializers.ModelSerializer):
    """AbstractSerializer definition for Challenge Model."""

    categories = CategorySerializer(
        read_only=True,
        many=True,
    )

    thumbnail = ImageSerializer(read_only=True)

    class Meta:
        """Meta definition for ChallengeSerializer."""

        model = Challenge
        fields = [
            "id",
            "title",
            "description",
            "categories",
            "prover_cnt",
            "point",
            "thumbnail",
            "start_at",
            "end_at",
        ]

        read_only_fields = [
            "id",
            "title",
            "description",
            "categories",
            "prover_cnt",
            "point",
            "start_at",
            "end_at",
        ]
