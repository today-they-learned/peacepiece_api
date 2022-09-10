from unittest import result

from rest_framework import serializers

from article.models import Article
from article.serializers.article_comment_serializer import ArticleCommentSerializer
from challenge.serializers import ChallengeAbstractSerializer
from config.serializers import BaseModelSerializer
from feedback.models import ArticleFeedback, ArticleUserFeedback, Feedback
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

    def get_is_feedbacked(self, article, feedback):
        if self.is_anonymous_user:
            return False
        return ArticleUserFeedback.objects.filter(article=article, feedback=feedback, user=self.current_user).exists()

    def get_feedbacks(self, article):
        result = []

        for article_feedback in self.context.get("feedbacks"):
            feedback_dict = {}
            feedback_dict["emoji"] = article_feedback.feedback.emoji
            feedback_dict["count"] = article_feedback.count
            feedback_dict["is_feedbacked"] = self.get_is_feedbacked(article, article_feedback.feedback)
            result.append(feedback_dict)

        return result
