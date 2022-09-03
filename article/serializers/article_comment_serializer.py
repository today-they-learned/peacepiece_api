from drf_writable_nested.serializers import WritableNestedModelSerializer

from article.models import ArticleComment
from user.serializers import UserAbstractSerializer


class ArticleCommentSerializer(WritableNestedModelSerializer):
    """Serializer definition for ArticleComment Model."""

    writer = UserAbstractSerializer(read_only=True)

    class Meta:
        """Meta definition for ArticleCommentSerializer."""

        model = ArticleComment
        fields = [
            "id",
            "article_id",
            "writer",
            "content",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "article_id",
            "writer",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "content": {
                "required": True,
            }
        }
