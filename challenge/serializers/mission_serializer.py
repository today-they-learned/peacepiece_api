from rest_framework import serializers

from challenge.models import ChallengeMission


class MissionSerializer(serializers.ModelSerializer):
    """Serializer definition for Mission Model"""


class Meta:
    model = ChallengeMission

    fields = ["challenge", "title", "description", "point"]
