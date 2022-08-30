from drf_writable_nested.serializers import WritableNestedModelSerializer

from article.models import Article
from file_manager.serializers import ImageSerializer
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

    class Meta:
        """Meta definition for ArticleSerializer."""

        model = Article

        fields = [
            "id",
            "writer",
            "content",
            "images",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "writer",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "content": {
                "required": True,
            }
        }
