from rest_framework import serializers

from article.models import Article
from challenge.serializers import ChallengeAbstractSerializer
from file_manager.serializers import ImageSerializer
from user.serializers import UserAbstractSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    """Serializer definition for Article Model."""

    writer = UserAbstractSerializer(
        read_only=True,
    )

    images = ImageSerializer(
        many=True,
        read_only=True,
    )

    challenge = ChallengeAbstractSerializer(read_only=True)

    class Meta:
        """Meta definition for ArticleListSerializer."""

        model = Article

        fields = [
            "id",
            "writer",
            "content",
            "images",
            "challenge",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "writer",
            "content",
            "created_at",
            "updated_at",
        ]
