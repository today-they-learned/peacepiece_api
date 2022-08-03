from rest_framework import serializers

from challenge.models import ChallengeCategory


class CategorySerializer(serializers.ModelSerializer):
    """Serializer definition for Category Model"""


class Meta:
    model = ChallengeCategory

    fields = ["title"]
