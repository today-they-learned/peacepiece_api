from rest_framework import serializers

from user.serializers import UserAbstractSerializer
from article.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    """Serializer definition for Article Model."""

    writer = UserAbstractSerializer(
        read_only = True,
    )

    class Meta:
        """Meta definition for ArticleListSerializer."""

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
            "content",
            "created_at",
            "updated_at",
        ]
