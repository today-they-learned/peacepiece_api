from rest_framework import serializers

from article.models import Article
from article.serializers.article_comment_serializer import ArticleCommentSerializer
from challenge.serializers import ChallengeAbstractSerializer
from config.serializers import BaseModelSerializer
from file_manager.serializers import ImageSerializer
from user.serializers import UserAbstractSerializer


class ArticleListSerializer(BaseModelSerializer):
    """Serializer definition for Article Model."""

    writer = UserAbstractSerializer(
        read_only=True,
    )

    images = ImageSerializer(
        many=True,
        read_only=True,
    )

    article_comments = ArticleCommentSerializer(many=True, read_only=True)

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
            "article_comments",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "writer",
            "content",
            "article_comments",
            "created_at",
            "updated_at",
        ]
