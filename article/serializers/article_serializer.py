from rest_framework import serializers

from article.models import Article
from user.serializers import UserAbstractSerializer


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer definition for Article Model."""

    writer = UserAbstractSerializer(
        read_only = True,
    )

    class Meta:
        """Meta definition for ArticleSerializer."""

        model = Article

        fields = [
            "id",
            "writer",
            "content",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "writer",
            "created_at",
            "updated_at",
        ]

