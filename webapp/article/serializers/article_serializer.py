from article.models import Article
from article.serializers.article_comment_serializer import ArticleCommentSerializer
from challenge.models import Challenge
from challenge.serializers import ChallengeAbstractSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from file_manager.serializers import ImageSerializer
from rest_framework import serializers
from user.serializers import UserAbstractSerializer


class ArticleSerializer(WritableNestedModelSerializer):
    """Serializer definition for Article Model."""

    writer = UserAbstractSerializer(
        read_only=True,
    )

    images = ImageSerializer(
        many=True,
        required=False,
    )

    article_comments = ArticleCommentSerializer(many=True, read_only=True)

    challenge_id = serializers.PrimaryKeyRelatedField(
        source="challenge",
        queryset=Challenge.objects.all(),
        write_only=True,
        required=False,
    )

    challenge = ChallengeAbstractSerializer(
        read_only=True,
    )

    feedbacks = serializers.SerializerMethodField()

    class Meta:
        """Meta definition for ArticleSerializer."""

        model = Article

        fields = [
            "id",
            "writer",
            "content",
            "images",
            "challenge_id",
            "challenge",
            "article_comments",
            "feedbacks",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "writer",
            "article_comments",
            "feedbacks",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "content": {
                "required": True,
            }
        }

    def get_feedbacks(self, article):
        return self.context.get("feedbacks") or []
