from unittest import result

from article.models import Article
from article.serializers.article_comment_serializer import ArticleCommentSerializer
from challenge.serializers import ChallengeAbstractSerializer
from config.serializers import BaseModelSerializer
from feedback.models import ArticleFeedback, ArticleUserFeedback, Feedback
from file_manager.serializers import ImageSerializer
from rest_framework import serializers
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

    feedbacks = serializers.SerializerMethodField()

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
            "feedbacks",
        ]

        read_only_fields = [
            "id",
            "writer",
            "content",
            "article_comments",
            "created_at",
            "updated_at",
            "feedbacks",
        ]

    def get_feedbacks(self, article):
        feedbacks_by_article_id = self.context.get("feedbacks_by_article_id", {})

        return feedbacks_by_article_id.get(article.id, {})
