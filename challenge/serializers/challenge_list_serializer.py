from rest_framework import serializers

from challenge.models import Challenge

class ChallengeListSerializer(serializers.ModelSerializer):
    """Serializer definition for Challenge Model."""

    class Meta:
        """Meta definition for ChallengeListSerializer."""

        model = Challenge
        fields = [
            "id",
            "title",
            "description",
            "categories",
            "prover_cnt",
            "point",
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
