from rest_framework import serializers

from challenge.models import Challenge

class ChallengeSerializer(serializers.ModelSerializer):
    """Serializer definition for Challenge Model"""

    class Meta:
        model = Challenge

        fields = [
            'id',
            'title',
            'category',
            'start_at',
            'end_at'
        ]

        read_only_fields = [
            "id",
        ]
