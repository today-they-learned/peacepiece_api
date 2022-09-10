from article.models import Article
from rest_framework import serializers


class ArticleAbstractSerializer(serializers.ModelSerializer):
    """Serializer definition for Article Model."""

    class Meta:
        """Meta definition for ArticleAbstractSerializer."""

        model = Article

        fields = [
            "id",
            "content",
        ]

        read_only_fields = [
            "id",
            "content",
        ]
