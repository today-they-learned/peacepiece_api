from article.serializers import ArticleAbstractSerializer
from challenge.serializers import ChallengeAbstractSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from item.serializers import ItemSerializer
from point.models import Point
from user.serializers import UserAbstractSerializer


class PointSerializer(WritableNestedModelSerializer):
    """Serializer definition for Point Model."""

    user = UserAbstractSerializer(
        read_only=True,
    )

    challenge = ChallengeAbstractSerializer(
        read_only=True,
    )

    article = ArticleAbstractSerializer(
        read_only=True,
    )

    item = ItemSerializer(
        read_only=True,
    )

    class Meta:
        """Meta definition for PointSerializer."""

        model = Point

        fields = [
            "id",
            "user",
            "challenge_id",
            "article_id",
            "item",
            "category",
            "amount",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "challenge_id",
            "article_id",
            "item",
            "category",
            "amount",
            "created_at",
            "updated_at",
        ]
