from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from article.models import Article, ArticleComment
from article.serializers import ArticleSerializer, CommentSerializer


class ArticleCommentSerializer(WritableNestedModelSerializer):
    """Serializer definition for ArticleComment Model."""

    article_id = serializers.PrimaryKeyRelatedField(
        source="article",
        queryset=Article.objects.all(),
        write_only=True,
    )
    article = ArticleSerializer(
        read_only=True,
    )
    comment = CommentSerializer(read_only=True)

    class Meta:
        """Meta definition for ArticleCommentSerializer."""

        model = ArticleComment
        fields = [
            "id",
            "article_id",
            "article",
            "comment",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "article_id",
            "article",
            "comment",
            "created_at",
            "updated_at",
        ]
